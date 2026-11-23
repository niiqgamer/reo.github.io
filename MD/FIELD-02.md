# Gadolinium Field 02 — ทุ่งแกโดลิเนียม 02

> Part of the REO docs. Sub-title: **Amber Dusk Meadows / ทุ่งอำพันยามสนธยา**. Recommended CP **450**.

Reached from the **north portal** of Gadolinium Field 01 (tile 61, 2). Arrival beside the south portal (39, 95), which leads back to Field 01. Tiles are on the 98 × 98 grid.

Look: violet dusk grass, amber/rose glowing mushrooms and crystals, amber nectar pools, dusk-violet and autumn trees.

## Travel
The south portal (39, 95) leads to Field 01. The **north portal (39, 2)** leads to Field 03. No monster spawns within 8 tiles of a portal.

## Monsters (passive)

| ID | Name (EN / TH) | Sprite | Lv | HP | ATK | DEF | Base / Job EXP | Scandium | Drop | Count | Zone (x · y, 98 grid) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `nebulite` | Nebulite / เนบิไลต์ | Lumite (blue) | 7 | 170 | 26 | 6 | 64 / 42 | 10–18 | Nebula Gel 40% | 27 + 2 Elites | 8–60 · 56–90 |
| `shardback` | Shardback / ชาร์ดแบ็ค | Crawlix (violet/amber) | 9 | 280 | 34 | 10 | 100 / 68 | 15–26 | Amber Shard 35% | 21 + 2 Elites | 16–88 · 26–64 |
| `cryoculus` | Cryoculus / ไครโอคูลัส | Oculoth (ice) | 11 | 450 | 46 | 13 | 170 / 110 | 25–40 | Frost Lens 30% | 15 + 2 Elites | 40–92 · 6–36 |

## Elite monsters (every field map)

**Two** Elites per monster type per map (`ELITE_PER`, v20).

| Property | Value |
|---|---|
| Visual | Same sprite ×1.3, rotating gold/violet magic circle at the feet, warm aura, gold “★ Elite” name |
| Level | base +2 |
| HP / ATK / DEF | ×5 / ×1.6 / +3 |
| EXP / Scandium | ×5 / ×4 |
| Drops | The type's loot table at ×1.6 chance, Refine Ore chance ×3, gear 12% (normal 3%) with better rarity odds (`ITEMS.md` §4). The old guaranteed ×3 material and 35% Elite Core are gone; Elite Core now only drops from Gadolith |
| Respawn | 45–60 s |
| Idle | Idle skips Elites unless Base Lv ≥ Elite Lv + 3 |
| Aggressive maps | On the Geosyncline and Ruins an Elite's aggro range is +1 tile |
