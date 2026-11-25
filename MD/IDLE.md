# Idle & Offline Idle

> Part of the REO docs. Idle rules are the source of truth; update this file first when they change.

## Rules

1. **Everyone can start or stop idle at any time** (VIP or not). In town, pressing Start walks the hero to Gadolinium Field 01 and starts idle on arrival. Stop ends idle immediately and the character stays where it is.
2. **Idle, game open:** normal rewards (100%) — Base EXP, Job EXP, Scandium, materials. Other players can see the character.
3. **Idle, game closed:**
   - **Non-VIP:** 80% of normal rewards (−20%). The character stays visible to other players and monsters are first come, first served. On the next login, the player may pay **1 Yttrium per hour (rounded up)** to upgrade to 100%.
     - Example: 2 h 32 m → 3 Yttrium.
   - **VIP:** 100% of normal rewards. The character is **hidden** from other players and farms the map's live monster data directly, so there is no contest for monsters. On the next login, the player may pay **1 Yttrium per hour (rounded up)** for a **+20%** bonus (120%).
     - Example: 5 h 2 m → 6 Yttrium.
4. Idle ends when the player **changes maps** (portal or return to town) or **dies**. Stopping idle, changing maps and dying all count as a normal exit.
   - **Exception (v21):** the automatic town errands from Idle Settings (VIP Auto-buy Fly Wing, VIP Auto Pocket Dimension) leave the map and come back without ending Idle; the session (time, kills, loot) carries on. "Return to town when full" goes to town and ends Idle there.
5. Closing the game while idle counts as "game closed". Idle time is measured from the moment the page is hidden or closed.

## Bosses and idle (v6, v21)
Idle **never auto-targets bosses** (and still skips Elites that are too strong, Base Lv < Elite Lv + 3). Bosses are hands-on. Since v21 there is no boss or Elite switch in Idle Settings: bosses are never in the monster list, and an Elite counts as its normal kind. Offline idle never counts bosses (EXP or drops). A player who starts auto-quest for a boss quest does fight it: auto-quest targets it on purpose and the skill rotation then runs.

## Auto-idle after standing still (v5.3)

- If the character stands still for **5 minutes in a field with monsters**, Idle starts automatically.
- "Still" means: not walking or auto-walking, no target, not casting, no open dialog or quest walk, not dead, not already idling.
- Towns never auto-start Idle (no monsters spawn there).
- After the player **stops Idle manually**, auto-start waits until the player moves again. This stops the game from restarting Idle right after a manual stop.
- Settings > Other has a toggle "Auto-idle after 5 min standing still" (on by default). Since v21 it is only there (no longer repeated in Idle Settings).

## Idle Settings (v21)

The gear badge on the Idle button opens **Idle Settings**. Rows whose buttons do not fit put the buttons on a second line; on phones the sub-option indent is removed and every button row sits under its label. Settings are saved per character in `S.iset` (`isetFix` cleans old or broken saves). Tabs: **Target · Combat · Recovery · Warp · Loot · VIP** (the VIP tab is shown only to VIP players).

### 1. Target
| Setting | Values | Rule |
|---|---|---|
| Target mode | **All** (default) · Chosen | All: every monster on the map (never bosses, never too-strong Elites). Chosen: only the kinds in the slots |
| Monsters to fight | 5 slots **per map** (`mons[mapId]`) | Tap a slot → list of this map's monsters (no bosses; an Elite counts as its kind) → tap once to choose, again to put it in the slot. A kind already in another slot is greyed out. All 5 empty = fight all. Only on a hunting map |
| Fight back when attacked | ON (default) / OFF | Also fights an aggressive monster within 4 tiles that is attacking, even if it is not in the list (never a boss) |
| Stop Idle after | Off · 30 min · 1 h · 2 h · 4 h | Stops Idle (same as pressing Stop: the summary opens) |

### 2. Combat
| Setting | Rule |
|---|---|
| Basic attack (ON default) | Can be turned off only while Skill attacks is on. Turning Skill attacks off turns Basic attack back on |
| Skill attacks + Attack skill set (9 slots) | Physical and magic skills only. **Rotation:** after slot *n* fires, the next try starts at slot *n*+1 and wraps (1 → 2 → 1 → 2 …); a skill that is not ready (cooldown, SP) is skipped. A self-area skill (Petrifaction) walks in until the target is inside its area, then fires (gives up after 4 s) |
| Buff skills + Buff skill set (9) | Buff skills only. Cast again when the buff has ≤ 1 s left |
| Healing skills + Healing skill set (9) + "Heal when HP is below" (5–95%, default 60%) | Heal and zone skills (Heal, First Aid, Sanctuary). Sanctuary is not recast while one is up |
| Movement skills + Movement skill set (9) | Movement skills (Evasive Leap). Used when an attacking monster is within 2 tiles |
| Sit to rest + "Rest when below" (5–95%, default 40%, OFF by default) | Sits when HP **or** SP is below the bar and no attacking monster is within 8 tiles; stands at 95% of both or when a monster comes. Needs Basic Skill Lv 2 |

Priority each tick: heal → movement → buff → attack. Tap a skill slot → list of this archetype's skills of that kind with level chips (1 … learned level); tap once to choose, again to put it in the slot (works the same on phones). Unlearned skills are greyed out. **If all four sets are empty, Idle picks skills by itself** (the built-in `REOC.pickSkill`), still obeying the four switches.

### 3. Recovery
| Setting | Values |
|---|---|
| Auto HP potion | ON (default). Order: Smallest first (default) / Biggest first. Below 5–95% (default 35%). Potions: Apple, Lesser Red, Red, Greater Red |
| Auto SP potion | ON (default). Same order choice. Below 5–95% (default 15%). Potions: Blue, Greater Blue, Aether Dew |
| Buff items | OFF by default. 5 slots, buff items from the bag (Glowmoss Herb, Ember Root, Frost Bloom, Sage Leaf). Each is used again **when its buff ends**, not on a timer. Potions and Fly Wings are not allowed here |

Idle uses at most one potion or item every 0.6 s, straight from the bag (no hotbar slot needed).

### 4. Warp
| Setting | Rule |
|---|---|
| Warp with Fly Wing (OFF default) | No wanted monster in sight (12 tiles) for 3 s → uses a Fly Wing. While it is on and wings are left, Idle only looks 12 tiles around; otherwise it searches 40 tiles and walks |
| Warp with Teleport skill | Supporter only. **Mockup:** the skill does not exist yet, so the switch is disabled ("Soon") |
| Return to town when full (OFF default) | Bag full → warps to town (price as on the World Map; walks if Scandium is short) and ends Idle there with the summary. **Hidden while VIP Auto Pocket Dimension is on** |

### 5. Loot
**Pick up:** All (default) / Filter. Quest items are always picked up. Filter:
| Setting | Values |
|---|---|
| Usable items | ON / OFF |
| Equipment | ON / OFF; when ON: |
| · by ★ | Off · ★1+ … ★5+ (Off = any) |
| · by archetype | Beginner, Fighter, Ranger, Spellcaster, Supporter, several at once (none chosen = any) |
| · by level | Lv 1+ (default, = any) · 10+ · 20+ · 30+ · 40+ · 50+ |
| Other items | ON / OFF (materials, Refine Ore …) |

Equipment is kept only if it passes every condition that is set. Filtered drops are simply not picked up.

### 6. VIP
| Setting | Rule |
|---|---|
| [VIP] Auto-buy Fly Wing + amount (1–999, default 50) | Needs "Warp with Fly Wing" on. Out of wings → warps to town, buys the amount (60 Sc each, as in the shop, keeping enough for the warp back), warps back to the same map and Idle continues |
| [VIP] Auto Pocket Dimension | Bag full → warps to town, stores every material and unlocked gear in the Pocket Dimension (potions, herbs, Fly Wings and quest items stay), warps back and Idle continues. Needs Basic Skill Lv 5 |
| [VIP] Auto resurrection | **Mockup:** needs the Resurrection Particle item, which does not exist yet ("Soon") |

**Town errand money rules:** each warp costs what the World Map charges (150 Sc per map passed). Short on the way **to** town: the character walks to town. Short on the way **back**: it stays in town and Idle ends (summary opens). If the errand cannot be done (nothing could be stored, no money for wings) Idle also ends in town. Pressing the Idle button during an errand cancels it.

### Offline idle (v21)
Offline rewards use the same settings: Chosen targets limit the monster kinds of that map (empty = all), and the loot filter removes items and gear that would not be picked up. Bosses never count. Potions, skills and errands are not simulated offline.

## Saving when the game is closed

- On `pagehide` or when the tab becomes hidden, the game saves immediately and records `away = { t, map, vip }` if idle was running in a field.
- The periodic autosave (every 5 s) and every other save leave `away` alone.
- Returning to the page clears `away` (the player never left).
- If the browser was killed without a close event, the last autosave is used as the close time.
- On load, if `away` is at least 60 s old, a reward window (“Idle reward”) opens. Under 60 s, idle simply resumes if it was running.

## Reward window choices

| Player | Base reward | Upgrade | Price |
|---|---|---|---|
| Non-VIP | 80% (auto) | → 100% | 1 Y / hour, rounded up |
| VIP | 100% (auto) | → 120% | 1 Y / hour, rounded up |

- **Yes:** pays Yttrium (if enough) and grants the upgraded amount.
- **No / close the window:** grants the base amount.
- If the player lacks Yttrium, the upgrade is refused and the window stays open.
- The window reopens from the idle panel (“Idle reward ready”) until it is answered.
- Idle time is capped at **12 hours** for the reward calculation.

## Offline formula (v5: simulated)

Since v5, kills per hour come from the combat simulator (real stats, skills, the map's monsters, deaths included). The section below is the previous formula, kept for reference.

## Previous offline formula (ATK + CP)

```
avgHP, avgDEF        = average over the map's normal monsters
DPS                  = max(1, ATK × 1.05 − avgDEF) × 1.05 / ASPD     // 1.05 ≈ crit factor
TTK (s)              = avgHP / DPS + 4                                // +4 s search & walk
KPH_base             = 3600 / TTK
power                = CP / recommendedCP(map)                        // Field 01: 150, Field 02: 450, Field 03: 900
efficiency           = power ≥ 1 ? min(1.25, 1 + (power − 1) × 0.25)
                                 : max(0.10, power²)
kills                = floor(hours × KPH_base × efficiency)           // 100% = normal idle rate
reward (100%)        = kills × avg monster EXP / Scandium / materials
reward (applied)     = reward (100%) × factor    // factor: 0.8 / 1.0 / 1.2 as in the table
```

Elites are excluded from offline results. The idle panel shows the live estimate for VIP players (“Offline estimate: X kills/h · Y% efficiency”).

## Not built yet (needs a real server)

- Hiding a VIP character from other players’ screens while offline.
- Real first-come-first-served kill contention for non-VIP players.
- Real monster instances per map that the server ticks while the player is away.
