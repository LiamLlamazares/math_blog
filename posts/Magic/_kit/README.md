# Magic kit

Shared by the Magic posts (`1-counting`, `2-playing`). A post opts in with, in its front matter:

    shortcodes: [../_kit/mana.lua]
    format:
      html:
        body-classes: mana-post
        css: [../_kit/mana.css, ../_kit/post.css]

Shortcodes:

    {{< mana U R >}}  or  {{< mana "{1}{U}" >}}     inline pips (W U B R G C T 0-9)
    {{< card lightning-bolt >}}  {{< cards mountain island swamp >}}   cards from cards.json
    {{< duel lucky >}}                               one click-through game from duel.json, by id (use one per game)
    {{< cn lightning-bolt >}}  {{< cn counterspell "the counter" >}}   a card's name in the text; hover or tap shows the card

Files: `mana.lua` (shortcodes), `cards.json` / `duel.json` (data), `mana.css` (pips, cards, duel),
`post.css` (figure paper, tables), `duel.js` (stepper), `cardname.js` (hover cards), `symbols/` (Scryfall SVGs), `art/` (card art, 480 px).
Add a card: one entry in `cards.json` plus `art/<id>.jpg`. Preview: `../preview.sh [1-counting|2-playing]`.
