# Rare Earth Online (REO) — Project Instructions

> This is the source of truth for building REO. Read it before every task. When a request conflicts with this file, follow the request and then update this file so it stays accurate.

---

## 1. Vision

REO is a **browser-based MMORPG with idle mechanics**. It plays like a classic quarter-view MMO (Ragnarok Online) with the cozy, hand-painted town feel of Tree of Savior. Every region is named after a **rare-earth element**; the magnetic, silver-violet glow of these elements is the visual and narrative thread of the world.

- **Genre:** MMORPG + idle (auto-hunt, offline rewards)
- **Platform:** Web browser first; must also work as a mobile web app / wrapped app
- **Languages:** Thai (default) and English, switchable at any time without a reload
- **Starting town:** every new player begins in **Gadolinium (แกโดลิเนียม) — Town of Beginnings (เมืองแห่งการเริ่มต้น)**

---

## 2. Non-negotiable rules

1. **Camera:** always locked on the player character at the center of the screen. No free camera panning.
2. **Movement:** click/tap anywhere on the map to walk there. Use A* pathfinding (8 directions, no corner cutting) plus line-of-sight smoothing. Holding the pointer keeps re-targeting (~every 0.3 s).
3. **Spawn:** new players spawn at the exact center of the starting map (Gadolinium tile 24, 24 → world 24.5, 24.5).
4. **Projection:** 2.5D isometric quarter view. Tile = 64 × 32 px. Depth-sort everything by `x + y`.
5. **Language swap:** never hard-code user-facing text. Every string goes through `t(key)`. Switching language must instantly update HTML UI, canvas labels, chat, dialogs, open windows and toasts.
6. **Layout swap:** support **Auto / Horizontal / Vertical**. Auto picks by aspect ratio. Switching must not reload or reset game state.
7. **Art is drawn in code** (canvas) unless real sprite assets are added later. No copyrighted characters, logos or assets from Ragnarok Online, Tree of Savior or any other game.

---

## 3. Art direction

**Style:** 2.5D anime, chibi proportions, semi-realistic shading.

| Element | Direction |
|---|---|
| Characters | Head ≈ 45% of height (~56 px tall at zoom 1). Big glossy eyes with two highlights, blush, spiky bangs, hair "angel ring" shine, thin dark outline `rgba(42,26,40,.6)` |
| Animation | Walk cycle (leg lift + arm swing + body bob), idle breathing bob, cape/ponytail sway |
| Facing | Front or back view, mirrored left/right from screen-space velocity |
| Buildings | Half-timbered walls, stone foundation, hip roofs with tile courses, warm lit windows with flower boxes, door awning |
| Nature | Layered round tree canopies (green, deep green, autumn, sakura), grass tufts, flower patches, smooth elliptical pond |
| Lighting | Sun from upper-left, shadows fall to the lower-right; lamps and crystal use additive glow |
| Ambience | Floating violet motes, soft vignette |

### Palette

| Name | Hex | Use |
|---|---|---|
| Gadolinium Violet | `#6E58E8` | Brand accent, crystal, buttons |
| Silver | `#EEF1FA` | Crystal light, player hair |
| Lantern Gold | `#E9C46A` | Highlights, NPC names, level-up |
| Plaza Stone | `#E3DCCD` | Town plaza |
| Meadow Green | `#4F8A4A` | Grass |
| Night Ink | `#141831` | Dark panels, banner |

### Type

- **Kanit** (Google Fonts) for all UI — supports Thai and Latin with one family.
- Fallbacks: `"Noto Sans Thai", Tahoma, system-ui, sans-serif`.
- No all-caps labels. Sentence case. Use typographic apostrophes (’) in English text.

---

## 4. Gadolinium — map spec

Grid: **49 × 49** tiles. Center tile **(24, 24)**.

| Feature | Location (tiles) | Notes |
|---|---|---|
| Main roads | rows 23–25 and columns 23–25 | Cobblestone, run edge to edge |
| Plaza | circle radius 7.3 around (24.5, 24.5) | Star inlay, rings, curb |
| Gadolinium Crystal | footprint 19–21 × 19–21 | Floating crystal, orbit rings, interactable |
| Adventurers’ Guild | x 13, y 13, 5 × 4 | Flag on roof |
| Tool Dealer | x 29, y 15, 3 × 3 | Bors stands outside |
| Silver Moon Inn | x 30, y 29, 4 × 4 | Two stories |
| Ironhart Forge | x 15, y 29, 4 × 3 | Chimney smoke, barrels |
| Houses | (36,19) (9,19) (27,7) (37,35) (8,34) (18,40), each 3 × 3 | Varied roof colors |
| Pond | ellipse center (37, 12), radii 4.2 × 3 | Blocked, animated glints |
| Market stalls | (28,21) (21,28) | Striped awnings |
| Forest edge | outer 4 tiles | Dense trees, road gaps act as gates (east → Field 01, west → Path to the Geosyncline, south → Road to the Ruins) |

Every building door is connected to the main road with a cobblestone path.

### NPCs

| ID | Name (EN / TH) | Tile | Role |
|---|---|---|---|
| `lumi` | Guide Lumi / ผู้นำทาง ลูมิ | (26, 21) | Starter quest giver |
| `bors` | Bors the Merchant / พ่อค้าบอร์ส | (31, 18) | Gives potions, shop |
| `veyra` | Captain Veyra / กัปตันเวย์รา | (19, 26) | Combat and idle tips |
| `helper` | Archetype Helper Sera / ผู้แนะแนวอาร์คีไทป์ เซร่า | (28, 27) | Explains the 4 archetypes; Archetype Trial at Job Lv 10 |

NPCs turn to face the player when within 3.5 tiles. Click an NPC → walk to an adjacent tile → open dialog on arrival.

### Starter quest chain — “A New Beginning / จุดเริ่มต้นใหม่”

| Stage | Objective | Reward |
|---|---|---|
| 0 | Talk to Guide Lumi | +40 Base EXP |
| 1 | Visit Bors at the Tool Dealer | +5 Red Potions, +60 Base EXP |
| 2 | Touch the Gadolinium Crystal | Light pillar effect, +180 Base EXP |
| 3 | Complete | — |

The current target shows a bouncing gold **!** marker. The quest tracker’s **Go** button auto-walks to it.

---

## 5. UI spec

### Horizontal (desktop)

```
┌──────────────┬──────────── map banner ───────────┬──────── tools ┐
│ Player card  │   Town of Beginnings / Gadolinium  │ ไทย|EN  ⟳ − + │
│ Idle panel   │   coords · channel · online        │ Minimap        │
│              │                                    │ Quest tracker  │
│                     (game world, player centered)                 │
│ Chat (tabs)  │            Hotbar 1–0              │ Menu 4×2       │
└──────────────┴────────────────────────────────────┴───────────────┘
```

### Vertical (mobile)

```
┌ Player card ────────┬ lang/layout/zoom ┐
│ Idle toggle         │ Minimap          │
│ Map banner          │ Quest tracker    │
│        (game world, player centered)   │
│ Chat ticker (tap to expand)            │
│        Hotbar 5 × 2                    │
├ Bottom nav: 8 menu icons ──────────────┤
```

- When forced **Vertical on a wide screen** → render inside a phone frame (9 : 19.5).
- When forced **Horizontal on a tall screen** → rotate the stage 90° and remap pointer input.
- Respect safe areas (`viewport-fit=cover`, `env(safe-area-inset-*)`).
- Theme-aware panels (light and dark tokens); the game world itself does not change with theme.

### Components

| Component | Contents |
|---|---|
| Player card | Chibi portrait, name, job, Lv badge, HP / SP / EXP bars, Gold |
| Idle panel | Auto-hunt switch, session time, defeated count, EXP/h, Gold/h, claim offline rewards |
| Map banner | Subtitle, town name, coordinates, channel, online count |
| Minimap | Whole-map iso view; dots: player (white/violet), NPC (gold), players (blue); click to walk |
| Status islands | FPS, ping (ms), players online, clock: four islands left of the minimap (portrait: one row at the top). See `STATUS.md` |
| Quest tracker | Title, objective, Go button |
| Chat | Tabs All / Party / Guild / System, input (Enter to focus), speech bubbles over heads |
| Hotbar | 8 skills + 2 potions, keys 1–0, conic cooldown overlay, SP cost |
| Menu | Character, Bag, Skills, Quests, Party, Guild, Shop, Settings |
| Windows | Centered, draggable in horizontal mode, Esc to close |
| Dialog | NPC portrait, name, text, Next / Close |
| Toasts | Neutral and gold (level-up, quest complete) |

### Skills (hotbar)

Skills belong to the archetype, not to a fixed list. The player chooses which skill, and which level of it, goes in each hotbar slot (`SKILL-SPEC.md` §5); potions sit in the hotbar as well. Skill points come from Job Lv: 1 Job Lv = 1 point (the first at Job Lv 2), spent by the player; every skill of every archetype, active or passive, starts at Lv 0 and is raised by hand (`SKILL-SPEC.md` §4). Changing class resets Job Lv, so the new class starts with no points. Full skill kits are in `ARCHETYPES.md`. The old fixed table (Guard, Thunder, Gd Pulse and so on) was removed.

---

## 6. Progression

- Base EXP to next level: `round(60 × lv^1.5)` (placeholder, see `CORE-LOOP.md`).
- Stat points, HP/SP growth and combat numbers: `COMBAT-FORMULAS.md` and `ARCHETYPES.md`.
- Idle rules and offline rewards: `IDLE.md`.
- Job Lv caps: Beginner 10, archetype 50 (`JOBS.md`).

---

## 7. Localization

- Dictionary `D = { en: {...}, th: {...} }`; lookup `t(key)` falls back to English, then the key.
- Placeholders use `{x}` with `fmt(key, {x: ...})`.
- Numbers use `toLocaleString("th-TH" | "en-US")`.
- Chat messages store both languages (`{en, th}`) or a key (`{k}`) so the log re-renders on swap. Player-typed text is stored raw.
- Hint text differs by input type: “Click…” on mouse, “Tap…” on touch.
- Thai tone: friendly fantasy-RPG voice; NPCs address the player as “เจ้า”.

**Adding any new text:** add the key to **both** `en` and `th` in the same change.

---

## 8. Technical architecture (current prototype)

- **Single self-contained HTML file**: HTML + CSS + JS inline, Google Fonts only. No build step.
- **Canvas 2D** for the world; HTML overlay for UI (`#ui`, `pointer-events: none` except panels).
- **Ground** pre-rendered once to an offscreen canvas at 1.25× scale; each frame draws only the visible source rect.
- **Draw order per frame:** background → ground → water glints → click marker → depth-sorted objects and characters → effects → labels (signs, names, bubbles, quest marks) → screen-space motes and vignette.
- **Culling:** skip objects outside the view plus a margin.
- **Key constants:** `TW=64, TH=32, N=49, GS=1.25`; iso helper `P(x, y, z)`.
- **Input:** pointer events; sprite hit-test before tile hit-test; wheel and +/− zoom (0.6–1.8×).
- **State:** single `S` object (level, EXP, HP, SP, gold, potions, quest stage, idle data, settings).

### Planned production direction

| Area | Target |
|---|---|
| Client | TypeScript + PixiJS (WebGL) or Phaser, sprite atlases |
| Server | Authoritative game server (WebSocket), tick-based movement validation |
| Data | Maps, NPCs, quests, items and strings in JSON |
| Packaging | PWA first, then Capacitor for app stores |

---

## 9. How to work on this project

1. Read this file first.
2. Keep the prototype a single HTML file until the move to a real engine is decided.
3. For small changes, edit the existing artifact in place instead of rewriting it.
4. Every change must keep working in **both languages** and **both layouts**.
5. Test: click-to-walk, NPC dialog, quest chain, idle toggle, language swap mid-dialog, layout swap with a window open.
6. After adding a feature, update the relevant section of this file.

### Definition of done

- [ ] No hard-coded user-facing strings
- [ ] Works in Horizontal, Vertical, and forced/rotated modes
- [ ] Player stays centered; pathfinding avoids all blocked tiles
- [ ] No console errors
- [ ] Original art only

---

## 10. Roadmap

1. ✅ **Field maps 01–03** with monsters, Elites and the Gadolith boss
2. ◐ **Job system:** Archetype Trial done (v5.1); the 16 classes and 32 jobs are still open (`JOBS.md`)
3. ✅ **Inventory and equipment** (10 slots, compare, multi-sell, refine)
4. **Party and guild** with real networking
5. ✅ **Path to the Geosyncline and Road to the Ruins** (v19): gated by Lv and CP, aggressive monsters with skills, no boss yet
6. **Next regions** named after rare-earth elements (e.g. Neodymium, Europium, Cerium)
7. ◐ **Sound and music:** generated 8-bit audio done (v18); volume sliders still open (`AUDIO.md`)
8. ◐ **Save system:** local accounts done; server accounts still open (`ACCOUNTS.md`)
