# Gadolinium Field 03 — ทุ่งแกโดลิเนียม 03

> Part of the REO docs. Sub-title: **Silverfrost Basin / แอ่งน้ำแข็งเงิน**. Recommended CP **900**. Home of the first boss, **Gadolith**.

## Travel
| Portal | Tile | Goes to | You arrive |
|---|---|---|---|
| Field 02 upper portal | (19, 2) | Field 03 | next to Field 03's return portal |
| Field 03 lower portal | (26, 46) | Field 02 | next to Field 02's upper portal |

Arrival always follows the portal rule in `FIELD-01.md` (nearest walkable tile beside the matching portal). Auto-quest knows the whole chain Town → 01 → 02 → 03.

## Look
Frosted blue-silver meadow, ice-blue pools, frosted and silver-white trees, pale crystal clusters and blue mushrooms. At the top of the map is the **boss arena**: a 5.6-tile stone circle with a glowing rune circle on the ground. No normal monsters spawn inside it.

## Monsters (passive until hit)
Same three sprites as Fields 01–02, recoloured icy, stronger.

| ID | Name (EN / TH) | Sprite | Lv | Element | HP | ATK | Hard DEF | MDEF | Base / Job EXP | Scandium | Drop | Count | Area |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `glacilite` | Glacilite / กลาซิไลต์ | Lumite | 13 | Water | 540 | 44 | 8% | 20% | 230 / 150 | 38–60 | Glacial Gel 40% | 9 + 1 Elite | south-west |
| `rimeback` | Rimeback / ไรม์แบ็ค | Crawlix | 15 | Earth | 760 | 54 | 28% | 8% | 330 / 215 | 52–82 | Rime Plate 35% | 7 + 1 Elite | south-east |
| `magnoculus` | Magnoculus / แมกโนคูลัส | Oculoth | 17 | Wind | 1,000 | 66 | 12% | 32% | 470 / 300 | 80–120 | Magnet Lens 30% | 5 + 1 Elite | north |

Elite rules are unchanged (`FIELD-02.md`): ×1.3 size, gold circle, HP ×5, ATK ×1.6, EXP ×5.

## Boss — Gadolith, the Crystal Warden (กาโดลิธ ผู้พิทักษ์คริสตัล)

| Property | Value |
|---|---|
| Level / element | **Lv 20** / Earth (weak to Fire, so Fire Bolt) |
| Stats | HP **8,000**, ATK 58, hard DEF 25%, soft DEF 12, MDEF 20%, attack every 2.6 s, speed 1.0 |
| Size | **×2.2** (Elites are ×1.3; the biggest Elite is about ×1.7) |
| Look | New sprite: floating crystal warden with a glowing eye-core, crown spikes, shoulder crystals, orbiting shards and hanging spikes. Core turns orange when it fights |
| **Aura** | Large rune circle on the ground (rotating dashed ring + hexagram + shock ring every 2.4 s) with rising motes. Ice blue when calm, **ember orange when aggro**. Bigger and busier than the Elite circle |
| Label / HP | "◆ Boss Gadolith Lv 20", wide HP bar over its head, and a **boss HP bar on the HUD** (shows within 12 tiles or while fighting) |
| Behavior | Passive until hit. Leashes at 16 tiles and heals 2%/s when it resets (normal monsters 5%/s) |
| **Crystal Slam** | Every 9–12 s while fighting it stops and marks a red circle (radius 3.4 tiles) for 1.4 s. If you are inside when it lands: ATK × 1.8 damage (armor applies). The HUD bar flashes "⚠ Crystal Slam!". Step out to avoid it |
| Immunities | Stun and freeze (shows "Immune") |
| Rewards | 2,600 Base EXP, 1,700 Job EXP, 1,000–1,600 Scandium, **Crystal Heart ×1–2**, Elite Core ×3, Gadolinium Ore ×5 |
| Respawn | 120 s (**test value**, production should be much longer) |
| Idle | Idle **never auto-targets the boss**. It is a hands-on fight. Auto-quest will target it if a quest asks for it |

### Balance (from `tests/test_combat.js`)
Simulated with auto stats and each archetype's skill AI, no potions and no kiting (the simulator does not model Crystal Slam either):

| CP | Fighter | Ranger | Spellcaster | Supporter |
|---|---|---|---|---|
| **1,100** (test value; the map recommends **900**) | 0 deaths per kill | 0.33 | 0.35 | 0 |
| 1,300 | 0 | 0.08 | 0.07 | 0 |

Field 03 normals at CP 900: 28–30 kills per 5 min with 0 deaths for every archetype (Fighter Lv 16, Ranger/Spellcaster Lv 22).

## Items (new)
| ID | EN / TH | Source |
|---|---|---|
| `mat_gel3` | Glacial Gel / เจลน้ำแข็ง | Glacilite |
| `mat_rime` | Rime Plate / แผ่นเกล็ดน้ำแข็ง | Rimeback |
| `mat_mag` | Magnet Lens / เลนส์แม่เหล็ก | Magnoculus |
| `mat_gheart` | Crystal Heart / หัวใจคริสตัล | Gadolith |

## Quests here
See `QUESTS.md`: 3 hunts, an Elite hunt, a repeatable boss hunt, and the new main-quest chapters (reach Field 03, defeat Gadolith).

## Open questions
1. Boss respawn and daily limits (and whether it becomes an instance boss, see `CORE-LOOP.md`).
2. Party fights: boss HP scaling and loot sharing.
3. A second boss mechanic (adds, enrage) for later bosses.
4. What the Crystal Heart is used for (refine? card?).
