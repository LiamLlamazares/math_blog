"""Tests for announce_post.py against a fake Mailchimp server.

    python -m unittest test_announce_post -v

No real email service is contacted.
"""

import contextlib
import io
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest import mock
from urllib.parse import urlparse

import announce_post

POST = "posts/Modelling/lands-part-1"
SUBJECT = "New post: What lands should I play? Part 1"
POST_URL = "https://nowheredifferentiable.com/posts/Modelling/lands-part-1/"


class FakeMailchimp(BaseHTTPRequestHandler):
    campaigns: list = []
    requests: list = []
    ready = True

    def log_message(self, *args):
        pass

    def _reply(self, status, body=None):
        raw = b"" if body is None else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _handle(self, method):
        cls = type(self)
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length") or 0)
        payload = json.loads(self.rfile.read(length)) if length else None
        cls.requests.append((method, path, payload))
        if not self.headers.get("Authorization", "").startswith("Basic "):
            return self._reply(401, {"title": "API Key Invalid", "detail": "bad key"})
        parts = path.strip("/").split("/")
        if method == "GET" and parts == ["lists"]:
            return self._reply(200, {"lists": [{
                "id": "list1", "name": "Readers", "stats": {"member_count": 12},
                "campaign_defaults": {"from_email": "liam@example.org"}}]})
        if method == "GET" and parts == ["campaigns"]:
            return self._reply(200, {"campaigns": cls.campaigns})
        if method == "POST" and parts == ["campaigns"]:
            campaign = {"id": f"c{len(cls.campaigns) + 1}", "status": "save", **payload}
            cls.campaigns.append(campaign)
            return self._reply(200, campaign)
        campaign = next((c for c in cls.campaigns if c["id"] == parts[1]), None)
        if campaign is None:
            return self._reply(404, {"title": "Not Found", "detail": "no such campaign"})
        if method == "PATCH" and len(parts) == 2:
            campaign["settings"].update(payload["settings"])
            return self._reply(200, campaign)
        if method == "PUT" and parts[2:] == ["content"]:
            campaign["html"] = payload["html"]
            return self._reply(200, {"html": payload["html"]})
        if method == "GET" and parts[2:] == ["send-checklist"]:
            items = [] if cls.ready else [
                {"type": "error", "heading": "Content", "details": "missing"}]
            return self._reply(200, {"is_ready": cls.ready, "items": items})
        if method == "POST" and parts[2:] == ["actions", "test"]:
            return self._reply(204)
        if method == "POST" and parts[2:] == ["actions", "send"]:
            campaign["status"] = "sent"
            return self._reply(204)
        return self._reply(404, {"title": "Not Found", "detail": path})

    def do_GET(self):
        self._handle("GET")

    def do_POST(self):
        self._handle("POST")

    def do_PATCH(self):
        self._handle("PATCH")

    def do_PUT(self):
        self._handle("PUT")


class AnnounceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), FakeMailchimp)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        FakeMailchimp.campaigns = []
        FakeMailchimp.requests = []
        FakeMailchimp.ready = True
        port = self.server.server_address[1]
        for patch in (
            mock.patch.object(announce_post, "API_URL", f"http://127.0.0.1:{port}"),
            mock.patch.dict("os.environ", {"MAILCHIMP_API_KEY": "test-key-us0",
                                           "MAILCHIMP_LIST_ID": ""}),
        ):
            patch.start()
            self.addCleanup(patch.stop)

    def run_script(self, *args, post=POST):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = announce_post.main([post, "--no-check", *args])
        return code, out.getvalue(), err.getvalue()

    def sends(self):
        return [r for r in FakeMailchimp.requests if r[1].endswith("/actions/send")]

    def test_default_creates_a_draft_and_sends_nothing(self):
        code, out, _ = self.run_script()
        self.assertEqual(code, 0)
        self.assertEqual(len(FakeMailchimp.campaigns), 1)
        campaign = FakeMailchimp.campaigns[0]
        self.assertEqual(campaign["status"], "save")
        self.assertEqual(campaign["settings"]["subject_line"], SUBJECT)
        self.assertEqual(campaign["recipients"], {"list_id": "list1"})
        self.assertFalse(campaign["tracking"]["html_clicks"])
        self.assertIn(POST_URL, campaign["html"])
        self.assertIn("cover.jpg", campaign["html"])
        self.assertIn("Dear reader,", campaign["html"])
        self.assertIn("<ol", campaign["html"])
        self.assertIn("Read the post", campaign["html"])
        self.assertIn("Not sent to subscribers", out)
        self.assertEqual(self.sends(), [])

    def test_second_run_updates_the_same_draft(self):
        self.run_script()
        code, out, _ = self.run_script()
        self.assertEqual(code, 0)
        self.assertEqual(len(FakeMailchimp.campaigns), 1)
        self.assertIn("Draft updated", out)

    def test_an_email_already_sent_is_left_alone(self):
        self.run_script()
        FakeMailchimp.campaigns[0]["status"] = "sent"
        before = len(FakeMailchimp.requests)
        code, _, err = self.run_script("--send", "--yes")
        self.assertEqual(code, 2)
        self.assertIn("already has", err)
        writes = [r for r in FakeMailchimp.requests[before:] if r[0] != "GET"]
        self.assertEqual(writes, [])

    def test_test_send_goes_only_to_the_given_address(self):
        code, out, _ = self.run_script("--test", "me@example.org")
        self.assertEqual(code, 0)
        tests = [r for r in FakeMailchimp.requests if r[1].endswith("/actions/test")]
        self.assertEqual([r[2]["test_emails"] for r in tests], [["me@example.org"]])
        self.assertEqual(self.sends(), [])
        self.assertIn("Not sent to subscribers", out)

    def test_send_with_yes_sends_once(self):
        code, out, _ = self.run_script("--send", "--yes")
        self.assertEqual(code, 0)
        self.assertEqual(len(self.sends()), 1)
        self.assertIn("all 12 subscribers", out)

    def test_send_needs_the_word_send(self):
        with mock.patch("sys.stdin.isatty", return_value=True), \
                mock.patch("builtins.input", return_value="y"):
            code, out, _ = self.run_script("--send")
        self.assertEqual(code, 1)
        self.assertEqual(self.sends(), [])
        self.assertIn("Not sent", out)
        with mock.patch("sys.stdin.isatty", return_value=True), \
                mock.patch("builtins.input", return_value="send"):
            code, _, _ = self.run_script("--send")
        self.assertEqual(code, 0)
        self.assertEqual(len(self.sends()), 1)

    def test_send_without_a_terminal_is_refused(self):
        with mock.patch("sys.stdin.isatty", return_value=False):
            code, _, err = self.run_script("--send")
        self.assertEqual(code, 2)
        self.assertIn("--yes", err)
        self.assertEqual(self.sends(), [])

    def test_send_stops_when_mailchimp_says_not_ready(self):
        FakeMailchimp.ready = False
        code, _, err = self.run_script("--send", "--yes")
        self.assertEqual(code, 2)
        self.assertIn("not ready", err)
        self.assertEqual(self.sends(), [])

    def test_preview_contacts_nobody(self):
        code, out, _ = self.run_script("--preview")
        self.assertEqual(code, 0)
        self.assertEqual(FakeMailchimp.requests, [])
        self.assertIn("Read the post", out)

    def test_missing_key_is_a_clear_error(self):
        with mock.patch.dict("os.environ", {"MAILCHIMP_API_KEY": ""}), \
                mock.patch.object(announce_post, "KEY_FILE",
                                  announce_post.ROOT / "no-such-key-file"):
            code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn("No Mailchimp API key", err)
        self.assertEqual(FakeMailchimp.requests, [])

    def test_unpublished_post_is_refused(self):
        code, _, err = self.run_script(post="posts/Modelling/lands-part-2")
        self.assertEqual(code, 2)
        self.assertIn("draft: true", err)
        self.assertEqual(FakeMailchimp.requests, [])

    def test_letter_markdown(self):
        text = "Hello **you**,\nsee [this](https://x.org/a).\n\n1. one\n2. two\n\n- a\n- b"
        out = announce_post.letter_html(text)
        self.assertIn("<strong>you</strong>, see <a href=\"https://x.org/a\"", out)
        self.assertEqual(out.count("<li"), 4)
        self.assertIn("<ol", out)
        self.assertIn("<ul", out)
        self.assertIn("&lt;b&gt;", announce_post.letter_html("a <b> c"))


if __name__ == "__main__":
    unittest.main()
