import { m, cache, deckText, problem, FORMAT } from "./lib.mts";
const spA = [[4,"Lightning Bolt"],[4,"Goblin Electromancer"],[4,"Counterspell"],[4,"Terminate"],[4,"Crosis's Charm"],[4,"Kolaghan's Command"],[4,"Electrolyze"],[4,"Nicol Bolas, the Ravager"],[4,"Thoughtseize"]] as [number,string][];
const lA = [[4,"Watery Grave"],[4,"Blood Crypt"],[4,"Steam Vents"],[4,"Island"],[4,"Swamp"],[4,"Mountain"]] as [number,string][];
const p = problem(deckText(spA,lA), lA);
console.log("horizon", p.playHorizon, p.supportHorizon, "landCount", p.incumbent.landCount);
for (const s of p.nonlands) console.log(JSON.stringify({ id: s.id, name: s.name, role: s.simulationRole, cost: s.manaCost, tt: s.targetTurn, tags: s.tags, rem: (s as any).manaCreatureRemovalChance }));
console.log(JSON.stringify(p.incumbent.counts));
for (const n of ["Watery Grave","Dismal Backwater","Bloodfell Caves","Swiftwater Cliffs","Dimir Guildgate","Rakdos Guildgate","Izzet Guildgate","Temple Garden","Sunpetal Grove","Drowned Catacomb"]) {
  const c: any = m.cls.resolveCardClassification(n, { format: FORMAT });
  console.log(n, c ? `${c.kind} family=${c.family} ${JSON.stringify({ t: c.card?.entersTapped, mana: c.card?.mana, ec: c.card?.entryCondition, life: c.card?.untappedEntryLifeCost, gain: (c.card as any)?.lifeGain })}` : "NOT MODELLED");
}
const l2: [number,string][] = [[4,"Temple Garden"],[4,"Sunpetal Grove"],[8,"Forest"],[8,"Plains"]];
const p2 = problem(deckText([[4,"Llanowar Elves"],[4,"Pelt Collector"],[4,"Emmara, Soul of the Accord"],[4,"Thrashing Brontodon"],[4,"Knight of Autumn"],[4,"Nullhide Ferox"],[4,"Vivien Reid"],[4,"Lyra Dawnbringer"],[4,"Shalai, Voice of Plenty"]],l2), l2);
for (const s of p2.nonlands) console.log(JSON.stringify({ name: s.name, role: s.simulationRole, cost: s.manaCost, tt: s.targetTurn, tags: s.tags, rem: (s as any).manaCreatureRemovalChance }));
const l3: [number,string][] = [[4,"Watery Grave"],[4,"Drowned Catacomb"],[9,"Island"],[7,"Swamp"]];
const p3 = problem(deckText([[4,"Thoughtbound Phantasm"],[4,"Thought Erasure"],[4,"Lazav, the Multifarious"],[4,"Blood Operative"],[4,"Sinister Sabotage"],[4,"Vraska's Contempt"],[4,"Doom Whisperer"],[4,"Nightveil Predator"],[4,"Dream Eater"]],l3), l3);
for (const s of p3.nonlands) console.log(JSON.stringify({ name: s.name, role: s.simulationRole, cost: s.manaCost, tt: s.targetTurn, tags: s.tags }));
