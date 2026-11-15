#!/bin/bash
# usage: ./build.sh name [name...]   e.g. ./build.sh fig_spells   (builds _plain and _art when the figure uses cards)
# Builds in a scratch directory outside the post folder and copies fig_*.pdf next to main.tex.
SRC="$(cd "$(dirname "$0")" && pwd)"; POST="$(dirname "$SRC")"
B=/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/figbuild1
mkdir -p "$B"; cd "$B"; export TEXINPUTS="$SRC:"
for n in "$@"; do
  if grep -q "mcard\|mchip\|duelpanel" "$SRC/$n.tex"; then
    pdflatex -interaction=nonstopmode -halt-on-error -jobname="${n}_plain" "\\input{$n}" >/dev/null || { echo FAIL $n plain; continue; }
    pdflatex -interaction=nonstopmode -halt-on-error -jobname="${n}_art" "\\def\\CARDART{1}\\input{$n}" >/dev/null || { echo FAIL $n art; continue; }
    cp "${n}_plain.pdf" "${n}_art.pdf" "$POST/"
  else
    pdflatex -interaction=nonstopmode -halt-on-error -jobname="$n" "\\input{$n}" >/dev/null || { echo FAIL $n; continue; }
    cp "$n.pdf" "$POST/"
  fi
done
