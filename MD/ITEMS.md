# Items, Equipment & Inventory

> Part of the REO docs. Rules live here. Code: `items` module in `index.html` (`ITEMDB`, `GBASE`, `LOOT`, `gStats`, `gReqs`).

## 0b. Sets, rolls and abilities (v10)

**3 sets per class per tier.** Each class has three set themes. Every tier (Lv 10, 20, … 90) has its own version of each theme, so there are **5 classes × 10 tiers × 3 sets = 150 sets**. Set names carry a roman numeral for the tier (e.g. *Ironclad IV*).

| Class | Set 1 | Set 2 | Set 3 |
|---|---|---|---|
| Beginner | Wanderer (AGI) | Scout (HIT, FLEE) | Apprentice (INT) |
| Fighter | Ironclad (DEF%) | Vanguard (ATK%) | Warbreaker (CRIT) |
| Ranger | Windrunner (FLEE) | Huntmaster (ATK%) | Shadowstep (CRIT) |
| Spellcaster | Arcanist (MATK%) | Stormcaller (HIT) | Attuned (HP%) |
| Supporter | Lightbringer (MATK%, Heal%) | Sentinel (DEF%) | Blessed (SP, VIT) |

**Set bonus:** 3 pieces of the same set give the 3-piece bonus; 6 pieces give the 6-piece bonus (it replaces the 3-piece bonus). Bonuses grow slightly with the tier.

**Every piece is rolled.** A drop is not a fixed item. When it drops, it gets:
- **Stat roll:** the base stats are multiplied by a random factor between **0.85 and 1.15**.
- **Affixes:** extra random stats, picked from primary stats (STR, AGI, VIT, INT, DEX, LUK), ATK, DEF, HP, SP, HIT, FLEE, CRIT and the % stats (ATK%, MATK%, DEF%, HP%). Count by rarity: ★ 1 → 1, ★★ → 1, ★★★ → 2, ★★★★ → 2, ★★★★★ → 3.
- **Abilities** (special effects), count by rarity: ★ 0, ★★ 0–1, ★★★ 1, ★★★★ 1–2, ★★★★★ 2.

| Ability | Effect | Range |
|---|---|---|
| Lifesteal / ดูดเลือด | heal this % of damage dealt | 2–5% |
| Thorns / หนาม | reflect this % of damage taken back to the monster | 5–15% |
| Crit damage / ดาเมจคริติคอล | crit damage +x% | 10–30% |
| Cooldown / คูลดาวน์ | skill cooldowns −x% | 5–15% |
| Damage reduction / ลดดาเมจ | take x% less damage | 3–8% |
| SP on kill / SP เมื่อฆ่า | +x SP per kill | 5–15 |

Pieces keep their rolls when they are equipped, sold or refined. The starter Beginner gear has no rolls (it is the same for everyone).

## 0c. Compare and multi-sell (v11)

**Compare before equipping.** Select a piece in the Inventory and the details show a comparison with the piece equipped in the same slot:
- every stat and affix that differs, shown as `old → new` with the change in green (gain) or red (loss);
- abilities too, with `NEW` when the slot had none and `−` when the new piece lacks one;
- an empty slot shows the full bonus as new.

Set bonuses are not part of the comparison (they depend on the whole set).

**Select many and sell.** ~~Press **Select many** in the Inventory.~~ **v19.2:** hold an item to start selecting (see the v19.2 section at the end). Tap pieces or stacks to add or remove them; the footer shows the count and the total Scandium. **Sell** sells everything chosen in one action. Stacks sell in full. Quest items are never sold and are skipped with a note.

## 1. Item types

| Type | Stacks | Examples | Sell | Discard |
|---|---|---|---|---|
| **Consumable** | yes | potions, herbs, Fly Wing | yes | yes |
| **Material** | yes | shells, gels, ores, Refine Ore | yes | yes |
| **Quest item** | yes | Lumite Gel, Gadolinium Ore, Crystal Heart | **no** | **no** |
| **Equipment** | no (each piece is its own item, with its own refine level) | gear by class, tier and rarity | yes | yes |

Stackable items total **46** (12 consumables, 34 materials/ores/quest items; v19 added 12 materials). Equipment has **2,500** distinct pieces (see §3).

## 2. Consumables

| Item (EN / TH) | Effect | Sell | Source |
|---|---|---|---|
| Lesser Red Potion / ยาแดงระดับต้น | +80 HP | 15 | Lumite, shop |
| Red Potion / ยาแดง | +120 HP (+2% per VIT) | 30 | start, shop |
| Greater Red Potion / ยาแดงชั้นสูง | +400 HP | 120 | Oculoth, Magnoculus |
| Blue Potion / ยาฟ้า | +60 SP (+1% per INT) | 40 | start, shop |
| Greater Blue Potion / ยาฟ้าชั้นสูง | +200 SP | 110 | Cryoculus, shop |
| Apple / แอปเปิล | +30 HP | 8 | start |
| Fly Wing / ปีกบิน | random teleport on this map | 60 | start, shop |
| Glowmoss Herb / สมุนไพรเรืองแสง | +1.5% Max HP per second, 15 s | 40 | Crawlix, Nebulite |
| Ember Root / รากเอมเบอร์ | **+10% ATK**, 60 s | 50 | Shardback |
| Frost Bloom / ดอกไม้น้ำแข็ง | **+15% DEF**, 60 s | 50 | Glacilite |
| Sage Leaf / ใบเซจ | **+50% SP regen**, 60 s | 45 | Rimeback |
| Aether Dew / น้ำค้างอีเธอร์ | +40% Max SP | 60 | (shop later) |

Herbs and potions use the hotbar/inventory "Use" button. Buffs show as icons under the character card.

## 3. Equipment

### Sets
- **5 class sets:** Beginner, Fighter, Ranger, Spellcaster, Supporter.
- **10 slots per class:** Top / Mid / Lower Headgear, Armor, Weapon, Shield, Garment, Shoes, Ring, Bracelet. Every slot has items for all 5 classes (50 designs). Legacy Off-hand, Legs and Necklace items map to Shield, Shoes and Bracelet. See `EQUIPMENT-SLOTS.md`.
- **10 tiers:** Lv **1, 10, 20, 30, 40, 50, 60, 70, 80, 90**. Each piece needs its tier level to equip.
- **5 rarities (tier stars):**

| Stars | Rarity (EN / TH) | Frame colour |
|---|---|---|
| ✪ | Common / ธรรมดา | white |
| ✪✪ | Uncommon / ดี | green |
| ✪✪✪ | Rare / หายาก | blue |
| ✪✪✪✪ | Epic / เอปิก | purple |
| ✪✪✪✪✪ | Legendary / ตำนาน | red |

Total: 5 classes × 10 slots × 10 tiers × 5 rarities = **2,500 pieces**.

### Stats of a piece
Let `m = (3 + Lv × 0.8) × rarity multiplier × (1 + 0.04 × refine)` with multipliers ×1, ×1.4, ×2, ×2.8, ×4.

| Slot | Bonus |
|---|---|
| Weapon | ATK = m × 2.2 (Spellcaster staff: weaponMATK = m × 2.2 instead, see `COMBAT-FORMULAS.md` §1) |
| Armor | DEF = m × 0.9, HP = m × 6 |
| Legs | DEF = m × 0.6, HP = m × 3 |
| Off-hand | DEF = m × 0.7, DEF% = rarity × 1% |
| Necklace | HP = m × 10, SP = m × 2 |
| Ring | CRIT = m × 0.08, HIT = m × 0.3 |
| All | Primary stat +m × 0.35 (STR for Fighter and Beginner, DEX for Ranger, INT for Spellcaster and Supporter) |

Equipped gear adds to the combat stats (`REOC.derive` with `gear`). Gear counts in **CP**.

### Requirements (checked before equip)
1. **Level** ≥ the piece's tier (Lv 1, 10, …).
2. **Class** = the piece's class. A class change moves other classes' gear to the bag.
3. **Stat** (uncommon and above, not Beginner): primary stat ≥ `Lv × 0.5 + 6`.

Failing requirements show ✗ in the details; the Equip button stays disabled.

### Refine (ตีบวก)
- Costs **1 Refine Ore** and a fee of **50% of the piece's sell price** (Scandium).
- Success chance: +1 → +3 **100%**, +3 → +6 **70%**, +6 → +9 **40%**, +9 → +10 **20%**. Maximum **+10**.
- Failure loses the ore and the fee, but the piece stays.
- Each refine level adds **+4%** to the piece's stats.

## 4. Drops

Every monster has a loot table (`LOOT`). Elites roll their table at ×1.6 chance and also have a bigger chance for gear. Bosses have fixed extra rewards.

| Source | Typical drops |
|---|---|
| Lumite | Lumite Gel (quest), Pale Spore, Lesser Red Potion |
| Crawlix | Crawlix Shard, Crawlix Claw, Glowmoss |
| Oculoth | Oculoth Lens, Oculoth Iris, Greater Red Potion |
| Nebulite | Nebula Gel, Stardust, Glowmoss |
| Shardback | Amber Shard, Shard Core, Ember Root |
| Cryoculus | Frost Lens, Frozen Iris, Greater Blue Potion |
| Glacilite | Glacial Gel, Frost Spark, Frost Bloom |
| Rimeback | Rime Plate, Rime Bone, Sage Leaf |
| Magnoculus | Magnet Lens, Magnetic Coil, Greater Red Potion |
| Faultcrawler | Fault Shard, Seismic Core, Greater Red Potion |
| Tidewraith | Abyssal Tear, Sunken Glyph, Frost Bloom |
| Strata Golem | Strata Slab, Pressure Crystal, Sage Leaf |
| Cinderling | Cinder Ash, Ember Core, Ember Root |
| Magmaback | Magma Plate, Lava Glass, Greater Red Potion |
| Ashen Sentinel | Scorched Relic, Inferno Shard, Aether Dew |
| Gadolith (boss) | Crystal Heart (quest), Elite Core ×3, Gadolinium Ore ×5, Refine Ore ×2–4, **2 gear pieces** |

**Refine Ore** drops from every monster (chance 2%–6%, ×3 for Elites). **Gear** drops: normal 3%, Elite 12%, boss 2 pieces.

Gear rarity odds (normal / Elite / boss): ✪ 70 / 45 / 10, ✪✪ 22 / 30 / 30, ✪✪✪ 6 / 15 / 35, ✪✪✪✪ 1.8 / 8 / 20, ✪✪✪✪✪ 0.2 / 2 / 5.
A drop's tier = the monster's level rounded down to a multiple of 10 (minimum Lv 1).

## 5. Inventory window (renamed from Bag)

- **Capacity:** 60 slots. Each stack and each equipment piece uses one slot. *(Superseded: see Inventory v17.)*
- **Tabs:** Everything · Equipment · Consumable · Material · Quest. *(Superseded: see Inventory v19.2.)*
- **Grid:** each item shows its icon, count, refine level (**+N at the top-right corner**) and star tier (★ along the bottom) with its frame colour. Refine and stars never overlap.
- **Details:** name, rarity, class and slot, stats (equipment), requirements (✓ / ✗), sell price.
- **Buttons:**
  - **Use** (consumables).
  - **Equip** (equipment; disabled until all requirements pass). Swapping moves the old piece to the bag.
  - **Refine** (equipment; shows how many Refine Ore you have).
  - **Sell** (price shown; quantity stepper for stacks, Max button).
  - **Discard** (two taps to confirm).
- Quest items cannot be sold or discarded.
- Equipped pieces are changed from the **Character** window: tap a slot to see the piece, then **Unequip** or **Refine**.

## 6. Open questions
1. Shop stock for the new potions and herbs (only the basics are in the shop now).
2. Stack limit per item and whether consumables should stack past 99.
3. Belt and Bracelet: which stats, and when they unlock.
4. Gear trade and market (see `ECONOMY.md`, Lanthanum rules).
5. Card slots: how cards are found and inserted.
6. **(v19.2)** Which items go in the new **Cash** tab (none are flagged yet).


## Inventory v17 (capacity and sorting)
- **Capacity:** 100 slots base. **Inventory Expansion Pack** (Cash Shop tab of the Shop): +20 slots per pack, up to 500 per character. Placeholder price per pack: 40 Yttrium or 8 Lanthanum (to be reviewed).
- **Pages:** ~~50 cells per page~~ **v19.2: 30 cells per page** (5 × 6), per type tab. The grid always has the same number of cells, so the window never changes size.
- **Auto sort:** type (equipment, consumable, material, quest) > name > stars (high first) > price (high first). Equipment sorts by slot first. New items are added at the end until the next sort.

## v19 materials (Geosyncline and Ruins)
| ID | EN / TH | Sell |
|---|---|---|
| `mat_fault` | Fault Shard / เศษหินรอยเลื่อน | 20 |
| `mat_seismic` | Seismic Core / แกนแผ่นดินไหว | 70 |
| `mat_tide` | Abyssal Tear / หยดน้ำเหวลึก | 24 |
| `mat_glyph` | Sunken Glyph / อักขระจมน้ำ | 85 |
| `mat_strata` | Strata Slab / แผ่นชั้นหิน | 28 |
| `mat_press` | Pressure Crystal / คริสตัลแรงอัด | 100 |
| `mat_cinder` | Cinder Ash / ขี้เถ้าเพลิง | 30 |
| `mat_embercore` | Ember Core / แกนเพลิง | 105 |
| `mat_magma` | Magma Plate / แผ่นหินหลอม | 38 |
| `mat_lavaglass` | Lava Glass / แก้วลาวา | 125 |
| `mat_relic` | Scorched Relic / ซากโบราณไหม้เกรียม | 45 |
| `mat_infernoshard` | Inferno Shard / เศษหัวใจนรก | 160 |

Drop chances, Refine Ore chances (6–10%) and sources are in `FIELD-GEOSYNCLINE.md` and `FIELD-RUINS.md`. Gear tier: Lv 25–29 monsters drop tier 20, Lv 30+ drop tier 30. These materials are not quest items and have no use yet (crafting is still open).

## Inventory v19.2 (light window; replaces the page size and tabs of v17)
- **Tabs:** Usable · Equipments · Other · Quest · **Cash** (Thai: ใช้ได้ · อุปกรณ์ · อื่น ๆ · เควสต์ · แคช). Opens on Usable. "Other" is the old Material tab.
- **Cash tab:** shows items whose `ITEMDB` entry has `cash:true`. **No item has this flag yet**, so the tab is empty for now (the Inventory Expansion Pack is applied at once and never enters the bag).
- **Pages:** **30 cells per page** (5 × 6 grid, as in the reference), per tab. Capacity rules (100 base, +20 per pack, max 500) are unchanged.
- **Bulk sell:** **hold an item for 0.45 s** to start selecting (it is ticked). While selecting, tap more items to add or remove them; the footer shows `n selected · total Sc` and a **Cancel** button. **Sell** sells everything ticked in one action (quest items are skipped, as before). Sell with nothing ticked shows the hint "Hold an item to start selecting." The old "Sell in bulk" toggle button is gone.
- **Sort:** same toggle as before (Name > Rarity in Equipments only > Price); the label reads `Sort by Name / Rarity / Price` (just `Sort` before the first press).
- A normal tap still opens the Item Detail window (Use / Equip / Refine / Sell / Discard).
