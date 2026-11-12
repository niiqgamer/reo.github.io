# REO (Rare Earth Online): Docs Index

> Synced with `index.html` v18.3. Read `REO-INSTRUCTIONS.md` first; it is the rulebook.

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
- Recommended CP: Field 01 **150**, Field 02 **450**, Field 03 **900**.
- Equipment: 5 classes × 10 slots × 10 tiers × 5 rarities = **2,500** pieces.
- Save keys: guest `reo.gameState.v2`, accounts `reo.accounts.v1`, session `reo.session.v1` (see ACCOUNTS.md).

## Changes in this update
- Recommended CP fixed in FIELD-01 (400 → 150), FIELD-02 (900 → 450), IDLE (formula example). FIELD-03 test table now labels 1,100 as a test value; the map recommends 900.
- FIELD-01: old v1 combat, idle and save sections replaced with pointers to COMBAT-FORMULAS, IDLE and ACCOUNTS.
- ITEMS: equipment count corrected to 2,500; the slot list now reflects 10 slots.
- REO-INSTRUCTIONS: helper NPC added; starter quest rewards say "Base EXP"; the fixed skill table replaced with a pointer to ARCHETYPES; progression section updated; roadmap status updated.
- QUESTS: main quest row now reaches the later chapters.

## Still open
- UI-UX.md and COMBAT-TEST-REPORT.md were not re-checked line by line against the code.
- ITEMS.md §3 stat table still lists the legacy Legs / Off-hand / Necklace rows (they remain as aliases).
- Lanthanum acquisition, teleport price curve, pack price and Gadolith respawn are placeholders (see each file's Open questions).
