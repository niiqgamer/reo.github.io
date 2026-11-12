# Combat Test Report — v5 archetype prototypes

Run: `node tests/test_combat.js` (Node, no dependencies). Result: **82 passed, 0 failed** (68 from v5 + 14 added in v6 for Field 03 and the boss).
The suite was run **before** the prototype was wired into the game, as requested.

## 1. Formulas vs iRO Classic (21 checks)
STR/DEX status ATK tables, MATK (INT 33 → 49~69, INT 100 → 296~500), CRIT, HIT, FLEE, HP/VIT, cast time, stat points (1,273 total), raise cost (628), ASPD cap 190, element table, the iRO Heal example, DEX narrowing damage, and the observed crit rate (24% expected, measured within 2.5 points).

## 2. Skill sets (21 checks)
Each prototype has 3–4 actives and 1–2 passives, every skill has SP and cooldown, no skill is shared, the Spellcaster covers all 4 elements, and ranges match the archetype spec (Fighter ≤ 3, Spellcaster 7, Ranger 12, Supporter heal 15).

## 2b. Signature mechanics (9 checks)
- Fighter: Crushing Blow at 5 Momentum hits ~2.4× harder than at 0.
- Ranger: +18% damage at 12 tiles vs 3 tiles.
- Spellcaster AI picks the weakness spell (Fire Bolt → earth, Lightning Spear → water, Stone Spike → wind) and Frost Nova for packs.
- Supporter: Heal = iRO formula ×1.2, shield cap 20%, heals below 55% HP.

## 3. Balance simulation (17 checks)
300 s fights, auto stats, skill AI, 3 seeds each. Targets: the three damage roles within ±25% of each other; Supporter ≥ 55% of their kill rate with the most HP left; Ranger takes the least damage of the damage roles; AoE roles clear packs fastest; Fighter survives Elites best and has the highest effective HP.

| Scenario | Fighter kills | Ranger | Spellcaster | Supporter |
|---|---|---|---|---|
| Lv10 Field 01 | 58 | 53.3 | 44 | 36 |
| Lv20 Field 02 | 53.3 | 48 | 44 | 32 |
| Lv30 Field 02 | 62.3 | 59.3 | 56 | 41.3 |
| Lv20 packs of 3 | 117 | 116 | 101 | 80 |
| Lv35 Field 02 Elites | 31.7 | 29.7 | 29 | 17.7 |

### Tuning made because of failing tests
1. Packs: Ranger out-cleared both AoE roles → Arrow Shower 140% → 90% (CD 3 → 4 s), Whirlwind Cleave 160% → 200% (CD 4 → 3.5 s), Frost Nova 160% → 260% (CD 6 → 5 s, freeze 30 → 40%), Fire Bolt 90% → 100%, staff MATK +15% → +20%.
2. Simulator bug: with zero travel time it never respawned monsters → fixed, suite re-run.
3. CP: the first formula (basic attacks only) rated a Lv12 Spellcaster at 409 vs a Fighter at 994 with similar kill speed → CP now uses simulated DPS with skills.

## 4. In-game checks (browser, after integration)
- All 16 actives fire on desktop with no errors; damage, buffs and buff icons verified.
- 25 s idle on Field 01 at Lv 12: Fighter 11 kills, Ranger 21, Spellcaster 9, Supporter 9. No deaths.
- Phone (Pixel 5): Spellcaster idle-casts with the cast bar; 2-line status bar fits.
- Old v2 save (no class data) loads as Beginner with auto-assigned stats and no lost points.
- Class choice persists through save and reload.

### Gap found in live play
The live idle sample shows a larger Ranger lead (≈2×) than the simulator (≈1.1×), because melee characters walk further between targets on real maps. Logged as the first item of the next balancing pass (`ARCHETYPES.md`, Known gaps). The sample is short (25 s, one seed each), so it needs a longer measurement before changing numbers.

## Full output
See `test-output.txt`.


## 5. v6: Field 03 and the first boss (14 checks)
Calibrated with the simulator before wiring into the game.
- First pass was too hard: Ranger and Spellcaster died 10+ times per 10 minutes against the boss and Spellcaster Lv 15 died 4 times per 5 minutes on Field 03 normals. Field 03 monsters were lowered (HP 640/900/1250 to 540/760/1000, ATK 56/68/84 to 44/54/66) and the boss went from HP 9,000 / ATK 96 / 2.0 s to HP 8,000 / ATK 58 / 2.6 s (heavy but slow).
- Recommended CP chosen by comparing archetypes at equal CP: Field 03 = **900** (all four farm safely), boss = **1,100** (Fighter and Supporter never die, Ranger and Spellcaster about one death in three kills with no potions or kiting; at CP 1,300 all are safe).
- Checks: monster levels 13/15/17 and boss Lv 20, boss HP ≥ 7× the strongest normal, boss out-levels every Elite, Spellcaster picks Fire Bolt against the earth boss, CP-900 farming for each archetype, boss kill rates and deaths per kill at CP 1,100 and 1,300, and "more CP never makes the boss harder".
- Known gap: the CP formula does not count healing, so the Supporter needs Lv 45+ to reach CP 1,100 although it already beats the boss without dying. Fix when CP gets a sustain term.

## 6. v6: in-game checks (browser)
- All 6 portal routes (incl. Field 02 ↔ 03) arrive 1–1.4 tiles from the matching portal.
- Boss fight end to end: aggro, Crystal Slam telegraph, kill, rewards (Heart ×1, Core ×3, Ore ×5), main quest completes, respawn timer 120 s.
- Idle never targets the boss; auto-quest walked Field 02 → 03 and targeted an Elite.
- Quests window grouped by map (17 available quests); an old save with the main quest finished is reactivated at chapter 7.
- Phone emulation: at most 2 ground textures (about 39 MB) during Town → 01 → 02 → 03 → 02.
- Regression: Archetype Trial flow, auto-idle after 5 min, live quest progress, loading screen. All pass.


## 7. v7: items, equipment and inventory (in-game checks)
- 1,500 equipment pieces (5 classes × 6 slots × 10 tiers × 5 rarities). Drops rolled over 3,600 normal and Elite kills, all of them valid pieces and consumables/materials.
- Requirements: Lv 12 cannot equip a Lv 30 piece, the class check and the stat check all block correctly.
- Gear effect: an Epic Lv 30 weapon raises CP from 1,343 to 2,113.
- Refine: success raises the piece by 1; the fee and the ore are used every attempt.
- Sell 5 claws → 45 Sc. Quest items cannot be sold or discarded. Discard needs a second tap.
- Class change moves the old class's gear to the bag.
- Consumables: Greater Red Potion heals; Ember Root sets the ATK buff.
- Regression: the archetype trial, the boss fight (loot and quest completion), auto-quest, portals and auto-idle all still pass.


## 8. v15: windows, 10 slots, and a bug found on the way
- **Bug fixed (since v10):** the percentage bonuses from set bonuses and affixes (ATK%, DEF%, HP%, MATK%, Heal%) were applied **twice** in the combat module, so +5% really gave about +10%. Now they apply once, and the results are whole numbers. Six checks were added (`[4b]`): ATK, HP, DEF and Heal each equal ×1.10 once for +10%, results are whole numbers, and no gear leaves `derive` unchanged. Suite: **88 passed, 0 failed**.
- **Migration to 10 slots:** with a save that has flat-stat gear (no % bonuses), the previous build and this one give identical numbers (CP 10,472, HP 4,974, ATK 943.14, DEF 185.31, Crit 5.68, Hit 76.56, Flee 65, abilities Lifesteal 3.1, Crit damage 20, Damage reduction 5, Thorns 8). A save with % bonuses differs by design, because of the fix above.
- Checks that passed: the 10 slots sit where the reference shows them; legacy items equip into Shoes, Shield and Bracelet and the replaced piece returns to the bag; a piece found in the wrong slot goes back to the bag; new characters get starter gear in the six slots that have items; 4,000 drops never produce the four item-less slots; Thai labels; the bottom bar switches Status, Skill and Items and is hidden in Quests.
- Regression (all pass): auto-idle, archetype trial and its button (now in Status), items and inventory, comparison and multi-sell, gear rolls and abilities, boss fight, portals and quests, level-up refresh of the open window, and the whole login system (register, login, guest, migration, lockout, edge cases).


## 9. v16: equipment for all ten slots (in-game checks)
- Coverage: every class × slot (50 combinations) has an EN and TH name and its own drawing; each class has 10 distinct drawings.
- Drops over 6,000 normal kills: every slot drops (568–643 each, no empty slot).
- Stats: each new slot gives its own stats (see EQUIPMENT-SLOTS §7); the seven new slots equip into their own slot, and CP changes.
- The regressions still pass: combat suite 88/88, rolls, compare and multi-sell, items, auto-idle, old-save migration (slots and power). The slot-model check now expects drops in all ten slots (the old check expected four empty ones).


## 10. v17: UI rebuild (in-game checks)
- Monster panel: hidden when not fighting; shows name, Lv, element and live HP; the trail runs ahead of the red bar while HP drops; Elite tag; hides about 5 s after combat.
- Map name: visible on entering, hidden after about 5 s (landscape included; this was a bug).
- **Live updates (open window, nothing reopened):** Inventory gains and loses items; the item detail window closes when its item is gone; Status kills; Quests list and progress (4/15); Cash Shop buttons enable when Yttrium arrives.
- Cash Shop: capacity 100 → 120 and Yttrium 100 → 60 on a pack; maximum 500.
- Inventory: 50 cells per page; 120 items = 3 pages; sort order checked (equipment by slot, then name); the window height is identical across tabs.
- Idle: toggle on/off; no panel under the player card; stopping opens the summary; the gear button opens Idle Settings.
- Announcements: system, then GM, queued one after another. Menu collapse is saved.
- Teleport: cost 150/300/450 from Town; unvisited maps blocked even with a forced click; teleport from Town to Field 02 costs 300 Sc and arrives on a walkable spot; blocked when Scandium is short.
- Navigation: for each of the 7 windows the bar lists the other windows only; Character opens a pair; the nav labels equal the menu labels; Esc and M keys.
- **Phones:** for 8 windows the menu buttons were never covered (checked with element hit-testing); no navigation label is cut in English or Thai, on phone or desktop.
- Regression (all pass): archetype trial and its button, auto stat refresh, auto-idle (stop is now the toggle), items, compare and multi-sell, gear rolls, abilities, boss fight, portals and auto-quest, the 10-slot model, and the three login test sets.


## 11. v18 (in-game checks)
- **Sound:** the audio context starts after the first tap; the music scheduler produces notes (16 to 19 in 1.5 s); the track changes with the map (town, field1, field2, field3); aggressive boss switches to the boss track and back when calm; 30 effects fired for a short sequence of menu, window, level up and pickup; Music off stops scheduling; Sound off silences effects.
- **Layout:** the Idle button is exactly the hotbar slot size (46 and 44 px); the gear badge is on its top-right; CP and Scandium are on the same row of the player card; the menu is 9 buttons in 3 columns and 3 rows; the World Map button is in the top-right corner of the minimap; the zoom label is hidden.
- **Windows:** Character and Status open alone; no navigation bar is shown; the wallet is in the Equipment window and follows the currencies live.
- **Inventory:** tab order Consumable > Equipment > Material > Quest; the layout rows are as specified; the sort toggle cycles Name > Rarity > Sell price in Equipment and Name > Sell price elsewhere; 5-star rows do not overflow the cell.
- **UI mode:** System, Light and Dim set the theme and are kept after a reload.
- **Status bar:** one row; expanded at start, only SERVER TIME after 30 s, expanded again after a map change; it fits the screen at 393 px and 320 px (English and Thai).
- **Town:** all NPC spots are free of overlapping props; the closest a wanderer came to an NPC in 40 s was 1.96 tiles.
- **Regression (all pass):** combat 88/88, archetype trial, auto stat, auto-idle, items, compare and multi-sell, gear rolls, abilities, boss fight, portals and quests, the 10-slot model, the three login test sets. Several older tests were updated for the new inventory tabs and the missing navigation bar.


## 12. v18.1: black screen fix (sandboxed hosts)
- **Cause:** the page read `window.localStorage` at startup without a guard. Some hosts (including the claude.ai artifact viewer) load pages in a sandbox that throws on that read, so the script stopped and the screen stayed black.
- **Fix:** the login code reads storage through a guarded getter. If storage is blocked, the login screen shows the existing notice and Guest play still works. The game's save code uses a wrapper that falls back to an in-page memory store (progress then lasts until the page is closed).
- **Checks:** no script errors inside a sandboxed iframe; the login screen renders with the storage notice; a guest enters the town inside the sandbox; the normal page, login (t140), storage-blocked login (t144) and auto-idle (t60) all pass.
