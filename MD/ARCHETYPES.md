# Archetype Prototypes (C1 baseline)

> Part of the REO docs. Formulas: `COMBAT-FORMULAS.md`. Test evidence: `tests/COMBAT-TEST-REPORT.md`.
> These are **baseline prototypes per archetype**, not the final 16 classes. Class names inside each archetype stay as in `JOBS.md`.
> All skills are prototyped at **skill Lv 5**. Range is in tiles.

| Archetype | Type | Range | Identity mechanic | Primary stats | Plays like |
|---|---|---|---|---|---|
| Fighter | MELEE | 1–3 (1.8) | **Momentum** stacks spent by a finisher | STR > VIT ≈ AGI > DEX | Tank / bruiser: highest effective HP, solid damage |
| Ranger | RANGED | 1–12 | **Distance bonus** + escape leap | DEX > AGI > LUK | Safest damage dealer: kills before monsters arrive |
| Spellcaster | MAGIC | 1–7 | **Cast times + elemental weakness**, spells never miss | INT > DEX > VIT | Burst and area damage, must read monster elements |
| Supporter | SUPPORT | 1–15 (heal/buff), 9 (attack) | **Sustain**: iRO Heal + overheal shield, zone | INT > VIT > DEX | Lowest solo damage, best survival; party glue later |

---

## Fighter — Momentum
Basic hits and Power Strike add Momentum (max 5, lost after 5 s without hitting). Crushing Blow spends all stacks.

| Active | Effect | SP | CD | Notes |
|---|---|---|---|---|
| Power Strike | 250% ATK, one enemy | 8 | 1.5 s | +1 Momentum |
| Whirlwind Cleave | 200% ATK to all within 2 tiles | 14 | 3.5 s | AoE around self |
| Crushing Blow | 180% ATK **+50% per stack** | 12 | 5 s | Spends stacks; stun 1.5 s at 3+ |
| War Cry | Taunt within 5 tiles, +20% DEF 8 s | 15 | 20 s | Tank tool |

| Passive | Effect |
|---|---|
| Weapon Mastery | +20 ATK, +5 HIT |
| Iron Body | +15% Max HP, VIT-based DEF ×1.5 |

## Ranger — Distance
+2% damage per tile beyond 3, max +18% at 12 tiles (Steady Aim). Monsters must walk to you.

| Active | Effect | SP | CD | Notes |
|---|---|---|---|---|
| Double Strafe | 2 × 125% ATK | 10 | 1.2 s | Core rotation |
| Arrow Shower | 90% ATK, all within 1.6 tiles of target | 14 | 4 s | AoE at target |
| Piercing Shot | 320% ATK, ignores 50% armor DEF | 18 | 6 s | Can crit, crit chance ×2 |
| Evasive Leap | Jump 3 tiles away, +30 FLEE 4 s | 10 | 10 s | Next shot +60% |

| Passive | Effect |
|---|---|
| Eagle Eye | +3 range (9 → 12), +10 HIT |
| Steady Aim | Distance bonus, +5% crit |

## Spellcaster — Casting + elements
Every spell has a cast time reduced by DEX (×(1 − DEX/150)). Spells **never miss**. One spell per element, so the caster can always hit a weakness:

| Monster element | Weak to | Spell |
|---|---|---|
| Water (Lumite, Cryoculus) | Wind | Lightning Spear |
| Earth (Crawlix, Shardback) | Fire | Fire Bolt |
| Wind (Nebulite) | Earth | Stone Spike |
| Fire (Oculoth) | Water | Frost Nova (area) |

| Active | Effect | SP | CD | Cast |
|---|---|---|---|---|
| Fire Bolt | 100% MATK per fireball, fire; fireballs = skill Lv (Lv 1–10), dropped one at a time, 0.3 s apart (0.2 s from Lv 6), they stop if the target dies | 12 + 2 per Lv | 0 s, then 1.4 s Global Delay | 0.5 s + 0.3 s per Lv |
| Frost Nova | 260% MATK water, all within 2.5 tiles; 40% freeze 2 s | 20 | 5 s | 0.6 s |
| Lightning Spear | 380% MATK wind | 22 | 3 s | 1.6 s |
| Stone Spike | 260% MATK earth; 20% stun 1 s | 16 | 2 s | 1.0 s |

| Passive | Effect |
|---|---|
| Mana Flow | SP regen +60%, skill SP cost −10% |
| Elemental Attunement | Weakness bonus 150% → 175% |

Basic attack: Arcane Bolt, 70% MATK neutral, 7 tiles.

Fire Bolt now follows `SKILL-SPEC.md` (draft, Lv 1–10, range 7, overMul 0.5). The other three spells are still Lv 5 prototypes. MATK now includes a flat `weaponMATK` from the staff (`COMBAT-FORMULAS.md` §1).

## Supporter — Sustain
Heal follows iRO Classic: `[(BaseLv + INT) / 8] × (4 + 8 × SkillLv)`. Overhealing turns into a **Grace shield** (up to 20% Max HP) that absorbs damage.

| Active | Effect | SP | CD | Notes |
|---|---|---|---|---|
| Heal | iRO Heal ×1.2 (Divine Grace) | 13 | 1 s | Range 15 |
| Holy Light | 200% MATK holy | 15 | 1.5 s | Cast 0.8 s, range 9 |
| Blessing | +8 STR, INT, DEX for 120 s | 24 | 30 s | Range 15 |
| Sanctuary | Zone 2.5 tiles, 8 s: heal 4% Max HP/s, 50% MATK holy/s to enemies | 35 | 18 s | |

| Passive | Effect |
|---|---|
| Divine Grace | Healing +20%, overheal shield cap 20% Max HP |
| Guardian Aura | +8% DEF, +10% MDEF (party-wide later) |

Basic attack: Light Orb, 60% MATK holy, 9 tiles.

---

## Prototype gear (stand-in until items exist)
Weapon ATK grows with Base Lv to stand in for gear upgrades.

| Archetype | Weapon ATK | Growth / Lv | Armor DEF | MATK bonus | Base attack delay |
|---|---|---|---|---|---|
| Beginner | 17 | +1.0 | 5% | — | 1.00 s |
| Fighter | 40 | +2.2 | 20% | — | 0.95 s |
| Ranger | 34 (bow, DEX-based) | +2.2 | 10% | — | 1.00 s |
| Spellcaster | 12 | +1.0 | 5% | +20% | 1.30 s |
| Supporter | 25 | +1.5 | 12% | +10% | 1.10 s |

HP / SP: `baseHP = 300 + hpLv × (Lv−1)`, `baseSP = 80 + spLv × (Lv−1)`. hpLv: Beginner 30, Fighter 55, Ranger 38, Spellcaster 30, Supporter 42. spLv: 5 / 5 / 6 / 11 / 9.

## Auto stat build (default on)
Stat points follow iRO (48 at creation, `floor(lv/5)+3` per level, raise cost `floor((x−1)/10)+2`). Auto-assign spends them by weight:

| Archetype | STR | AGI | VIT | INT | DEX | LUK |
|---|---|---|---|---|---|---|
| Fighter | 5 | 3 | 3 | – | 2 | – |
| Ranger | – | 4 | 1 | – | 6 | 2 |
| Spellcaster | – | – | 2 | 6 | 4 | – |
| Supporter | – | – | 4 | 5 | 3 | – |

Players can switch auto-assign off and spend points by hand in the Character window.

## Prototype-only behavior
- **v5.1:** no more free switching. A Beginner picks **one** archetype, permanently, through the Archetype Trial (Job Lv 10 → 10 Elites → choose). See `JOBS.md` §4.
- Settings has two **test shortcuts** for checking the flow quickly: set Job Lv 10, and +10 Elite kills on the trial. Remove them before release.
- Recommended CP: Field 01 **150**, Field 02 **450**.

## Known gaps / next balancing pass
1. **Melee travel time:** in live play on Field 01 (Lv 12, 25 s idle), Ranger killed 21 vs Fighter 11. The simulator places melee 2.2 tiles from each target, but real maps make Fighters walk further between targets. Next pass: add travel distance to the simulator, then consider +10–15% Fighter movement speed or a gap-closer.
2. **Low levels:** before Lv ~8, Spellcaster and Supporter are weak (few INT points). This matches the design (C1 starts at Lv 10) but feels bad if you switch class at Lv 1 in the test picker.
3. Supporter buffs and Guardian Aura are self-only until parties exist.
4. Monster elements and DEF/MDEF/FLEE values are first-pass (`COMBAT-FORMULAS.md` §5).
