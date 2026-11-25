# REO (Rare Earth Online): Docs Index

> Synced with `index.html` v22a. Read `REO-INSTRUCTIONS.md` first; it is the rulebook.

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
| FIELD-ASHFALL.md | Ashfall Ruins (Ruins south portal, Lv 40+ / CP 6,000+, rec. 9,000): fast, far-seeing, ranged and magic Fire monsters, boss Magma Gatekeeper |
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
- Recommended CP: Field 01 **150**, Field 02 **450**, Field 03 **900**, Path to the Geosyncline **2,000**, Road to the Ruins **3,000**, Ashfall Ruins **9,000**.
- Gates: Geosyncline needs Base Lv 25+ and CP 2,000+; Ruins needs Base Lv 30+ and CP 3,000+; Ashfall Ruins needs Base Lv 40+ and CP 6,000+.
- Equipment: 5 classes × 10 slots × 10 tiers × 5 rarities = **2,500** pieces.
- Save keys: guest `reo.gameState.v2`, accounts `reo.accounts.v1`, session `reo.session.v1` (see ACCOUNTS.md).

## Changes in v22a (this update)
- **Ranger balance (NIIQ):** Aim Strike VCT 1 → 0.5 s, Global Delay 2 → 1 s, cooldown 2 → 1 s, **SP 10 at every level** (was 12–20; damage and split unchanged). Aiming Shower cooldown 2 → 1 s.
- **Ranger AI (Idle built-in choice and simulator):** Aim Strike first only when 2+ monsters are close (splash); against one target Double Strafe comes first (more damage per SP), then Aim Strike.
- Ranger CP Lv 10 / 20 / 30 = 656 / 1,044 / 1,761 (Fighter 598 / 1,090 / 1,576); Ruins DPS 200 (Fighter 181, Spellcaster 200). `SKILL-SPEC.md` §3m, §3n.

## Changes in v22
- **New map: Ashfall Ruins / ซากอารยธรรมพรอมีเธีย** (`ashfall`, `FIELD-ASHFALL.md`), through a new **south portal on Road to the Ruins** (Lv 40+ and CP 6,000+, recommended CP 9,000, two "Monster Lv.40+" signs). The ruins of Promethea, buried by a volcanic eruption that also spewed rare earth veins: ash ground, lava fissures (palette-coloured chasm tiles), lava pools, glowing rare earth veins (`vein`), broken columns, a boss arena and the Sealed Caldera Gate (`bgate`). Music `ashfall`.
- **Three aggressive monsters, ~3× Road to the Ruins**, fast (chase 3.2–4.2 tiles/s) and far-seeing (aggro 6.5–8, Elites +1): **Scoria Hound** (Lv 42, melee pack hunter), **Cinderbow Revenant** (Lv 45, **ranged 7 tiles**), **Pyroclast Magus** (Lv 48, **magic 6 tiles**: never misses, armor does not help, MDEF does). Five new monster skills, some magic (`MSK.*.mg`). New monster fields `rng` and `mag`; `monShoot`, `magDmg` (`COMBAT-FORMULAS.md`).
- **Boss: Magma Gatekeeper** (Lv 55, 120,000 HP): Caldera Slam, Magma Gate, enrage below 30% HP. Boss code is generic now (`slam`, `warnK`, `enrage`, `heart`, `downK`, `sysK`, `col` per boss; boss music on any map with a boss; Map Info Boss tab rewards per boss).
- 7 new items (rare earth ores Neodymium / Samarium / Promethium, Scoria Fang, Revenant Ash, Pyroclast Glyph, quest item Caldera Heart), 3 hunts, Elite Hunt: Ashfall, Boss Hunt: Magma Gatekeeper. Map Info Monster tab shows Fast / Ranged / Magic. World Map node beside Ruins. Text in en / th / jp.
- Wiki: new map, monsters, boss section (both bosses), hunts for Geosyncline / Ruins / Ashfall; new images in `images/monsters` and `images/maps`. `window.__reo.monPortrait` renders a monster sprite for wiki images.

## Changes in v21h
- **Aim Strike is an attack skill again, toned down** (new spec from NIIQ, `SKILL-SPEC.md` §3m): one arrow of 100–200% ATK **in total**; a 20–38% chance to split into 2 arrows (Lv 1–5) or 3 (Lv 6–10) that **share** that total; each arrow splashes 50% of its share on 3 × 3; crit chance ×0.5. SP 12–20, FCT 0.5 s, VCT 1 s, Global Delay 2 s, cooldown 2 s. The v21g buff is gone.
- **Aiming Shower:** FCT 0.5 s, VCT 0.5 s, Global Delay 0.1 s, **cooldown 2 s** (was FCT 0.1 s, CD 0).
- **Balance:** Ranger CP Lv 10 / 20 / 30 = 637 / 1,023 / 1,708 (Fighter 598 / 1,090 / 1,576), Ruins DPS 185 (v21g 407). Aim Strike is now slightly below just shooting against one target (the cast stops basic attacks); it pays off on packs.

- **Deploy note (2026-11-25):** the first Pages deploy of v21h failed with HTTP 500 during GitHub's incident ("degraded experiences across GitHub products", high database load, from about 16:08 UTC); run #62 stayed queued and could not be cancelled. This entry is a new commit on main so Pages builds and deploys v21h again. No game code changed.

## Changes in v21g
- **Aim Strike is now a Self Cast buff** (new spec from NIIQ, `SKILL-SPEC.md` §3m). For 60–150 s, every basic shot has a 20–38% chance to split in mid-air into 2 / 2 / 3 / 3 / 4 / 4 / 5 / 5 / 6 / 7 arrows of 100–200% ATK each (0.1 s apart, crit chance ×0.5); every arrow splashes 50% on a 3 × 3 area. SP 60–150, FCT 2 s, Global Delay 2 s, cooldown = duration. The v21f burst (a full SP bar in 1 s) is gone. Idle and the simulator keep the buff up; buff icon in the status island; text in en / th / jp.
- **Balance:** Ranger CP Lv 10 / 20 / 30 = 654 / 1,056 / 1,996 (v21f 640 / 1,065 / 1,614; Fighter 598 / 1,090 / 1,576). ⚠ At Lv 10 a basic shot under the buff averages ~6× a normal shot: Ruins DPS 407 (Fighter 181, Spellcaster 200). Ideas in `SKILL-SPEC.md` §3n balance check.

## Changes in v21f
- **Five new Ranger skills** (from NIIQ, `SKILL-SPEC.md` §3i–3n; the old Ranger prototype skills stay): **No Arrow** (passive Lv 1–5: Scandium arrows, 20 / 18 / 15 / 13 / 10 Sc per arrow shot, no Scandium = no shot), **Ranger Mastery** (passive Lv 1–10: DEX, HIT, AGI +Lv), **Focusing** (Self Cast Lv 1–10: DEX and AGI +3–12% for 60–240 s, SP 25–70), **Aim Strike** (Lv 1–10: 100–200% ATK arrow, 20–40% chance to split into 2–7 arrows 0.1 s apart, 50% splash on 3 × 3, crit chance ×0.5, SP 12–25, GD 0.1 s), **Aiming Shower** (Lv 1–10: 160–250% ATK, pushes the target 2 tiles back incl. bosses, SP 20, FCT 0.1 s, GD 0.1 s). New **skill requirements** (`SKREQ`): the four need No Arrow Lv 1 / 3 / 5 / 5; locked tiles show what they need, Skill Info has a Requires line. Text in en / th / jp.
- **Fix: the Status window showed no bonus from Ranger Mastery / Focusing.** The green "+N" next to each base stat counted only gear and Blessing; it now shows everything on top of the base stat (gear, Blessing, Ranger Mastery, Focusing), read from the derived stats. The bonuses always applied in combat.
- **Arrows look like arrows** (`arrowDraw`): every Ranger shot is an arrow turned along its arc; Scandium arrows glow pale gold with a sparkling trail (`UI-UX.md` §30). New icons for the five skills.
- **Balance:** Ranger CP Lv 10 / 20 / 30: 457 / 861 / 1,354 → 640 / 1,065 / 1,614 (Fighter 598 / 1,090 / 1,576), mostly from Ranger Mastery. ⚠ Aim Strike can empty a full SP bar in about 1 s (~9,000 damage at Lv 30), and No Arrow costs more Scandium than Field 01–02 pay. Details and suggested fixes in `SKILL-SPEC.md` §3n, `ECONOMY.md` §5; idle / offline arrow cost in `IDLE.md`.

## Changes in v21e
- **Fire Bolt: splash + Burning.** Every fireball that hits also does 50% of its MATK as Fire to the other monsters in a 3 × 3 square round the target, and each cast has a 30 / 40 / 50 / 60 / 70% chance (by level) to set the target **Burning** (burns for 10% MATK Fire every second, Water hits it +50%, it keeps moving; a Freeze puts it out). **Freezer: splash** of 50% MATK Water on a 3 × 3 square while the target is Frozen. New `STATUS.brn`; statuses now say whether they hold the monster (`hold`). Skill text and Skill Info updated in en / th / jp. CP (Lv 10 / 20 / 30): 236 / 496 / 922 → 233 / 546 / 971 (`SKILL-SPEC.md` §3, §3e, §3h; `COMBAT-FORMULAS.md` §5).
- **Status looks.** Frozen monsters turn icy blue inside ice crystals, Petrified ones turn to cracked grey stone, Burning ones glow orange in flames with embers and smoke, and stunned ones get circling stars. Ice shatters and stone crumbles when the status ends (`UI-UX.md` §29).

## Changes in v21d
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
