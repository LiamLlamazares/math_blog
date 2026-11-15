#!/usr/bin/env python3
"""Email subscribers about a published post, through Mailchimp's API.

    python announce_post.py lands-part-1                 # create (or update) a draft
    python announce_post.py lands-part-1 --test me@x.org # ... and send the draft to one address
    python announce_post.py lands-part-1 --send          # ... and send it to every subscriber
    python announce_post.py lands-part-1 --preview       # print the email text, contact nobody

Nothing reaches subscribers without --send, and --send asks for confirmation.

The email is built from the post's front matter (title, description, image).
To write your own letter for a post, put it in `_email.md` next to the post's
`index.qmd` (Markdown: paragraphs, lists, **bold**, *italic*, [links](url);
Quarto ignores files that start with an underscore). The title, cover image,
"Read the post" button and sign-off are added around it. Mailchimp adds the
footer with the unsubscribe link and postal address.

The API key is read from the environment variable MAILCHIMP_API_KEY or from
the file ~/.config/mailchimp/api_key. It must never be committed.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEY_FILE = Path.home() / ".config" / "mailchimp" / "api_key"
API_URL = os.environ.get("MAILCHIMP_API_URL", "")  # set only by the tests
USER_AGENT = "announce_post.py (nowheredifferentiable.com)"

FROM_NAME = "Liam"
SUBJECT = "New post: {title}"
DEFAULT_LETTER = """Dear reader,

A new post is up on {site}: **{title}**.

{description}"""
SIGN_OFF = ["I hope you enjoy it!<br>Liam"]

SERIF = "Georgia, 'Times New Roman', serif"
P_STYLE = "margin:0 0 16px 0;"


class Problem(Exception):
    """Something the user has to fix; printed without a traceback."""


# ---------------------------------------------------------------- the post


def find_post(name: str) -> Path:
    """Return the post's index.qmd from a path or from part of its folder name."""
    given = Path(name)
    for candidate in (given, ROOT / given):
        if candidate.is_file() and candidate.name == "index.qmd":
            return candidate.resolve()
        if (candidate / "index.qmd").is_file():
            return (candidate / "index.qmd").resolve()
    posts = [
        p
        for p in (ROOT / "posts").glob("**/index.qmd")
        if "Future" not in p.relative_to(ROOT).parts
    ]
    wanted = name.strip("/").lower()
    exact = [p for p in posts if p.parent.name.lower() == wanted]
    matches = exact or [p for p in posts if wanted in p.parent.name.lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise Problem(f"No post folder matches '{name}'.")
    listing = "\n  ".join(str(p.parent.relative_to(ROOT)) for p in sorted(matches))
    raise Problem(f"'{name}' matches several posts; be more specific:\n  {listing}")


def read_front_matter(index_qmd: Path) -> dict:
    import yaml  # PyYAML

    text = index_qmd.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise Problem(f"{index_qmd} has no front matter.")
    end = text.find("\n---", 3)
    if end == -1:
        raise Problem(f"{index_qmd}: the front matter is not closed.")
    meta = yaml.safe_load(text[3:end]) or {}
    if not isinstance(meta, dict):
        raise Problem(f"{index_qmd}: the front matter is not a mapping.")
    return meta


def site_settings() -> tuple[str, str]:
    import yaml

    config = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    website = config.get("website", {})
    url = str(website.get("site-url", "")).rstrip("/")
    if not url:
        raise Problem("_quarto.yml has no website.site-url.")
    return url, str(website.get("title", url))


def inline_html(text: str) -> str:
    """**bold**, *italic* and [text](url) in one line of Markdown."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                 lambda m: f'<a href="{html.escape(m.group(2))}" style="color:#2a4b8d;">{m.group(1)}</a>',
                 out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def letter_html(markdown: str) -> str:
    """The small part of Markdown a letter needs: paragraphs and lists."""
    blocks = re.split(r"\n\s*\n", markdown.strip())
    out = []
    for block in blocks:
        lines = [line.rstrip() for line in block.splitlines() if line.strip()]
        numbered = all(re.match(r"\s*\d+[.)]\s+", line) for line in lines)
        bulleted = all(re.match(r"\s*[-*]\s+", line) for line in lines)
        if numbered or bulleted:
            tag = "ol" if numbered else "ul"
            items = "".join(
                '<li style="margin-bottom:6px;">'
                + inline_html(re.sub(r"^\s*(\d+[.)]|[-*])\s+", "", line))
                + "</li>"
                for line in lines
            )
            out.append(f'<{tag} style="margin:0 0 16px 0; padding-left:24px;">{items}</{tag}>')
        else:
            out.append(f'<p style="{P_STYLE}">' + inline_html(" ".join(lines)) + "</p>")
    return "\n".join(out)


def email_html(site: str, title: str, post_url: str, image_url: str,
               image_alt: str, letter: str) -> str:
    url = html.escape(post_url)
    cell = f"font-family:{SERIF}; font-size:17px; line-height:1.6; color:#1f2937;"
    image_row = ""
    if image_url:
        image_row = (
            f'<tr><td style="padding:0;"><a href="{url}">'
            f'<img src="{html.escape(image_url)}" width="600" alt="{html.escape(image_alt)}" '
            'style="display:block; width:100%; max-width:600px; height:auto; border:0;">'
            "</a></td></tr>"
        )
    sign_off = "".join(f'<p style="{P_STYLE}">{line}</p>' for line in SIGN_OFF)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(SUBJECT.format(title=title))}</title>
<style>
  body {{ margin:0; padding:0; background-color:#f6f4ee; }}
  @media (max-width: 620px) {{
    .wrap {{ width:100% !important; }}
    .pad {{ padding-left:20px !important; padding-right:20px !important; }}
  }}
</style>
</head>
<body style="margin:0; padding:0; background-color:#f6f4ee;">
<span style="display:none; max-height:0; overflow:hidden; opacity:0;">*|MC_PREVIEW_TEXT|*</span>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f6f4ee;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px; background-color:#ffffff; border-radius:8px;">
<tr><td class="pad" style="padding:28px 36px 8px 36px; font-family:{SERIF}; font-size:14px; letter-spacing:0.04em; color:#6b7280;">{html.escape(site)}</td></tr>
<tr><td class="pad" style="padding:0 36px 20px 36px; font-family:{SERIF}; font-size:26px; line-height:1.25; color:#1f2937;">{html.escape(title)}</td></tr>
{image_row}
<tr><td class="pad" style="padding:28px 36px 8px 36px; {cell}">
{letter_html(letter)}
</td></tr>
<tr><td class="pad" align="left" style="padding:0 36px 24px 36px;">
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="background-color:#2a4b8d; border-radius:6px;"><a href="{url}" style="display:inline-block; padding:12px 22px; font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:bold; color:#ffffff; text-decoration:none;">Read the post</a></td>
</tr></table>
</td></tr>
<tr><td class="pad" style="padding:0 36px 20px 36px; {cell}">{sign_off}</td></tr>
</table>
</td></tr>
</table>
</body>
</html>
"""


def build_email(index_qmd: Path) -> dict:
    meta = read_front_matter(index_qmd)
    if meta.get("draft"):
        raise Problem(f"{index_qmd.parent.name} is still marked `draft: true`.")
    title = str(meta.get("title", "")).strip()
    if not title:
        raise Problem(f"{index_qmd} has no title.")
    site_url, site_title = site_settings()
    folder = index_qmd.parent.relative_to(ROOT).as_posix()
    post_url = f"{site_url}/{urllib.parse.quote(folder)}/"
    description = str(meta.get("description", "") or "").strip()

    image = str(meta.get("image", "") or "").strip()
    image_url = urllib.parse.urljoin(post_url, image) if image else ""
    image_alt = str(meta.get("image-alt", "") or title).strip()

    letter_file = index_qmd.parent / "_email.md"
    if letter_file.is_file():
        letter = letter_file.read_text(encoding="utf-8").strip()
    else:
        letter = DEFAULT_LETTER.format(
            site=site_title, title=title, description=description
        ).strip()

    return {
        "name": f"announce: {folder}",  # how a rerun finds its own draft
        "subject": SUBJECT.format(title=title),
        "preview_text": description,
        "post_url": post_url,
        "image_url": image_url,
        "letter": letter,
        "letter_file": letter_file if letter_file.is_file() else None,
        "html": email_html(site_title, title, post_url, image_url, image_alt, letter),
    }


def check_live(url: str, what: str) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        status = error.code
    except urllib.error.URLError as error:
        raise Problem(f"Could not reach {what} at {url}: {error.reason}") from error
    if status != 200:
        raise Problem(
            f"{what} is not live yet ({url} answered {status}). "
            "Publish the post first, or pass --no-check."
        )


# --------------------------------------------------------------- Mailchimp


def api_key() -> str:
    key = os.environ.get("MAILCHIMP_API_KEY", "").strip()
    if not key and KEY_FILE.is_file():
        key = KEY_FILE.read_text(encoding="utf-8").strip()
    if not key:
        raise Problem(
            "No Mailchimp API key. Set MAILCHIMP_API_KEY or put the key in "
            f"{KEY_FILE} (use --preview to see the email without one)."
        )
    return key


def api_base(key: str) -> str:
    if API_URL:
        return API_URL
    if "-" not in key:
        raise Problem("The Mailchimp API key should end in its data centre, like '-us11'.")
    return f"https://{key.rsplit('-', 1)[1]}.api.mailchimp.com/3.0"


class ApiError(Exception):
    def __init__(self, status: int, title: str, detail: str):
        super().__init__(f"Mailchimp answered {status}: {detail or title or 'no detail'}")
        self.status, self.title, self.detail = status, title, detail


def call(method: str, path: str, key: str, payload: dict | None = None,
         query: dict | None = None):
    url = api_base(key) + path
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, method=method)
    token = base64.b64encode(f"announce:{key}".encode()).decode()
    request.add_header("Authorization", f"Basic {token}")
    request.add_header("User-Agent", USER_AGENT)
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raw = error.read().decode("utf-8", "replace")
        try:
            body = json.loads(raw)
        except ValueError:
            body = {}
        if not isinstance(body, dict):
            body = {}
        raise ApiError(error.code, str(body.get("title", "")),
                       str(body.get("detail", "") or raw[:300])) from error
    except urllib.error.URLError as error:
        raise Problem(f"Could not reach Mailchimp: {error.reason}") from error
    return json.loads(raw) if raw.strip() else {}


def audience(key: str) -> dict:
    wanted = os.environ.get("MAILCHIMP_LIST_ID", "").strip()
    lists = call("GET", "/lists", key, query={
        "count": 50,
        "fields": "lists.id,lists.name,lists.stats.member_count,"
                  "lists.campaign_defaults.from_email",
    }).get("lists", [])
    if wanted:
        lists = [item for item in lists if item["id"] == wanted]
    if len(lists) != 1:
        raise Problem(
            f"Expected one Mailchimp audience, found {len(lists)}. "
            "Set MAILCHIMP_LIST_ID to the one to use."
        )
    return lists[0]


def existing_campaign(key: str, list_id: str, name: str) -> dict | None:
    """The campaign an earlier run made for this post, found by its internal name."""
    campaigns = call("GET", "/campaigns", key, query={
        "list_id": list_id, "count": 200,
        "fields": "campaigns.id,campaigns.web_id,campaigns.status,campaigns.settings.title",
    }).get("campaigns", [])
    for campaign in campaigns:
        if campaign.get("settings", {}).get("title") == name:
            return campaign
    return None


def save_draft(key: str, fields: dict, target: dict) -> tuple[dict, str]:
    settings = {
        "subject_line": fields["subject"],
        "preview_text": fields["preview_text"],
        "title": fields["name"],
        "from_name": FROM_NAME,
        "reply_to": target["campaign_defaults"]["from_email"],
    }
    found = existing_campaign(key, target["id"], fields["name"])
    if found is None:
        campaign = call("POST", "/campaigns", key, {
            "type": "regular",
            "recipients": {"list_id": target["id"]},
            "settings": settings,
            "tracking": {"opens": True, "html_clicks": False, "text_clicks": False},
        })
        verb = "created"
    elif found.get("status") != "save":
        raise Problem(
            f"Mailchimp already has the email for this post with status "
            f"'{found.get('status')}'. It was not touched."
        )
    else:
        campaign = call("PATCH", f"/campaigns/{found['id']}", key, {"settings": settings})
        verb = "updated"
    call("PUT", f"/campaigns/{campaign['id']}/content", key, {"html": fields["html"]})
    return campaign, verb


def check_ready(key: str, campaign: dict) -> None:
    checklist = call("GET", f"/campaigns/{campaign['id']}/send-checklist", key)
    if not checklist.get("is_ready"):
        errors = [f"{item.get('heading')}: {item.get('details')}"
                  for item in checklist.get("items", []) if item.get("type") == "error"]
        raise Problem("Mailchimp says the email is not ready to send:\n  "
                      + "\n  ".join(errors or ["no reason given"]))


# -------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Email subscribers about a published post (Mailchimp).",
        epilog="Without --send, subscribers receive nothing.",
    )
    parser.add_argument("post", help="post folder, or part of its name (e.g. lands-part-1)")
    parser.add_argument("--preview", action="store_true",
                        help="print the email text and stop; Mailchimp is not contacted")
    parser.add_argument("--html", metavar="FILE",
                        help="with --preview: also write the email's HTML to FILE")
    parser.add_argument("--test", metavar="ADDRESS", action="append", default=[],
                        help="send the draft to this address only (repeatable)")
    parser.add_argument("--send", action="store_true",
                        help="send to every subscriber, after a confirmation prompt")
    parser.add_argument("--yes", action="store_true",
                        help="with --send: skip the confirmation prompt")
    parser.add_argument("--no-check", action="store_true",
                        help="do not check that the post and its cover are online")
    args = parser.parse_args(argv)

    try:
        index_qmd = find_post(args.post)
        fields = build_email(index_qmd)
        print(f"Post:    {index_qmd.parent.relative_to(ROOT)}")
        print(f"Subject: {fields['subject']}")
        print(f"Link:    {fields['post_url']}")
        if fields["letter_file"] is None:
            print("Letter:  default text (write _email.md in the post folder for your own)")
        else:
            print(f"Letter:  {fields['letter_file'].relative_to(ROOT)}")

        if args.preview:
            print("\n" + "-" * 72 + "\n" + fields["letter"] + "\n\n[Read the post]\n\n"
                  + "\n\n".join(line.replace("<br>", "\n") for line in SIGN_OFF)
                  + "\n" + "-" * 72)
            if args.html:
                Path(args.html).write_text(fields["html"], encoding="utf-8")
                print(f"HTML written to {args.html}")
            return 0

        if not args.no_check:
            check_live(fields["post_url"], "The post")
            if fields["image_url"]:
                check_live(fields["image_url"], "The cover image")

        key = api_key()
        target = audience(key)
        campaign, verb = save_draft(key, fields, target)
        print(f"Draft {verb} in Mailchimp (id {campaign.get('id')}).")

        if args.test:
            call("POST", f"/campaigns/{campaign['id']}/actions/test", key,
                 {"test_emails": args.test, "send_type": "html"})
            print("Test sent to: " + ", ".join(args.test))

        if not args.send:
            print("Not sent to subscribers. Rerun with --send when you are happy with it.")
            return 0

        check_ready(key, campaign)
        count = target.get("stats", {}).get("member_count")
        people = f"all {count} subscribers of '{target.get('name')}'"
        if not args.yes:
            if not sys.stdin.isatty():
                raise Problem("--send needs a terminal to confirm in (or --yes).")
            answer = input(f"Send '{fields['subject']}' to {people}? Type 'send': ")
            if answer.strip().lower() != "send":
                print("Not sent. The draft is kept.")
                return 1
        call("POST", f"/campaigns/{campaign['id']}/actions/send", key)
        print(f"Sent to {people}.")
        return 0
    except (Problem, ApiError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
