import { writeFileSync } from "node:fs";
import { performance } from "node:perf_hooks";
import { m, deckText, problem, heldOutSeeds, FORMAT, POLICY } from "./lib.mts";

type L = [number, string][];
const S = "/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad";
const spellsA: L = [[4,"Lightning Bolt"],[4,"Goblin Electromancer"],[4,"Counterspell"],[4,"Terminate"],[4,"Crosis's Charm"],[4,"Kolaghan's Command"],[4,"Electrolyze"],[4,"Nicol Bolas, the Ravager"],[4,"Thoughtseize"]];
const spellsB1: L = [[4,"Llanowar Elves"],[4,"Pelt Collector"],[4,"Emmara, Soul of the Accord"],[4,"Thrashing Brontodon"],[4,"Knight of Autumn"],[4,"Nullhide Ferox"],[4,"Vivien Reid"],[4,"Lyra Dawnbringer"],[4,"Shalai, Voice of Plenty"]];
const spellsB2: L = [[4,"Thoughtbound Phantasm"],[4,"Thought Erasure"],[4,"Lazav, the Multifarious"],[4,"Blood Operative"],[4,"Sinister Sabotage"],[4,"Vraska's Contempt"],[4,"Doom Whisperer"],[4,"Nightveil Predator"],[4,"Dream Eater"]];
const tg: L = [[4,"Temple Garden"],[4,"Sunpetal Grove"]];
const wg: L = [[4,"Watery Grave"],[4,"Drowned Catacomb"]];
const EXPS: Record<string, { spells: L; reference: string; lists: Record<string, L> }> = {
  A: { spells: spellsA, reference: "A-shock", lists: {
    "A-shock": [[4,"Watery Grave"],[4,"Blood Crypt"],[4,"Steam Vents"],[4,"Island"],[4,"Swamp"],[4,"Mountain"]],
    // Dismal Backwater / Bloodfell Caves / Swiftwater Cliffs are not modelled; same-colour guildgates are (family tapped-dual).
    "B-tapped(guildgate-substitute)": [[4,"Dimir Guildgate"],[4,"Rakdos Guildgate"],[4,"Izzet Guildgate"],[4,"Island"],[4,"Swamp"],[4,"Mountain"]],
    "C-basics": [[8,"Island"],[8,"Swamp"],[8,"Mountain"]] } },
  B1: { spells: spellsB1, reference: "8F/8P", lists: {
    "8F/8P": [...tg,[8,"Forest"],[8,"Plains"]], "10F/6P": [...tg,[10,"Forest"],[6,"Plains"]],
    "12F/4P": [...tg,[12,"Forest"],[4,"Plains"]], "6F/10P": [...tg,[6,"Forest"],[10,"Plains"]] } },
  B2: { spells: spellsB2, reference: "9I/7S", lists: {
    "9I/7S": [...wg,[9,"Island"],[7,"Swamp"]], "8I/8S": [...wg,[8,"Island"],[8,"Swamp"]],
    "10I/6S": [...wg,[10,"Island"],[6,"Swamp"]], "7I/9S": [...wg,[7,"Island"],[9,"Swamp"]] } }
};
const [expName, nArg] = process.argv.slice(2);
const exp = EXPS[expName!]; if (!exp) throw new Error("usage: score.mts A|B1|B2 [seeds]");
const nSeeds = Number(nArg ?? 512);
const t0 = performance.now();
const probs = Object.entries(exp.lists).map(([name, lands]) => ({ name, lands, p: problem(deckText(exp.spells, lands), lands) }));
const base = probs[0]!.p;
for (const x of probs) {
  if (JSON.stringify(x.p.nonlands) !== JSON.stringify(base.nonlands) || x.p.playHorizon !== base.playHorizon) throw new Error(`${x.name}: spells differ`);
  if (x.p.incumbent.landCount !== 24) throw new Error(`${x.name}: ${x.p.incumbent.landCount} lands`);
}
const seeds = heldOutSeeds(nSeeds);
const ranked = m.rank.rankCandidateManabases({
  candidates: probs.map((x) => ({ ...x.p.incumbent, id: x.name })),
  nonlands: [...base.nonlands, ...base.sideboardTargets], seeds, turns: base.playHorizon, supportHorizon: base.supportHorizon,
  policy: m.mull.LONDON_CURVE_POLICY, playDrawPositions: ["play", "draw"], evidenceContextKey: m.rep.CURRENT_OPTIMIZER_SCORE_CONTRACT
});
const by = new Map(ranked.map((r) => [r.candidate.id, r]));
const nameOf = (id: string) => base.nonlands.find((s) => s.id === id)?.name ?? id.replace(/#\d+$/, "");
function perCard(r: any) {
  const out: Record<string, any> = {};
  const rows = r.score.targetCastabilityRows as any[];
  for (const row of rows) {
    const n = nameOf(row.id); const o = (out[n] ??= { targetTurn: row.targetTurn, copies: 0, rateSum: 0, games: 0, onTime: 0, late1: 0, late2: 0, late3: 0, notBy: 0 });
    o.copies += 1; o.rateSum += row.rate;
    const g = r.targetSampleCounts?.[row.id] ?? 0; o.games += g;
    const w = r.targetSupport?.[row.id]?.whenCastable;
    if (w) for (const k of ["onTime","late1","late2","late3","notBy"]) o[k] += w[k];
  }
  for (const o of Object.values(out)) { o.delayedCreditRate = o.rateSum / o.copies; o.exactOnTimeShare = o.games > 0 ? o.onTime / o.games : null; delete o.rateSum; }
  return out;
}
const parts = (r: any) => ({ total: r.score.total, cast: r.score.castability.score, manaUse: r.score.manaUsage.score, usefulLands: r.score.usefulLands.score, keepable: r.score.mulliganScore.score, life: r.score.lifeScore.score });
const ref = by.get(exp.reference)!;
const lists = Object.fromEntries(probs.map((x) => {
  const r = by.get(x.name)!;
  const d = m.rank.computePairedScoreDifferenceInterval(r, ref, undefined, "all-paired-seeds");
  const rp = parts(ref), mp = parts(r);
  return [x.name, { lands: x.lands.map(([n, c]) => `${n} ${c}`), counts: x.p.incumbent.counts, ...parts(r), averageLifePaid: r.score.raw.averageLifePaid, averageMulligans: r.averageMulligans, zeroMulliganRate: r.zeroMulliganRate, sampleCount: r.sampleCount,
    vsReference: { reference: exp.reference, mean: d.meanDifference, lower95: d.lower95, upper95: d.upper95, half: d.lower95 === null ? null : (d.upper95! - d.lower95!) / 2, pairedSeeds: d.pairedSeedCount, excludesZero: d.lower95 !== null && (d.lower95 > 0 || d.upper95! < 0),
      partsDiff: Object.fromEntries(Object.keys(rp).map((k) => [k, (mp as any)[k] - (rp as any)[k]])) },
    perCard: perCard(r) }];
}));
const out = { experiment: expName, settings: { gameFormat: FORMAT, candidateLegalityPolicy: POLICY, heldOutSeeds: `${nSeeds} seeds, 1000001 + 13*i`, playDrawPositions: ["play","draw"], playHorizon: base.playHorizon, supportHorizon: base.supportHorizon, mulliganPolicy: "LONDON_CURVE_POLICY", scoreWeights: ranked[0]!.score.weights, scoreContract: m.rep.CURRENT_OPTIMIZER_SCORE_CONTRACT, manaUsageBasis: ranked[0]!.score.raw.manaUsageBasis, spells: exp.spells.map(([n, c]) => `${n} ${c}`) }, wallSeconds: (performance.now() - t0) / 1000, lists };
writeFileSync(`${S}/exp/results/${expName}-fixed-lists.json`, JSON.stringify(out, null, 1));
console.log(JSON.stringify(out.settings), out.wallSeconds);
for (const [n, l] of Object.entries(lists) as any) console.log(n, l.total.toFixed(2), JSON.stringify(Object.fromEntries(Object.entries(l).filter(([k]) => ["cast","manaUse","usefulLands","keepable","life","averageLifePaid","averageMulligans"].includes(k)).map(([k, v]: any) => [k, +v.toFixed(3)]))), "vsRef", l.vsReference.mean.toFixed(3), "±", l.vsReference.half?.toFixed(3), l.vsReference.excludesZero);
