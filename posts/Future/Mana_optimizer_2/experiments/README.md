# Experiments behind the two mana posts

Run on 2026-11-13 against origin/main (2aff4fd) of manabase-calculator: 512 held-out seeds, each on the play and on the draw,
default policy, score contract v5. From a checkout of that repo:

    npx tsx fetchFacts.mts            # fetches 16 card facts missing from the default file (network)
    for e in A B1 B2; do scripts/studies/heavy.sh npx tsx score.mts $e 512; done
    scripts/studies/heavy.sh npx tsx optimize.mts

The scripts hold absolute scratch paths from the session that wrote them; adjust before rerunning.
A = same sources, shock lands vs guildgates vs basics. B1, B2 = Karsten 2018 example manabases.

## Second round, 2026-11-15 (same origin/main 2aff4fd, same 512 held-out seeds)

    scripts/studies/heavy.sh npx tsx score2.mts T 512 trade.json    # Archibaldus: four tapped three-colour lands for four basics
    scripts/studies/heavy.sh npx tsx score2.mts K 512 trade.json    # Karsten's green-white list: four Selesnya Guildgates for basics
    scripts/studies/heavy.sh npx tsx score2.mts F 512 fetch.json    # same source counts: shock, fetch, pain, fast, check lands, basics
    scripts/studies/heavy.sh npx tsx score2.mts G 512 grid.json     # every split of twelve basics behind twelve shock lands
    scripts/studies/heavy.sh npx tsx optimize_tri4.mts              # search started from the post-swap list (pool: its seven lands)

T is the example used in both posts (results/T-fixed-lists.json: base vs tri4, +1.09, range 0.35 to 1.82).
K gate4_8F4P vs 10F6P: -0.52 (range -0.90 to -0.14). F and G were explored and not used.
rulefreq/: how often each play rule decides something (instrumentation.patch is the diff against src/ used to count;
totals were checked to be identical with and without it).
