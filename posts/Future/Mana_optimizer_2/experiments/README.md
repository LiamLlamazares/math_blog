# Experiments behind the two mana posts

Run on 2026-11-13 against origin/main (2aff4fd) of manabase-calculator: 512 held-out seeds, each on the play and on the draw,
default policy, score contract v5. From a checkout of that repo:

    npx tsx fetchFacts.mts            # fetches 16 card facts missing from the default file (network)
    for e in A B1 B2; do scripts/studies/heavy.sh npx tsx score.mts $e 512; done
    scripts/studies/heavy.sh npx tsx optimize.mts

The scripts hold absolute scratch paths from the session that wrote them; adjust before rerunning.
A = same sources, shock lands vs guildgates vs basics. B1, B2 = Karsten 2018 example manabases.
