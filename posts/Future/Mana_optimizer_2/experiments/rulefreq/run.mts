import { readFileSync, writeFileSync } from "node:fs";
import { performance } from "node:perf_hooks";
import { m, deckText, problem, heldOutSeeds } from "./lib.mts";
const R = "/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/rulefreq";
const key = process.argv[2]!; const nSeeds = Number(process.argv[3] ?? 512);
const SRC = process.env.SRC ?? "main-instr";
const d = JSON.parse(readFileSync(`${R}/decks.json`, "utf8"))[key];
const stats: Record<string, number> = {};
if (SRC === "main-instr") (globalThis as any).__ruleStats = stats;
const t0 = performance.now();
const p = problem(deckText(d.spells, d.lands), d.lands);
const ranked = m.rank.rankCandidateManabases({
  candidates: [{ ...p.incumbent, id: key }], nonlands: [...p.nonlands, ...p.sideboardTargets], seeds: heldOutSeeds(nSeeds), turns: p.playHorizon,
  supportHorizon: p.supportHorizon, policy: m.mull.LONDON_CURVE_POLICY, playDrawPositions: ["play", "draw"], evidenceContextKey: m.rep.CURRENT_OPTIMIZER_SCORE_CONTRACT
});
const r: any = ranked[0];
const out = { key, src: SRC, nSeeds, playHorizon: p.playHorizon, supportHorizon: p.supportHorizon, total: r.score.total, averageMulligans: r.averageMulligans, zeroMulliganRate: r.zeroMulliganRate, deepMulliganRate: r.deepMulliganRate, averageLifePaid: r.score.raw.averageLifePaid, sampleCount: r.sampleCount, wallSeconds: (performance.now() - t0) / 1000, stats };
writeFileSync(`${R}/raw-${SRC}-${key}-${nSeeds}.json`, JSON.stringify(out, null, 1));
console.log(key, SRC, "total", r.score.total.toFixed(4), "mull", r.averageMulligans, "zero", r.zeroMulliganRate, "wall", out.wallSeconds.toFixed(1), "games", stats.games);
