# Road to the Ruins — ถนนสายเพลิงผลาญ

> Part of the REO docs (v19). Sub-title: **Road of Cinders / ถนนสายเพลิงผลาญ**. Recommended CP **3,000**. A road of devouring fire to merciless ruins: black flames from the pits of hell scorch every step, and the land is ready to burn every intruder to ash.
> TH: ถนนสายเพลิงผลาญมุ่งสู่ซากปรักหักพังอันไร้ซึ่งความปรานี ทุกย่างก้าวแผดเผาด้วยเปลวเพลิงทมิฬจากขุมนรก แผ่นดินนี้ถูกหล่อหลอมด้วยอัคคีเดือดระอุ พร้อมมอดไหม้ผู้บุกรุกให้กลายเป็นเถ้าธุลีไปตลอดกาล

## 1. Entry rules
| Rule | Value |
|---|---|
| Gate | Town south gate, tile (24, 46) |
| Requirement | Base Lv **30+** AND Combat Power **3,000+**. Both are checked at the portal and for World Map teleport |
| If not met | The player is pushed back to the tile beside the gate and a toast shows the requirement and the player's own Lv and CP. The portal never opens |
| Warning sign | Next to the gate: "Monster Lv.30+" with a red WARNING banner |
| Teleport | Needs a visited map (150 Scandium per map passed) and the same Lv and CP |

## 2. Travel
| Portal | Tile | Goes to | You arrive |
|---|---|---|---|
| Town south gate | (24, 46) | Road to the Ruins | beside the north portal below |
| Ruins north portal | (28, 2) | Gadolinium | beside the town south gate |

Arrival follows the portal rule in `FIELD-01.md` (nearest walkable tile beside the matching portal). No monster spawns within 7 tiles of the portal, and monsters ignore the player for 3 s after any map change.

## 3. Look
49 × 49 tiles. Scorched black-red ground with rust-brick roads, charred trees with ember tips, **5 lava pools** (blocked), ember crystals. **Broken columns and burning braziers** line the north–south road in pairs every 5 tiles, plus random ones. Roads: north–south (`x = 24 + round(sin(0.16y+0.8)·4)`) and east–west (`y = 26 + round(sin(0.19x)·3)`). Orange embers float in the air. Music: `ruins` (104 BPM, double harmonic, driving drums, pulsing bass).

## 4. Monsters (**aggressive**, with skills)
Aggressive means a monster that sees the player inside its **aggro range** (Elites +1 tile) starts chasing at ×1.6 speed and attacks first, with a red "!" above its head. It gives up beyond 16 tiles. Respawn 8–15 s (Elite 45–60 s). Every type also has 1 Elite (rules in `FIELD-02.md`).

| ID | Name (EN / TH) | Lv | Element | HP | ATK | Hard DEF | Soft DEF | MDEF | HIT | FLEE | Base / Job EXP | Scandium | Count | Aggro | Skills |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `cinderling` | Cinderling / ซินเดอร์ลิง | 32 | Fire | 3,000 | 104 | 10% | 24 | 22% | 112 | 54 | 1,250 / 800 | 190–290 | 8 + 1 Elite (north, y 5–24) | 6.5 | emberburst |
| `magmaback` | Magmaback / แมกมาแบ็ค | 35 | Fire | 4,000 | 122 | 26% | 34 | 12% | 120 | 40 | 1,480 / 940 | 230–350 | 7 + 1 Elite (middle, y 16–38) | 5.5 | lavaspit |
| `ashsentinel` | Ashen Sentinel / แอชเชนเซนทิเนล | 38 | Fire | 5,200 | 140 | 24% | 38 | 26% | 128 | 30 | 1,750 / 1,110 | 275–415 | 5 + 1 Elite (south, y 28–45) | 5 | inferno, ashwave |

### Monster skills
A skill puts a **red circle on the ground**; it lands after the wind-up and hits the player for `ATK × multiplier` (armor applies) only if the player is still inside. Move out of the circle to avoid it. A cast stops the monster while it winds up. First cast comes 35–85% of one cooldown after the fight starts.

| Skill (EN / TH) | Used by | Circle | Wind-up | Damage | Cooldown | Range | Effect |
|---|---|---|---|---|---|---|---|
| Ember Burst / ระเบิดเถ้าถ่าน | Cinderling | on the player, r 1.7 | 0.8 s | ATK ×1.2 | 4.5–7 s | 7 | Burning 5 s |
| Lava Spit / พ่นลาวา | Magmaback | on the player, r 2.1 | 1.0 s | ATK ×1.5 | 6–9 s | 8 | Burning 4 s |
| Inferno Pillar / เสาเพลิงนรก | Ashen Sentinel | on the player, r 2.8 | 1.3 s | ATK ×1.9 | 8–11 s | 8 | Burning 6 s |
| Ashen Wave / คลื่นเถ้าถ่าน | Ashen Sentinel | around itself, r 4.2 | 1.4 s | ATK ×1.7 | 10–14 s | 4.2 | — |

**Burning:** 10% of the monster's ATK per second for the stated time (tick every 1 s). **Soaked:** movement speed −35%. Both show as red-bordered icons under the character card and are cleared on death.

## 5. Drops
| Monster | Drops (chance, amount) | Refine Ore |
|---|---|---|
| Cinderling | Cinder Ash 40% ×1–2 · Ember Core 13% · Ember Root 9% | 8% |
| Magmaback | Magma Plate 36% ×1–2 · Lava Glass 12% · Greater Red Potion 7% | 9% |
| Ashen Sentinel | Scorched Relic 32% ×1–2 · Inferno Shard 10% · Aether Dew 7% | 10% |

Gear drops use the standard rules (`ITEMS.md` §4): tier Lv 30, normal 3%, Elite 12%. No boss on this map yet.

### New items
| ID | EN / TH | Sell | Source |
|---|---|---|---|
| `mat_cinder` | Cinder Ash / ขี้เถ้าเพลิง | 30 Sc | Cinderling |
| `mat_embercore` | Ember Core / แกนเพลิง | 105 Sc | Cinderling |
| `mat_magma` | Magma Plate / แผ่นหินหลอม | 38 Sc | Magmaback |
| `mat_lavaglass` | Lava Glass / แก้วลาวา | 125 Sc | Magmaback |
| `mat_relic` | Scorched Relic / ซากโบราณไหม้เกรียม | 45 Sc | Ashen Sentinel |
| `mat_infernoshard` | Inferno Shard / เศษหัวใจนรก | 160 Sc | Ashen Sentinel |

## 6. Balance (simulator, `COMBAT-FORMULAS.md`)
Characters built to the gate CP (gear scaled until `combatPower` ≈ 3,000, 300 s per fight, no potions, no kiting; the simulator does not model monster skills):
| Archetype | CP | Cinderling | Magmaback | Ashen Sentinel |
|---|---|---|---|---|
| Fighter (Lv 30) | 2,983 | 27 kills · 0 deaths | 20 · 0 | 16 · 0 |
| Ranger | 3,074 | 29 · 0 | 21 · 1 | 17 · 1 |
| Spellcaster | 2,567 (fit stopped short of 3,000) | 10 · 4 | 9 · 4 | 5 · 5 |
| Supporter | 2,921 | 31 · 0 | 28 · 0 | 20 · 0 |

Kills per 5 min, one monster at a time. Spellcasters at this CP are glass cannons; expect them to need potions and kiting.

## Open questions
1. Boss for this map (none yet).
2. Whether the CP gate should also kick out a character whose CP drops below the gate while inside (today: no).
3. Spellcaster survival at the gate CP (glass cannon: CP comes mostly from damage).
