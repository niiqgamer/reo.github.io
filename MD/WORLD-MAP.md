# World Map, Teleport and Announcements

> Part of the REO docs. Code: `WORLD MAP` and `HUD v17` sections in `index.html`. Status: working; economy numbers are first guesses.

## 1. World Map
- Open with the globe button in the minimap header, or press **M**.
- The chart shows the connected maps: Town → Field 01 → Field 02 → Field 03, plus Town → Path to the Geosyncline (west) and Town → Road to the Ruins (south) → Ashfall Ruins (v22, node to the right of Ruins). Each map is a card with its name, recommended CP, and the teleport cost. "You are here" marks the current map.
- Tap a map to open **Map Info** beside the chart.

## 2. Teleport
| Rule | Value |
|---|---|
| Price | **150 Scandium per map passed** (Town → Field 02 = 300; Field 03 → Geosyncline = 600 via Field 02, Field 01, Town). Same map: not allowed |
| Gate | Geosyncline needs Base Lv 25+ and CP 2,000+; Ruins needs Lv 30+ and CP 3,000+; Ashfall Ruins needs Lv 40+ and CP 6,000+. The teleport button is disabled and says what is missing |
| Where | **Only maps the character has already visited.** Others show `???`, a lock and "Not visited yet" |
| Arrival | at the entrance that leads back toward town (Town: the plaza) |
| Minimap Return to town (v21) | costs the same as teleporting to Town (150 Sc per map passed); the button's tooltip shows the price; blocked if Scandium is short |
| Side effects | ends Idle; blocked while dead or while changing map; blocked if Scandium is short (the button says how much is needed) |

**Visited maps** are saved (`visited`). Saves from before this version get a guess from progress: Town always; Field 01 if the character has any kills, level or EXP; Field 02 if the main quest reached chapter 5; Field 03 if it reached chapter 7. The map the character stands in always counts.

## 3. Map Info (5 tabs)
| Tab | Shows |
|---|---|
| Map Info | description, recommended CP, monster levels, monster count (+ Elites), boss, connected maps |
| Monster | name, level, element, HP, EXP (Base / Job), Scandium range; aggressive monsters also show Fast (speed ≥ 2), Ranged / Magic with range, and their skills; Elite note |
| Boss | level, HP, element, EXP, Scandium, respawn, mechanics text, reward list (per boss: its heart item, its fixed drops, gear of its tier) |
| Item Drop | per monster: each drop with its chance, Refine Ore chance; equipment tier and chance |
| Quests | quests for that map (hunts, Elite hunt, boss hunt; in Town the main quest), with status or an Accept button |

An unvisited map shows only a lock message. No info and no teleport.

## 4. Announcements (mock-up)
- Shown as a bold bar at the very top centre for 9 seconds, one at a time (queued). **System** = amber bar, **GM** = blue bar. Also written to the System chat tab.
- The system sends one **every 5 minutes**, rotating 4 sample messages.
- **Only the system or a GM can post.** Until there is a server this is a test switch: Settings > Other > "GM mode (test)" shows a text box plus "Announce" and "Preview system announcement". The switch is never saved. A real GM check needs a server.

## 5. Open questions
1. Teleport price curve (per map vs. distance, free first teleport, cooldown, daily limit).
2. Should teleport be allowed from inside a boss fight or a party?
3. Real GM roles and who can announce, plus per-channel or per-map announcements.
4. The chart is hand-placed for 6 maps (v19: landscape 340 px high, portrait 440 px); more maps need a new layout.
5. Map Info of a gated map shows an extra row **Entry needs** (Lv + CP). The Monster tab shows an Aggressive line with the skill names.
