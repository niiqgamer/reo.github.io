# Path to the Geosyncline — เส้นทางแห่งรอยเลื่อนบรรพกาล

> Part of the REO docs (v19). Sub-title: **Ancient Fault Line / รอยเลื่อนบรรพกาล**. Recommended CP **2,000**. The road of the ancient fault lines: cracked earth seething with seismic calamity, mysterious deep water washing over a lost civilization, and crushing pressure under the crust.
> TH: เส้นทางแห่งรอยเลื่อนบรรพกาล พื้นพิภพปริแตกคุกรุ่นด้วยมหาภัยธรณี ขณะที่สายน้ำลึกลับหลั่งไหลอาบซากอารยธรรมที่สูญหาย ที่นี่คือเขตแดนอันเดือดพล่าน ซึ่งแรงกดดันมหาศาลใต้เปลือกโลกพร้อมบดขยี้ทุกสรรพสิ่งให้จมดิ่งสู่ก้นเหวแห่งกาลเวลา

## 1. Entry rules
| Rule | Value |
|---|---|
| Gate | Town west gate, tile (2, 24) |
| Requirement | Base Lv **25+** AND Combat Power **2,000+**. Both are checked at the portal and for World Map teleport |
| If not met | The player is pushed back to the tile beside the gate and a toast shows the requirement and the player's own Lv and CP. The portal never opens |
| Warning sign | Next to the gate: "Monster Lv.25+" with a red WARNING banner |
| Teleport | Needs a visited map (150 Scandium per map passed) and the same Lv and CP |

## 2. Travel
| Portal | Tile | Goes to | You arrive |
|---|---|---|---|
| Town west gate | (2, 24) | Path to the Geosyncline | beside the east portal below |
| Geosyncline east portal | (46, 22) | Gadolinium | beside the town west gate |

Arrival follows the portal rule in `FIELD-01.md` (nearest walkable tile beside the matching portal). No monster spawns within 7 tiles of the portal, and monsters ignore the player for 3 s after any map change.

## 3. Look
49 × 49 tiles. Dark slate-brown ground with grey dead trees. **Fault cracks** (4 glowing teal fissures) are blocked tiles that only break where a road crosses; they never reach the map edge, so no area is cut off. 5 blocked pools of glowing water. **Ancient steles** with pulsing teal glyphs, teal crystals, mossy rocks, and two steles flanking the east portal. Roads: one east–west road (`y = 24 + round(sin(0.2x+1)·3)`) and one north–south road (`x = 22 + round(sin(0.17y)·3)`). Music: `geo` (76 BPM, harmonic minor, soft drums).

## 4. Monsters (**aggressive**, with skills)
Aggressive means a monster that sees the player inside its **aggro range** (Elites +1 tile) starts chasing at ×1.6 speed and attacks first, with a red "!" above its head. It gives up beyond 16 tiles. Respawn 8–15 s (Elite 45–60 s). Every type also has 1 Elite (rules in `FIELD-02.md`).

| ID | Name (EN / TH) | Lv | Element | HP | ATK | Hard DEF | Soft DEF | MDEF | HIT | FLEE | Base / Job EXP | Scandium | Count | Aggro | Skills |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `faultcrawler` | Faultcrawler / ฟอลต์ครอว์เลอร์ | 25 | Earth | 2,000 | 78 | 22% | 22 | 8% | 90 | 36 | 750 / 480 | 120–180 | 8 + 1 Elite (east part, x 24–45) | 5.5 | tremor |
| `tidewraith` | Tidewraith / ไทด์เรธ | 27 | Water | 2,300 | 84 | 8% | 16 | 25% | 96 | 44 | 880 / 560 | 140–210 | 7 + 1 Elite (middle, x 10–36) | 6 | undertow |
| `stratagolem` | Strata Golem / สตราตาโกเลม | 30 | Earth | 3,200 | 100 | 26% | 26 | 12% | 104 | 24 | 1,060 / 680 | 170–260 | 5 + 1 Elite (west, x 3–24) | 4.5 | crust, debris |

### Monster skills
A skill puts a **red circle on the ground**; it lands after the wind-up and hits the player for `ATK × multiplier` (armor applies) only if the player is still inside. Move out of the circle to avoid it. A cast stops the monster while it winds up. First cast comes 35–85% of one cooldown after the fight starts.

| Skill (EN / TH) | Used by | Circle | Wind-up | Damage | Cooldown | Range | Effect |
|---|---|---|---|---|---|---|---|
| Tremor Stomp / กระทืบสั่นสะเทือน | Faultcrawler | around itself, r 3.0 | 1.1 s | ATK ×1.5 | 6–9 s | 3.2 | — |
| Undertow / คลื่นดูดลึก | Tidewraith | on the player, r 1.8 | 1.0 s | ATK ×1.4 | 5–8 s | 8 | Soaked 4 s |
| Crust Crush / บดเปลือกโลก | Strata Golem | around itself, r 3.6 | 1.3 s | ATK ×1.9 | 8–11 s | 3.6 | — |
| Falling Debris / ก้อนหินถล่ม | Strata Golem | on the player, r 2.2 | 1.1 s | ATK ×1.5 | 7–10 s | 7 | — |

**Burning:** 10% of the monster's ATK per second for the stated time (tick every 1 s). **Soaked:** movement speed −35%. Both show as red-bordered icons under the character card and are cleared on death.

## 5. Drops
| Monster | Drops (chance, amount) | Refine Ore |
|---|---|---|
| Faultcrawler | Fault Shard 40% ×1–2 · Seismic Core 14% · Greater Red Potion 6% | 6% |
| Tidewraith | Abyssal Tear 38% ×1–2 · Sunken Glyph 12% · Frost Bloom 8% | 7% |
| Strata Golem | Strata Slab 35% ×1–2 · Pressure Crystal 12% · Sage Leaf 7% | 8% |

Gear drops use the standard rules (`ITEMS.md` §4): tier Lv 20, normal 3%, Elite 12%. No boss on this map yet.

### New items
| ID | EN / TH | Sell | Source |
|---|---|---|---|
| `mat_fault` | Fault Shard / เศษหินรอยเลื่อน | 20 Sc | Faultcrawler |
| `mat_seismic` | Seismic Core / แกนแผ่นดินไหว | 70 Sc | Faultcrawler |
| `mat_tide` | Abyssal Tear / หยดน้ำเหวลึก | 24 Sc | Tidewraith |
| `mat_glyph` | Sunken Glyph / อักขระจมน้ำ | 85 Sc | Tidewraith |
| `mat_strata` | Strata Slab / แผ่นชั้นหิน | 28 Sc | Strata Golem |
| `mat_press` | Pressure Crystal / คริสตัลแรงอัด | 100 Sc | Strata Golem |

## 6. Balance (simulator, `COMBAT-FORMULAS.md`)
Characters built to the gate CP (gear scaled until `combatPower` ≈ 2,000, 300 s per fight, no potions, no kiting; the simulator does not model monster skills):
| Archetype | CP | Faultcrawler | Tidewraith | Strata Golem |
|---|---|---|---|---|
| Fighter (Lv 25) | 1,987 | 26 kills · 0 deaths | 25 · 0 | 17 · 0 |
| Ranger | 2,052 | 26 · 0 | 26 · 0 | 18 · 1 |
| Spellcaster | 1,986 | 33 · 0 | 17 · 2 | 18 · 2 |
| Supporter | 1,965 | 35 · 0 | 27 · 0 | 24 · 0 |

Kills per 5 min, one monster at a time. With two monsters at once Fighters still take at most 1 death and Rangers 2–3; Spellcasters 3–5.

## Open questions
1. Boss for this map (none yet).
2. Whether the CP gate should also kick out a character whose CP drops below the gate while inside (today: no).
3. Spellcaster survival at the gate CP (glass cannon: CP comes mostly from damage).
