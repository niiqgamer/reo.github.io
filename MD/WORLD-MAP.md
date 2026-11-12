# World Map, Teleport and Announcements

> Part of the REO docs. Code: `WORLD MAP` and `HUD v17` sections in `index.html`. Status: working; economy numbers are first guesses.

## 1. World Map
- Open with the globe button in the minimap header, or press **M**.
- The chart shows the connected maps (Town → Field 01 → Field 02 → Field 03). Each map is a card with its name, recommended CP, and the teleport cost. "You are here" marks the current map.
- Tap a map to open **Map Info** beside the chart.

## 2. Teleport
| Rule | Value |
|---|---|
| Price | **150 Scandium per map passed** (Town → Field 02 = 300). Same map: not allowed |
| Where | **Only maps the character has already visited.** Others show `???`, a lock and "Not visited yet" |
| Arrival | at the entrance that leads back toward town (Town: the plaza) |
| Side effects | ends Idle; blocked while dead or while changing map; blocked if Scandium is short (the button says how much is needed) |

**Visited maps** are saved (`visited`). Saves from before this version get a guess from progress: Town always; Field 01 if the character has any kills, level or EXP; Field 02 if the main quest reached chapter 5; Field 03 if it reached chapter 7. The map the character stands in always counts.

## 3. Map Info (5 tabs)
| Tab | Shows |
|---|---|
| Map Info | description, recommended CP, monster levels, monster count (+ Elites), boss, connected maps |
| Monster | name, level, element, HP, EXP (Base / Job), Scandium range; Elite note |
| Boss | level, HP, element, EXP, Scandium, respawn, mechanics text, reward list |
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
4. More maps will need a new chart layout (the chart is hand-placed for 4 maps).
