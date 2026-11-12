# Gadolinium Field 01 — ทุ่งแกโดลิเนียม 01

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> Sub-title: **Outskirts of Gadolinium / ชานเมืองแกโดลิเนียม**. Recommended CP **150**. Upper-right portal (30, 2) → Field 02. Each monster type also has 1 Elite (see `FIELD-02.md`). Idle rules moved to `IDLE.md`.

First hunting map, reached through the **east gate portal** of Gadolinium.

## 1. Travel

| Portal | Tile | Goes to | Arrival |
|---|---|---|---|
| Gadolinium east gate | (46, 24) | Field 01 | (5.5, 26.5) |
| Field 01 west portal | (2, 24) | Gadolinium | (44.5, 24.5) |

- Stepping within 0.6 tiles of a portal starts a 0.38 s fade, swaps the map, then saves.
- **Arrival rule:** you always appear on the walkable tile nearest to the destination map's portal that leads back to where you came from (1 tile away). Never a random or fixed coordinate. Warp scrolls (Fly Wing) and Return to town are the only exceptions: they go to a random tile / the town center.
- Safe zone: no monsters spawn within 7 tiles of the west portal.

## 2. Map

49 × 49 tiles, alien meadow (teal grass, glowing flowers), winding dirt paths, two glowing pools, giant mushrooms, crystal clusters, mossy rocks, teal-canopy forest edge.

## 3. Monsters (passive — they never attack first)

| ID | Name (EN / TH) | Lv | HP | ATK | DEF | Atk speed | Base / Job EXP | Scandium | Drop | Count | Zone (x) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lumite` | Lumite / ลูไมต์ — floating three-eyed jelly | 1 | 60 | 10 | 1 | 1.6 s | 20 / 14 | 3–7 | Lumite Gel 45% | 9 | 5–24 |
| `crawlix` | Crawlix / ครอลลิกซ์ — crystal-backed crawler | 3 | 125 | 17 | 4 | 1.5 s | 42 / 30 | 6–12 | Crawlix Shard 35% | 7 | 17–36 |
| `oculoth` | Oculoth / โอคูลอธ — floating rock eye | 6 | 250 | 32 | 7 | 1.8 s | 90 / 60 | 12–22 | Oculoth Lens 30% | 5 | 30–46 |

All monsters: 8% chance of **Gadolinium Ore**. Respawn 8–15 s after death at a random point in their zone.

Behavior: wander near home → when hit, become aggressive, chase at 1.6× speed and attack in melee → give up beyond 14 tiles and return home. Out-of-combat monsters regenerate 5% HP/s.

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
