# UI / UX

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.

---

## 1. Layouts

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
├ Bottom nav: menu icons ────────────────┤
```

- **Auto** picks by aspect ratio.
- Forced **Vertical on a wide screen** → phone frame (9 : 19.5).
- Forced **Horizontal on a tall screen** → stage rotated 90°, pointer input remapped.
- Respect safe areas (`viewport-fit=cover`, `env(safe-area-inset-*)`).
- Panels are light/dark theme-aware; the game world is not.

---

## 2. HUD components

| Component | Contents |
|---|---|
| Player card | Portrait, name, **tier + class/job name**, Base Lv badge, **Job Lv**, HP / SP bars, **Base EXP bar, Job EXP bar** |
| Wallet | Scandium, Yttrium, Lanthanum with icons (see `ECONOMY.md`) |
| CP | Shown on player card or character window |
| Idle panel | Auto-hunt switch, session time, defeated count, EXP/h, materials/h, claim offline rewards |
| Map banner | Subtitle, map name, coordinates, channel, online count |
| Minimap | Whole map; dots: player (white/violet), NPC (gold), players (blue); click to walk |
| Quest tracker | Title, objective, progress (e.g. “Job Lv 7 / 10”), **Go** button |
| Chat | Tabs All / Party / Guild / System, Enter to focus, speech bubbles |
| Hotbar | 10 slots, keys 1–0, cooldown overlay, SP cost |
| Menu | Character, Bag, Skills, Quests, Party, Guild, Shop, Settings (+ Dungeons later) |
| Windows | Centered, draggable in horizontal, Esc closes |
| Dialog | NPC portrait, name, text, Next / Close |
| Toasts | Neutral and gold (level-up, quest complete, job change) |

### Changes required by the new design
- Split EXP into **Base EXP** and **Job EXP** bars.
- Replace “Gold” with the **three-currency wallet**.
- Show **tier and class/job** instead of the fixed “Novice” label.
- Character window: add **CP**, refine level and card slots per equipped item.
- Add a **Dungeons** entry (daily dungeons + instance bosses) to the menu.

---

## 3. Prototype hotbar (placeholder skills)

| Key | Skill (EN / TH) | SP | Cooldown | Effect |
|---|---|---|---|---|
| 1 | Bash / ฟันกระแทก | 8 | 1.2 s | Slash arc |
| 2 | Heal / ฟื้นฟู | 12 | 3 s | +80 HP |
| 3 | Fire Bolt / ลูกไฟ | 15 | 2.5 s | Burst |
| 4 | Frost Nova / วงน้ำแข็ง | 18 | 4 s | Ring |
| 5 | Guard / ตั้งการ์ด | 6 | 5 s | Shield dome |
| 6 | Thunder / สายฟ้า | 20 | 5 s | Lightning |
| 7 | Gd Pulse / คลื่นแกโดลิเนียม | 30 | 8 s | Violet rings + pillar |
| 8 | Fly Wing / ปีกบิน | 0 | 6 s | Teleport within plaza |
| 9 | Red Potion / ยาแดง | — | 0.8 s | +120 HP |
| 0 | Blue Potion / ยาฟ้า | — | 0.8 s | +60 SP |

These will be replaced by real skills per class/job (`JOBS.md`).

---

## 4. Localization

- Every string through `t(key)`; both `th` and `en` required.
- Swapping language instantly updates HTML UI, canvas labels, chat, dialogs, open windows.
- Hint text: “Click…” on mouse, “Tap…” on touch.
- Thai NPC voice: friendly, calls the player “เจ้า”.
