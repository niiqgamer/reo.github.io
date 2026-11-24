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
| Chat | Tabs All / Party / Guild / System, Enter to focus, speech bubbles. Whispers show in All in pink |
| Hotbar | 10 free slots, keys 1–0, cooldown overlay, SP cost; drag and drop (§25) |
| Menu | Character, Status, Bag, Skills, Quests, Social, Shop, Settings (+ Dungeons later). Social holds the Friends, Party and Guild tabs |
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

> *Historical (v3).* Superseded: Bash is now **Heavy Strike** (SP 5, cooldown 5 s, range 1.6 tiles, Basic Skill Lv 4). Current skills: `JOBS.md` §1b and `ARCHETYPES.md`.

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

- Every string through `t(key)`; `th`, `en` and `jp` required (v20.8: Japanese added as the third language).
- Pair data (`[en, th]` arrays and `{en, th}` objects: items, gear, abilities, set names, RARN, chat seed lines) takes its Japanese from the `JPX` table, keyed by the English text. Read it with `LP(pair)`, `LO(obj)` or `PT(msg)`, never `[lang=="th"?1:0]`.
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
Full-screen page shown before the game. Dark violet background with floating crystal shards and the Gadolinium crystal as the logo. Three tabs (Login, Register, Guest), a Thai / EN / 日本語 switch at the top right, a password strength bar on Register, and a small note that accounts are stored in this browser only. Works on phones (single column, 16 px inputs so iOS does not zoom, scrolls when the form is taller than the screen). Details and rules: `ACCOUNTS.md`.


---

## 9. Window system (v15, after the Character Info reference)

All menu windows share one look. It is always dark navy, whatever the page theme. **(v19.2: Character, Status, Inventory and Item Detail use the light frame, see §17. v19.6: every window uses it, in Light or Dim, see §21. The navy look is retired.)**

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

**Status islands (left of the minimap, v18.3):** four separate islands in a column: FPS, ping, players online, clock. FPS and ping turn amber and red when they get worse. See §13.

**Menu (bottom right):** landscape has a collapse button; phones keep the full bottom bar.

**Windows**
- Up to three open at once: slot A (main), slot B (second), slot C (item detail). Each window has its own fixed size, so nothing bounces when the content changes. **Exception: Character** has no fixed height. Its height follows the content, so it never shows a scroll bar; the Equipment and Costume pages share one minimum height (`.chr-panel{min-height:447px}`), so the window does not jump when you switch tabs. A scroll bar appears only if the screen itself is shorter than the window.
- **Character** opens **Equipment + Status** together (side by side; stacked on phones in one scrolling column). Equipment is 20% smaller, with only your face beside the name, a **Title (soon)** row where the potions were, and no item strip: tap a worn piece to open the **Item Detail** window (Unequip, Refine).
- **Inventory**: 100 base slots, 50 per page, per type, Auto sort (type > name > stars > price), Select many, and a **+** to the Cash Shop. Item details open in their own window (scrolls if long).
- **Navigation bar** at the bottom of Character, Status, Inventory, Skills, Quests and Social, using the same words as the menu. It never shows a button to a window that is already open.
- **Live updates:** an open window redraws itself within a quarter of a second when the data it shows changes (items, quests, EXP, currencies, equipment). It never redraws while a button is pressed or a text box is focused.
- On phones windows stop above the menu bar, so the menu is always reachable.
- Esc closes the item detail first, then everything. **M** opens the World Map.

**Settings:** Graphic | Sound | Other | Account. Each setting has a short description and, for switches, an ON/OFF label. (**v20.11:** Graphic also has Character look, see §27.)


---

## 11. Changes in version 18 (these replace parts of §10)

- **Navigation bar removed** from every window (it was repeated and used too much space). Windows are a little shorter.
- **Character opens alone** (Equipment). **Status** has its own button in the menu, right after Character. The menu is a **3 × 3** grid on desktop; phones keep one bar with 9 buttons.
- **Player card:** a bottom row with the **CP island on the left** and **Scandium on the right** (for example `CP 18,894` and `578,568 Scandiums`). The full wallet (Scandium, Yttrium, Lanthanum) moved to the **Equipment window, under the Title row**. **(v19.2: the wallet row is removed from the Character window, see §17.)**
- **Idle button:** the same size as a hotbar slot (46 px; 44 on phones), **gold** with a glint sweeping across it. It shows `IDLE` or `IDLING` and a spinning ring while on (**v19.1:** the ring is replaced by four circling arrows, and the button now sits inside the hotbar panel, see §16). The **settings gear is a small badge** on its top-right corner. Idle Summary and Idle Settings are unchanged.
- ~~**Status bar:** one row, top right~~ **Replaced in v18.3** by four status islands beside the minimap (see §13). The 30 second expand and collapse is gone.
- **Minimap:** zoom buttons have no text (tooltip only). The **World Map button** is in the **top-right corner** of the map frame (the Return to town button stays at the bottom left).
- **Announcements** appear at the top centre (v18.3: there is no status row any more, so they sit at 12 px). **v19.1:** portrait moved to the bottom, see §16.
- **Inventory:** tabs **Consumable > Equipment > Material > Quest** (no "All"; opens on Consumable). Bottom of the window, top to bottom: grid; one row with `Select many` and the page arrows `Page x/x`; last row with `Sort items` on the left and `Slots xx/100` plus `+ Expand slots` on the right. **Sort items** is one toggle: Name > Rarity (Equipment tab only) > Sell price, and each press sorts. Stars are the same small size as in the Character window and never overflow the cell. **(v19.2: tabs, page size and footer replaced, see §17.)**
- **Settings > Graphic > UI Display Mode:** System, Light, Dim. It changes the panels on the main screen (~~the windows stay navy~~ **v19.6:** and every window, see §21). Saved.


---

## 12. Changes in version 18.2

**Monster panel** (name, Lv, element, live HP; Elite and Boss colours unchanged)
- Now has its own container (`#mobC`) instead of sitting under the map banner, so it can be placed on its own.
- **Landscape:** compact. 300 px wide (boss 380 px), about 48 px tall, smaller text and a 16 px HP bar. Top centre at 72 px, a little below the top edge, not at the very top. While a system announcement shows it shifts down 40 px to make room.
- **Portrait:** bottom centre, directly above the hotbar (about 9 px gap; `bottom: 186px`; **v19.1:** `188px`, centred on the same line as the hotbar panel, see §16). Width follows the screen (screen width − 140 px, max 260 px) so it never covers the Chat button or the Idle button. Hidden while an NPC dialog is open, because the dialog uses the same spot.
- Behaviour is unchanged: it shows when fighting, hides about 5 s after combat, white trail on damage, Crystal Slam warning for the boss.

**Menu (landscape):** fixed **3 × 3** at every window width. Before, the compact layout (window narrower than 1120 px) switched it to 4 columns (4 × 3). Compact buttons keep their size (42 px, icons only). Portrait is unchanged: one bottom bar with 9 buttons.


---

## 13. Changes in version 18.3 (status islands)

The old status bar (`FPS | PING | USER ONLINE | USER ON MAP | SERVER TIME`) is **removed**. Its readings now live in four separate **islands** beside the minimap.

**Landscape**
- A column of 4 islands, right-aligned, directly **left of the minimap**: `🎮 60 FPS`, `📡 25 ms`, `🌏 1,286 ONLINE`, `⏱ 12:25 PM` (the icons are drawn in code, not emoji). Each island is 32 px tall with a rounded 12 px corner and uses the same panel colours as the minimap, so it follows System, Light and Dim.
- Position: top 12 px, level with the top of the minimap panel, 10 px from it (`right: 272px`). Gap between islands: 8 px. While a system announcement shows, the column slides down 46 px so it never sits under the announcement (portrait: no shift).
- **USER ON MAP is removed.** There is no SERVER TIME label any more: the clock island shows only the time (device clock, locale format; Thai uses 24 hours).
- Always visible. The 30 second expand and collapse after entering a map is gone.
- Colours: FPS and ping numbers are green, amber or red (FPS ≥ 50 / ≥ 30 / lower; ping < 40 / < 120 ms / higher; `—` when unknown). The online number is green. Labels and the clock are plain text colour. Icons: FPS blue, ping violet, online sky blue, clock neutral.
- The minimap column moved back up to 12 px, and system announcements now sit at 12 px (the banner shifts 60 px down while one shows).

**Portrait**
- There is no room beside the minimap (the player card fills the left), so the same four islands sit in **one row at the very top**, right-aligned (22 px tall, 9.8 px text). Below 350 px width the `ONLINE` label is hidden so the row still fits (checked at 320 px).

**Data and rules (unchanged):** FPS is measured every 0.5 s; ping and online are simulated until a server exists (hover says so); the row is redrawn only when a value, the language or the minute changes. English labels: `FPS`, `ms`, `ONLINE`; Thai: `FPS`, `ms`, `ออนไลน์`. `netExpand()` still exists for old callers and does nothing.


---

## 14. Floating combat text (v18.4)

Damage numbers the player deals now use a bouncy cartoon style. Drawn on the game canvas in `drawFx` (`k:"dmg"` with `pop:true`); font is **Kanit** (`FONT`), weight 700.

| | Normal hit | Critical hit | Weak-point hit |
|---|---|---|---|
| Colour | white (or skill colour) | gold `#ffd84a` | cyan `#8ff0ff` |
| Size | 18 px | 30 px | 22 px |
| Outline | 4 px, `rgba(13,18,48,.92)` | 5 px, same colour | 4 px |
| Entrance | scale 0.3 → 1.25 → 1.0 (first 20 % of life) | scale 0.1 → 1.5 → 1.0 with a wobble −12° → +8° → −5° → +3° → 0° (first 32 %) | like normal, larger |
| Rise | 30 px | 36 px | 30 px |
| Life | 0.95 s | 1.15 s | 0.95 s |
| Label | none | **CRITICAL!** (EN) / **คริติคอล!** (TH), 12 px, above the number | none |

- The label comes from the localization key `fctCrit` (`D2.en` / `D2.th`) and follows the language setting instantly.
- The old "!" after a critical number is gone; the label replaces it.
- Unchanged: MISS, damage taken by the player, `+EXP` / `+Sc` / item floats, boss warnings (they still use the old `dmg` style without `pop`).
- Changed in code: `applyHit` (adds `pop`, `crit`, longer life for crits) and `drawFx` (new branch before the old `dmg` branch).


---

## 15. Pixel hit effects (v18.4)

Every hit the player lands on a monster now plays a small pixel-art effect, replacing the old 6-dot `burst`. Pixels are 2×2 world px (one "cell"); everything snaps to that grid. Effects are centred on the monster's body (half its height) and scale with monster size (`k = height / 36`, clamped 0.8–1.8). Code: `hitFx()` (spawns), `hfxDraw()` (draws), `k:"hfx"` entries in `fx`.

| | Normal hit | Critical hit | Weak-point hit |
|---|---|---|---|
| Palette | white → skill colour → dark (white → yellow → orange → dark red if the skill has no colour) | gold ramp `#fff → #fff2a8 → #ffd84a → #f29a1d → #a3441a` | ice ramp `#fff → #c9f6ff → #8ff0ff → #3aa5d6 → #17336b` |
| Flash | small cross, 0.09 s | solid white disc, 0.05 s (hero frame) | like normal |
| Slash | 3-line diagonal streak, 0.14 s, angled from the attack direction | – | like normal |
| Sparks | 7 pixel sparks, 1–2 cells, gravity, one bounce off the ground | 18 shards, 2–3 cells, faster, one bounce | like normal |
| Extras | – | dithered expanding ring (4×4 Bayer, 0.4 s, max 6 at once), 10 speed rays, 5 twinkling stars | – |
| Screen shake | none | ±3 px, decays over 0.3 s | none |
| Hit-stop | none | 0.06 s freeze of the whole update loop, at most once per 0.4 s | none |

**Performance / comfort**
- Low graphics (`S.gfx==="lo"`) and LITE devices: fewer sparks (4 / 10), rays (6) and stars (3).
- More than 420 live effects: new hit effects are skipped.
- `prefers-reduced-motion`: no screen shake and no hit-stop (the pixel effects still play).

**Floating text:** unchanged from §14 and still drawn on top.

**Code touched:** `applyHit` (calls `hitFx`), `drawFx` (new `hfx` branch), `update` (hit-stop and shake timers at the top), `render` (shake offset in the world transform; clicks are not affected because `ox/oy` are not modified).

---

## 16. HUD changes in v19.1

**1. Idle button inside the hotbar panel (landscape and portrait)**
- The hotbar and the Idle button now share **one panel** (`#botC` carries the panel background; `#hotbar` itself has no background any more). A thin divider line separates the slots from Idle.
- Landscape: one row, slots 1–0, divider, Idle. Idle is vertically centred, level with the slots.
- Portrait: the hotbar stays 5 × 2; Idle sits in a 6th column on the **bottom row, next to slot 0**. The cell above Idle is empty.
- Portrait: the whole panel is now **centred** on the screen (before: pinned 12 px from the right edge).
- The gear badge moved slightly in (`top/right: -7px`). The Claim button still appears above the panel, right-aligned.

**2. Idling motion**
- While idling, the icon is **four arrows chasing each other round a circle** (after the user's reference image), spinning once every 1.6 s. The old spinning ring and the stop square are removed.
- Colour: navy → royal blue → sky blue gradient (`#1c2a8c → #3f5fd8 → #8fb4ff`), matching the navy gear badge, on the gold button. Icon 26 px.
- The button's glow pulses between green and blue while idling.
- `prefers-reduced-motion`: the arrows turn slower (4 s) and the glow does not pulse.

**3. Monster panel, portrait**
- Centred on the screen (`left: 50%`), so it lines up with the centred hotbar panel. `bottom: 188px` (about 9 px above the panel). Width unchanged: screen width − 140 px, max 260 px.
- Landscape is unchanged (top centre, 72 px).

**4. System / GM announcement, portrait**
- Moved from the top to the **lower part of the screen, above the monster panel** (`bottom: 250px`), so it no longer covers the character card, minimap and status islands.
- Full width (8 px from each side) with 16 px corners, so long text wraps to 2–3 lines instead of squeezing into a tall oval. It slides up 16 px as it appears.
- The top-centre banner no longer shifts down in portrait when an announcement shows.
- Landscape is unchanged (top centre).

**Code touched:** one CSS block at the end of the stylesheet (`v19.1 HUD`) and `renderIdle()` (new `ib-cyc` icon).

---

## 17. Light windows: Character, Status, Inventory (v19.2, after the user's reference image)

These three windows, and the **Item Detail** window that opens from them, now use a **light frame**. ~~Every other window keeps the navy look of §9.~~ **v19.6:** every window uses this frame, with a Dim version, see §21.

**Frame (all four windows)**
- Light grey body `#e6e5e2`, white 1 px edge, soft shadow, 16 px corners.
- **Blue title bar** `#0a6fc2` with a white icon and a bold 25 px title, centred: Character (person), Status (pillared building), Inventory (backpack). Item Detail has no icon.
- Close button: **white circle with a blue ×** on the right of the title bar.
- Sections are split by a **double grey line** (`.lt-hr`).
- Colour jobs: **blue** = active / information pills, **white** = idle buttons and empty cells, **grey** = info rows, **green** = gains and "Expand Slots", **red** = Reset Status and Sell.
- Code: the window gets the class `lt` when it shows `char`, `status`, `inv` or `itemdet` (`LIGHT_W` in `drawSlot`); the styles are one CSS block at the end of the stylesheet (`v19.2 light windows`).

**Character (420 px wide, height follows the content)**
- Tabs **Basic Equipment** (selected: darker grey with an inset edge) and **Costume Equipment** (white). Thai: อุปกรณ์พื้นฐาน / อุปกรณ์คอสตูม.
- Blue name bar: `Arin ✦ [archetype icon] Ranger ✦ C1 ✦ LV99 ✦ Job50`.
- 10 slots in two columns of five (78 px, white, rounded) around the character, same order as before: left **Top Headgear, Lower Headgear, Weapon, Garment, Ring**; right **Mid Headgear, Armor, Shield, Shoes, Bracelet**. An empty slot shows a **grey line icon** for its slot (crown, mask, dagger, jacket, ring / glasses, shirt, shield, shoe, beads). A worn piece shows its art on white with a rarity-coloured frame, `Lv` tag, refine and stars. Tap a slot → Item Detail (unchanged).
- The character stands on a soft blue platform (no navy disc). The round Style button is gone (the Costume tab does the same).
- **Combat Point box** under the character: blue header `COMBAT POINT (CP)`, big dark number on white.
- Two grey rows at the bottom: **NO TITLE** and **NO GUILD**, each with a blue **SOON** pill (tapping shows a "coming soon" toast).
- **Removed:** the face portrait in the name bar and the wallet row (Scandium, Yttrium, Lanthanum). Scandium is still on the player card; Yttrium and Lanthanum are in the Shop.

**Status (440 px wide)**
- **ID card:** the character's head and shoulders (drawn live) on the left; on the right blue pills for **Name**, **Level | Job** (`99 | 50`), **Archetype** (icon + name), **Class** (`No Class`), **Job** (`No Job`). At C0 the Archetype pill is grey `No Archetype`; once Job Lv 10 is reached it becomes a gold **Archetype Trial** button (same action as the old trial button).
- **Basic Status card** (white, blue header): Str, Agi, Vit (left) and Int, Dex, Luk (right). Each row: icon and name, then a grey bar with the value (`base` and a small green `+bonus` from gear and Blessing), a **1 ▶** button (+1), a **10 ▶** button (up to +10, as far as the free points allow) and the **points needed for the next +1**. At 99 the cost shows `—`.
- Card footer: red **Reset Status**, a small **Auto** toggle (auto-assign, blue when on; kept because it was already a feature), and on the right **Status Point Left** in a green pill.
- **Details table**, two striped columns:

| Left | Right |
|---|---|
| Attack | Magic Attack |
| Defence (`hard% +soft`) | Magic Defence |
| Health Point | Stamina Point (SP) |
| Attack Speed (`ASPD (x.xx sec)`) | Global Delay |
| Flee | Perfect Dodge |
| Hit | Perfect Hit |
| Critical Rate | Critical Damage (`+40%`, the crit multiplier ×1.4) |
| Overload Rate | Overload Damage (`+30%`, the Overload multiplier ×1.3) |
| Variable Casting (`−(1 − vctMul)%`: `√((DEX×2+INT)/530)` and gear) | Fixed Casting (`−%` from gear) |
| Ignore DEF | Ignore Magic DEF |

- **Placeholders:** Perfect Hit, Ignore DEF and Ignore Magic DEF have **no system yet** (nothing raises them), so they show `0%`; hovering says so. **Fixed Casting** and **Global Delay** show the gear reduction (`−x%`); no item gives it yet, so they read `0%` with the same hover note (v20.9). **Overload Rate** shows the base chance (= CRIT); each magic skill multiplies it by its own Overload rate (`COMBAT-FORMULAS.md` 3b).
- **Removed from Status:** kills / deaths record, the EXP bars (the player card has them), weapon and armor type rows.

**Inventory (440 px wide)**
- Five tabs: **Usable · Equipments · Other · Quest · Cash** (selected tab blue). Rules in `ITEMS.md` (Inventory v19.2).
- **Blue well** with a **5 × 6 grid** of white cells (30 per page). Items show their art, count, refine and stars; the frame takes the rarity colour.
- Footer row 1: green **Expand Slots** (opens the Cash Shop tab) and `Slots x/y` on the left; `◀ Page x/y ▶` with solid triangles on the right.
- Footer row 2: **Sort** (`Sort by Name / Rarity / Price`) on the left; the hint "Hold & select items for bulk sell." and a red **Sell** button on the right.
- **Hold an item 0.45 s** to start selecting (ticked in green, the well darkens a little); then tap to add or remove. While selecting, the hint changes to `n selected · total Sc` with a **Cancel** button. A finger that moves more than 10 px cancels the hold, and the click that follows a hold is ignored. On phones the hint text is hidden to save room.

**Item Detail:** same content and buttons as before, on the light frame: white header card with the item art and name in its rarity colour, white stat and comparison cards, blue main button, red-tinted Discard.

**Phones:** the windows fill the width as before; Character slots 64 px; Status portrait 118 px and the six stats in one column; the Inventory hint is hidden.

**Tested:** desktop 1440 × 860 and phone 390 × 844, English and Thai, Beginner and Ranger Lv 99 with gear, hold-select + Sell (3 pieces sold for the right total), Sell with nothing selected, +1 / +10 stat buttons, item detail beside Character, and the whole game inside a sandboxed iframe (no errors).

---

## 18. Item cells in the light windows (v19.3)

Applies to the **Character** equipment slots and the **Inventory** cells (both use the same rules now).

- **Art fills the cell:** the item art is centred and stretched to the cell, with a 5% margin on the left, right and top and 13% at the bottom (room for the stars). Before, the art was a fixed 42 px (Character) or 70% (Inventory) and in Inventory it sat towards the top-left.
- **Stars (rarity) bottom-centre** in both windows: 11 px (9.5 px on phones), drawn above the art. Before, Character had them at the bottom-left.
- `Lv` tag stays top-left, refine `+N` top-right, stack count bottom-right; all drawn above the art. **(v19.7: Lv and refine are now corner islands, see §22.)**
- **Phones:** the five Inventory tabs use 10.5 px text and less padding so "Equipments" is no longer cut to "Equipme…" (checked at 360 px width).
- Code: one small CSS block inside the `v19.2 light windows` block, marked `v19.3`. No JavaScript changed.

---

## 19. Item Info window (v19.4, replaces Item Detail; after the user's reference image)

The **Item Detail** window is renamed **Item Info** (Thai: ข้อมูลไอเท็ม) and redrawn. It opens from the Inventory (tap an item) and from the Character window (tap a worn piece).

**Size:** fixed **360 × 550 px**, never scrolls (`overflow: hidden`). On phones the width shrinks to the screen (minus 16 px) and the height stays 550 px. Tested with a Legendary +7 weapon in compare mode (the longest case): the content fits with no overflow.

**Title bar:** note-and-pencil icon + "Item Info", white close button (same light frame as §17).

**Layout**
- **Left column (72 px):** the item icon in a white rounded box. Equipment also gets a **LOCK** button under it (green; when locked it turns amber and reads **LOCKED**; tap again to unlock).
- **Right: white info card**, top to bottom:
  1. **Name**, bold, in the rarity colour (consumables blue, other items dark). Refine shows as `+N` after the name (v19.7: a small blue pill, see §22).
  2. **Tags:** equipment: stars + rarity pill (e.g. `LEGENDARY`, rarity colour) + slot pill (e.g. `WEAPON`, teal). Consumable: blue `USABLE` pill + "Double-click to use it." (phones: "Double-tap to use it."). Other items: dark pill `OTHER` / `QUEST` / `CASH`.
  3. **REQ** (equipment; Thai **เงื่อนไข**; was "Requirement" before v19.5): dark pills `LV50`, `FIGHTER`, `STR31`. A requirement you do not meet turns its pill red.
  4. Double line, then **description** (items) or the **stat table** (equipment): name on the left, value right-aligned in the middle. Abilities (Crit damage, Lifesteal, …) are in violet.
  5. Double line, then the **set**: the set name in a rarity-coloured pill on its own line, then **one line for the 3-piece bonus** `(3) …` and **one line for the 6-piece bonus** `(6) …` (v19.5; before, all on one line as `(3) … | (6) …`). A line too long for the card ends with "…" and shows in full on hover.
  6. Double line, then the **price** in a gold pill at the bottom right, e.g. `10,296 Scandium`. For stacks it is price × the chosen quantity.
- **Action row under the card:**
  - Consumables and other items: `−  1  +  MAX` and a light-pink **Sell** button.
  - Equipment in the bag: **Compare OFF** (blue) / **Compare ON** (green) on the left, **Sell** on the right.
  - A worn piece (opened from Character): **Unequip** on the left, blue **Refine (ore count)** on the right.

**Compare ON** (equipment in the bag): the table shows "Compared with equipped" (red, italic) and the worn piece's name (tan, italic), then for every stat either piece has: `old→new` in grey and the difference in green (gain) or red (loss), `-` when unchanged, `—` when a piece lacks that stat. (v19.6 accidentally turned the green/red into plain text colour; fixed in v19.7, see §22.) With nothing worn in that slot: "Nothing equipped in this slot" and every stat counts as new. The ON/OFF choice is kept while the game is open.

**Double-click / double-tap** (new): on an Inventory cell or on the Item Info icon. A consumable is **used**, an equipment piece is **equipped** (if the requirements fail you get the usual "cannot equip" toast). The two clicks must be within 0.38 s and within 8 px. Since v19.5 the windows no longer move when Item Info opens (§20); the safety check that counts a second click landing on something else is kept.

**Lock** (new, equipment only): a locked piece cannot be sold (Sell is greyed out, with a tooltip), cannot be picked for bulk sell (a toast says it is locked), and bulk sell skips it if it was picked before. The Inventory cell shows a small amber lock badge in the top-left corner. The lock is stored on the piece (`lock:true`) and stays with it when it is equipped or taken off.

**Removed from this window** (not in the reference): the **Use** and **Equip** buttons (now double-click), **Refine for pieces in the bag** (refine a piece after equipping it, from the Character window), **Discard** (Sell replaces it), and the requirement ✓/✗ list (now the pills).

**Code:** `invDetail()` rewritten; new `infRows()`, `invDouble()`, `invToggleLock()`, `detCmp`; click handlers `invsel` (double-click), `infdbl`, `invlock`, `detcmp`; a check at the top of `winClick` for the second click of a double-click; `lock` carried through `invEntries`, `invFind`, `detEntry`, `equipUid`; `invSell` and `invSellMulti` skip locked pieces. CSS block `v19.4 Item Info`.

**Tested** (desktop 1440 × 860): consumable, material, Legendary +7 weapon with Compare OFF and ON, locked weapon (Sell disabled, lock badge on the cell), worn piece from Character (Unequip / Refine), double-click to use a Red Potion (3 → 2) and to equip a weapon, window always 360 × 550 with no overflow, no script errors.

---

## 20. Item Info no longer pushes the windows (v19.5)

**Problem:** the open windows sit in one centred row. Opening Item Info added a window to that row, so every other window slid sideways, and the second click of a double-click landed on a different item.

**Fix (desktop and tablet landscape):** Item Info is taken out of the row (`position: absolute`) and placed **beside** the open windows, so the others stay exactly where they were (checked: Inventory left edge 500 px before and after, item cell moved 0 px).
- Placement order: **right** of the open windows (12 px gap) → if that does not fit, **left** of them → if neither fits (narrow screens, e.g. 1100 px wide), over the right edge of the screen, 8 px in.
- Vertically centred in the play area. It is placed again when the screen is resized.
- **Phones (portrait):** unchanged, Item Info still opens as a centred pop-up over the windows.
- Code: new `placeDet()`, called at the end of `renderWin()` and on `resize`.

**Also in v19.5 (see §19):** the set name has its own line, followed by one line for the (3) bonus and one for the (6) bonus; the "Requirement" label is now **REQ** (Thai **เงื่อนไข**).

**Tested:** 1440 × 860, 1920 × 1000 and 1100 × 760: the Inventory does not move when Item Info opens; double-click at normal speed equips the piece; Item Info stays 360 × 550 with no overflow; no script errors.

---

## 21. One window theme, Light and Dim (v19.6)

**Every window** now uses the frame and pieces of §17: Character, Status, Inventory, Item Info, Skills, Quests, Party, Guild, Shop, Settings, World Map, Map Info, Idle Summary, Idle Settings, Idle reward and Choose your Archetype. The old navy window look is gone.

**Follows Settings > Graphic > UI Display Mode**, like the main-screen panels:

| Mode | Windows |
|---|---|
| **Light** | light grey frame `#e6e5e2`, white cards and cells, dark text `#1d2433` |
| **Dim** | dark grey frame `#24272e`, cards and cells `#2f333c`, light text `#e9ebf1`, lines `#474d59` |
| **System** | Light or Dim from the device's own light/dark setting |

What stays the same in both: the blue title bars and accent (`#0a6fc2`, slightly brighter `#1d7fd8` in Dim), green / red / gold buttons and pills, rarity colours, item art, and the World Map chart (a dark star chart in both modes). The Inventory well is a deeper blue in Dim (`#17518d`). The setting's description now says it changes "the panels on the main screen and the menu windows" (Thai: "เปลี่ยนทั้งแผงบนหน้าจอหลักและหน้าต่างเมนู").

**Shared pieces** (same look in every window):
- **Section bars** (e.g. "Active skills", "In progress"): solid blue bar with white text; sub-sections (e.g. a map group in Quests) a darker blue.
- **Rows and setting rows**: card colour, 1 px line, 10 px corners.
- **Tabs and segmented choices** (Shop, Settings, Map Info): white (Dim: card colour) with a line; the selected one blue. Same as the Inventory tabs.
- **Buttons**: neutral = card colour with a line; main = blue; danger = light red with red text.
- **Switches**: grey when off, green when on. **Drop-down lists**: card colour with a line.
- **"Soon" notes and badges** (Idle Settings): soft yellow box with dark gold text (Dim: dark gold box with light gold text).
- **Stat tiles and item tiles** (Idle Summary, Idle reward): card colour with a line.

**How it works (code):** all window colours are CSS variables `--w-*` set on `.win.lt` (the Light values), with the Dim values under `:root[data-theme="dark"] .win.lt` and, for System on a dark device, under `@media (prefers-color-scheme: dark)`. The `lt` class is now on every window (`LIGHT_W` matches all ids). The CSS of §17–§20 was changed to use these variables instead of fixed colours, and a few colours written by JavaScript in Item Info (item name, common rarity, category and REQ pills) use them too. New CSS block: `v19.6 window theme`.

**Not changed:** the HUD itself (player card, minimap, status islands, hotbar, 3 × 3 menu buttons) already followed System / Light / Dim and keeps its own look.

**Tested:** all 16 windows in Light and in Dim at 1440 × 860 (Idle reward only in its empty state, as there were no offline rewards to show); System mode on a device set to dark (Map Info and World Map); Idle Summary with sample data; phone 390 × 844 switching to Dim with the real Settings button (Settings, Inventory, Quests); the whole game inside a sandboxed iframe. No script errors.

---

## 22. Compare colours and refine islands (v19.7)

**1. Compare: better in green, worse in red (bug fix).** In Item Info with **Compare ON**, the difference column shows **green** when the new piece is better (`+…`) and **red** when it is worse (`−…`). The colours had stopped showing in v19.6: a general rule that set the text colour of every bold word in a window (`.win.lt .win-b b`) overrode them. That rule now sets the colour of the window body only, and bold text inherits it, so coloured text keeps its own colour again. The same fix brings back the white text in the green **Status Point Left** pill.
- Light mode: green `#1c9a52`, red `#d23a4a`. Dim mode: brighter green `#6fe0a0`, red `#ff8d9b`, so they read well on the dark card.
- The label column stays in the normal text colour and `old→new` stays grey, as in the user's mock.

**2. Refine level as a blue island** (after the user's mock), on the **Character** slots and **Inventory** cells:
- `+N` sits in a **blue island in the top-right corner** (blue gradient, white bold 13 px text, rounded bottom-left corner, small shadow), flush with the cell edge.
- `Lv N` (Character slots) is the matching **dark island in the top-left corner**.
- Phones: 11 px (Lv 9.5 px).
- **Item Info:** the `+N` after the item name is a small blue pill too.
- Same in Light and Dim.

**Code:** CSS only. The body text rule in the `v19.6 window theme` block, the compare diff colours (now `var(--w-good)` / `var(--w-bad)`), and a `v19.7` CSS block for the islands and the name pill.

**Tested** (Light and Dim, 1440 × 860): computed colours of the compare differences (green for gains, red for losses, in both modes); refine islands on Inventory cells (+2 to +10) and on worn pieces in Character (+10, +3); Status Point Left pill text white again; Skills, Quests, Shop, Settings, Idle Settings and Choose your Archetype checked unchanged; no script errors.

## 23. Right-click menu, Social window, sitting and whispers (v20.1)

The browser menu ("Save image as…") never opens on the game. Right-click (phones: long-press about 0.55 s) on a character opens the game menu; right-click anywhere else does nothing. The menu closes on any other click, Escape, the mouse wheel or a map change.

| Target | Menu items |
|---|---|
| Another player | Add friend (Remove friend if already a friend) · Whisper · Invite to party (only for a party leader; hidden for your own members) · Invite to guild (only with invite rights: guild master or officer; hidden without a guild) · Trade (*Soon*, disabled) |
| Yourself | Sit and rest / Stand up · Set status / Clear status · Create a party (only when you have no party) · Open a stall (*Soon*, disabled) |
| NPC | Talk (desktop right-click only; on phones a tap already talks) |

**Sit and rest.** HP and SP recover 3× faster (`SIT_REGEN`). You can sit anywhere except within 3 tiles of an NPC (`SIT_NPC_GAP`), while Idle is on, or while casting. You stand up by yourself when a monster hits you, when you walk, attack, cast, use quest auto-walk, start Idle, die or change map. The chibi sits cross-legged.

**Status.** Only while sitting and only in town. A bar asks for up to 20 letters (`STATUS_MAX`; a Thai consonant with its vowel and tone marks counts as one letter). The status shows above your head in a mint plate shaped like the NPC plate. Standing up or leaving town clears it.

**Friends.** Social → Friends lists up to 50 friends (`FRIEND_MAX`, saved in `S.friends`) with online state, Whisper and Remove (click twice to confirm). Until the server exists, the other player accepts a request after 1–3 s.

**Whisper.** A small draggable 1:1 window (`#wsp`). Messages also go to the chat log (All tab, pink `[Whisper]`). Until the server exists, the other player answers with a short canned reply.

### Party and guild (v20.2, party rewards v20.3)

**Party** (`S.party = {name, lead, members:[{name, lv}], share:{exp, items}, rr}`, saved). Right-click yourself → *Create a party* opens Social → Party, where you type a name (2–10 characters; empty uses "Party" / "ปาร์ตี้", `PT_NAME_MAX` = 10) and press Create or Enter. The window shows the title as "{character} ({party name})". The leader can rename the party (*Rename* → input → Save or Enter, same 2–10 rule). A party holds up to 6 people including you (`PARTY_MAX`). The leader can invite: if the other player is already in a party, or the party is full, or the invite would make the level gap above `PT_LV_GAP` (20), the toast says so; otherwise the player joins after 1–3 s (simulated). The Party tab lists the leader (crown) and members with *Remove* (click twice), and *Disband* / *Leave* (click twice). Under the members, two segmented controls set the sharing: **EXP sharing** (Off · own EXP / Split equally) and **Item & Scandium sharing** (Off · top damage gets it / On · rotate); members see them read-only. Party members' name tags use the party colour, and joins and leaves are posted in the Party chat tab. Rules and numbers: `ECONOMY.md` §4.

**Guild** (`S.guild = {name, rank: "master" | "officer" | "member", members, canInvite?}`, saved). Guild creation is not built yet, so a new character has no guild and the invite item never shows. *Invite to guild* appears only for a guild master or officer (or `canInvite`). Players already in a guild get a warning toast. The Guild tab shows "No guild yet · Soon" when you have none; the Character window shows the guild name instead of "NO GUILD".

**Basic Skill locks (v20.4).** Menu items whose Basic Skill level is not reached are disabled with a "Requires Basic Skill Lv N" hint: Sit (Lv 2), Set status (Lv 2), Add friend (Lv 6), Create a party (Lv 7), Trade / Open a stall (Lv 8). In Social, a locked Friends / Party / Guild tab shows one locked row with its requirement (`JOBS.md` §1b).

Simulated players: about a quarter already have a party and a third already have a guild (`hasParty` / `hasGuild`).

## 24. Basic Skill and Pocket Dimension windows (v20.4)

**Skills window.** *Replaced in v20.10 by the Skills Tree (§26).* The Basic Skill levels and what each teaches now show in the Basic Skill tile and its detail box.

**Pocket Dimension window** (`storage`, 640 × 380, icon: cube). Hint line, two tabs (Bag · Dimension), a 10 × 3 grid in the light-window cell style, then both capacities ("Bag slots 12/100 · Dimension slots 4/300") and the page arrows. Click a cell to move it to the other side. Rules: `ITEMS.md` §7.

## 25. Drag and drop on the hotkey bar (v20.5)

**Drag sources.** Mouse: the drag starts once the pointer has moved 6 px. Touch: a bag cell or a worn piece starts when the finger moves; a Skills Tree tile starts after a 230 ms hold, so the window still scrolls.
- **Bag cells** (every tab: Usable, Gear, Other, Quest, Cash): every item can be picked up. Pocket Dimension (storage) cells cannot.
- **Skills Tree (§26):** every tile except Basic Skill, active or passive. The level arrows and the drop-downs are not drag handles.
- **Character window:** a worn piece can be picked up.
- **Hotkey slots:** a filled slot can be dragged.

**Drop zones.** A drop zone is an element with `data-drop`. Today the hotkey bar is the only one (all 10 slots). A future trade or sell window adds its own entry to `DROP_ZONES`.

**What the hotkey bar accepts**

| Dragged | Result |
|---|---|
| Usable item from the bag | Goes on the slot. The bag count does not change. |
| Active skill of this archetype (or a Basic Skill active) | Goes on the slot at the level picked with the tile’s ◀ ▶ arrows (v20.10); with no pick, at the highest learned level. |
| Another hotkey slot | Moves there. If the target has something, the two swap. |
| Gear, materials, quest or cash items, worn pieces | Refused. Notice: "This item can't be placed here." (ไอเท็มนี้ไม่สามารถวางที่นี่ได้) |
| Passive skill | Refused. Notice: "Passive skills can't go on the hotkey bar." (สกิลแบบ Passive ใส่บนแถบ hotkey ไม่ได้) |

While a drag is over the bar, the slot under the pointer shows a **gold** ring when it accepts the drag and a **red** ring when it refuses it.

**Dropped outside any zone**
- From the bag, the Skills window or a worn slot: **nothing happens.** The item or skill is not discarded, moved or changed.
- From a hotkey slot: **only that slot is cleared.** The item or skill stays in the bag or in the Skills window.

**Clicks.** A plain click or tap works as before (use the slot, open the bag cell). The click that ends a real drag does nothing.

**Free slots.** A slot is not tied to one skill or item. The same item can sit on more than one slot. On a class change, skills that the new archetype does not have are removed from the bar, the empty skill slots are filled with the new skills (the four archetype skills first, then First Aid and Heavy Strike), and items stay where they are.

**Hotkey setup.** Removed in v20.10: slots are filled only by drag and drop. The level comes from the Skills Tree arrows (§26).

## 26. Skills Tree window (v20.10)

Replaces the old Skills list (§24). Window `skill`, title **Skills Tree / ผังสกิล / スキルツリー** with a sparkle icon, **440 px wide, height fits the content** (the same frame as Status and Bag).

**One tab: the character's current class line.** A Beginner sees only the C0 **Beginner** tab. After the Archetype choice the Beginner tab is gone and only the C1 archetype tab shows, because the archetype tree already holds the Beginner skills in column 1. C2 and C3 get their tabs when those classes exist. Each line has one colour (`ARC_COL` / `SKG` in the code), used for its tab, tiles, level pills and the skill icons everywhere (hotkey bar, drag ghost):

| Line | Colour |
|---|---|
| C0 Beginner | blue `#0a6fc2` |
| Fighter | red `#d23b34` |
| Ranger | green `#2e9447` |
| Spellcaster | purple `#7440c8` |
| Supporter | yellow `#d69a0c` |

**Grid.** 5 columns × 5 rows (more rows if a line ever needs them); empty cells are dashed. **Column 1** holds the Beginner skills top to bottom: Basic Skill, First Aid, Heavy Strike. **Columns 2–5** hold the archetype, one row at a time (`skGrid`, `SKT_ROWS`): by default the passives on row 1 and the actives on row 2 (a row longer than 4 wraps). Spellcaster: row 1 Mana Flow, Elemental Attunement, Overload Energy; row 2 Fire Bolt, Frost Nova, Lightning Spear, Stone Spike. The Beginner tab has only column 1. Each cell: name on top (cut with … when long), the 56 px tile, then a pill under it.

| Tile | Look |
|---|---|
| Active, learned | archetype-colour fill, white line, white icon |
| Passive (and Basic Skill), learned | white fill, archetype-colour line and icon; outlined pill |
| Not learned | grey (active: grey fill; passive: pale grey) and a grey name |
| Selected | gold ring |
| Draft (planned, not yet learned) | in colour again, with a gold **+N** badge (levels planned) |

The pill shows the learned level. These tiles always show **◀ level ▶** instead: a learned active with levels (Fire Bolt, Overload Energy), and a learned skill that can still be raised (Basic Skill as a Beginner, a passive below its max). Any tile also shows them while it is selected or has a draft. (They must not depend on the selection alone: on a phone, closing Skill Info clears it.) ▶ is greyed only at the max level; with no points left it stays tappable and says "Not enough skill points." First Aid and Heavy Strike before they unlock show "Basic Lv 3" / "Basic Lv 4".

**Learning (draft, then Learn).** Tap a grey skill: it turns to colour as a **Lv 1 draft** and the pill becomes **◀ level ▶**. ▶ plans one more level (1 skill point each), ◀ takes one back (◀ at Lv 1 of a skill that is not learned drops the draft). Several skills can be planned at once. Nothing is spent until **Learn**; **Reset** drops every draft. Both are disabled when there is no draft. ▶ stops at the max level and when the drafts already use every point left ("Not enough skill points."). Basic Skill is planned the same way, but only as a Beginner; First Aid and Heavy Strike have no draft (they come from Basic Skill Lv 3 / 4; tapping them says so). Learning Basic Skill levels shows what each new level teaches and can start the Archetype Trial (`JOBS.md` §1b).

**Level for the hotkey bar.** On a learned skill with levels (Fire Bolt, Overload Energy), ◀ ▶ below the learned level pick the level a drag puts on the hotkey bar (`data-dnd="s:id:lv"`; the slot keeps that level, `SKILL-SPEC.md` §5). Example: Fire Bolt learned at Lv 5, ◀ ◀ shows 3, drag → the slot casts Lv 3.

**Skill Info window** (`skinfo`, title Skill Info / ข้อมูลสกิล / スキル情報, note icon). A left click on a tile opens it in the Item Info slot, with the Item Info size and placement (beside the tree; on a phone it floats in the middle over a dimmed screen). Escape or × closes it; switching tabs (when a line has more than one) closes it too. Content, in a white card:
- the 76 px tile and "**Name Lv.learned/max**" in the line colour; chips: archetype, then Passive, or the targeting (**Self Cast** / **Target Cast**) and the kind (Physical, Magic · element, Heal, Buff, Zone, Movement);
- the description;
- **Level 1 … Level max**: what each level gives (Fire Bolt: fireballs, total % MATK, SP; Overload Energy: Overload Rate, duration, SP; Mana Flow / Elemental Attunement: the passive effect; Basic Skill: what the level teaches; a one-level active: SP and range). The learned level is bold, higher levels are faded. One-level passives have no level list;
- **In details** (actives only): a table Lv | VCT (Variable Cast, before DEX/INT and gear) | FCT (Fixed Cast; 0 shows as –) | CD | Delay (Global Delay), base values from the skill data (`vct`, `fct`, `cd`, `gd`, `COMBAT-FORMULAS.md` §2b), the learned row tinted. No line under the header row. This replaces the old Skills list line "Cast x s (VCT a + FCT b)" from v20.9.
SP shown is the real cost (after Mana Flow).

**Footer.** "Skill Points : N" = the points **not spent yet**; while there is a draft it already counts the draft (it drops as levels are planned) and the box gets a gold ring. Then **Learn** (blue) and **Reset** (grey). The footer never grows wider than the window (no horizontal scroll). The old Hotbar setup drop-downs are gone (§25).

**Skill icons (v20.10).** Every skill has its own duotone icon (`SKI`, 32 × 32 grid, lines in `currentColor`, class `a` = soft fill). Tiles colour them (white on actives, line colour on passives); the hotkey bar and drag ghost show them white on the line gradient. The element no longer changes the icon colour.

| Line | Skill | Icon |
|---|---|---|
| Beginner | Basic Skill | sprout |
| | First Aid | cross in a rounded square |
| | Heavy Strike | sword with impact marks |
| Fighter | Power Strike | burst star |
| | Whirlwind Cleave | spinning arc |
| | Crushing Blow | hammer with cracks |
| | War Cry | horn with sound waves |
| | Weapon Mastery (passive) | crossed swords |
| | Iron Body (passive) | cross shield |
| Ranger | Double Strafe | two arrows |
| | Arrow Shower | arrows falling on a ring |
| | Piercing Shot | arrow through a target |
| | Evasive Leap | wing |
| | Eagle Eye (passive) | eye |
| | Steady Aim (passive) | crosshair |
| Spellcaster | Fire Bolt | falling fireball with trails |
| | Frost Nova | snowflake |
| | Lightning Spear | lightning bolt |
| | Stone Spike | rock spikes |
| | Overload Energy | four-point sparkle |
| | Mana Flow (passive) | drop with waves |
| | Elemental Attunement (passive) | ring with four element points |
| Supporter | Heal | heart with plus |
| | Holy Light | sun |
| | Blessing | star under a halo |
| | Sanctuary | pillars on a glowing circle |
| | Divine Grace (passive) | feather |
| | Guardian Aura (passive) | shield in an aura |

These are placeholders drawn in code; a later art pass can replace any entry of `SKI` without touching the rest.

## 27. Hero sprite for the main character (v20.11, female set v20.12, female poses v20.13, male poses v20.14, death v20.15, test)

The player is drawn from sprite sheets instead of the canvas chibi. Two sets: **male** and **female**.

- **Files:** `images/hero/male/idle.webp` (1 frame per direction) and `walk.webp` (4 frames per direction), about 460 KB together; `images/hero/female/idle.webp` (3 frames, 3 fps) and `walk.webp` (3 frames), about 620 KB together. They are made from the 256 px PNG sheets and saved as WebP to cut the size. A set loads the first time it is drawn (`heroLoad`). The female `run` sheet is not used (the game has one walking speed). Five female idle frames (NE ×2, N ×1, NW ×2) still have a hair tip or headphone slightly cut at the frame edge; it is barely visible in game. Rows are 8 directions in the order S, SE, E, NE, N, NW, W, SW; columns are frames. Each frame is 256 × 256 with the feet at (128, 236).
- **Size:** drawn at 0.34 of the sheet (`HERO.male.sc`), so the hero is about as tall as the old chibi (~71 px at zoom 1).
- **Facing:** 8 directions, taken from the on-screen direction of movement or of the target (`face8`, stored as `c.f8`). It falls back to the old 4-way `dir` / `back` when there is no `f8` yet.
- **Female poses (v20.13):** `sit.webp`, `attack.webp`, `cast.webp`, one frame per direction, same layout (8 rows, 256 px, feet at (128, 236)). Cut from five 4 × 2 pose sheets (back row N, NE, E, SE / front row S, SW, W, NW; the sit sheet runs S, SE, E, NE / N, NW, W, SW). Background noise under alpha 9 removed; pieces were split by connected parts, so the knife and the magic circles stay with their own figure. Scale 0.502 (the standing sheet's height matched to the old idle, 209 px); the sit sheet is drawn 0.8 of that so its head matches the standing head. The standing and run sheets were cut too but are not used (the 3-frame idle and the walk stay).
- **Male poses (v20.14):** `images/hero/male/sit.webp`, `attack.webp`, `cast.webp`, same layout. All five male pose sheets (stand, run, sit, attack, cast) use the N, NE, E, SE / S, SW, W, NW grid, the sit sheet included. Scale 0.510 (standing sheet matched to the old male idle, 209 px); the sit sheet is drawn 0.9 of that. Stand and run cut but not used.
- **Death (v20.15):** `death.webp` for both sets, in a 320 px frame (lying bodies are wide) with the feet at (160, 296); an anim can set its own `fw` / `ax` / `ay`. Male: 8 frames at 10 fps, stored at 3/4 size (240 px frames, `res: .75`, drawn back at full size) because the source was drawn small and scaled up about 2×; the source has 6 directions (N, NE, E, SE, S, W), so SW and NW are the SE and NE rows mirrored. Female: 3 frames at 5 fps; the source sheet's direction labels were wrong (its "N" column faces the camera), so columns were matched by what they show (S, SE, E, NE, N, NW, W, SW). The fall starts at `player.dieAt` (set in `die()`), plays once and holds the last frame until respawn. With a death sheet loaded the old tipped-over rotation is skipped (`heroDeath()`).
- **Pose order (`drawHero`):** dead → death; casting (`player.casting`) → cast; walking → walk; a short pose flash `player.pose` for `player.poseT` s → attack or cast; sitting → sit; else idle. Basic attack sets the flash for 0.32 s (`attack` for physical, `cast` for magic); a finished skill sets it for 0.36 s (`attack` for physical skills, `cast` for the rest) and turns the hero toward the target. A set without a pose sheet falls back to idle, and sitting without a sit sheet uses the pressed-down idle frame.
- **Animation:** walking steps through the walk frames with the walk phase (one cycle = 2π; male 4 frames, about 7 fps; female 3 frames). Standing plays the idle frames at their fps (female); a one-frame idle (male) gets a small breathing bob instead. **Sitting** reuses the idle frame pressed down a little (no sit art yet). **Dead** keeps the old tipped-over rotation.
- **Portraits:** the player card avatar (first idle frame, still), the Character window doll and the Status portrait use the front (S) direction of the chosen set.
- **Fallback:** while the sheets load, or if they fail, the old chibi is drawn. Other players and NPCs still use the chibi.
- **Settings > Graphic > Character look:** Male (default), Female or Classic (the old chibi). Saved as `S.look` (`"male"`, `"female"`, `"classic"`; a v20.11 save with `"new"` reads as Male). For testing only; a real gender choice belongs in character creation later.
- Missing art for later: true SW and NW death rows for the male set.

