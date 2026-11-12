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

---

## 5. v3 HUD changes
- Removed Thai/English and layout buttons from the HUD — they live in **Settings**.
- **Minimap panel:** header with map name and collapse button; on the map: **Return to town** (fields only) and **zoom + / −** with 5 steps: Very far 0.6 · Far 0.8 · Standard 1.0 · Near 1.25 · Very near 1.55 (mouse wheel steps too; no slider).
- **Quest tracker:** collapsible, up to 5 tracked quests, color-coded, tap to auto-quest.
- **Idle:** single prominent button; status panel expands once idle starts (see `IDLE.md`).
- Banner shows recommended CP in fields.


---

## 6. Character info page (v6, after the reference screenshot)

Big two-panel window (dark navy theme in every theme mode). On phones the panels stack.

**Left panel**
- Portrait column: the active character (highlighted, small HP bar) and **2 locked slots** reserved for future characters.
- Equipment around the character: top row **Belt, Bracelet** (empty, unlock later); left column **Weapon, Armor, Legs**; right column **Off-hand, Necklace, Ring**. A round **Style** (costume) button sits at the character's feet.
- Each item frame: border and background colour by rarity (grey common, blue uncommon, red rare, violet epic), **Lv** top-left, **refine +N** bottom-left, **3 card-slot pips** top-right (filled = card inserted).
- Quick-item row with counts (Red Potion, Blue Potion, Fly Wing, Apple), then **CP** in big gold numbers.
- Tap an item for its details (name, rarity, slot, Lv, refine, card slots, mock stat).
- The character is drawn large with idle animation on a glowing platform.

**Right panel**
- Record: monsters defeated and defeats.
- Role icon + role (Melee / Ranged / Magic / Support), then `[C1] [Lv 20] Fighter`, Job Lv `x/cap`, and the yellow **Archetype Trial / Job Change** button. At C0 with Job Lv 10 it is enabled and walks you to the Archetype Helper (warps to town first if you are in a field). At C1 it is disabled until C2 exists.
- Base EXP bar (gold, percentage and numbers) and Job EXP bar (green).
- Left column of stat tiles (STR, AGI, VIT, INT, DEX, LUK, **Total stats**) with `+` buttons and Blessing bonus in green; right column: weapon type, armor type, then a striped **Details** table (ATK, MATK, DEF, MDEF, HP, SP, ASPD, HIT, FLEE, CRIT, Perfect dodge, Cast).
- Auto-assign and Reset buttons at the bottom.

**Equipment is a mockup:** the gear shown per archetype (names, levels, refine, cards) is display only and does not change stats yet. Real equipment, refine, card and option systems come later (`CORE-LOOP.md` §4).

**Not copied from the reference:** the achievement score, the top tab icons (rewards, bag, premium) and multiple playable characters.


---

## 7. Inventory (v7, replaces "Bag")
Title "Inventory" / "คลังของ". Full rules in `ITEMS.md` §5. Layout: tabs and capacity on top; a 5-column grid on the left (6 on phones); details on the right (stacked below on phones) with the buttons Use / Equip / Refine / Sell / Discard.


---

## 8. Login page (v14)
Full-screen page shown before the game. Dark violet background with floating crystal shards and the Gadolinium crystal as the logo. Three tabs (Login, Register, Guest), a Thai/English switch at the top right, a password strength bar on Register, and a small note that accounts are stored in this browser only. Works on phones (single column, 16 px inputs so iOS does not zoom, scrolls when the form is taller than the screen). Details and rules: `ACCOUNTS.md`.


---

## 9. Window system (v15, after the Character Info reference)

All menu windows share one look. It is always dark navy, whatever the page theme.

**Frame:** rounded navy frame with a periwinkle border; a **periwinkle title bar** (bold white title, round close button); an inner darker panel for the content; and, for the character group, a **bottom bar** of three buttons.

**Palette (muted on purpose, each colour has one job):**

| Token | Colour | Used for |
|---|---|---|
| `--nv1` / `--nv2` / `--nv3` | `#101a5c` / `#1a2780` / `#2b3a9a` | frame and body / raised / dark buttons |
| `--pv` periwinkle | `#7c88d8` | the active thing: selected tab, main button, section bars, title bar |
| `--wh` off-white | `#f2f4ff` | the idle thing: unselected tabs and neutral buttons (text in navy) |
| gold | `#e8cb78` | levels and rewards |
| mint | `#7ae6ac` | gains (stat lines, comparison up) |
| rose | `#f2909c` | losses and warnings |
| red `#a8161f` on white | | the CP number |

Rarity frames keep their colours (white, green, blue, purple, red).

**Components:** tabs are rounded pills (periwinkle = selected, off-white = not selected); section headings are fading periwinkle bars; buttons are pills with a soft bottom edge; tiles and rows are translucent periwinkle on navy.

**Character Info (the hub):**
- Name bar: `Arin [C1] [Fighter] Lv 38`, with the active portrait and two locked character slots at the left.
- Tabs **Equipment** and **Costume**.
- Equipment: 10 slots around the character (left: Top Headgear, Lower Headgear, Weapon, Garment, Ring; right: Mid Headgear, Armor, Shield, Shoes, Bracelet), the **Combat Point** box under the character, the quick-item row, and a detail strip (stats, abilities, set, Unequip, Refine) for the selected slot.
- Costume: the character on its platform with a "coming soon" note (the round shirt button on the Equipment page opens it).
- **Status** (bottom bar): record, class line and the Archetype Trial button, EXP bars, the six stats with + buttons, total, weapon and armor types, the details table, and Auto-assign and Reset.
- Bottom bar: **Status, Skill, Items**. Skill opens Skills, Items opens the Inventory. The same bar appears in those two windows, with the current one highlighted.

Every earlier feature is still there; Status is where the old right-hand panel went.

**Phones:** the card takes the full width, slots shrink (58 px), and the content scrolls inside the frame. A new page starts at the top; actions on the same page keep the scroll position.


---

## 10. HUD and windows, version 17

**Top centre:** the map name shows only when you enter a map, then fades. During a fight the top centre shows the **monster panel** (position and size changed in v18.2, see §12): name, Lv, element, then a live HP bar with `435 / 600`. A white trail follows the red bar down so you see how much each hit took, and the damage number floats up. Elite and Boss get their own colours. It hides about 5 seconds after the fight. Announcements appear above it (`WORLD-MAP.md` §4).

**Idle:** one large toggle button to the right of the hotbar (not part of it). Off: "Idle". On: a spinner, "Idling…" and the running time. No panel opens. Pressing it again stops Idle and opens the **Idle Summary** (time, kills, Base/Job EXP, Scandium, equipment, every item gained). The gear button beside it opens **Idle Settings** (mock-up).

**Status islands (top right):** FPS, ping, clock, players online, players on this map. Each has its own colour; FPS and ping turn amber and red when they get worse.

**Menu (bottom right):** landscape has a collapse button; phones keep the full bottom bar.

**Windows**
- Up to three open at once: slot A (main), slot B (second), slot C (item detail). Each window has its own fixed size, so nothing bounces when the content changes.
- **Character** opens **Equipment + Status** together (side by side; stacked on phones in one scrolling column). Equipment is 20% smaller, with only your face beside the name, a **Title (soon)** row where the potions were, and no item strip: tap a worn piece to open the **Item Detail** window (Unequip, Refine).
- **Inventory**: 100 base slots, 50 per page, per type, Auto sort (type > name > stars > price), Select many, and a **+** to the Cash Shop. Item details open in their own window (scrolls if long).
- **Navigation bar** at the bottom of Character, Status, Inventory, Skills, Quests, Party and Guild, using the same words as the menu. It never shows a button to a window that is already open.
- **Live updates:** an open window redraws itself within a quarter of a second when the data it shows changes (items, quests, EXP, currencies, equipment). It never redraws while a button is pressed or a text box is focused.
- On phones windows stop above the menu bar, so the menu is always reachable.
- Esc closes the item detail first, then everything. **M** opens the World Map.

**Settings:** Graphic | Sound | Other | Account. Each setting has a short description and, for switches, an ON/OFF label.


---

## 11. Changes in version 18 (these replace parts of §10)

- **Navigation bar removed** from every window (it was repeated and used too much space). Windows are a little shorter.
- **Character opens alone** (Equipment). **Status** has its own button in the menu, right after Character. The menu is a **3 × 3** grid on desktop; phones keep one bar with 9 buttons.
- **Player card:** a bottom row with the **CP island on the left** and **Scandium on the right** (for example `CP 18,894` and `578,568 Scandiums`). The full wallet (Scandium, Yttrium, Lanthanum) moved to the **Equipment window, under the Title row**.
- **Idle button:** the same size as a hotbar slot (46 px; 44 on phones), **gold** with a glint sweeping across it. It shows `IDLE` or `IDLING` and a spinning ring while on. The **settings gear is a small badge** on its top-right corner. Idle Summary and Idle Settings are unchanged.
- **Status bar:** **one row**, top right: `FPS | PING | USER ONLINE | USER ON MAP | SERVER TIME`. It opens fully for **30 seconds** when you enter the game or change map, then shrinks to one island, **SERVER TIME**. FPS and ping are coloured. Phones use shorter labels.
- **Minimap:** zoom buttons have no text (tooltip only). The **World Map button** is in the **top-right corner** of the map frame (the Return to town button stays at the bottom left).
- **Announcements** appear under the status row.
- **Inventory:** tabs **Consumable > Equipment > Material > Quest** (no "All"; opens on Consumable). Bottom of the window, top to bottom: grid; one row with `Select many` and the page arrows `Page x/x`; last row with `Sort items` on the left and `Slots xx/100` plus `+ Expand slots` on the right. **Sort items** is one toggle: Name > Rarity (Equipment tab only) > Sell price, and each press sorts. Stars are the same small size as in the Character window and never overflow the cell.
- **Settings > Graphic > UI Display Mode:** System, Light, Dim. It changes the panels on the main screen (the windows stay navy). Saved.


---

## 12. Changes in version 18.2

**Monster panel** (name, Lv, element, live HP; Elite and Boss colours unchanged)
- Now has its own container (`#mobC`) instead of sitting under the map banner, so it can be placed on its own.
- **Landscape:** compact. 300 px wide (boss 380 px), about 48 px tall, smaller text and a 16 px HP bar. Top centre at 72 px, a little below the status row, not at the very top. While a system announcement shows it shifts down 40 px to make room.
- **Portrait:** bottom centre, directly above the hotbar (about 9 px gap; `bottom: 186px`). Width follows the screen (screen width − 140 px, max 260 px) so it never covers the Chat button or the Idle button. Hidden while an NPC dialog is open, because the dialog uses the same spot.
- Behaviour is unchanged: it shows when fighting, hides about 5 s after combat, white trail on damage, Crystal Slam warning for the boss.

**Menu (landscape):** fixed **3 × 3** at every window width. Before, the compact layout (window narrower than 1120 px) switched it to 4 columns (4 × 3). Compact buttons keep their size (42 px, icons only). Portrait is unchanged: one bottom bar with 9 buttons.

