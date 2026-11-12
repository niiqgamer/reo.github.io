# Quests & Auto-quest

> Part of the REO docs.

## Rules
- Unlimited quests can be accepted at once.
- The on-screen tracker shows up to **5** tracked quests, color-coded: **Main** gold `#E9C46A`, **Job** violet `#B98CFF`, **Side** blue `#5AA9FF`, **Normal** green `#3FC6A8`.
- Quest progress updates live: the tracker and the open Quests window refresh on every kill, no reopening needed.
- The tracker panel collapses/expands. Quests window: accept, track/untrack, auto, abandon (not Main).
- **Auto-quest:** tapping a quest in the tracker walks the hero to the next objective across maps (via portals): talks to the NPC, touches the crystal, or hunts the right monsters until done. Any manual map click cancels it.

## Objective types
`talk(npc)` · `crystal` · `reach(map)` · `kill(map, mon?, elite?, n)` · `collect(item, n, consume?)`

## Quests window
Available quests are **grouped by map** (Field 01, 02, 03, Path to the Geosyncline, Road to the Ruins, General) with the map's recommended CP, and sorted by monster level. Each row shows type, repeatable tag and the monster level.

## Current quests
| ID | Type | Title (EN / TH) | Stages | Reward |
|---|---|---|---|---|
| `arch` | **Job** (violet `#B98CFF`), from Archetype Helper only | Archetype Trial / บททดสอบอาร์คีไทป์ | Job Lv 10 → defeat 10 Elites (any field) → return and choose 1 of 4 archetypes | 500 Base EXP, 30 Y, becomes C1 |
| `main` | Main | A New Beginning / จุดเริ่มต้นใหม่ | Lumi → Bors → Crystal → 10 kills in Field 01 → reach Field 02 → defeat 1 Elite → reach Field 03 → defeat Gadolith (see below) | per stage; 8 chapters in total (see below) |
| `qs_gel` | Side | Glowing Lamp Oil / น้ำมันตะเกียงเรืองแสง | collect 8 Lumite Gel → Bors | 150 / 90 EXP, 300 Sc |
| `qs_crawl` | Side | Crawler Control / กำจัดเจ้าตัวคลาน | 12 Crawlix → Veyra | 260 / 150 EXP, 15 Y |
| `qs_eye` | Side | Eyes in the Dusk / ดวงตาในยามสนธยา | 6 Cryoculus → Veyra | 600 / 300 EXP, 25 Y |
| `qn_lumite` | Normal, repeatable | Hunt: Lumite | 15 Lumite | 120 / 80 EXP, 150 Sc |
| `qn_nebulite` | Normal, repeatable | Hunt: Nebulite | 12 Nebulite | 400 / 220 EXP, 300 Sc |
| `qn_shard` | Normal, repeatable | Hunt: Shardback | 10 Shardback | 520 / 280 EXP, 380 Sc |
| `qn_ore` | Normal, repeatable | Ore Delivery | 3 Gadolinium Ore | 200 / 100 EXP, 500 Sc |


## Hunting quests per map (v6)
Every monster has one repeatable **Normal** hunt (15 kills, Hunt Lumite/Nebulite/Shardback keep their older counts of 15/12/10). **One formula for all hunts:** Base EXP = kills × monster EXP × 0.9, Job EXP the same with Job EXP, Scandium = kills × average Scandium × 1.6. The reward is shown as a bonus on top of the EXP from the kills.

| Quest | Map | Goal | Base EXP | Job EXP | Scandium |
|---|---|---|---|---|---|
| Hunt: Lumite (`qn_lumite`) | 01 | 15 × Lumite | 270 | 189 | 120 |
| Hunt: Crawlix (`qn_crawlix`) | 01 | 15 × Crawlix | 567 | 405 | 216 |
| Hunt: Oculoth (`qn_oculoth`) | 01 | 15 × Oculoth | 1,215 | 810 | 408 |
| Hunt: Nebulite (`qn_nebulite`) | 02 | 12 × Nebulite | 691 | 454 | 269 |
| Hunt: Shardback (`qn_shard`) | 02 | 10 × Shardback | 900 | 612 | 328 |
| Hunt: Cryoculus (`qn_cryoculus`) | 02 | 15 × Cryoculus | 2,295 | 1,485 | 780 |
| Hunt: Glacilite (`qn_glacilite`) | 03 | 15 × Glacilite | 3,105 | 2,025 | 1,176 |
| Hunt: Rimeback (`qn_rimeback`) | 03 | 15 × Rimeback | 4,455 | 2,903 | 1,608 |
| Hunt: Magnoculus (`qn_magnoculus`) | 03 | 15 × Magnoculus | 6,345 | 4,050 | 2,400 |
| Elite Hunt: Field 01 (`qe_field1`) | 01 | 3 × Elite | 900 | 500 | 700 (+5 Y) |
| Elite Hunt: Field 02 (`qe_field2`) | 02 | 3 × Elite | 2,400 | 1,400 | 1,500 (+8 Y) |
| Elite Hunt: Field 03 (`qe_field3`) | 03 | 3 × Elite | 5,200 | 3,000 | 3,000 (+12 Y) |
| Boss Hunt: Gadolith (`qb_gadolith`) | 03 | 1 × Gadolith | 2,500 | 1,500 | 2,500 (+20 Y) |
| Hunt: Faultcrawler (`qn_faultcrawler`) | Geosyncline | 15 × Faultcrawler | 10,125 | 6,480 | 3,600 |
| Hunt: Tidewraith (`qn_tidewraith`) | Geosyncline | 15 × Tidewraith | 11,880 | 7,560 | 4,200 |
| Hunt: Strata Golem (`qn_stratagolem`) | Geosyncline | 15 × Strata Golem | 14,310 | 9,180 | 5,160 |
| Hunt: Cinderling (`qn_cinderling`) | Ruins | 15 × Cinderling | 16,875 | 10,800 | 5,760 |
| Hunt: Magmaback (`qn_magmaback`) | Ruins | 15 × Magmaback | 19,980 | 12,690 | 6,960 |
| Hunt: Ashen Sentinel (`qn_ashsentinel`) | Ruins | 15 × Ashen Sentinel | 23,625 | 14,985 | 8,280 |
| Elite Hunt: Geosyncline (`qe_geo`) | Geosyncline | 3 × Elite | 9,000 | 5,600 | 4,800 (+16 Y) |
| Elite Hunt: Ruins (`qe_ruins`) | Ruins | 3 × Elite | 16,000 | 10,000 | 8,000 (+22 Y) |

Repeatable quests are unlimited in the prototype. Add daily limits before release.

## Main quest "A New Beginning": now 8 chapters
Lumi → Bors → Crystal → 10 kills in Field 01 → reach Field 02 → defeat 1 Elite → **reach Field 03** (500 Base / 260 Job EXP) → **defeat Gadolith** (3,000 Base / 1,800 Job EXP, 100 Yttrium).
Saves that had finished the old 6 chapters get the quest back at chapter 7 automatically.


## Quest items (v7)
Quest items are shown in the **Quest** tab of the Inventory and can't be sold or discarded. Current quest items: Lumite Gel (Glowing Lamp Oil), Gadolinium Ore (Ore Delivery), Crystal Heart (Gadolith boss hunt and chapter).
