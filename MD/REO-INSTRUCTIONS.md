# Rare Earth Online (REO) — Project Instructions

> Master instruction file. Read it before every task, then read the design file that matches the task (see **Document map**). When a request conflicts with these files, follow the request and update the affected file in the same change.

---

## 1. Vision

REO is a **browser-based MMORPG with idle mechanics**. It plays like a classic quarter-view MMO (Ragnarok Online) with the cozy, hand-painted town feel of Tree of Savior. Every region, currency and key item is named after a **rare-earth element**; their magnetic, silver-violet glow is the visual and narrative thread of the world.

- **Genre:** MMORPG + idle (auto-hunt, idle material farming, offline rewards)
- **Platform:** web browser first; must also work as a mobile web app / wrapped app
- **Languages:** Thai (default) and English, switchable at any time without a reload
- **Starting town:** every new player begins in **Gadolinium (แกโดลิเนียม) — Town of Beginnings** as a **Beginner (C0)**

---

## 2. Document map

| File | Read it when working on |
|---|---|
| `REO-INSTRUCTIONS.md` (this file) | Anything — rules, art, tech, workflow, glossary |
| `design/CORE-LOOP.md` | Combat rewards, leveling, EXP, equipment, CP, quests, instance bosses, daily dungeons, idle farming |
| `design/JOBS.md` | Archetypes, classes, jobs, attack ranges, job change quests, level caps |
| `design/ECONOMY.md` | Currencies (Scandium, Yttrium, Lanthanum), shops, trading, fees |
| `design/GADOLINIUM.md` | Starting town map, buildings, NPCs, starter quest |
| `design/UI-UX.md` | HUD, layouts (horizontal / vertical), windows, hotbar, localization |

Each design file ends with **Open questions**. Do not invent answers to those in code; use clearly marked placeholders until they are decided.

---

## 3. Non-negotiable rules

1. **Camera** is always locked on the player character at the center of the screen. No free panning.
2. **Movement:** click/tap anywhere on the map to walk there. A* pathfinding (8 directions, no corner cutting) plus line-of-sight smoothing. Holding the pointer keeps re-targeting (~every 0.3 s).
3. **Spawn:** new characters spawn at the exact center of Gadolinium (tile 24, 24 → world 24.5, 24.5).
4. **Projection:** 2.5D isometric quarter view. Tile = 64 × 32 px. Depth-sort by `x + y`.
5. **Ranges are measured in tiles** (see `design/JOBS.md`).
6. **No hard-coded user-facing text.** Every string goes through `t(key)` and exists in both `th` and `en`.
7. **Layout swap** Auto / Horizontal / Vertical never reloads or resets state.
8. **Original art only.** No characters, logos or assets from Ragnarok Online, Tree of Savior or any other game.
9. **Use the official terms** in the glossary below — in code identifiers, UI text and docs.

---

## 4. Glossary

| Term | Meaning |
|---|---|
| **Archetype** | One of 4 combat roles: Fighter, Ranger, Spellcaster, Supporter |
| **Class** | One of 16 first-tier specializations (e.g. Swordman). Reached at **C1** |
| **Job** | One of 32 final specializations (e.g. Knight). Reached at **C2** |
| **C0 / C1 / C2** | Character tier: Beginner / Class / Job |
| **Base Level (Base Lv)** | Character level. Current cap **99** |
| **Job Level (Job Lv)** | Level within the current tier. Cap 10 at C0, 50 at C1, 50 at C2 |
| **Base EXP / Job EXP** | Separate EXP pools for Base Lv and Job Lv |
| **CP** | Combat Power — a single number summarizing a character’s strength |
| **Refine** | Upgrade level on a piece of equipment |
| **Card slot** | Socket on equipment that holds a card |
| **Equipment options** | Random or rolled bonus stats on equipment |
| **Scandium (Sc)** | Common in-game gold |
| **Yttrium (Y)** | Untradable, earnable cash (bound) |
| **Lanthanum (La)** | Tradable premium cash |
| **Instance boss** | Boss fought in a private instanced map |
| **Daily dungeon** | Dungeon with a daily entry limit |
| **Idle farming** | Offline/auto activity that yields materials |

---

## 5. Art direction

**Style:** 2.5D anime, chibi proportions, semi-realistic shading.

| Element | Direction |
|---|---|
| Characters | Head ≈ 45% of height (~56 px at zoom 1). Glossy eyes with two highlights, blush, spiky bangs, hair shine, thin outline `rgba(42,26,40,.6)` |
| Animation | Walk cycle (leg lift, arm swing, bob), idle breathing, cape/ponytail sway |
| Facing | Front or back view, mirrored left/right from screen-space velocity |
| Buildings | Half-timbered walls, stone foundation, hip roofs with tile courses, warm windows with flower boxes |
| Nature | Layered round canopies (green, deep green, autumn, sakura), grass tufts, flower patches |
| Lighting | Sun from upper-left, shadows to lower-right; additive glow for lamps, crystals, skills |
| Ambience | Floating violet motes, soft vignette |

### Palette

| Name | Hex | Use |
|---|---|---|
| Gadolinium Violet | `#6E58E8` | Brand accent, crystal, primary buttons |
| Silver | `#EEF1FA` | Crystal light, highlights |
| Lantern Gold | `#E9C46A` | NPC names, level-up, quest marks |
| Plaza Stone | `#E3DCCD` | Town paving |
| Meadow Green | `#4F8A4A` | Grass |
| Night Ink | `#141831` | Dark panels, banner |

Archetype accent colors are defined in `design/JOBS.md`; currency colors in `design/ECONOMY.md`.

### Type

- **Kanit** (Google Fonts) for all UI — Thai and Latin in one family.
- Fallbacks: `"Noto Sans Thai", Tahoma, system-ui, sans-serif`.
- Sentence case, no all-caps labels, typographic apostrophes (’) in English.

---

## 6. Technical architecture

### Current prototype

- **Single self-contained HTML file** (HTML + CSS + JS inline, Google Fonts only). No build step.
- **Canvas 2D** for the world; HTML overlay `#ui` for HUD (`pointer-events: none` except panels).
- **Ground** pre-rendered once to an offscreen canvas at 1.25×; each frame draws only the visible rect.
- **Frame order:** background → ground → water glints → click marker → depth-sorted objects & characters → effects → labels → screen-space motes & vignette.
- **Constants:** `TW=64, TH=32, N=49, GS=1.25`; iso helper `P(x, y, z)`.
- **State:** single `S` object. Must be extended to hold `baseLv, jobLv, baseExp, jobExp, tier, archetype, class, job, sc, y, la` (see design files).

### Production direction

| Area | Target |
|---|---|
| Client | TypeScript + PixiJS (WebGL) or Phaser, sprite atlases |
| Server | Authoritative game server over WebSocket; server validates movement, damage, drops, currency |
| Data | Maps, monsters, jobs, skills, items, quests, shops and strings as JSON |
| Packaging | PWA first, then Capacitor for app stores |

**Server authority rule:** anything that creates value — EXP, items, Scandium, Yttrium, Lanthanum, refine results — is decided on the server, never the client.

---

## 7. Localization rules

- Dictionary `D = { en: {...}, th: {...} }`; `t(key)` falls back to English, then the key.
- Placeholders `{x}` with `fmt(key, {x})`; numbers via `toLocaleString("th-TH" | "en-US")`.
- Chat stores `{en, th}` or `{k}` so the log re-renders on swap; player-typed text stays raw.
- **Proper names stay in English in both languages** for jobs/classes/currencies unless a Thai name is defined in the design file (e.g. show “Knight” in Thai UI as `Knight` until a Thai name is approved).
- NPC voice in Thai: friendly fantasy-RPG tone; NPCs call the player “เจ้า”.
- Add every new key to **both** languages in the same change.

---

## 8. How to work on this project

1. Read this file, then the design file for the task.
2. Keep the prototype a single HTML file until the move to a real engine is decided.
3. Small changes: edit the existing artifact in place instead of rewriting it.
4. Every change must work in **both languages** and **both layouts**.
5. Test: click-to-walk, NPC dialog, quest chain, idle toggle, language swap mid-dialog, layout swap with a window open.
6. Update the relevant design file whenever behavior changes.

### Definition of done

- [ ] No hard-coded user-facing strings
- [ ] Works in Horizontal, Vertical and forced/rotated modes
- [ ] Player stays centered; pathfinding avoids blocked tiles
- [ ] Uses glossary terms (Scandium, not “Gold”; Beginner, not “Novice”)
- [ ] No console errors
- [ ] Original art only

---

## 9. Roadmap

| Step | Goal | Design file |
|---|---|---|
| 1 | Rename prototype terms: Gold → Scandium, Novice → Beginner (C0); split EXP into Base/Job | CORE-LOOP, ECONOMY |
| 2 | Field map east of Gadolinium with original monsters and real combat (targeting, damage numbers, drops) | CORE-LOOP |
| 3 | C0 → C1 class change quests for the 4 archetypes | JOBS |
| 4 | Equipment: refine, card slots, options, CP | CORE-LOOP |
| 5 | Daily dungeon + first instance boss | CORE-LOOP |
| 6 | Idle material farming + offline rewards | CORE-LOOP |
| 7 | Currency wallet, NPC shop (Scandium), Yttrium shop, Lanthanum premium shop and trading | ECONOMY |
| 8 | C1 → C2 job change quests | JOBS |
| 9 | Party, guild, real networking | — |
| 10 | Next regions named after rare-earth elements (e.g. Neodymium, Europium, Cerium) | — |
