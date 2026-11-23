# Gadolinium — Town of Beginnings

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> Thai: **แกโดลิเนียม — เมืองแห่งการเริ่มต้น**

Every new character starts here as a **Beginner (C0)**, in front of the Gadolinium Crystal at the center of the map.

---

## 1. Map spec

Grid **98 × 98** tiles (2× the old 49 × 49 town). Center **(49, 49)**; spawn at **(54.5, 54.5)**, just in front of the monument.

| Feature | Location (tiles) | Notes |
|---|---|---|
| Main roads | 4 tiles wide (rows/columns 47–50) | Cobblestone, edge to edge |
| Plaza | circle radius 11.5 around (49, 49) | Mosaic rays, compass star, gold rings, curb, 12 lamps on the rim |
| Gadolinium Crystal monument | center (49, 49), blocked radius 4.4 | About 2× the old crystal: 3-tier round dais with rune bands, 4 crystal pylons feeding light arcs, the original four-face crystal scaled 2.8× and floating, rune rings, orbiting shards, light beam, pulse ring. Interactable |
| Market ring | 8 stalls at radius 14.5 between the roads | Striped awnings |
| Adventurers’ Guild | x 26, y 26, 5 × 4 | Flag on roof |
| Tool Dealer | x 58, y 30, 3 × 3 | Scandium shop |
| Silver Moon Inn | x 60, y 58, 4 × 4 | Two stories |
| Ironhart Forge | x 30, y 58, 4 × 3 | Chimney smoke |
| Houses | 10 houses, 3 × 3 each (see `HOUSES` in `buildTown`) | Varied roofs |
| Ponds | (74, 24) radii 6.7 × 4.8 and (20, 82) radii 4 × 3 | Blocked |
| Forest edge | outer 4 tiles | Road gaps act as gates |
| East gate | (95, 49) | → Field 01 |
| West gate | (2, 49) | → Path to the Geosyncline. Warning sign at (4, 45). Needs Lv 25+ and CP 2,000+ |
| South gate | (49, 95) | → Road to the Ruins. Warning sign at (45, 93). Needs Lv 30+ and CP 3,000+ |

Every building door connects to the main road with a cobblestone path.

The ground texture is drawn in chunks of up to 2048 px (`groundGen` / `groundChunk`) and its scale drops on big maps to stay inside a memory budget (`groundScale`). Every device keeps only the current map and the one ahead in memory.

---

## 2. NPCs

| ID | Name (EN / TH) | Anchor in code → tile after placement | Role |
|---|---|---|---|
| `lumi` | Guide Lumi / ผู้นำทาง ลูมิ | (55, 43) → (55, 43), beside the monument | Starter quest giver |
| `bors` | Bors the Merchant / พ่อค้าบอร์ส | (61, 36) → (59, 36), Tool Dealer path | Potions, Scandium shop |
| `veyra` | Captain Veyra / กัปตันเวย์รา | (37, 62) → (37, 61), Forge path | Combat and idle tips |
| `helper` | Archetype Helper Sera / ผู้แนะแนวอาร์คีไทป์ เซร่า | (57, 63) → (57, 62), Inn path | Teaches the 4 archetypes; takes the Archetype Trial turn-in (the trial starts automatically at Job Lv 10 with Basic Skill Lv 10) |
| `narvis` | Narvis / นาร์วิส (role tag POCKET DIMENSION) | (41, 57) → (41, 57), west edge of the plaza (`NARVIS_AT`) | Opens the Pocket Dimension (personal storage) for Basic Skill Lv 5+ (`ITEMS.md` §7). Every main town gets its own Narvis |

`placeTownNpcs` snaps each NPC to the nearest free road or plaza tile where no prop covers it (`TOWN-ALIEN.md` §2), so the final tile can be one off the anchor in `index.html`.

NPCs face the player within 3.5 tiles. Click an NPC → walk to an adjacent tile → dialog opens on arrival.

**Planned NPCs** (see `JOBS.md`, `CORE-LOOP.md`): archetype change quest givers (4, likely at the Adventurers’ Guild), refine/card NPC at Ironhart Forge, daily dungeon gatekeeper.

---

## 3. Starter quest — “A New Beginning / จุดเริ่มต้นใหม่”

The main quest starts here and now has **9 chapters**: Lumi → Bors (+5 Red Potions) → touch the Gadolinium Crystal (light pillar) → 3 kills in Field 01 → reach Field 02 → 3 kills in Field 02 → reach Field 03 → 3 kills in Field 03 → return to Lumi. Rewards per chapter (Base / Job EXP, Yttrium) are in `QUESTS.md`.

The current target shows a bouncing gold **!**. The quest tracker’s **Go** button auto-walks to it, across maps.

---

## Open questions

1. ✅ Job EXP rewards for the starter quest are set per chapter (`QUESTS.md`).
2. Where each of the 4 archetype change quests starts (all at the Guild, or one NPC per archetype around town?).
3. Is the Gadolinium Crystal a save/respawn point or teleporter?
