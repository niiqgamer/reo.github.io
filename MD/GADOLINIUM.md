# Gadolinium — Town of Beginnings

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> Thai: **แกโดลิเนียม — เมืองแห่งการเริ่มต้น**

Every new character starts here as a **Beginner (C0)**, at the exact center of the map.

---

## 1. Map spec

Grid **49 × 49** tiles. Center tile **(24, 24)**; spawn at world **(24.5, 24.5)**.

| Feature | Location (tiles) | Notes |
|---|---|---|
| Main roads | rows 23–25 and columns 23–25 | Cobblestone, edge to edge |
| Plaza | circle radius 7.3 around (24.5, 24.5) | Star inlay, rings, curb |
| Gadolinium Crystal | footprint 19–21 × 19–21 | Floating crystal, orbit rings, interactable |
| Adventurers’ Guild | x 13, y 13, 5 × 4 | Flag on roof; future job change hub |
| Tool Dealer | x 29, y 15, 3 × 3 | Scandium shop |
| Silver Moon Inn | x 30, y 29, 4 × 4 | Two stories |
| Ironhart Forge | x 15, y 29, 4 × 3 | Chimney smoke; future refine NPC |
| Houses | (36,19) (9,19) (27,7) (37,35) (8,34) (18,40), 3 × 3 each | Varied roofs |
| Pond | ellipse center (37, 12), radii 4.2 × 3 | Blocked |
| Market stalls | (28,21) (21,28) | Striped awnings |
| Forest edge | outer 4 tiles | Road gaps act as gates (east gate → first field map) |

Every building door connects to the main road with a cobblestone path.

---

## 2. NPCs

| ID | Name (EN / TH) | Tile | Role |
|---|---|---|---|
| `lumi` | Guide Lumi / ผู้นำทาง ลูมิ | (26, 21) | Starter quest giver |
| `bors` | Bors the Merchant / พ่อค้าบอร์ส | (31, 18) | Potions, Scandium shop |
| `veyra` | Captain Veyra / กัปตันเวย์รา | (19, 26) | Combat and idle tips |
| `helper` | Archetype Helper Sera / ผู้แนะแนวอาร์คีไทป์ เซร่า | (28, 27) | Teaches the 4 archetypes; gives the Archetype Trial at Job Lv 10 |

NPCs face the player within 3.5 tiles. Click an NPC → walk to an adjacent tile → dialog opens on arrival.

**Planned NPCs** (see `JOBS.md`, `CORE-LOOP.md`): archetype change quest givers (4, likely at the Adventurers’ Guild), refine/card NPC at Ironhart Forge, daily dungeon gatekeeper.

---

## 3. Starter quest — “A New Beginning / จุดเริ่มต้นใหม่”

| Stage | Objective | Reward |
|---|---|---|
| 0 | Talk to Guide Lumi | +40 Base EXP |
| 1 | Visit Bors at the Tool Dealer | +5 Red Potions, +60 Base EXP |
| 2 | Touch the Gadolinium Crystal | Light pillar, +180 Base EXP |
| 3 | Complete | Leads into the C0 → C1 path |

The current target shows a bouncing gold **!**. The quest tracker’s **Go** button auto-walks to it.

---

## Open questions

1. Job EXP rewards for the starter quest.
2. Where each of the 4 archetype change quests starts (all at the Guild, or one NPC per archetype around town?).
3. Is the Gadolinium Crystal a save/respawn point or teleporter?
