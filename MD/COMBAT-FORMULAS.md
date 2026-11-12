# Combat Formulas

> Part of the REO docs. Reference: iRO Wiki Classic — Stats (https://irowiki.org/classic/Stats).
> Code: `tests/combat.js` (same module the game runs). Lines marked **REO** are deliberate changes from classic.

## 1. Primary stats → substats

| Substat | Formula | Source |
|---|---|---|
| Status ATK (melee) | `STR + ⌊STR/10⌋² + ⌊DEX/5⌋ + ⌊LUK/5⌋` | iRO |
| Status ATK (bow) | `DEX + ⌊DEX/10⌋² + ⌊STR/5⌋ + ⌊LUK/5⌋` | iRO |
| MATK | min `INT + ⌊INT/7⌋²` ~ max `INT + ⌊INT/5⌋²`, × (1 + weapon MATK%) | iRO |
| HIT | `DEX + BaseLv` (+ passives) | iRO |
| FLEE | `AGI + BaseLv` (+ buffs) | iRO |
| Perfect dodge | `1 + LUK × 0.1` % | iRO |
| CRIT | `1 + LUK × 0.3` % (+ passives); target LUK/5 reduces it | iRO |
| Max HP | `baseHP × (1 + VIT/100)` | iRO |
| Max SP | `baseSP × (1 + INT/100)` | iRO |
| Soft DEF | `⌊VIT × 0.8⌋` flat | iRO (≈) |
| Hard DEF | armor % | iRO |
| Soft MDEF | `⌊INT / 2⌋` flat | **REO** (classic ≈ 1 per INT) |
| Attack delay | `base × (1 − AGI×0.004 − DEX×0.001)`, min 0.2 s; ASPD = `200 − 50 × delay` | iRO (−0.4% / −0.1%), cap 190 |
| Cast time | `base × (1 − DEX/150)` | iRO |
| HP regen /s | `(MaxHP/200 + VIT/5) / 4` | iRO per tick, adapted |
| SP regen /s | `(MaxSP/100 + INT/6 + 1) / 2` | iRO per tick, adapted |
| Potion healing | Red: `120 × (1 + VIT×0.02)` · Blue: `60 × (1 + INT×0.01)` | iRO |

Stat points: 48 at creation, `⌊lv/5⌋ + 3` per level (1,273 total at Lv 99). Raising `x → x+1` costs `⌊(x−1)/10⌋ + 2` (628 for 1 → 99).

## 2. Physical damage

```
hit%   = clamp(80 + HIT − targetFLEE, 5, 95)                       // iRO
crit%  = CRIT × critMul − targetLUK/5   (basic attacks; only Piercing Shot among skills)
weaponRoll = weaponATK × U(lo, 1),  lo = min(1, 0.5 + DEX×0.005)    // DEX narrows the roll; DEX 100 = always max
raw    = (statusATK + weaponRoll + masteryATK) × skill% × element × bonus
bonus  = distance (Ranger) × leap shot (+60%) …
normal = max(1, ⌊raw × (1 − hardDEF × (1 − ignoreDEF)) − softDEF⌋)
crit   = ⌊(statusATK + weaponATK + mastery) × skill% × element × bonus × 1.4⌋   // ignores DEF and FLEE
```
**REO:** crits get ×1.4 (classic crits only use max roll and ignore DEF).

## 3. Magic damage
```
MATKroll = U(MATKmin, MATKmax)
dmg = max(1, ⌊MATKroll × skill% × element × (1 − targetMDEF%) − targetSoftMDEF⌋)     // never misses
```

## 4. Heal (iRO Classic)
```
Heal = ⌊(BaseLv + INT) / 8⌋ × (4 + 8 × SkillLv) × (1 + healing bonus)
```
Example: Lv 20, INT 40, Heal Lv 5 → ⌊60/8⌋ × 44 = **308** (369 with Divine Grace).

## 5. Elements

| Attacker \ Defender | Fire | Water | Wind | Earth |
|---|---|---|---|---|
| Fire | 0.75 | 0.75 | 1.0 | **1.5** |
| Water | **1.5** | 0.75 | 0.75 | 1.0 |
| Wind | 1.0 | **1.5** | 0.75 | 0.75 |
| Earth | 0.75 | 1.0 | **1.5** | 0.75 |

Neutral and Holy deal 1.0 to these elements. Elemental Attunement raises 1.5 → 1.75. **REO:** classic weak multipliers go lower than 0.75.

| Monster | Lv | Element | HP | ATK | Hard DEF | Soft DEF | MDEF | HIT | FLEE |
|---|---|---|---|---|---|---|---|---|---|
| Lumite | 1 | Water | 60 | 10 | 2% | 1 | 5% | 20 | 10 |
| Crawlix | 3 | Earth | 125 | 17 | 10% | 3 | 0% | 28 | 15 |
| Oculoth | 6 | Fire | 250 | 32 | 5% | 5 | 20% | 35 | 12 |
| Nebulite | 7 | Wind | 170 | 26 | 5% | 5 | 15% | 40 | 30 |
| Shardback | 9 | Earth | 280 | 34 | 25% | 8 | 5% | 45 | 25 |
| Cryoculus | 11 | Water | 450 | 46 | 10% | 10 | 30% | 55 | 22 |
| Glacilite | 13 | Water | 540 | 44 | 8% | 10 | 20% | 62 | 34 |
| Rimeback | 15 | Earth | 760 | 54 | 28% | 13 | 8% | 68 | 30 |
| Magnoculus | 17 | Wind | 1,000 | 66 | 12% | 15 | 32% | 74 | 28 |
| **Gadolith (boss)** | 20 | Earth | 8,000 | 58 (attack every 2.6 s) | 25% | 12 | 20% | 80 | 20 |

Elite: Lv +2, HP ×5, ATK ×1.6, soft DEF +3. Bosses are not Elites: they have their own stats, are immune to stun and freeze, and Crystal Slam deals ATK × 1.8 in an area (see `FIELD-03.md`).

## 6. Monster → player
```
perfect dodge first (1 + LUK×0.1 %)
hit% = clamp(80 + monsterHIT − playerFLEE, 5, 95)
dmg  = max(1, ⌊monsterATK × U(0.85, 1.15) × (1 − playerHardDEF) − playerSoftDEF⌋)
Grace shield absorbs first.
```

## 7. Combat Power (CP)
```
CP = DPS × 6 + EffectiveHP / 20
DPS          = simulated 180 s vs a mix of all field monsters, using the archetype's own skill AI
EffectiveHP  = MaxHP / (1 − hardDEF) + softDEF × 30
```
It uses the simulation because counting only basic attacks undervalued Spellcasters by about 2.5× (see the test report).

## 7b. Gear and herbs (v7)
Equipped gear feeds the same derivation as the base stats: weapon ATK adds to weapon ATK, armor/legs/off-hand add to soft DEF, Off-hand adds hard DEF %, necklace adds HP and SP, ring adds CRIT and HIT, and each piece's primary stat adds to the character's stats before the formulas run. Herb buffs apply afterwards: Ember Root ×1.1 ATK, Frost Bloom ×1.15 soft DEF, Sage Leaf ×1.5 SP regen. CP and offline idle use the same totals (see `ITEMS.md` §3).

## 8. Offline idle (VIP and non-VIP)
Kills per hour now come from the same simulator, using the character's real stats, skills and map monsters (deaths included). Reward rules (80% / 100% / 120%, Yttrium upgrades) are unchanged; see `IDLE.md`.
