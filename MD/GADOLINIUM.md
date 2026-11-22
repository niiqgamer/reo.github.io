# Gadolinium — Town of Beginnings

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> Thai: **แกโดลิเนียม — เมืองแห่งการเริ่มต้น**

Every new character starts here as a **Beginner (C0)**, in front of the Gadolinium Crystal at the center of the map.

---

## 1. Map spec

Grid **147 × 147** tiles (3× the old 49 × 49 town). Center **(73.5, 73.5)**; spawn at **(79.5, 79.5)**, just in front of the monument.

| Feature | Location (tiles) | Notes |
|---|---|---|
| Main roads | 5 tiles wide, centered on row/column 73 | Cobblestone, edge to edge |
| Plaza | circle radius 15.5 around (73.5, 73.5) | Mosaic rays, compass star, gold rings, curb, 16 lamps on the rim |
| Gadolinium Crystal monument | center (73.5, 73.5), blocked radius 4.4 | About 2× the old crystal: 3-tier round dais with rune bands, 4 crystal pylons feeding light arcs, large floating crystal, rune rings, orbiting shards, light beam, pulse ring. Interactable |
| Market ring | 8 stalls at radius 18.5 between the roads | Striped awnings |
| Adventurers’ Guild | x 39, y 39, 5 × 4 | Flag on roof |
| Tool Dealer | x 87, y 45, 3 × 3 | Scandium shop |
| Silver Moon Inn | x 90, y 87, 4 × 4 | Two stories |
| Ironhart Forge | x 45, y 87, 4 × 3 | Chimney smoke |
| Houses | 13 houses, 3 × 3 each (see `HOUSES` in `buildTown`) | Varied roofs |
| Ponds | (111, 36) radii 8.4 × 6 and (30, 120) radii 5.6 × 4 | Blocked |
| Forest edge | outer 4 tiles | Road gaps act as gates |
| East gate | (144, 73) | → Field 01 |
| West gate | (2, 73) | → Path to the Geosyncline. Warning sign at (4, 69). Needs Lv 25+ and CP 2,000+ |
| South gate | (73, 144) | → Road to the Ruins. Warning sign at (69, 142). Needs Lv 30+ and CP 3,000+ |

Every building door connects to the main road with a cobblestone path.

The ground texture is drawn in chunks of up to 2048 px (`groundGen` / `groundChunk`) and its scale drops on big maps to stay inside a memory budget (`groundScale`). Every device keeps only the current map and the one ahead in memory.

---

## 2. NPCs

| ID | Name (EN / TH) | Anchor tile | Role |
|---|---|---|---|
| `lumi` | Guide Lumi / ผู้นำทาง ลูมิ | (80, 68), beside the monument | Starter quest giver |
| `bors` | Bors the Merchant / พ่อค้าบอร์ส | (90, 51), Tool Dealer path | Potions, Scandium shop |
| `veyra` | Captain Veyra / กัปตันเวย์รา | (52, 91), Forge path | Combat and idle tips |
| `helper` | Archetype Helper Sera / ผู้แนะแนวอาร์คีไทป์ เซร่า | (86, 92), Inn path | Teaches the 4 archetypes; gives the Archetype Trial at Job Lv 10 |

`placeTownNpcs` snaps each NPC to the nearest free road or plaza tile.

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
