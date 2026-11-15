import { writeFileSync } from "node:fs";
import { performance } from "node:perf_hooks";
import { m, cache, deckText, problem, heldOutSeeds, FORMAT, POLICY } from "./lib.mts";
const S = "/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad";
const spells: [number, string][] = [[4,"Lightning Bolt"],[4,"Goblin Electromancer"],[4,"Counterspell"],[4,"Terminate"],[4,"Crosis's Charm"],[4,"Kolaghan's Command"],[4,"Electrolyze"],[4,"Nicol Bolas, the Ravager"],[4,"Thoughtseize"]];
const lA: [number, string][] = [[4,"Watery Grave"],[4,"Blood Crypt"],[4,"Steam Vents"],[4,"Crumbling Necropolis"],[3,"Island"],[2,"Swamp"],[3,"Mountain"]];
const text = deckText(spells, lA);
const t0 = performance.now();
const report: any = m.rep.buildFixtureOptimizerReport({
  deckText: text, gameFormat: FORMAT, precision: "balanced", cardFactsCache: cache, candidateLegalityPolicy: POLICY,
  controls: { candidateMode: "guided", refinementRounds: 2 },
  mainboardRepresentationPolicy: "relaxed-classification-preview-fixture",
  explanationSeedCount: 1, includeSensitivity: false
} as any);
const searchSeconds = (performance.now() - t0) / 1000;
const win = report.rankedManabases[0];
const searchSeeds: number[] = report.inputSummary.seeds;
const seeds = heldOutSeeds(512);
const overlap = seeds.filter((s) => searchSeeds.includes(s)).length;
console.log("search", searchSeconds.toFixed(0), "s; seeds", searchSeeds.length, "overlap", overlap, "winner", JSON.stringify(win.counts));
// Score the starting list A and the winner on the held-out seeds (same machinery as score.mts).
const pA = problem(text, lA);
const names = new Map(m.cls.listKnownLands({ commander: false }).map((l: any) => [l.id, l.name]));
const winLands = Object.entries(win.counts as Record<string, number>).filter(([, n]) => n > 0);
const pW = (() => { const ls: [number, string][] = winLands.map(([id, n]) => [n, names.get(id) ?? id]); return { ls, p: problem(deckText(spells, ls), ls) }; })();
const ranked = m.rank.rankCandidateManabases({
  candidates: [{ ...pA.incumbent, id: "A-start" }, { ...pW.p.incumbent, id: "optimizer" }],
  nonlands: [...pA.nonlands, ...pA.sideboardTargets], seeds, turns: pA.playHorizon, supportHorizon: pA.supportHorizon,
  policy: m.mull.LONDON_CURVE_POLICY, playDrawPositions: ["play", "draw"], evidenceContextKey: m.rep.CURRENT_OPTIMIZER_SCORE_CONTRACT
});
const by = new Map(ranked.map((r) => [r.candidate.id, r]));
const d = m.rank.computePairedScoreDifferenceInterval(by.get("optimizer")!, by.get("A-start")!, undefined, "all-paired-seeds");
const parts = (r: any) => ({ total: r.score.total, cast: r.score.castability.score, manaUse: r.score.manaUsage.score, usefulLands: r.score.usefulLands.score, keepable: r.score.mulliganScore.score, life: r.score.lifeScore.score, averageLifePaid: r.score.raw.averageLifePaid, averageMulligans: r.averageMulligans });
const cse: any = report.candidateSearchExplanation; console.log("WORKED", JSON.stringify(cse.workedExample)?.slice(0, 3000)); console.log("ROUNDS", JSON.stringify(cse.refinementRounds)); console.log("CHECK", JSON.stringify(report.recommendationCheck)?.slice(0,600));
const out = { settings: { poolLandCount: cse.poolLandCount, rounds: cse.refinementRounds, workedExample: cse.workedExample, stages: cse.stages, precision: "balanced", searchDepth: "standard (default)", refinementRounds: 2, candidateMode: "guided", gameFormat: FORMAT, candidateLegalityPolicy: POLICY, start: lA, searchSeedCount: searchSeeds.length, heldOutSeeds: "512, 1000001+13*i", seedOverlapWithSearch: overlap, playHorizon: pA.playHorizon, searchSeconds },
  optimizerLands: pW.ls.map(([n, c]) => `${n} ${c}`), searchScoreWinner: win.score.total, heldOut: { "A-start": parts(by.get("A-start")), optimizer: parts(by.get("optimizer")) },
  optimizerMinusA: { mean: d.meanDifference, lower95: d.lower95, upper95: d.upper95, half: (d.upper95! - d.lower95!) / 2 } };
writeFileSync(`${S}/exp/results/T-optimizer-from-tri4.json`, JSON.stringify(out, null, 1));
console.log(JSON.stringify(out, null, 1));
