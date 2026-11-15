#!/usr/bin/env bash
# Live preview of the two Magic posts in the blog's real theme.
#
#   posts/Magic/preview.sh            # Part 1 (1-counting)
#   posts/Magic/preview.sh 2-playing  # Part 2
#   posts/Magic/preview.sh 1-counting --no-browser --port 4300
#
# Why this script exists: a plain `quarto preview` re-renders a page only when its .qmd
# changes, hides drafts (Part 2 while it is unpublished) and writes into the repo's _site.
# So the script copies the blog's chrome (theme, navbar, css) into a scratch folder, mirrors
# this Magic folder into it as posts/Magic/, shows drafts, and previews there. Edits you
# save here are mirrored every second, and a change to a _kit/ file re-renders the page.
# The repo is only read. It works from wherever this folder sits inside the blog.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG="$(cd "$HERE" && while [ ! -f _quarto.yml ] && [ "$PWD" != / ]; do cd ..; done; pwd)"
[ -f "$BLOG/_quarto.yml" ] || { echo "No _quarto.yml above $HERE" >&2; exit 1; }
SCRATCH="${MAGIC_PREVIEW_DIR:-${TMPDIR:-/tmp}/math_blog_magic_preview}"
PART="${1:-1-counting}"
[ $# -gt 0 ] && shift

[ -f "$HERE/$PART/index.qmd" ] || { echo "No $HERE/$PART/index.qmd" >&2; exit 1; }
command -v quarto >/dev/null || { echo "quarto not on PATH (try ~/.local/bin)" >&2; exit 1; }

mkdir -p "$SCRATCH/posts/Magic"
# the blog without its posts (posts/ and previous output in the scratch folder are left alone)
rsync -a --delete --exclude .git --exclude _site --exclude .quarto --exclude __pycache__ \
      --exclude /posts "$BLOG/" "$SCRATCH/"
[ -f "$BLOG/posts/_metadata.yml" ] && cp "$BLOG/posts/_metadata.yml" "$SCRATCH/posts/_metadata.yml"
# show drafts, and drop the exclusion that blocks previews
sed -i -e 's/^website:/website:\n  draft-mode: visible/' -e '/"!posts\/Future\/\*\*"/d' "$SCRATCH/_quarto.yml"

sync_magic() {
  rsync -a --delete --exclude preview.sh --exclude .quarto --exclude '*.html' --exclude '*_files' \
        "$HERE/" "$SCRATCH/posts/Magic/"
}
sync_magic
# quarto preview re-renders only when the .qmd itself changes. Cards and duels are built by
# _kit/ at render time, so when a kit file changes we nudge the page: one extra newline in
# the scratch copy, which the next sync puts back.
kit_sig() { find "$HERE/_kit" -type f -printf '%T@ %s %p\n' | sort | cksum; }
( SIG="$(kit_sig)"
  while sleep 1; do
    sync_magic || true
    NEW="$(kit_sig)"
    if [ "$NEW" != "$SIG" ]; then SIG="$NEW"; echo >> "$SCRATCH/posts/Magic/$PART/index.qmd"; fi
  done ) &
SYNC=$!
trap 'kill $SYNC 2>/dev/null || true' EXIT INT TERM

cd "$SCRATCH"
quarto preview "posts/Magic/$PART/index.qmd" "$@"
