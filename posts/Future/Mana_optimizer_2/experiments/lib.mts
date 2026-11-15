import { readFileSync } from "node:fs";
const S = "/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad";
const M = `${S}/main/src`;
export const m = {
  facts: await import(`${M}/cardFacts.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/cardFacts"),
  rep: await import(`${M}/optimizerReport.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/optimizerReport"),
  rank: await import(`${M}/manabaseRanking.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/manabaseRanking"),
  mull: await import(`${M}/mulligan.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/mulligan"),
  cls: await import(`${M}/cardClassification.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/cardClassification"),
  cand: await import(`${M}/manabaseCandidates.ts`) as typeof import("/tmp/claude-249092/-home-llamazar-github-Personal-manabase-calculator/4a575847-4f72-4452-88c9-1183ae9d8b65/scratchpad/main/src/manabaseCandidates"),
};
export const cache = m.facts.buildCardFactsCache(JSON.parse(readFileSync(`${S}/exp/merged-card-facts.json`, "utf8")));
export const FORMAT = "modern";
export const POLICY = "custom-unrestricted" as const;
export const HELD_OUT_FIRST = 1_000_001;
export const heldOutSeeds = (n: number) => Array.from({ length: n }, (_, i) => HELD_OUT_FIRST + 13 * i);

export function deckText(spells: [number, string][], lands: [number, string][]): string {
  return ["Deck", ...spells.map(([n, c]) => `${n} ${c}`), ...lands.map(([n, c]) => `${n} ${c}`)].join("\n");
}
export function landIds(lands: [number, string][]): Record<string, number> {
  const out: Record<string, number> = {};
  for (const [n, name] of lands) {
    const c: any = m.cls.resolveCardClassification(name, { format: FORMAT });
    if (c === null || c.kind !== "land") throw new Error(`land not modelled: ${name}`);
    out[c.card.id] = (out[c.card.id] ?? 0) + n;
  }
  return out;
}
/** A problem whose only candidate is the fixed list (every land pinned min = max). */
export function problem(text: string, lands: [number, string][]) {
  const pins = landIds(lands);
  return m.rep.prepareOptimizerExperimentProblem({
    deckText: text, gameFormat: FORMAT, cardFactsCache: cache, candidateLegalityPolicy: POLICY,
    mainboardRepresentationPolicy: "relaxed-classification-preview-fixture",
    controls: { includedLandIds: Object.keys(pins), minCopiesById: pins, maxCopiesById: pins }
  } as any);
}
