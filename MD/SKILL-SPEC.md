# Skill Spec: the standard for writing a skill (DRAFT)

> Part of the REO docs. Combat numbers: `COMBAT-FORMULAS.md`. Kits per archetype: `ARCHETYPES.md`.
> Status: draft from NIIQ. Fire Bolt (§3) is the first skill written to this standard. These are skills of the **archetype**; classes are not split yet. **Fire Bolt, skill levels, the hotbar level choice, Global Delay, weaponMATK and Overload are in the game (v20 build).** Items marked ⚠ are assumptions or open questions.

## 1. Fields every skill states

| Field | Meaning |
|---|---|
| MAX Lv | Highest skill level |
| ประเภท | Active or Passive |
| Type | Physical, Magic or Support |
| เป้าหมาย | Target (for example one enemy) and the **hit type** (§2) |
| การใช้ (Targeting) | **Self Cast** (กดแล้วร่ายเลย ไม่ต้องเลือกเป้าหมาย; may still have a cast time) or **Target Cast** (must pick an enemy or ally first). Do not write “Instant Cast”: in MMOs it means *no cast time* |
| ระยะห่างระหว่างฮิต | For multi-hit skills: seconds between two hits, and what happens if the target dies in the middle |
| ระยะ | Maximum range in tiles |
| เงื่อนไขก่อนเรียน | Prerequisite skills. “None” means it can be learned right away |
| อัตราเกินพิกัด | `overMul` for magic (`COMBAT-FORMULAS.md` §3b). **Not stated = 0: the skill cannot Overload** |
| คูลดาวน์ (Cooldown) | How long **this same skill** is locked after it is used. Starts when the **cast ends**. 0 s means it can be cast again at once (only the Global Delay still applies) |
| Global Delay | The delay between this skill and the **next skill** (any skill). Each skill states its own value. ⚠ Assumed to start when the cast ends and to leave basic attacks free |
| รายละเอียด | What the skill does, with the % of ATK or MATK |
| Per level | What changes at each level: hits, SP, cast time |

## 2. Hit types

| Cast | Real hits | Damage rolls | Shown as | Name |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 hit | **Single hit** |
| 1 | 1 | 1 | several hits | **Visual multi-hit** (split display) |
| 1 | several | 1 | per hit | **Shared-roll multi-hit** |
| 1 | several | per hit | per hit | **True multi-hit** (per-hit roll) |

Today’s code already rolls damage per hit (a skill with `hits` loops and calls the damage function once per hit), but it resolves all hits at the same instant. Fire Bolt will be the first skill with a gap between hits.

## 3. Fire Bolt (draft, replaces the prototype)

| | |
|---|---|
| MAX Lv | 10 |
| ประเภท | Active |
| Type | Magic, Fire element |
| เป้าหมาย | One enemy, **True multi-hit**. One fireball per skill level, dropped **one at a time** |
| ระยะห่างระหว่างฮิต | **0.3 s** at Lv 1–5, **0.2 s** at Lv 6–10. **If the target dies, the fireballs still to come are not released** |
| ระยะ | 7 tiles |
| เงื่อนไขก่อนเรียน | None |
| อัตราเกินพิกัด | ×0.5 |
| คูลดาวน์ | **0 s**. Different levels do not block each other: Lv 2 then Lv 10 is allowed straight away |
| Global Delay | **1.4 s** before the next skill (any skill) |
| รายละเอียด | Hits the enemy with fireballs. Each fireball deals Fire-element magic damage equal to **100% MATK** |

| Lv | Fireballs | Total | Gap | Volley length ⚠ | SP | Cast |
|---|---|---|---|---|---|---|
| 1 | 1 | 100% | – | 0 s | 12 | 0.5 s |
| 2 | 2 | 200% | 0.3 s | 0.3 s | 14 | 0.8 s |
| 3 | 3 | 300% | 0.3 s | 0.6 s | 16 | 1.1 s |
| 4 | 4 | 400% | 0.3 s | 0.9 s | 18 | 1.4 s |
| 5 | 5 | 500% | 0.3 s | 1.2 s | 20 | 1.7 s |
| 6 | 6 | 600% | 0.2 s | 1.0 s | 22 | 2.0 s |
| 7 | 7 | 700% | 0.2 s | 1.2 s | 24 | 2.3 s |
| 8 | 8 | 800% | 0.2 s | 1.4 s | 26 | 2.6 s |
| 9 | 9 | 900% | 0.2 s | 1.6 s | 28 | 2.9 s |
| 10 | 10 | 1,000% | 0.2 s | 1.8 s | 30 | 3.2 s |

Pattern: fireballs = Lv; SP = 12 + 2 × (Lv − 1); cast = 0.5 + 0.3 × (Lv − 1) s (reduced by DEX as before, `× (1 − DEX/150)`).

⚠ Assumptions (built into the game, not stated by NIIQ): the first fireball is released the moment the cast ends and the next ones follow every gap (so volley length = (fireballs − 1) × gap; Lv 6 is therefore shorter than Lv 5). A fireball takes (gap − 0.02) s to fall (0.28 s at Lv 1–5, 0.18 s at Lv 6–10) and deals its damage when it lands. If the target dies, fireballs not yet released are never released; a fireball already falling just fizzles. The character is free to act while the volley is still falling. SP is not refunded when a volley stops early.

**Old prototype (replaced):** 3 × 100% MATK, SP 12, cast 1.0 s, CD 0.5 s, range 7, all hits at once.

### Balance check (simulator on the game’s own combat module, not real play)
The game’s combat code was run in Node: 300 s, 3 seeds, auto stats, with the new rules (`weaponMATK` on the staff, Fire Bolt as in §3, Overload per `COMBAT-FORMULAS.md` §3b, a 1.4 s Global Delay after each Fire Bolt that blocks every skill but not basic attacks). The simulator casts Fire Bolt at a fixed level and always has every skill learned. The other three spells keep their prototype cooldowns.

**1. Staff weaponMATK, no gear.** The old staff gave +20% MATK. A flat `2 + 0.65 × (Lv − 1)` gives about the same total MATK, so the other three spells keep their ratios. Kills in 300 s:

| | Fighter | Ranger | Spellcaster, old | Fire Bolt Lv 3 | Fire Bolt Lv 5 | Fire Bolt Lv 10 |
|---|---|---|---|---|---|---|
| Lv 10, Field 01 | 59.3 | 54.0 | 44.0 | 38.0 | 41.0 | 38.0 |
| Lv 20, Field 02 | 53.3 | 50.0 | 44.0 | 44.0 | 44.0 | 40.0 |
| Lv 30, Field 02 | 63.3 | 58.3 | 56.0 | 54.0 | 52.3 | 49.3 |
| Lv 20, packs of 3 | 83.0 | 69.0 | 73.0 | 66.0 | 62.0 | 47.0 |
| Lv 35, Elites | 31.7 | 30.3 | 29.0 | 27.3 | 28.0 | 27.0 |

The old numbers match `COMBAT-TEST-REPORT.md` (Spellcaster 44 / 44 / 56 / 101 / 29). Fire Bolt Lv 5 is between 0% and −15% of the old prototype; Lv 10 is between −7% and −36% (worst against packs, with 2 deaths per run). A lower level does better against low-HP monsters: the long cast of Lv 10 is wasted when the target dies in the first few fireballs. The Global Delay also holds back Frost Nova and the other spells for 1.4 s after each Fire Bolt, which is why packs suffer most.

**2. Staff weaponMATK from gear, at gate-level gear** (Lv 30 vs the Ruins monsters; common tier-30 pieces, weapon first: 2 pieces = weapon and armor; 5 pieces ≈ the Fighter’s 3,136 CP). Kills · deaths in 300 s.

| | 2 pieces | 5 pieces |
|---|---|---|
| Fighter | 14.7 · 0.7 | 19.3 · 0 |
| Ranger | 16 · 2 | 22.3 · 0 |
| Supporter | 11 · 0 | 20 · 0 |
| Spellcaster, old (no weapon bonus) | 9 · 3.7 | 26 · 0 |
| Fire Bolt Lv 5, staff × 0 | 6 · 4 | 20 · 0 |
| Fire Bolt Lv 5, staff × **1** (`m × 2.2`) | **8.7 · 4** | **22 · 0** |
| Fire Bolt Lv 5, staff × 1.5 | 12 · 3 | 23 · 0 |
| Fire Bolt Lv 5, staff × 2 | 13.7 · 3 | 25 · 0 |
| Fire Bolt Lv 10, staff × 1 | 12.3 · 3 | 24.7 · 0 |

With 5 pieces, staff × 1 puts the Spellcaster level with the Ranger, so the rule stays `weaponMATK = m × 2.2`, the same as other weapons; × 0 is clearly weaker than the old prototype. With only 2 pieces the Spellcaster is behind (about 9 kills against 14.7 to 16) and still dies 3–4 times even at × 2, so that gap is about survivability, not damage. It belongs to the parked CP homework (§6).

**3. Overload value** (Lv 30, full tier-30 ★3 gear, CRIT ≈ 11, vs LUK 11–13 monsters, Fire Bolt Lv 5): about +1% damage at overMul 0.5 and ×1.3; +1.4% at overMul 1; +1.9% at overMul 2 with ×2.0 (earlier run of the same setup). With no gear CRIT, the chance is 0. In the game with CRIT 30.7 (LUK 99), an Overload hit did about 1.5 times the damage of a normal hit.

## 3b. Mana Flow (v20.6, from NIIQ)

| | |
|---|---|
| MAX Lv | 10 |
| ประเภท | Passive |
| รายละเอียด | ฝึกการไหลเวียน SP ทั่วทั้งร่างกาย ให้มีประสิทธิภาพสูงสุด |

| Lv | Max SP | SP regen | SP cost |
|---|---|---|---|
| 1 | +1% | +10% | −1% |
| 2 | +2% | +12% | −2% |
| 3 | +3% | +14% | −3% |
| 4 | +4% | +16% | −4% |
| 5 | +5% | +18% | −5% |
| 6 | +6% | +20% | −6% |
| 7 | +7% | +22% | −7% |
| 8 | +8% | +24% | −8% |
| 9 | +9% | +26% | −9% |
| 10 | **+12%** | **+30%** | **−12%** |

Pattern Lv 1–9: Max SP +Lv%, regen +(8 + 2 × Lv)%, cost −Lv%; Lv 10 is a jump. In code (`manaFlow()`): Max SP % multiplies the base Max SP (after INT, before flat gear SP); regen % multiplies natural SP regen; cost % lowers every skill's SP cost (rounded up). The old prototype (one level: regen +60%, cost −10%) is gone.

## 3c. Elemental Attunement (v20.6, from NIIQ)

| | |
|---|---|
| MAX Lv | 5 |
| ประเภท | Passive |
| รายละเอียด | เรียนรู้จุดอ่อนเกี่ยวกับธาตุหลักในจักรวาล |
| Per level | ตีจุดอ่อนธาตุแรงเพิ่มขึ้นอีก +5% |

⚠ Read as **cumulative**: the weakness multiplier is 1.5 + 0.05 × Lv (Lv 1 = 155%, Lv 5 = 175%, the same as the old one-level passive). Applies to the basic attack and every spell that hits a weakness.

## 3d. Overload Energy (v20.6, from NIIQ)

| | |
|---|---|
| MAX Lv | 5 |
| ประเภท | Buff |
| การใช้ | **Self Cast**: กดแล้วร่ายเลย ไม่ต้องเลือกเป้าหมาย (still has the cast time below) |
| เป้าหมาย | ตัวเอง และสมาชิกใน Party ทั้งหมดในระยะ 12 × 12 ช่องรอบตัวเอง (6 tiles each way, a square) |
| คูลดาวน์ | 60 s at every level |
| Global Delay | 1 s at every level |
| รายละเอียด | ตั้งสมาธิอันแน่วแน่ที่จะดึงทุกพลังของจักรวาล มาเพิ่มอัตราเกินพิกัดให้ตัวเองและเพื่อน |

| Lv | Overload Rate | Duration | Cast | SP |
|---|---|---|---|---|
| 1 | +1% | 20 s | 1.0 s | 50 |
| 2 | +2% | 40 s | 1.2 s | 65 |
| 3 | +3% | 60 s | 1.4 s | 80 |
| 4 | +4% | 80 s | 1.6 s | 95 |
| 5 | +5% | 120 s | 2.0 s | 110 |

SP = 35 + 15 × Lv (lowered by Mana Flow like every skill).

How it is built:
- The bonus is added to the base Overload Rate before the target's LUK and the skill's overMul: `max(0, CRIT + bonus − targetLUK/5) × overMul` (`COMBAT-FORMULAS.md` §3b). It does not raise physical CRIT.
- Self Cast (NIIQ: the spec's “Instant Cast” meant “press and it casts, no target needed”). The cast time in the table applies, shortened by DEX like every spell; the buff takes effect the moment the cast ends.
- Party members are simulated players (no combat stats yet), so the buff only works on the caster; party members in town within the 12 × 12 area get the visual effect. It will apply to them when party combat exists.
- Recasting refreshes the duration and replaces the bonus with the new level's.
- Idle casts it when the target is in range and the buff is not up. The simulator (CP, offline estimate) does the same at Lv 5.

Balance check (simulator, 3 seeds, 300 s, every skill and passive at max): Spellcaster kills −2 to −4% compared with v20.5 (Lv 10: 50 → 48.3; Lv 20: 46.7 → 45; Lv 30: 45.3 → 43.7; Lv 20 packs of 3: 80 → 78), no deaths either way, CP at Lv 30 1,006 → 1,017. The loss comes from the buff's cast + Global Delay and the weaker max Mana Flow regen (+30% instead of +60%).

## 4. Skill levels and skill points
**Decided (NIIQ):**
- Skill points come from **Job Lv**: 1 Job Lv = 1 skill point. At Job Lv 1 a character has none; **Job Lv 2 gives the first point**.
- **Every skill of every archetype, active or passive, is raised by hand by the player.** Nothing is learned for free.
- When the class changes (Beginner → archetype) Job Lv resets to 1, so the character starts with **no points** and must gain Job Lv first (`JOBS.md`).

**In the game now:** every skill starts at Lv 0 (not learned) and costs 1 point per level. Since v20.9 points are spent in the **Skills Tree** as a draft: tap a skill, plan levels with ◀ ▶, then **Learn** (Reset drops the draft; `UI-UX.md` §26). A skill at Lv 0 cannot be used (a toast says so; Idle skips it; its hotbar slot is greyed). A C1 class (Job Lv cap 50) gets 49 points in total; Beginner (cap 10) gets 9.
- **Fire Bolt** has Lv 1–10 (§3).
- **Overload Energy** has Lv 1–5 (§3d); **Mana Flow** Lv 1–10 and **Elemental Attunement** Lv 1–5 (§3b, §3c): the first passives with levels.
- **Every other skill has one level** (1 point to learn it, the prototype numbers) until its levels are designed. ⚠ NIIQ has not given per-level effects for them yet.
- **Passives** are learned the same way (1 point each) and only work once learned.
- **Beginner (v20.4):** a Beginner spends points only on **Basic Skill** (Lv 1 given, Lv 2–10 cost 1 point each). First Aid and Heavy Strike come from Basic Skill Lv 3 and Lv 4 and stay learned after the Archetype choice (`JOBS.md` §1b).

**⚠ Still open:** points reset (respec), whether unspent points carry over on class change (the answer so far is no, because Job Lv resets), the max level and per-level effect of every skill except Fire Bolt.

## 5. Hotbar
The player chooses, for each hotbar slot, **which skill and which level** goes in it. v20.9: in the Skills Tree, ◀ ▶ under a learned skill pick the level and dragging the tile puts that level on the slot (`UI-UX.md` §26). The Hotbar setup drop-downs were removed in v20.9. A slot filled with no level picked uses the highest level learned. A slot uses that level’s own SP cost, cast time and number of hits, and a level above the one learned is not possible. Example: Fire Bolt Lv 3 on slot 1 and Fire Bolt Lv 10 on slot 2. The 10 slots are free: a slot holds a skill or a usable item, dragged from the bag or the Skills Tree (`UI-UX.md` §25). The default layout puts skills on 1–7 and Fly Wing, Red Potion and Blue Potion on 8, 9 and 0. Auto-potion uses the slot that holds Red Potion (HP below 35%) or Blue Potion (SP below 15%); if no slot holds it, it does nothing.

**Decided:** Fire Bolt has a 0 s cooldown, so levels do not block each other. After Lv 2 the player can cast Lv 10 straight away; only the Global Delay (1.4 s) has to pass.

**Built as (⚠ assumption, not stated):** Idle (auto-hunt) uses the level set on the **first hotbar slot that holds the skill**, and skips skills that are not learned. If NIIQ prefers “always the highest learned level”, it is a one-line change.

**⚠ Not decided:** whether the two potion slots and the wing slot stay fixed.

## 6. Parked (homework for NIIQ)
**CP.** With a full set of tier-appropriate gear the Spellcaster is far ahead of the other roles in the simulator, **before and after** this draft. Full set, base rolls, no affixes: Lv 30 with ★2 gear, CP 20,761 vs Fighter 7,241 / Ranger 8,348 / Supporter 7,923; Lv 50 with ★3 gear, CP 101,558 vs 28,408 / 40,460 / 32,479. Kills stay close because respawn and travel time cap them.

Cause: every gear slot adds `m × 0.35` to the primary stat, and MATK has an `⌊INT/5⌋²` term (STR and DEX use `⌊/10⌋²`). At INT 225, max MATK is about 2,250. The staff’s `m × 2.2` (119 at tier 30 ★2) is only about 5% on top of that, so weaponMATK does not cause this. It matters for the CP gates (Geosyncline 2,000, Ruins 3,000).

New side effect of stopping fireballs when the target dies: CP counts damage dealt, and the old simulator counted overkill. With 2 common pieces the Spellcaster’s CP falls from 3,126 (old prototype) to about 2,140 with Fire Bolt Lv 5 and the staff × 1 (3,515 vs 6,698 with 5 pieces). Note that the CP simulation (and the Idle offline estimate) uses Fire Bolt Lv 5 and counts every skill and passive as learned. Nothing was changed for this.

## 7. ⚠ Open items
1. Max level and per-level effects of every skill except Fire Bolt, Overload Energy, Mana Flow and Elemental Attunement (now one level each).
1b. Overload Energy: party members without combat stats (§3d).
2. Potion and wing slots (§5).
3. Respec (reset skill points).
4. Global Delay for the other skills, and whether it really starts when the cast ends (it does in the game).
5. Fireball timing assumptions and the SP refund (§3).
6. Overload strength, the *Crit damage* ability (not applied to Overload in the game) and the label (OVERLOAD! / เกินพิกัด!, orange) (`COMBAT-FORMULAS.md` §3b).
7. Supporter staff: left as it is (+10% MATK, no weaponMATK) until classes are split.
8. CP and the gates (§6).
