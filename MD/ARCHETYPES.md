# Archetype Prototypes (C1 baseline)

> Part of the REO docs. Formulas: `COMBAT-FORMULAS.md`. Test evidence: `tests/COMBAT-TEST-REPORT.md`.
> These are **baseline prototypes per archetype**, not the final 16 classes. Class names inside each archetype stay as in `JOBS.md`.
> All skills are prototyped at **skill Lv 5**. Range is in tiles.

| Archetype | Type | Range | Identity mechanic | Primary stats | Plays like |
|---|---|---|---|---|---|
| Fighter | MELEE | 1–3 (1.8) | **Shield & Log**: pull a pack, smash it with Timber!!, build Timber Logging and hurl the bundle | STR > VIT ≈ AGI > DEX | Tank / bruiser: highest effective HP, solid damage |
| Ranger | RANGED | 1–9 | **Scandium arrows** (No Arrow) + split / push shots | DEX > AGI > LUK | Safest damage dealer: kills before monsters arrive |
| Spellcaster | MAGIC | 1–7 | **Cast times + elemental weakness**, spells never miss | INT > DEX > VIT | Burst and area damage, must read monster elements |
| Supporter | SUPPORT | 1–15 (heal/buff), 9 (attack) | **Sustain**: iRO Heal + overheal shield, zone | INT > VIT > DEX | Lowest solo damage, best survival; party glue later |

---

## Fighter — Shield & Log
v22e skills from NIIQ (full tables: `SKILL-SPEC.md` §3o–3t). **v22g: the prototype skills (Power Strike, Whirlwind Cleave, Crushing Blow, War Cry, Iron Body) and Momentum are removed**; old saves get those skill points back and their hotbar slots clear. **v22h: Forbear is replaced by Logging** (Momentum's idea moved onto Timber!!).

| Passive | Effect |
|---|---|
| Weapons Mastery (Lv 1–10, v22e) | ATK +4 per level with a knife or sword (every Fighter weapon for now). Was Weapon Mastery: +20 ATK, +5 HIT, one level |
| Shield Mastery (Lv 1–10, v22e) | While a shield is worn: STR and VIT +Lv, DEF +2% × Lv, attack speed −2% × Lv |

| Active | Effect | SP | Needs |
|---|---|---|---|
| Timber!! (Lv 1–10) | 130–400% ATK on one enemy, HIT +5–50, 70% ATK on the others in 3 × 3 round it, 20% Stun 3 s, no crit. VCT 0.5 s, GD 0.5 s, CD 1.5 s | 8 (Lv 1–5) / 15 | – |
| Gaslighting (Lv 1–10) | Ground 3 × 3 at the target: non-boss monsters turn on the Fighter, soft DEF −10–55%, their ATK +5–32%, 5 s (Lv 1–5) / 10 s. GD 0.3 s, CD 1 s | 4–13 | – |
| Logging (Self Cast, Lv 1–10) | Buff for 10–100 s: every Timber!! that hits adds a Timber Logging; at 2–5 logs they are bound and hurled at the target: logs × (20–350%) ATK on a 5 × 5 square, no crit (Lv 10: 5 × 350% = 1,750%); then a new bundle can start; logs left when it ends are lost. VCT 5 s, CD 10–100 s | 20–50 | Timber!! 3 |

## Ranger — Scandium arrows
Range 9 tiles, 10–12 with Ranger Mastery (v22d). Every arrow is a Scandium arrow once No Arrow is learned (costs Scandium per shot). v21f adds five skills from NIIQ (full tables: `SKILL-SPEC.md` §3i–3n); the four that are not No Arrow need it first. **v22b: the prototype skills (Double Strafe, Arrow Shower, Piercing Shot, Evasive Leap, Eagle Eye, Steady Aim) are removed**, and with them the distance bonus (+2% per tile beyond 3), the +3 range (now 9 instead of 12), +10 HIT, +5% crit and the escape leap.

| New skill | Effect | SP | Needs |
|---|---|---|---|
| No Arrow (passive, Lv 1–5) | Shoot Scandium arrows: every arrow shot costs 20 / 16 / 12 / 8 / 4 Sc (v22d). Not enough Sc = no shot | – | – |
| Ranger Mastery (passive, Lv 1–10) | DEX +Lv, HIT +Lv, AGI +Lv; range +1 at Lv 1, 6, 10 (range 9 → 12 at Lv 10) | – | No Arrow 1 |
| Focusing (Self Cast, Lv 1–10) | DEX and AGI +3–12% for 60–240 s | 25–70 | No Arrow 3 |
| Aim Strike (Lv 1–10) | 1 arrow of 100–200% ATK in total; 20–38% chance to split into 2–3 arrows (0.1 s apart) that share it; each splashes 50% of its share on a 3 × 3 area; crit chance ×0.5. FCT 0.5 s, VCT 0.5 s, GD 1 s, CD 1 s | 10 | No Arrow 5 |
| Aiming Shower (Lv 1–10) | 1 arrow of 160–250% ATK, pushes the target 2 tiles back (bosses too); no crit. FCT 0.5 s, VCT 0.5 s, GD 0.1 s, CD 1 s | 20 | No Arrow 5 |

Points: the five skills cost 45 points at max; a C1 Ranger has 49.

## Spellcaster — Casting + elements
Every spell has a variable cast (VCT) reduced by DEX and INT (×(1 − √((DEX × 2 + INT) / 530))) and a fixed cast (FCT) only gear reduces (`COMBAT-FORMULAS.md` §2b). Spells **never miss**. One spell per element, so the caster can always hit a weakness:

| Monster element | Weak to | Spell |
|---|---|---|
| Water (Lumite, Cryoculus) | Wind | Lightning Spear (5 × 5 area) |
| Earth (Crawlix, Shardback) | Fire | Fire Bolt |
| Wind (Nebulite) | Earth | Petrifaction (7 × 7 around the caster) |
| Fire (Oculoth) | Water | Freezer |

| Active (Lv 1–5) | Effect | SP | CD · Global Delay | Cast (FCT + VCT) |
|---|---|---|---|---|
| Fire Bolt | Fire, 1 enemy: 1 / 3 / 5 / 7 / 10 fireballs of 120% MATK, 0.3 s apart (0.2 s at Lv 4–5); every fireball always falls | 12 / 17 / 22 / 27 / 40 | 0 s · 1 s | FCT 0.5 / 0.6 / 0.7 / 0.8 / 1.0 s, VCT 0 |
| Freezer (was Frost Nova) | Water, 1 enemy: 110 / 130 / 150 / 170 / 200% MATK; Freeze 35–75% (Wind +50% on it) | 25 | 0 s · 0.5 s | FCT 0.16 + VCT 0.64 s |
| Lightning Spear | Wind, ground magic on a 5 × 5 area: 2 / 4 / 6 / 8 / 10 spears of 100% MATK, 0.1 s apart, each hits every enemy inside | 30 / 42 / 54 / 66 / 78 | 0 s · 2 s | FCT 1.5 + VCT 1.0–1.8 s |
| Petrifaction (was Stone Spike) | Earth, Self Cast, 7 × 7 around the caster: 75 / 80 / 85 / 90 / 100% MATK; Petrifaction 30–75% (Fire +50% on it) | 25 / 27 / 28 / 32 / 35 | 0 s · 0 s | FCT 0.2 + VCT 0.8 s |
| Overload Energy (buff) | +Lv% Overload Rate to self and party within a 12 × 12 area; lasts 20 / 40 / 60 / 80 / 120 s | 50 / 65 / 80 / 95 / 110 | 60 s · 1 s | VCT 1 / 1.2 / 1.4 / 1.6 / 2 s |

| Passive | Effect |
|---|---|
| Mana Flow (Lv 1–10) | Lv N: Max SP +N%, SP regen +(8 + 2N)%, skill SP cost −N%. Lv 10: +12% / +30% / −12% |
| Elemental Attunement (Lv 1–5) | Weakness bonus +5% per level: 150% → 155 / 160 / 165 / 170 / 175% |

Full per-level tables: `SKILL-SPEC.md` §3b–3d.

Basic attack: Arcane Bolt, 70% MATK neutral, 7 tiles.

All five Spellcaster actives have Lv 1–5 and follow `SKILL-SPEC.md` §3, §3d–3h (v20.18). Freeze and Petrifaction stop the monster and open a weakness (§3h). MATK includes a flat `weaponMATK` from the staff (`COMBAT-FORMULAS.md` §1).

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
- **v5.1:** no more free switching. A Beginner picks **one** archetype, permanently, through the Archetype Trial (Job Lv 10 → 1 Elite → choose). See `JOBS.md` §4.
- Settings has one **test shortcut** for checking the flow quickly: set Job Lv 10. Remove it before release. (The old "+10 Elite kills" shortcut was removed in v20.7.)
- Recommended CP: Field 01 **150**, Field 02 **450**.

## Known gaps / next balancing pass
1. **Melee travel time:** in live play on Field 01 (Lv 12, 25 s idle), Ranger killed 21 vs Fighter 11. The simulator places melee 2.2 tiles from each target, but real maps make Fighters walk further between targets. Next pass: add travel distance to the simulator, then consider +10–15% Fighter movement speed or a gap-closer.
2. **Low levels:** before Lv ~8, Spellcaster and Supporter are weak (few INT points). This matches the design (C1 starts at Lv 10) but feels bad if you switch class at Lv 1 in the test picker.
3. Supporter buffs and Guardian Aura are self-only until parties exist.
4. Monster elements and DEF/MDEF/FLEE values are first-pass (`COMBAT-FORMULAS.md` §5).
