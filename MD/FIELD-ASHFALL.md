# Ashfall Ruins — ซากอารยธรรมพรอมีเธีย

> Part of the REO docs (v22). Sub-title: **Remnants of Promethea / ซากอารยธรรมพรอมีเธีย**. Recommended CP **9,000**. Map key `ashfall`. The ruins of Promethea, a civilization buried in one night when the great volcano erupted. The same eruption spewed veins of rare earth up from the deep; everything that survived the fire guards them.
> TH: ซากของพรอมีเธีย อารยธรรมที่ถูกฝังกลบในชั่วข้ามคืนเมื่อภูเขาไฟยักษ์ปะทุอย่างรุนแรง เถ้าถ่านยังโปรยปรายลงบนถนนที่แตกพังราวหิมะ และธารลาวาไหลผ่านที่ซึ่งเคยเป็นถนนสายใหญ่ ทว่าการระเบิดครั้งนั้นก็พ่นสายแร่หายากขึ้นมาจากใต้พิภพ แสงของมันเรืองรองผ่านกองซากปรักหักพังและล่อนักล่าเข้ามา ขณะที่ทุกสิ่งที่รอดจากเปลวเพลิงเฝ้าปกป้องมันอย่างไร้ความปรานี

## 1. Entry rules
| Rule | Value |
|---|---|
| Gate | Road to the Ruins **south portal**, design tile (28, 46) (game tile (57, 95)) |
| Requirement | Base Lv **40+** AND Combat Power **6,000+** (`GATE.ashfall`). Checked at the portal and for World Map teleport |
| If not met | Pushed back beside the portal with the usual toast (`gate_block`) |
| Warning signs | Two "Monster Lv.40+" signs on both sides of the Ruins south portal |
| Recommended CP | **9,000** (the gate lets you in at 6,000; the monsters are tuned for 9,000) |
| Teleport | Needs a visited map. Town → Ashfall = 300 Sc (Town → Ruins → Ashfall) |

## 2. Travel
| Portal | Design tile | Goes to | You arrive |
|---|---|---|---|
| Ruins south portal | (28, 46) | Ashfall Ruins | beside the Ashfall north portal |
| Ashfall north portal | (26, 2) | Road to the Ruins | beside the Ruins south portal |

`NEIGH.ashfall = ["ruins"]`, `AHEAD.ashfall = "ruins"`, `ROUTE.ruins.ashfall = 1` (portal index 1 on the Ruins map). Auto-quest / auto-walk from Town goes Town south gate → Ruins → Ashfall. Monsters ignore the player for 3 s after the map change and never spawn within 8 tiles of the portal.

## 3. Look
98 × 98 tiles (49-grid design × 2). Grey ash over black rock (`FPAL.ashfall`), charred trees, scattered rocks and ember crystals.
- **Roads:** the old avenue runs north–south (`ashPathX(y) = 24 + round(sin(0.15y + 0.3)·4)`, y 2–36) into the boss arena; a broken east–west street (`ashPathY(x) = 18 + round(sin(0.21x + 0.5)·3)`).
- **Lava fissures** (`ASH_RIFTS`, tile `T_C`, blocked): six glowing orange cracks cut the city; you cross them only where a road passes. The chasm look is now palette-driven (`FPAL.*.chasm`; Geosyncline keeps its cyan).
- **Lava pools:** 6 (blocked).
- **Rare earth veins** (`vein` prop, blocked): dark outcrops with glowing seams in violet (neodymium), amber (samarium) or green (promethium). Random ones plus some along the avenue.
- **Broken columns** line the avenue every 6 tiles; **braziers** ring the arena.
- **Boss arena:** circle at design (24.5, 40), radius 5.6, ember rune rings (`FPAL.ashfall.arenaC`). Behind it (south) stands the **Sealed Caldera Gate** (`bgate` prop, 7 × 3 tiles blocked): two cracked towers, a lava portcullis and a burning seal.
- Music: `ashfall` (118 BPM, Phrygian dominant, driving drums, pulsing bass). The `boss` track plays while any boss on the current map is fighting.

## 4. Monsters (all **aggressive**, ~3× Road to the Ruins)
Every type is fast, sees far (aggro range 6.5–8, Elites +1 = up to 9), comes in large numbers, and two of the three attack from range. Counts: 3× the base count scattered + 2 Elites per kind + 1 pack per kind (Scoria Hound ×6, Cinderbow ×6, Magus ×5). About 95 monsters in total.

| ID | Name (EN / TH) | Lv | Elem | HP | ATK | Hard DEF | Soft DEF | MDEF | HIT | FLEE | Speed (chase ×1.6) | Base / Job EXP | Scandium | Count | Aggro | Attack | Skills |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `scoriahound` | Scoria Hound / สกอเรียฮาวนด์ | 42 | Fire | 9,000 | 312 | 14% | 60 | 14% | 150 | 72 | 2.6 (4.16) | 3,750 / 2,400 | 570–870 | 10 (north and middle, y 4–30) | 7 | melee, every 1.2 s | moltenpounce |
| `cinderbow` | Cinderbow Revenant / ซินเดอร์โบว์ เรเวแนนต์ | 45 | Fire | 12,000 | 366 | 18% | 70 | 20% | 168 | 60 | 2.3 (3.68) | 4,440 / 2,820 | 690–1,050 | 8 (y 8–36) | 8 | **ranged 7 tiles** (fire arrow), every 1.5 s | cindervolley |
| `pyromagus` | Pyroclast Magus / ไพโรคลาสต์ เมกัส | 48 | Fire | 15,600 | 420 | 20% | 76 | 36% | 176 | 46 | 2.0 (3.2) | 5,250 / 3,330 | 825–1,245 | 6 (south, y 16–44) | 6.5 | **magic, ranged 6 tiles** (magma orb), every 2.0 s | meteor, eruption |

The player walks at 3.6 tiles/s: a chasing Scoria Hound (4.16) and Cinderbow (3.68) are faster than you.

**Ranged attack (`MON.rng`):** the monster stops at `rng` tiles and shoots; the hit lands when the arrow / orb arrives (0.30 / 0.38 s) and only if the monster is still alive. Arrows use the normal monster hit (can miss, armor applies).
**Magic attack (`MON.mag`):** never misses and ignores armor: `ATK × U(0.85, 1.15) × (1 − player MDEF) − player soft MDEF` (`magDmg`).

### Monster skills
Red circle rules as in `FIELD-RUINS.md`. `mg` = magic damage (formula above).
| Skill (EN / TH) | Used by | Circle | Wind-up | Damage | Cooldown | Range | Effect |
|---|---|---|---|---|---|---|---|
| Molten Pounce / กระโจนหินหลอม | Scoria Hound | on the player, r 1.8 | 0.7 s | ATK ×1.4 | 5–8 s | 6 | Burning 4 s |
| Cinder Volley / ห่าธนูเถ้าถ่าน | Cinderbow Revenant | on the player, r 2.4 | 1.0 s | ATK ×1.6 | 6–9 s | 9 | Burning 4 s |
| Meteor Fall / อุกกาบาตเพลิง | Pyroclast Magus | on the player, r 3.0 | 1.5 s | ATK ×2.4 (magic) | 9–12 s | 10 | Burning 6 s |
| Eruption Nova / ระเบิดปะทุ | Pyroclast Magus | around itself, r 4.6 | 1.4 s | ATK ×2.0 (magic) | 11–15 s | 4.6 | — |

## 5. Boss: Magma Gatekeeper — แมกมา เกทคีปเปอร์
*Warden of the Sealed Caldera / ผู้เฝ้าประตูปล่องภูเขาไฟ*. An obsidian titan with a molten core, a gate-shaped shield and a magma fist. Spawns in the arena (zone design x 22–27, y 38–42); never targeted by Idle; does not count for offline idle.

| Lv | Elem | HP | ATK | Hard DEF | Soft DEF | MDEF | HIT | FLEE | Attack | EXP | Scandium | Respawn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 55 | Fire | 120,000 | 560 | 32% | 90 | 30% | 195 | 40 | melee every 2.4 s, speed 1.4 | 31,500 / 20,000 | 10,000–16,000 | 120 s |

| Mechanic | Rule |
|---|---|
| **Caldera Slam** (`MON.magmagk.slam`) | every 9–12 s a red circle r 4 around it, 1.4 s wind-up, ATK ×2.0 (armor applies) + Burning 6 s. Warning text `caldera_warn` in the boss bar |
| **Magma Gate** (`magmagate`) | every 7–10 s, range 10: circle r 3.2 on the player, 1.2 s wind-up, magic ATK ×2.2 + Burning 5 s |
| **Enrage** (`enrage: 0.3`) | below 30% HP: toast "{boss} is enraged!", attacks 30% faster, slam cooldown ×0.6, skill cooldowns tick 1.5× faster, the core turns white-hot. Ends if it heals back above 30% (out of combat it regains 2%/s) |
| Immunities | stun and freeze (all bosses) |
| Defeat | toast `bd_magmagk`, system chat `sb_magmagk`, orange pillar |

**Drops:** Caldera Heart ×1 (quest item), Promethium / Neodymium / Samarium Ore ×2–3 each, Elite Core ×3, Gadolinium Ore ×5, Refine Ore ×2–4, 2 pieces of tier 50 gear (boss rarity table).

Boss code is now generic: per-boss `slam`, `warnK`, `enrage`, `heart`, `downK`, `sysK`, `col` in `MON`. Gadolith uses the old defaults (Crystal Slam r 3.4, ATK ×1.8, `boss_down`, `mat_gheart`).

## 6. Drops
| Monster | Drops (chance, amount) | Refine Ore |
|---|---|---|
| Scoria Hound | Scoria Fang 40% ×1–2 · Neodymium Ore 12% · Greater Red Potion 8% | 9% |
| Cinderbow Revenant | Revenant Ash 38% ×1–2 · Samarium Ore 10% · Ember Root 9% | 10% |
| Pyroclast Magus | Pyroclast Glyph 34% ×1–2 · Promethium Ore 8% · Greater Blue Potion 8% | 11% |

Gear drops: standard rules, tier 40 (normal 3%, Elite 12%).

### New items
| ID | EN / TH | Sell | Source |
|---|---|---|---|
| `mat_scoria` | Scoria Fang / เขี้ยวหินภูเขาไฟ | 85 Sc | Scoria Hound |
| `mat_neodym` | Neodymium Ore / แร่นีโอดิเมียม | 280 Sc | Scoria Hound, boss |
| `mat_revash` | Revenant Ash / เถ้าวิญญาณ | 100 Sc | Cinderbow Revenant |
| `mat_samar` | Samarium Ore / แร่ซาแมเรียม | 320 Sc | Cinderbow Revenant, boss |
| `mat_pyroglyph` | Pyroclast Glyph / อักขระไพโรคลาสต์ | 120 Sc | Pyroclast Magus |
| `mat_prometh` | Promethium Ore / แร่โพรมีเทียม | 400 Sc | Pyroclast Magus, boss |
| `mat_calheart` | Caldera Heart / หัวใจปล่องภูเขาไฟ (quest item) | 1,500 Sc | Magma Gatekeeper |

## 7. Quests
Hunts (15 kills, daily): Scoria Hound 50,625 / 32,400 EXP + 17,280 Sc; Cinderbow 59,940 / 38,070 + 20,880 Sc; Magus 70,875 / 44,955 + 24,840 Sc. Elite Hunt: Ashfall (3 Elites, 1 Y). **Boss Hunt: Magma Gatekeeper** (`qb_magmagk`): 30,000 / 19,000 EXP, 25,000 Sc, 40 Y.

## 8. Balance (simulator, `COMBAT-FORMULAS.md`)
Lv 40 characters with tier-40 gear of their own class, picked to be closest to CP 6,000 (the gate). 300 s, one monster at a time, no potions. Kills / deaths.
| Archetype | CP | Scoria Hound | Cinderbow | Pyroclast Magus | Magma Gatekeeper |
|---|---|---|---|---|---|
| Fighter | 5,982 | 17 / 0 | 13 / 0 | 10 / 0 | 1 / 0 |
| Ranger | 6,011 | 24 / 0 | 19 / 0 | 15 / 0 | 2 / 2 |
| Spellcaster | 5,394 | 30 / 0 | 25 / 0 | 17 / 0 | 0 / 5 |
| Supporter | 2,186 (best fit) | 4 / 0 | 3 / 0 | 1 / 0 | 0 / 0 |

⚠ The simulator still treats every monster as plain melee: it does **not** model ranged attacks, magic damage, skills, Burning, packs or the 6.5–9 tile aggro. In the real map you fight several fast monsters at once, so the true danger is much higher than this table; the recommended CP is 9,000 for that reason.

## Open questions
1. Gate CP: 6,000 lets in characters well below the recommended 9,000. Raise it once gear above tier 40 exists?
2. Supporter reaches only ~2,200 CP at Lv 40; it cannot enter alone.
3. Uses for the rare earth ores and the Caldera Heart (crafting / quests).
4. The simulator should learn ranged / magic monsters.
