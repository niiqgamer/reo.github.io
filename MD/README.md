# REO (Rare Earth Online): Docs Index

> Synced with `index.html` v20.2. Read `REO-INSTRUCTIONS.md` first; it is the rulebook.

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

## Changes in v20.2 (this update)
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
