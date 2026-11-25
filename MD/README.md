# REO (Rare Earth Online): Docs Index

> Synced with `index.html` v21b. Read `REO-INSTRUCTIONS.md` first; it is the rulebook.

## Core
| File | What it covers |
|---|---|
| REO-INSTRUCTIONS.md | Vision, non-negotiable rules, art direction, UI spec, roadmap |
| STATUS.md | Effect icons and the status islands (FPS, ping, online, clock) |
| CORE-LOOP.md | Progression loop, level caps, equipment and CP |
| COMBAT-FORMULAS.md | Stats, damage, elements, monster → player, CP |
| ECONOMY.md | Scandium, Yttrium, Lanthanum |

## World
| File | What it covers |
|---|---|
| GADOLINIUM.md | Starting town: map, NPCs, starter quest |
| TOWN-ALIEN.md | Town look and NPC placement rules |
| FIELD-01.md | Field 01 (CP 150): monsters, portals, save |
| FIELD-02.md | Field 02 (CP 450): monsters, Elites for every field |
| FIELD-03.md | Field 03 (CP 900): monsters and the Gadolith boss |
| FIELD-GEOSYNCLINE.md | Path to the Geosyncline (town west gate, Lv 25+ / CP 2,000+): aggressive Earth and Water monsters, skills, drops |
| FIELD-RUINS.md | Road to the Ruins (town south gate, Lv 30+ / CP 3,000+): aggressive Fire monsters, skills, drops |
| WORLD-MAP.md | World Map, teleport, Map Info, announcements |
| LOADING.md | Loading screens and background asset builds |

## Characters and systems
| File | What it covers |
|---|---|
| JOBS.md | Job tree, Archetype Trial, job change |
| ARCHETYPES.md | Four archetype prototypes: skills, passives, auto stat build |
| QUESTS.md | Quest list, hunts, main chapters, quest items |
| IDLE.md | Idle rules, offline rewards, VIP split |
| ITEMS.md | Item types, consumables, sets, rolls, abilities |
| EQUIPMENT-SLOTS.md | The 10 equipment slots and how to add new items |
| ACCOUNTS.md | Login, register, guest, security, save keys |
| AUDIO.md | Generated 8-bit music and sound effects |

## UI and tests
| File | What it covers |
|---|---|
| UI-UX.md | Screen layouts and components (not re-checked line by line) |
| COMBAT-TEST-REPORT.md | Simulator results and balance evidence (historical) |

## Key numbers (single source)
- Recommended CP: Field 01 **150**, Field 02 **450**, Field 03 **900**, Path to the Geosyncline **2,000**, Road to the Ruins **3,000**.
- Gates: Geosyncline needs Base Lv 25+ and CP 2,000+; Ruins needs Base Lv 30+ and CP 3,000+.
- Equipment: 5 classes × 10 slots × 10 tiers × 5 rarities = **2,500** pieces.
- Save keys: guest `reo.gameState.v2`, accounts `reo.accounts.v1`, session `reo.session.v1` (see ACCOUNTS.md).

## Changes in v21d (this update)
- **Death crumble effect.** A dying monster breaks into shards in its colour that scatter and float up, then curve into the player with glowing trails and flash on arrival (~1 s). Normal 22 shards, Elite 38, boss 70 (half on Low graphics). A soft whoosh + rising sparkle (`absorb`, bigger `absorbbig` for Elites and bosses) plays as the shards arrive. See `UI-UX.md` §15b, `AUDIO.md`.

## Changes in v21c
- **Monster packs.** Every hunting map (Field 01–03, Geosyncline, Ruins) keeps its scattered monsters and now also has 3 packs, one per kind: 6 of the weakest kind, 5 of the middle, 4 of the strongest. A pack stays within 2.5 tiles of its centre (wanders 3 tiles), respawns there, and the whole pack (within 10 tiles) charges when one member is hit or spots you. Code: `PACK_*`, `packSize`, `packSpot`, `packAggro` next to `newMon`. Docs: the five `FIELD-*.md` files, wiki Monsters.

## Changes in v21b
- **The Idle buff skill set rotates too**, like the attack set: after slot n comes slot n+1 (wrapping); a buff that is still running (more than 1 s left) is skipped.

## Changes in v21a
- **Fix: the Idle attack skill set only cast one skill.** The set now rotates (after slot n comes slot n+1, wrapping; a skill that is not ready is skipped), so Petrifaction + Fire Bolt goes Petrifaction > Fire Bolt > Petrifaction … Self-area skills (Petrifaction) were never cast from range because no monster stood inside the area; Idle now walks in first (the pending-skill walk also handles skills without a range).

## Changes in v21
- **Idle Settings built** (gear badge on the Idle button): six tabs, Target · Combat · Recovery · Warp · Loot · VIP, saved in `S.iset`. Chosen targets (5 slots per map, no bosses, Elites count as their kind), fight back when attacked, stop timer; basic attack switch (forced on when skill attacks are off) and four 9-slot skill sets (attack, buff, healing, movement) with level picks; sit to rest; HP / SP potions with order and 5–95% bars; 5 buff-item slots re-used when the buff ends; Fly Wing when nothing is in sight for 3 s; return to town when full; loot filter (usable, gear by ★ / archetype / level, other; quest items always); VIP auto-buy Fly Wing and auto Pocket Dimension (errands keep Idle running). Teleport skill and auto resurrection are mockups. The boss / Elite switches and the auto-idle row are gone from this window. Offline idle uses the chosen targets and the loot filter. Details: `IDLE.md` "Idle Settings".
- **Minimap Return to town now costs** the World Map price to Town (150 Sc per map passed); the tooltip shows it.

## Changes in v20.18
- **Spellcaster spells rebalanced, all Lv 1–5.** **Fire Bolt** 1 / 3 / 5 / 7 / 10 fireballs of 120% MATK, SP 12 / 17 / 22 / 27 / 40, FCT 0.5–1.0 s (VCT 0), Global Delay 1 s; every fireball always falls even after the target dies, and no basic-attack bolt leaves the hand as a spell goes off. **Frost Nova → Freezer** (1 enemy, 110–200% MATK Water, Freeze 35–75%). **Lightning Spear** is ground magic: 2–10 spears of 100% MATK Wind on a 5 × 5 area, FCT 1.5 + VCT 1.0–1.8 s, GD 2 s. **Stone Spike → Petrifaction** (Self Cast, 7 × 7 around the caster, 75–100% MATK Earth, Petrifaction 30–75%). New status debuffs: Freeze (Wind +50%) and Petrifaction (Fire +50%) stop the monster; time, resistance and boss immunity are placeholders (⚠). New icons for the four spells. Old saves keep their levels (Fire Bolt above 5 drops to 5, points come back). The simulator now picks spell levels itself; Spellcaster CP at Lv 30 without gear 1,158 → 922. Bigger casting circles: a magic circle under the feet and a larger one at the hands while casting (`UI-UX.md` §27). See `SKILL-SPEC.md` §3, §3e–3h, `ARCHETYPES.md`, `COMBAT-FORMULAS.md` §5, `UI-UX.md`.

## Changes in v20.17a
- **Fix: inventory Sort crashed** ("loc is not defined"). `sortInventory` now builds its name-compare locale from the current language (`ja` for Japanese).

## Changes in v20.17
- **Character creator + code-drawn hero.** After login / register / guest, a save without an appearance opens a character creator in the login screen's style: gender, 7 hairstyles per gender, 8 hair colours, 6 eye colours, 5 outfit colours (Standard is the default) and the character name, with a live preview (Stand / Walk, turn through 8 directions). Saved as `S.app`; a new name is also written to the session and account (`AUTH.rename`). The main character is now drawn in code (`drawHero8`) in 8 directions with idle, walk, sword attack, cast, bow (Rangers), sit, hit (new `player.hurtT`) and death poses; it is the new default look (`S.look="custom"`). The sprite sets and classic chibi stay in Settings > Graphic > Character look; Settings > Graphic > Appearance > Edit reopens the creator. All text in Thai, English and Japanese. See `UI-UX.md` §28, `ACCOUNTS.md` §4b.

## Changes in v20.16
- **Illustrated skill icons.** All 28 skill icons are redrawn as full-colour pictures based on each skill's description (gradients, light, glow, dark outline): e.g. Fire Bolt is a fireball comet, Frost Nova an ice crystal, Crushing Blow a hammer cracking the ground with 3 stack orbs, Elemental Attunement four element orbs. They replace the one-colour duotone set from v20.10 in the Skills Tree, Skill Info, hotkey bar, drag ghost and archetype cards. Locked skills show the picture in grey. Shared gradients live in `<svg id="skdefs">`. See `UI-UX.md` §26.

## Changes in v20.15
- **Hero death animation.** New `images/hero/male/death.webp` (8 frames) and `images/hero/female/death.webp` (3 frames), 8 directions. On death the hero falls once and stays down until respawn, instead of the old tipped-over chibi. Male SW / NW rows are mirrored from SE / NE. See `UI-UX.md` §27.

## Changes in v20.14
- **Male hero poses.** New `images/hero/male/sit.webp`, `attack.webp`, `cast.webp` (one frame × 8 directions), used the same way as the female poses: sit when sitting, cast while casting, a short attack or cast flash after attacks and skills. See `UI-UX.md` §27.

## Changes in v20.13
- **Female hero poses.** New `images/hero/female/sit.webp`, `attack.webp`, `cast.webp` (one frame × 8 directions). Sitting uses the sit pose; casting shows the cast pose for the whole cast; a basic attack or skill flashes the attack pose (physical) or cast pose (magic, buffs) for about 0.3 s and turns the hero to the target. Male still uses the old fallbacks. See `UI-UX.md` §27.

## Changes in v20.12
- **Female hero sprite.** New set `images/hero/female/idle.webp` (3-frame idle, 3 fps) and `walk.webp` (3 frames), 8 directions. Settings > Graphic > **Character look** is now Male / Female / Classic (`S.look`; the old `"new"` value reads as Male). Sets load the first time they are drawn. See `UI-UX.md` §27.

## Changes in v20.11
- **Hero sprite (test, male only).** The main character is drawn from sprite sheets (`images/hero/male/idle.webp`, `walk.webp`): 8 facing directions, a 4-frame walk, idle bob; sitting and death reuse the idle frame. The player card avatar, Character doll and Status portrait use the front frame. Settings > Graphic > **Character look** switches between New and Classic (the old chibi), saved as `S.look`. The female set is on hold until its clipped frames are redrawn. See `UI-UX.md` §27.

## Changes in v20.10
- **Fix (Skills Tree on phones):** Basic Skill (and any learned skill that can still be raised) keeps its ◀ ▶ arrows on, so it can be raised after Skill Info closes; ▶ with no points left says "Not enough skill points." instead of doing nothing. See `UI-UX.md` §26.
- **Skills Tree window** replaces the Skills list. Same frame as Status and Bag (440 px wide). One tab for the current class line: **Beginner** (blue) for a Beginner; after the Archetype choice only the archetype tab (Fighter red, Ranger green, Spellcaster purple, Supporter yellow), which already holds the Beginner skills (C2 / C3 tabs later). A 5 × 5 grid laid out as in the design: column 1 = Basic Skill, First Aid, Heavy Strike; columns 2–5 = the archetype (passives row, actives row; Spellcaster puts Overload Energy on the first row). Tiles: active = colour fill, passive = white with a colour line, not learned = grey. Learning is a draft: tap a skill, plan levels with ◀ ▶, then **Learn**; **Reset** drops the draft. On a learned skill, ◀ ▶ pick the level a drag puts on the hotkey bar. Footer "Skill Points : N" (points not spent yet, drafts included), Learn, Reset. A left click on a skill opens the new **Skill Info** window (Item Info size): name and level, chips, description, every level, and a VCT / FCT / CD / Delay table (base values; it replaces the v20.9 "Cast x s (VCT a + FCT b)" line of the old list). The Hotbar setup drop-downs are removed (skills reach the bar by drag and drop). Every skill has a new duotone icon in its line colour (hotkey bar too); the element no longer colours the icon. See `UI-UX.md` §26 (and §24, §25), `SKILL-SPEC.md` §4–5, `JOBS.md` §1b.

## Changes in v20.9
- **Casting split into VCT and FCT (iRO Renewal).** Every skill can state four timing values: Variable Cast (`vct`), Fixed Cast (`fct`), Cooldown (`cd`) and Global Delay (`gd`); a missing value is 0. Real cast = `VCT × (1 − √((DEX×2+INT)/530)) × gear + FCT × gear` (replaces `× (1 − DEX/150)`). FCT, Cooldown and Global Delay are lowered by gear only (`ab.fct`, `ab.cdr`, `ab.gd`; only *Cooldown* exists so far). Every spell's old cast time is now its VCT, FCT 0 for now. The cooldown now starts when the cast ends, as `SKILL-SPEC.md` says (it used to start with the cast). The Skills window shows `Cast x s (VCT a + FCT b)`; the Status window shows the FCT and Global Delay reductions. Wiki Fire Bolt row brought up to date. See `COMBAT-FORMULAS.md` §2b, `SKILL-SPEC.md` §1, `UI-UX.md`.

## Changes in v20.8
- **Japanese (日本語) added as a third language.** The language switch now reads ไทย · EN · 日本語 in Settings (Other tab) and on the login page. The browser picks Japanese when its language starts with `ja`. Every key of the dictionary has a `jp` text (`D.jp`, 984 keys) and the login page has `I.jp`. Bilingual data (items, gear, abilities, set names, rarity, chat seed lines) gets its Japanese from the `JPX` table, keyed by the English text, read with `LP` / `LO` / `PT`. Numbers and times use `LOCALE[lang]` (`ja-JP`). Japanese text uses Noto Sans JP. The wiki (`wiki.html`) is Thai-only and is unchanged. See `UI-UX.md` §4, `REO-INSTRUCTIONS.md` (Languages, Localization).

## Changes in v20.7
- **Quests.** Main quest "A New Beginning" is now 9 chapters (3 kills each in Field 01/02/03, then return to Lumi). The Archetype Trial needs 1 Elite and **starts automatically** at Job Lv 10 + Basic Skill Lv 10; it can't be abandoned. Finishing it gives the chosen archetype's **full 10-piece class set** (Lv 10, Common, no random options), equipped at once. The "+10 Elite kills" test button is gone from Settings. Every Normal quest can be done **once per day**; every Elite Hunt pays only 1 Yttrium. See `QUESTS.md`, `JOBS.md` §4.

## Changes in v20.6
- **Spellcaster skills.** Mana Flow is now Lv 1–10 (Max SP +1–12%, SP regen +10–30%, SP cost −1–12%) and Elemental Attunement Lv 1–5 (+5% weakness bonus per level, 175% at Lv 5). New buff **Overload Energy** Lv 1–5: +1–5% Overload Rate for 20–120 s to self and party within 12 × 12 tiles, cooldown 60 s, Global Delay 1 s, cast 1–2 s, SP 50 / 65 / 80 / 95 / 110, Self Cast (no target needed). New spec term: **Self Cast** vs **Target Cast** (`SKILL-SPEC.md` §1). The Skills window shows each passive's current and next level. See `SKILL-SPEC.md` §3b–3d, `ARCHETYPES.md`, `COMBAT-FORMULAS.md` §3b.

## Changes in v20.5
- **Drag and drop on the hotkey bar.** Drag a usable item from the bag or a skill from the Skills window onto any of the 10 hotkey slots. The bar is no longer locked: a slot holds a skill or a usable item (potion, Fly Wing, apple), and a slot can be moved (drop it on another slot to swap) or cleared (drop it outside the bar; the item or skill is kept). Bag gear, materials, quest and cash items, worn pieces and passive skills are refused on the bar with a notice. A bag item dropped outside any zone does nothing. Worn pieces and bag items can be picked up for future trade and sell zones. Auto-potion uses whichever slot holds Red or Blue Potion. Saves with the old layout (7 skill slots, then Fly Wing, Red Potion, Blue Potion) migrate on load. See `UI-UX.md` §25, `SKILL-SPEC.md` §5 and `REO-INSTRUCTIONS.md` §5.

## Changes in v20.4
- **Basic Skill**, the Beginner skill tree: one skill, Lv 1–10 (Lv 1 given, 1 skill point per level, 9 points at Job Lv 10). Each level unlocks one ability: sit / status (2), First Aid 50 HP · SP 10 · CD 5 s (3), Heavy Strike 200% ATK · SP 5 · CD 5 s · range 1.6 tiles, same as the basic attack (4), Pocket Dimension (5), friends (6), party (7), trade (8), guild (9), Archetype Trial (10). Kept for good after the Archetype choice. See `JOBS.md` §1b.
- New NPC **Narvis** (Gadolinium, west edge of the plaza) opens the **Pocket Dimension**, a 300-slot personal storage. See `ITEMS.md` §7, `GADOLINIUM.md`, `UI-UX.md` §24.

## Changes in v20.3
- Party rewards: a size bonus on EXP, Items and Scandium (2 people +5%, 3 +12%, 4 +21%, 5 +32%, 6 +47%, cumulative). Two leader settings: EXP sharing (own / split equally) and Item & Scandium sharing (own / rotate). A party needs a level gap of at most 20; the invite is refused otherwise. The leader can rename the party (2–10 characters); the title shows as "Character (Party)". See `ECONOMY.md` §4 and `UI-UX.md` §23.

## Changes in v20.2
- Parties: create a party from the right-click menu on yourself (name it in Social → Party), invite other players from their right-click menu (leader only, max 6, warning if they already have a party), remove members, disband. Guild invite appears only with invite rights. See `UI-UX.md` §23.

## Changes in v20.1
- Right-click (phones: long-press) menu on characters: add friend, whisper, sit and rest (3× HP / SP regen), status sign in town. Trade and stalls are listed as *Soon*.
- Menu: Party and Guild merged into **Social** (Friends / Party / Guild tabs). See `UI-UX.md` §23.

## Changes in v20
- All maps are now 98 × 98 tiles (the old 49 × 49 layouts scaled 2×). Fields keep prop sizes, have 3× monsters and 2 Elites per kind; field portals sit 2 tiles from the edge. See `GADOLINIUM.md`, `FIELD-*.md`.
- Gadolinium re-laid out around a bigger plaza with a market ring; the Gadolinium Crystal is now a monument (3-tier dais, 4 pylons, the original crystal shape at 2.8×).
- Ground textures are drawn in chunks under a memory budget; only the current map and the one ahead stay loaded. Saves carry `mv` and old positions are scaled up.
- New `CLAUDE.md` at the repo root: rules for keeping `MD/` and the `MD/index.html` copy in sync.

## Changes in v19.1
- HUD: Idle button moved inside the hotbar panel (same plane as the slots), new circling-arrows idling motion, portrait monster panel centred with the hotbar, portrait announcement moved to the bottom. See `UI-UX.md` §16.

## Changes in v19.0
- Two new maps from the town gates (west and south), with warning signs, entry gates (Lv + CP), 6 aggressive monsters with ground-circle skills, Burning and Soaked debuffs, 12 new materials, 2 new music tracks, new World Map layout (6 maps), Elite hunts and per-monster hunts.
- New docs: `FIELD-GEOSYNCLINE.md`, `FIELD-RUINS.md`. Updated: `WORLD-MAP`, `GADOLINIUM`, `TOWN-ALIEN`, `ITEMS`, `QUESTS`, `AUDIO`, `COMBAT-FORMULAS`, `REO-INSTRUCTIONS`, wiki.

## Changes in the v18.3 update
- Recommended CP fixed in FIELD-01 (400 → 150), FIELD-02 (900 → 450), IDLE (formula example). FIELD-03 test table now labels 1,100 as a test value; the map recommends 900.
- FIELD-01: old v1 combat, idle and save sections replaced with pointers to COMBAT-FORMULAS, IDLE and ACCOUNTS.
- ITEMS: equipment count corrected to 2,500; the slot list now reflects 10 slots.
- REO-INSTRUCTIONS: helper NPC added; starter quest rewards say "Base EXP"; the fixed skill table replaced with a pointer to ARCHETYPES; progression section updated; roadmap status updated.
- QUESTS: main quest row now reaches the later chapters.

## Still open
- UI-UX.md and COMBAT-TEST-REPORT.md were not re-checked line by line against the code.
- ITEMS.md §3 stat table still lists the legacy Legs / Off-hand / Necklace rows (they remain as aliases).
- Lanthanum acquisition, teleport price curve, pack price and Gadolith respawn are placeholders (see each file's Open questions).
