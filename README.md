# LiamLlamazares.github.io
Files for mathematics blog at nowheredifferentiable.com

## Project Structure

```text
.
├── _config.yml       # Jekyll configuration
├── _includes/        # Reusable HTML snippets
├── _layouts/         # Page templates
├── _posts/           # Blog posts
├── assets/           # Static assets (images, css, js)
├── Gemfile           # Ruby dependencies
└── index.html        # Homepage
```

## Emailing subscribers about a new post

`announce_post.py` builds the announcement from the post's front matter
(title, description, cover image) and puts it in Mailchimp through its API.

```bash
python announce_post.py lands-part-1 --preview        # print the email, contact nobody
python announce_post.py lands-part-1                  # create or update the draft
python announce_post.py lands-part-1 --test me@x.org  # also send the draft to one address
python announce_post.py lands-part-1 --send           # send to every subscriber (asks first)
```

- Nothing reaches subscribers without `--send`.
- To write the letter yourself, put it in `_email.md` in the post's folder.
  The cover image, the link and the sign-off are added around it.
- The API key is read from `MAILCHIMP_API_KEY` or `~/.config/mailchimp/api_key`.
  Never commit it.
- Tests (no email service is contacted): `python -m unittest test_announce_post`.
