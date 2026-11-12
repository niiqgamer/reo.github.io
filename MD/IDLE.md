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
5. Closing the game while idle counts as "game closed". Idle time is measured from the moment the page is hidden or closed.

## Bosses and idle (v6)
Idle **never auto-targets bosses** (and still skips Elites that are too strong, Base Lv < Elite Lv + 3). Bosses are hands-on. A player who starts auto-quest for a boss quest does fight it: auto-quest targets it on purpose and the skill rotation then runs.

## Auto-idle after standing still (v5.3)

- If the character stands still for **5 minutes in a field with monsters**, Idle starts automatically.
- "Still" means: not walking or auto-walking, no target, not casting, no open dialog or quest walk, not dead, not already idling.
- Towns never auto-start Idle (no monsters spawn there).
- After the player **stops Idle manually**, auto-start waits until the player moves again. This stops the game from restarting Idle right after a manual stop.
- Settings has a toggle "Auto-idle after 5 min standing still" (on by default).

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
