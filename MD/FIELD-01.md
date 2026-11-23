# Gadolinium Field 01 — ทุ่งแกโดลิเนียม 01

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> Sub-title: **Outskirts of Gadolinium / ชานเมืองแกโดลิเนียม**. Recommended CP **150**. North portal (61, 2) → Field 02. Each monster type also has 2 Elites (see `FIELD-02.md`). Idle rules moved to `IDLE.md`.
> All tiles below are on the real 98 × 98 grid.

First hunting map, reached through the **east gate portal** of Gadolinium.

## 1. Travel

| Portal | Tile | Goes to | Arrival |
|---|---|---|---|
| Gadolinium east gate | (95, 49) | Field 01 | next to the Field 01 west portal |
| Field 01 west portal | (2, 49) | Gadolinium | next to the town east gate |
| Field 01 north portal | (61, 2) | Field 02 | next to the Field 02 south portal |

- Stepping within 0.6 tiles of a portal starts a 0.38 s fade, swaps the map, then saves.
- **Arrival rule:** you always appear on the walkable tile nearest to the destination map's portal that leads back to where you came from (the closest ring of tiles around it, 1–6 tiles out, picking the tile that faces the map centre; `arriveAt` / `walkableNear`). Never a random or fixed coordinate. Warp scrolls (Fly Wing) and Return to town are the only exceptions: they go to a random tile / the town center.
- Safe zone: no monster spawns within 8 tiles of any portal (`spawnPos`).

## 2. Map

98 × 98 tiles (the original 49 × 49 layout scaled 2×; props keep their size, 3× monsters, 2 Elites per kind; portals sit 2 tiles from the map edge), alien meadow (teal grass, glowing flowers), winding dirt paths, two glowing pools, giant mushrooms, crystal clusters, mossy rocks, teal-canopy forest edge.

## 3. Monsters (passive — they never attack first)

| ID | Name (EN / TH) | Lv | HP | ATK | DEF | Atk speed | Base / Job EXP | Scandium | Main drop | Count | Zone (x, 98 grid) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lumite` | Lumite / ลูไมต์ — floating three-eyed jelly | 1 | 60 | 10 | 1 | 1.6 s | 20 / 14 | 3–7 | Lumite Gel 45% | 27 + 2 Elites | 10–48 |
| `crawlix` | Crawlix / ครอลลิกซ์ — crystal-backed crawler | 3 | 125 | 17 | 4 | 1.5 s | 42 / 30 | 6–12 | Crawlix Shard 35% | 21 + 2 Elites | 34–72 |
| `oculoth` | Oculoth / โอคูลอธ — floating rock eye | 6 | 250 | 32 | 7 | 1.8 s | 90 / 60 | 12–22 | Oculoth Lens 30% | 15 + 2 Elites | 60–92 |

Count = `MON.count × 3` (`MON_MULT`) plus 2 Elites per kind (`ELITE_PER`). Full loot tables and Refine Ore chances: `ITEMS.md` §4. Respawn 8–15 s after death at a random point in their zone.

**Gadolinium Ore** is no longer a Field 01 drop: since the per-monster loot tables (`LOOT`) it only comes from Gadolith (×5). The Ore Delivery quest (3 ore) therefore needs a boss kill (see Open questions).

Behavior: wander near home → when hit, become aggressive, chase at 1.6× speed and attack in melee → give up beyond 16 tiles and return home. Out-of-combat monsters regenerate 5% HP/s.

## 4. Combat

Live combat rules are in `COMBAT-FORMULAS.md`. The v1 prototype numbers that used to sit here were removed so there is only one source of truth. Monster stats are in this file and `FIELD-02.md` / `FIELD-03.md`.

## 5. Idle

Rules, offline rewards and the VIP split live in `IDLE.md`. The v1 idle loop and offline formula were removed.

## 6. Save

Save keys are listed in `ACCOUNTS.md` §4 (guest save `reo.gameState.v2`; accounts use `reo.save.<id>.v2`). Autosave runs every 5 s and on map change, level up, quest progress, idle toggle, tab hide and page close.

## Open questions

1. Death penalty (EXP loss?) for later maps.
2. Final balance of EXP and kill speed — the prototype is tuned fast for testing.
3. Should idle be allowed in town at all, or only in fields?
4. Offline reward efficiency and cap.
5. Should Field 01 monsters drop Gadolinium Ore again (the old 8%), so Ore Delivery can be done without the boss?
