# Equipment Slots (10) and the hand-off for new items

> Part of the REO docs. Status (v16): **all 10 slots have items for all 5 classes** (50 pieces: names in EN and TH, a drawing each, stats, drops and set bonuses). The checklist in §3 is kept for future slots.

## 1. The ten slots

| # | Slot id | EN label | TH label | Screen position | Items today |
|---|---|---|---|---|---|
| 1 | `headTop` | Top Headgear | หมวกบน | left, row 1 | yes (Helm, Cap, Feather Cap, Wizard Hat, Halo Crown) |
| 2 | `headMid` | Mid Headgear | หมวกกลาง | right, row 1 | yes (Visor, Mask, Veil, Blessed Veil) |
| 3 | `headLow` | Lower Headgear | หมวกล่าง | left, row 2 | yes (Gorget, Collar, Rune Collar, Prayer Collar) |
| 4 | `armor` | Armor | เกราะ | right, row 2 | yes |
| 5 | `weapon` | Weapon | อาวุธ | left, row 3 | yes |
| 6 | `shield` | Shield | โล่ | right, row 3 | yes (Shield, Buckler, Ward, Aegis) |
| 7 | `garment` | Garment | ผ้าคลุม | left, row 4 | yes (Cloak, War Cape, Mantle, Stole) |
| 8 | `shoes` | Shoes | รองเท้า | right, row 4 | yes (Boots, Sabatons, Slippers, Sandals) |
| 9 | `ring` | Ring | แหวน | left, row 5 | yes |
| 10 | `bracelet` | Bracelet | กำไล | right, row 5 | yes (Bracer, Guard, Bangle) |

Screen layout is fixed by `SLOT_LAYOUT` in the code (same as the reference screenshot). Empty slots show their label. Selecting an empty slot with no items yet says "Items for this slot are coming soon."

## 2. What was kept from the old six slots (so nothing was lost)

Items made before this layout keep their ids. They simply equip into the slot they map to (`SLOT_ALIAS`):

| Old item family (id slot) | Equips into | Note |
|---|---|---|
| `offhand` (Tower Shield, Arrow Quiver, Grimoire, Blessed Symbol) | `shield` | quivers, tomes and symbols sit in "Shield" until real class items replace them |
| `legs` (Plate Greaves, Scout Leggings, Mage/Cleric Skirt, Traveler's Boots) | `shoes` | skirts and leggings in "Shoes" are placeholders |
| `necklace` (War Pendant, Eagle Charm, Mana Amulet, Prayer Beads, Crimson Scarf) | `bracelet` | pendants in "Bracelet" are placeholders |

Saves are migrated on load: equipped pieces move to the new keys, every slot exists, and a piece that does not fit its slot goes back to the bag. **Power is unchanged by the migration** (checked: CP, HP, ATK, DEF, Crit, Hit, Flee and abilities identical before and after).

## 3. What the next model must add per new item family

An item id is `gear|<class>|<slot>|<tier level>|<rarity 1-5>|<set 0-2>`. The `<slot>` in the id decides everything below. For a new slot (e.g. `headTop`) add all of these in `index.html`:

1. **Names**: `GBASE[<class>].<slot> = ["English","ไทย"]` for all 5 classes (`beginner`, `fighter`, `ranger`, `spellcaster`, `supporter`).
2. **Art**: `GEAR_ART[<class>].<slot> = '<svg parts>'` (48×48 viewBox; see `item-art-sheet.html`). Tier looks (Lv 10–50) and the rarity frame are added by the game.
3. **Stats**: a `case "<slot>":` in `gStats()` giving the base stats from `m = (3 + Lv×0.8) × rarity multiplier × (1 + 0.04×refine)`. Keep the budget comparable to the existing slots so CP stays balanced (see §4).
4. **Drops**: add the slot id to `ITEM_SLOTS` so monsters can drop it. Until then drops never include it.
5. **Slot name for equipping**: if the id slot equals the screen slot, nothing else is needed. (`SLOT_ALIAS` is only for the three legacy mappings above.)
6. **Requirements** (already generic): level = tier, class, and a primary-stat requirement for uncommon and above. Change `gReqs()` only if a slot needs something special.
7. **Sets**: the 3 set themes per class apply to every slot automatically (3 and 6 pieces). Note a full set is now **10 pieces**, but the bonuses still trigger at 3 and 6, so consider adding a third bonus (e.g. at 10). That is a design decision.
8. **Item art sheet** (`item-art-sheet.html`) and `ITEMS.md` should list the new designs.

## 4. Stat budget guide (existing slots, per piece before roll)

With `m` as above: weapon ATK = m×2.2; armor DEF m×0.9 and HP m×6; shoes (old legs) DEF m×0.6, HP m×3; shield (old off-hand) DEF m×0.7 and a hard-DEF %; bracelet (old necklace) HP m×10, SP m×2; ring CRIT m×0.08, HIT m×0.3; every piece also gives its class's primary stat m×0.35.
Adding 4 more pieces that each give a normal budget will raise total power. Either lower each piece's share or re-run the balance tests (below) and re-tune.

## 5. Check list before shipping new items
- `node tests/test_combat.js` passes (88 checks).
- Equip a new piece: stats appear in Status, CP changes, comparison panel shows differences.
- Old saves still load (see the migration check in `tests/COMBAT-TEST-REPORT.md`).
- Rarity frames and ★ stars never overlap the +N refine label (top-right).

## 6. Open questions
1. Should the three legacy mappings be retired once real shoes, shield and bracelet items exist? (Old pieces could be converted or kept as "classic" gear.)
2. Is Garment a cloak for all classes, or a class-specific item?
3. Do headgear slots have a visual effect on the character, as in the reference game's costume style?
4. Is there a rule for Mid and Lower headgear (face and mouth) such as "cannot wear both with Top"?


## 7. v16: the new items (what was made)

Every slot now has its own piece for each class. Names are in `GBASE` (EN and TH), drawings in `V16_ART`, and the stat cases in `gStats`.

| Slot | Fighter | Ranger | Spellcaster | Supporter | Beginner |
|---|---|---|---|---|---|
| Top Headgear | Iron Helm | Feather Cap | Wizard Hat | Halo Crown | Beginner Cap |
| Mid Headgear | Visor | Scout Mask | Veil | Blessed Veil | Cloth Mask |
| Lower Headgear | Gorget | Hunter Collar | Rune Collar | Prayer Collar | Scarf Guard |
| Armor | Plate Armor | Hunter Vest | Arcane Robe | Cleric Vestment | Beginner Tunic |
| Weapon | Greatsword | Longbow | Crystal Staff | Holy Mace | Silver Knife |
| Shield | Tower Shield | Leather Buckler | Arcane Ward | Grace Aegis | Wooden Buckler |
| Garment | War Cape | Forest Cloak | Mage Mantle | Cleric Stole | Traveler's Cloak |
| Shoes | Plate Sabatons | Swift Boots | Mage Slippers | Pilgrim Sandals | Traveler's Boots |
| Ring | Iron Ring | Sniper Ring | Focus Ring | Grace Ring | Copper Ring |
| Bracelet | Iron Bracer | Wrist Guard | Mana Bangle | Blessed Bangle | Copper Bracelet |

**Stats per piece (before the roll):** Top Headgear DEF m×0.6, HP m×4, FLEE m×0.3 · Mid Headgear HP m×4, SP m×2.5 · Lower Headgear DEF m×0.4, SP m×3 · Garment DEF m×0.5, HP m×5 · Shoes DEF m×0.5, FLEE m×0.6 · Shield DEF m×0.9, hard DEF from rarity · Bracelet CRIT m×0.1, HP m×6. Every piece also gives its class's primary stat m×0.35, like all other gear.

**Drops:** all ten slots drop equally (checked: about 10% each over 6,000 normal kills).
**Sets:** each class's three set themes apply to all ten slots, so a full set is now 10 pieces. The bonuses still trigger at 3 and 6 pieces (see §3, point 7).
**Old saves:** pieces from before v16 keep working. Off-hand, Legs and Necklace items still map to Shield, Shoes and Bracelet.

**Balance note:** four more slots with items raise total power. The 88 combat checks still pass, but CP rose for every character with the new starter kit (for example, the test weapon-equip check went from 1,539 → 3,599 CP). Re-tune the power curve when the balance pass comes around.
