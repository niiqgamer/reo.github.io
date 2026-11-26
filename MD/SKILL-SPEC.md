# Skill Spec: the standard for writing a skill (DRAFT)

> Part of the REO docs. Combat numbers: `COMBAT-FORMULAS.md`. Kits per archetype: `ARCHETYPES.md`.
> Status: draft from NIIQ. Fire Bolt (§3) is the first skill written to this standard; v20.18 adds Freezer, Lightning Spear and Petrifaction (§3e–3h). These are skills of the **archetype**; classes are not split yet. **Fire Bolt, skill levels, the hotbar level choice, Global Delay, weaponMATK and Overload are in the game (v20 build).** Items marked ⚠ are assumptions or open questions.

## 1. Fields every skill states

| Field | Meaning |
|---|---|
| MAX Lv | Highest skill level |
| ประเภท | Active or Passive |
| Type | Physical, Magic or Support |
| เป้าหมาย | Target (for example one enemy) and the **hit type** (§2) |
| การใช้ (Targeting) | **Self Cast** (กดแล้วร่ายเลย ไม่ต้องเลือกเป้าหมาย; may still have a cast time) or **Target Cast** (must pick an enemy or ally first). Do not write “Instant Cast”: in MMOs it means *no cast time* |
| ระยะห่างระหว่างฮิต | For multi-hit skills: seconds between two hits, and what happens if the target dies in the middle |
| ระยะ | Maximum range in tiles, counted from the caster as a **square** like RO (v22c): range 9 reaches every tile of the 19 × 19 square round the player, diagonals as far as straight lines. An area written A × A (3 × 3, 5 × 5, 7 × 7) is the whole width |
| เงื่อนไขก่อนเรียน | Prerequisite skills. “None” means it can be learned right away |
| อัตราเกินพิกัด | `overMul` for magic (`COMBAT-FORMULAS.md` §3b). **Not stated = 0: the skill cannot Overload** |
| ร่ายแปรผัน (VCT) | Variable cast time in seconds; DEX and INT shorten it (`COMBAT-FORMULAS.md` §2b). Not stated = 0 |
| ร่ายคงที่ (FCT) | Fixed cast time in seconds; only gear shortens it. Not stated = 0 |
| คูลดาวน์ (Cooldown) | How long **this same skill** is locked after it is used. Starts when the **cast ends** (in the game since v20.9; before that it started with the cast). Only gear shortens it. 0 s means it can be cast again at once (only the Global Delay still applies) |
| Global Delay | The delay between this skill and the **next skill** (any skill). Each skill states its own value. Starts when the cast ends and leaves basic attacks free. Only gear shortens it |
| รายละเอียด | What the skill does, with the % of ATK or MATK |
| Per level | What changes at each level: hits, SP, VCT / FCT |

v20.18: NIIQ now writes the fields in English. They map to the rows above: **Skill Requirement** = เงื่อนไขก่อนเรียน, **Skill Form** = ประเภท + การใช้ (Active / Self Cast), **Type** may add **Debuff** or **Ground Magic**, **Elements** = the element, **Overload Rate** True / False = can Overload or not, **Overload Damage** (⚠ see §3), **Gaps** = ระยะห่างระหว่างฮิต, **FCT / VCT / Global Delay / Skill Cooldown** per level.

## 2. Hit types

| Cast | Real hits | Damage rolls | Shown as | Name |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 hit | **Single hit** |
| 1 | 1 | 1 | several hits | **Visual multi-hit** (split display) |
| 1 | several | 1 | per hit | **Shared-roll multi-hit** |
| 1 | several | per hit | per hit | **True multi-hit** (per-hit roll) |

Today’s code already rolls damage per hit (a skill with `hits` loops and calls the damage function once per hit), but it resolves all hits at the same instant. Fire Bolt will be the first skill with a gap between hits.

## 3. Fire Bolt (v20.18, from NIIQ: Lv 1–5; splash + Burning v21e)

| | |
|---|---|
| MAX Lv | 5 |
| Skill Requirement | – |
| Skill Form | Active, Target Cast |
| Type | Magic |
| Target | 1 enemy, **True multi-hit**, fireballs dropped **one at a time**, **Splash Damage** (v21e) |
| Type (v21e) | Magic, Debuff (Burning) |
| Elements | Fire |
| Overload Rate | True (⚠ the game keeps `overMul` 0.5 on the chance, see below) |
| Overload Damage | ×0.5 (⚠ see below) |
| ระยะ | 7 tiles |
| Global Delay | **1 s** at every level |
| Skill Cooldown | **0 s** at every level |
| Detail | โจมตีศัตรูด้วยลูกไฟ สร้างความเสียหายทางเวทมนตร์ธาตุ Fire เท่ากับ MATK 100% → **120% MATK per fireball** (NIIQ: the level table is right, "100%" was a typo) เมื่อลูกไฟโดนเป้าหมายจะ Splash Damage Fire รอบเป้าหมายกว้าง 3x3 ช่อง ด้วย MATK 50% และสร้างผลทำให้ติดสถานะ **Burning (ติดไฟ)** ที่ลดความต้านทานต่อธาตุ Water ลง 50% เพิ่มเติม โอกาสและระยะเวลาติดสถานะ Burning เปลี่ยนไปตามเลเวล พลังป้องกันทางเวทมนตร์ และ LUK ของเป้าหมาย |

| Lv | Fireballs | MATK in total | Burning chance | Gaps | FCT | VCT | SP |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 120% | 30% | 0 s | 0.5 s | 0 s | 12 |
| 2 | 3 | 360% | 40% | 0.3 s | 0.6 s | 0 s | 17 |
| 3 | 5 | 600% | 50% | 0.3 s | 0.7 s | 0 s | 22 |
| 4 | 7 | 840% | 60% | 0.2 s | 0.8 s | 0 s | 27 |
| 5 | 10 | 1,200% | 70% | 0.2 s | 1.0 s | 0 s | 40 |

- **Splash (v21e):** every fireball that hits a live target also hits every *other* monster in a 3 × 3 square round it (1.5 tiles each way) for 50% of the fireball's MATK (60% MATK), Fire, no Overload. Fireballs that land after the target died do not splash.
- **Burning (v21e):** rolled **once per cast**, on the first fireball that hits (Lv 1–5: 30–70%). See §3h. It is rolled once per cast, not per fireball (confirmed by NIIQ).

- The cast is all **FCT**, so DEX and INT do not shorten it (only gear `fct` does).
- **Every fireball always falls**, even if the target dies first (NIIQ, v20.18). Fireballs that land after the target died hit nothing (a small burst on the spot). SP is not refunded.
- No basic-attack bolt flies from the caster's hand the moment a spell goes off: casting a magic skill restarts the basic-attack timer (NIIQ, v20.18).
- The first fireball is released the moment the cast ends and the next ones follow every gap; a fireball takes (gap − 0.02) s to fall (Lv 1: 0.28 s) and deals its damage when it lands. The caster is free to act while the volley falls.
- ⚠ **Overload fields.** The spec now says “Overload Rate: True” and “Overload Damage: ×0.5”. The game keeps what it did before: the skill can Overload, the chance is `(CRIT + bonus − LUK/5) × 0.5` and an Overload hit does ×1.3. If “×0.5” is meant for the damage instead (for example half the Overload bonus, +15% instead of +30%), it is a one-line change.

**Before v20.18:** Lv 1–10, Lv N fireballs of 100% MATK, SP 12 + 2 × (Lv − 1), VCT 0.5 + 0.3 × (Lv − 1) s, Global Delay 1.4 s, fireballs stopped when the target died. Before that, the prototype: 3 × 100% MATK, SP 12, cast 1.0 s, CD 0.5 s.

### Balance check of the v20 draft (historical: Fire Bolt Lv 1–10, before v20.18)
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

| Lv | Overload Rate | Duration | VCT (FCT 0) | SP |
|---|---|---|---|---|
| 1 | +1% | 20 s | 1.0 s | 50 |
| 2 | +2% | 40 s | 1.2 s | 65 |
| 3 | +3% | 60 s | 1.4 s | 80 |
| 4 | +4% | 80 s | 1.6 s | 95 |
| 5 | +5% | 120 s | 2.0 s | 110 |

SP = 35 + 15 × Lv (lowered by Mana Flow like every skill).

How it is built:
- The bonus is added to the base Overload Rate before the target's LUK and the skill's overMul: `max(0, CRIT + bonus − targetLUK/5) × overMul` (`COMBAT-FORMULAS.md` §3b). It does not raise physical CRIT.
- Self Cast (NIIQ: the spec's “Instant Cast” meant “press and it casts, no target needed”). The VCT in the table applies, shortened by DEX and INT like every spell (FCT 0); the buff takes effect the moment the cast ends.
- Party members are simulated players (no combat stats yet), so the buff only works on the caster; party members in town within the 12 × 12 area get the visual effect. It will apply to them when party combat exists.
- Recasting refreshes the duration and replaces the bonus with the new level's.
- Idle casts it when the target is in range and the buff is not up. The simulator (CP, offline estimate) does the same at Lv 5.

Balance check (simulator, 3 seeds, 300 s, every skill and passive at max): Spellcaster kills −2 to −4% compared with v20.5 (Lv 10: 50 → 48.3; Lv 20: 46.7 → 45; Lv 30: 45.3 → 43.7; Lv 20 packs of 3: 80 → 78), no deaths either way, CP at Lv 30 1,006 → 1,017. The loss comes from the buff's cast + Global Delay and the weaker max Mana Flow regen (+30% instead of +60%).

## 3e. Freezer (v20.18, from NIIQ; replaces Frost Nova)

| | |
|---|---|
| MAX Lv | 5 |
| Skill Requirement | – |
| Skill Form | Active, Target Cast |
| Type | Magic, Debuff |
| Target | 1 enemy, **Splash Damage** while it is Frozen (v21e) |
| Elements | Water |
| Overload Rate | False (cannot Overload) |
| ระยะ | 7 tiles |
| FCT / VCT | 0.16 s / 0.64 s at every level |
| Global Delay | 0.5 s · Cooldown 0 s |
| SP | 25 at every level |
| Detail | ยึดจับและเหนี่ยวนำด้วยพลังน้ำแข็ง สร้างความเสียหายทางเวทมนตร์ธาตุ Water ต่อศัตรู 1 ตัว และสร้างผลทำให้ติดสถานะ **Freeze (แช่แข็ง)** ที่ลดความต้านทานต่อธาตุ Wind ลง 50% เพิ่มเติม เมื่อเป้าหมายติดสถานะ Freeze จะ Splash Damage Water รอบเป้าหมายกว้าง 3x3 ช่อง ด้วย MATK 50% โอกาสและระยะเวลาติดสถานะเปลี่ยนไปตามเลเวล พลังป้องกันทางเวทมนตร์ และ LUK ของเป้าหมาย |

| Lv | MATK | Freeze chance |
|---|---|---|
| 1 | 110% | 35% |
| 2 | 130% | 45% |
| 3 | 150% | 55% |
| 4 | 170% | 65% |
| 5 | 200% | 75% |

- **Splash (v21e):** when the target is Frozen after the hit (newly, or still frozen from before), every *other* monster in a 3 × 3 square round it takes 50% of Freezer's MATK as Water (Lv 5: 100% MATK).

## 3f. Lightning Spear (v20.18, from NIIQ)

| | |
|---|---|
| MAX Lv | 5 |
| Skill Requirement | – |
| Skill Form | Active, Target Cast (aimed at an enemy) |
| Type | **Ground Magic** |
| Target | Enemies in a **5 × 5** tile square, **True multi-hit**: each spear hits every enemy inside |
| Elements | Wind |
| Overload Rate | True · Overload Damage ×0.5 (⚠ same reading as Fire Bolt, §3) |
| ระยะ | 7 tiles |
| Gaps | 0.1 s |
| FCT | 1.5 s at every level |
| Global Delay | 2 s · Cooldown 0 s |
| Detail | สร้างหอกแห่งสายฟ้า และฟาดลงมาที่พื้นที่อย่างรุนแรง สร้างความเสียหายทางเวทมนตร์ธาตุ Wind เป็นวงกว้าง 5x5 ช่อง |

| Lv | Spears | MATK per spear | VCT | SP |
|---|---|---|---|---|
| 1 | 2 | 100% | 1.0 s | 30 |
| 2 | 4 | 100% | 1.2 s | 42 |
| 3 | 6 | 100% | 1.4 s | 54 |
| 4 | 8 | 100% | 1.6 s | 66 |
| 5 | 10 | 100% | 1.8 s | 78 |

- ⚠ Ground magic is built as: the 5 × 5 square is centred where the target stood **when the cast started** and stays there; monsters that walk out during the cast are missed. The spears fall one by one, 0.1 s apart, at random points inside the square, and every spear hits **every** enemy inside at that moment. The square is drawn on the ground while the spears fall.

## 3g. Petrifaction (v20.18, from NIIQ; replaces Stone Spike)

| | |
|---|---|
| MAX Lv | 5 |
| Skill Requirement | – |
| Skill Form | **Self Cast** |
| Type | Magic, Debuff |
| Target | Enemies in the **7 × 7** tile square around the caster |
| Elements | Earth |
| Overload Rate | False (cannot Overload) |
| FCT / VCT | 0.2 s / 0.8 s at every level |
| Global Delay | 0 s · Cooldown 0 s |
| Detail | เรียนรู้กระบวนการทางธรณีศาสตร์ ปรับมวลสารทุกสรรพสิ่งให้เป็นซากฟอสซิล สร้างความเสียหายทางเวทมนตร์ธาตุ Earth ต่อศัตรูโดยรอบ 7x7 รอบตัวเอง และสร้างผลทำให้ติดสถานะ **Petrifaction (แข็งเป็นหิน)** ที่ลดความต้านทานต่อธาตุ Fire ลง 50% เพิ่มเติม โอกาสและระยะเวลาติดสถานะเปลี่ยนไปตามเลเวล พลังป้องกันทางเวทมนตร์ และ LUK ของเป้าหมาย |

| Lv | MATK | Petrifaction chance | SP |
|---|---|---|---|
| 1 | 75% | 30% | 25 |
| 2 | 80% | 40% | 27 |
| 3 | 85% | 55% | 28 |
| 4 | 90% | 65% | 32 |
| 5 | 100% | 75% | 35 |

## 3h. Freeze, Petrifaction and Burning (status debuffs, v20.18; Burning v21e)
- A Frozen or Petrified monster **cannot move or attack** until it ends (it takes damage normally; damage does not break it). A **Burning** monster keeps moving and attacking, but **burns for 10% MATK Fire every second** (`STATUS.brn.dot`, no Overload, MDEF and soft MDEF apply as for any magic hit; one last tick when it ends). **A Freeze puts the fire out** (Burning ends, a puff of steam), so Fire Bolt → Freezer trades the burn for the Freeze (NIIQ, v21e).
- **Freeze:** Wind hits it +50%. **Petrifaction:** Fire hits it +50%. **Burning:** Water hits it +50%. So the spells feed each other: Fire Bolt → Freezer → Lightning Spear, Petrifaction → Fire Bolt. Built as **+0.5 added to the element multiplier** (`COMBAT-FORMULAS.md` §5): for example a Water monster (weak to Wind) that is Frozen takes Wind at 1.5 + 0.5 = 2.0 (+ Attunement).
- ⚠ **Not given yet, placeholders in the game:**
  - Chance = `skill chance × (1 − target MDEF%) − target LUK / 5` (in % points).
  - Time = `3 / 4 / 5 / 6 / 7 s` by skill level (Burning too), `× (1 − target MDEF%)`.
  - Bosses are immune (as they already are to stun). Elites are not.
- Looks (v21e, `UI-UX.md` §29): Freeze turns the monster icy blue inside a block of ice crystals with frost on the ground; Petrifaction turns it to grey cracked stone with rubble; Burning tints it orange with flames, embers and smoke; a stun (Crushing Blow) shows stars circling the head. The pose stops while Frozen or Petrified, and the ice / stone shatters when it ends. The text แช่แข็ง! / แข็งเป็นหิน! / ติดไฟ! pops over it.

### Balance check (simulator, v21e)
v21e (Fire Bolt splash + Burning, Freezer splash), same method as below, seed 3: **CP Lv 10 / 20 / 30 = 233 / 546 / 971** with the Burning DoT (v20.18: 236 / 496 / 922). Lv 30 vs Field 03 monsters, 300 s: 50 kills alone (v20.18: 51), **108** in packs of 3 (v20.18: 105). The AI values Burning at a quarter of a Freeze (it does not stop the monster), and a spell that only gives Burning still needs a weakness to be cast outside a pack.

### Balance check (simulator, v20.18)
Simulator on the game's combat module, 300 s, 3 seeds, auto stats, every skill and passive learned, no gear. **The simulator now picks the level of each spell itself** (`autoLv`): the hits that can still land on the HP left, per second while SP is above half and per SP below that. Kills · deaths (Fighter for scale).

| | v20.17 Spellcaster | v20.18 Spellcaster | Fighter |
|---|---|---|---|
| Lv 10, Field 01 | 52 · 0 | 52.3 · 0 | 63 · 0 |
| Lv 20, Field 02 | 48.3 · 0 | 49 · 0 | 60 · 0 |
| Lv 30, Field 03 | 48.3 · 0 | 45 · 0 | 49.3 · 0 |
| Lv 20, packs of 3 | 87 · 0 | **100** · 0 | 100 · 0 |
| Lv 35, Ruins Elites | 0 · 8 | 2.3 · 3.3 | 3.3 · 3 |
| Lv 30, Geosyncline | 16.7 · 2 | **25** · 1 | 16.3 · 0 |
| **CP, Lv 30, no gear** | **1,158** | **922** (−20%) | 1,576 |

With every spell fixed at Lv 5 (no level choice) CP would be 724: Fire Bolt Lv 5 spends 40 SP and drops 10 fireballs on monsters that die after 2–3, so SP runs out. The CP drop matters for the gates (Geosyncline 2,000, Ruins 3,000; `CORE-LOOP.md`).

## 3i. Ranger skills (v21f, from NIIQ)
Five new Ranger skills, written to this standard. **v22b: they are the whole Ranger tree**; the prototype skills (Double Strafe, Arrow Shower, Piercing Shot, Evasive Leap, Eagle Eye, Steady Aim) are removed (NIIQ). Old saves get their points back and those hotbar slots are cleared. **Skill requirements** are new in v21f (`SKREQ`): the Skills Tree does not let a skill be learned (or drafted) until the skills it needs reach their level; a draft counts. If a requirement is lost (points taken back), the skill that needed it goes back to Lv 0 and its points return.

## 3j. No Arrow (passive)
| | |
|---|---|
| MAX Lv | 5 |
| Skill Requirement | – |
| Skill Form | Passive |
| Detail | ลูกธนูที่ทำมาจากแร่ Rare Earth นั้นหายากยิ่ง เหล่าบรรพบุรุษแห่ง Ranger จึงได้เล่นแร่แปรธาตุ จนเจอวิธีการที่จะยิงลูกธนูแต่ละดอกออกไป โดยไม่ต้องถือลูกธนูเลยสักดอก นั่นคือการยิงออกไปด้วยลูกธนู Scandium |

| Lv | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Scandium per arrow (v22d) | 20 | 16 | 12 | 8 | 4 |
| (v21f–v22c) | 20 | 18 | 15 | 13 | 10 |

Built as (`NA_SC`, `payArrows`):
- Every arrow that **leaves the bow** costs Scandium: a basic attack 1, Double Strafe 2, Arrow Shower / Piercing Shot / Aim Strike / Aiming Shower 1. The extra arrows of an Aim Strike split come out of the same arrow and cost nothing more (⚠ assumption).
- Not enough Scandium = the shot does not happen (basic attack or skill; no SP is spent on a skill); a toast says so (at most every 3 s).
- ⚠ **A Ranger without No Arrow shoots for free.** Arrow items do not exist yet, so there is nothing to spend. Once arrows exist, a Ranger without No Arrow should need them.
- Idle: the session summary shows Scandium net of arrows. Offline idle subtracts the arrows the simulator shot (`aph`, arrows per hour) × the cost; the wallet never goes below 0.

## 3k. Ranger Mastery (passive)
| | |
|---|---|
| MAX Lv | 10 |
| Skill Requirement | No Arrow Lv 1 |
| Skill Form | Passive |
| Detail | เรียนรู้สัญชาตญาณแห่งนักล่า เพิ่มความเชี่ยวชาญในการถือธนู ความแม่นยำ และการหลบหลีก |
| Per level | Lv N: **DEX +N, HIT +N, AGI +N** (Lv 10: +10 each). **v22d: range +1 tile at Lv 1, 6 and 10** (Lv 1–5 +1, Lv 6–9 +2, Lv 10 +3: range 9 → 12) |

Built as stat points on top of the character's DEX and AGI (they count for ATK, ASPD, FLEE, cast time) plus flat HIT.

## 3l. Focusing
| | |
|---|---|
| MAX Lv | 10 |
| Skill Requirement | No Arrow Lv 3 |
| Skill Form | Self Cast · Type Buff, Support · Target Self |
| FCT / VCT / Global Delay / Cooldown | not given = 0 |
| Detail | ตั้งสมาธิให้แน่วแน่ เพ่งกระแสจิตทะลุมวลอวกาศ เพื่อเพิ่มความสามารถให้ตัวเอง |

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| DEX, AGI | +3% | +4% | +5% | +6% | +7% | +8% | +9% | +10% | +11% | +12% |
| Time | 60 s | 80 s | 100 s | 120 s | 140 s | 160 s | 180 s | 200 s | 220 s | 240 s |
| SP | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 65 | 70 |

The % multiplies DEX and AGI after Ranger Mastery (rounded down). Recasting refreshes the time and takes the new level's %. Idle keeps it up.

## 3m. Aim Strike (v21h: an attack skill again, damage shared)
| | |
|---|---|
| MAX Lv | 10 |
| Skill Requirement | No Arrow Lv 5 |
| Skill Form | Active, Target Cast · Type Range (physical) |
| Target | 1 enemy, Multi-hit (split arrows), Splash Damage |
| Critical Rate | ×0.5 (built as **crit chance ×0.5**; ⚠) |
| Gaps 0.1 s · **FCT 0.5 s · VCT 0.5 s · Global Delay 1 s · Cooldown 1 s** (every level; v22a, v21h had VCT 1 s, GD 2 s, CD 2 s) |
| Detail | พลังที่จะทำให้ Ranger ง้างธนูได้อย่างอย่างสุดกำลัง และทำให้ปล่อยพลังทั้งหมดไปที่ลูกศรที่พุ่งออกไปได้ ในบางจังหวะ มีโอกาสที่ลูกธนูดอกนั้น จะแยกตัวออกมาสร้างความเสียหายให้เป้าหมายมากกว่า 1 ดอกด้วย และเมื่อยิงถูกเป้าหมาย แรงอัดอากาศทำหน้าที่อีกครั้ง Splash Damage 50% ออกไปอีก 3x3 ช่อง |

| Lv | ATK in total | Split chance | Arrows when split | SP (v22a: 10 at every level; v21h 12–20) |
|---|---|---|---|---|
| 1 | 100% | 20% | 2 | 10 |
| 2 | 110% | 22% | 2 | 10 |
| 3 | 120% | 24% | 2 | 10 |
| 4 | 130% | 26% | 2 | 10 |
| 5 | 140% | 28% | 2 | 10 |
| 6 | 150% | 30% | 3 | 10 |
| 7 | 160% | 32% | 3 | 10 |
| 8 | 170% | 34% | 3 | 10 |
| 9 | 180% | 36% | 3 | 10 |
| 10 | 200% | 38% | 3 | 10 |

Built as (`aimStrike`):
- One arrow of the "ATK in total" %. ⚠ **"in total" is read as shared**: when the arrow splits, the N arrows split that total between them (Lv 10, split into 3: 66.7% ATK each). So a split does not raise the total; it spreads it over more hits (each arrow rolls its own crit at ×0.5 and its own splash). The split is rolled once per cast.
- **Splash:** every arrow that hits does 50% of its share to every other monster in a 3 × 3 square round the target; splash cannot crit.
- The text says "ยิงธรรมดามีโอกาส…" but the skill form is Active, so the split is a property of the skill's own arrow, not of the basic shots (⚠).
- The cast (0.5 s FCT + 0.5 s VCT, VCT shortened by DEX: about 0.8 s at Lv 30) stops basic attacks while it runs, like any cast.
- Idle / simulator AI (v22a): Aim Strike comes first when 2+ monsters are close (splash); against one target it is used after Double Strafe, which gives more damage per SP (250% against 200% for the same 10 SP, and Double Strafe has no cast).
- History: v21f attack skill (each arrow full %, GD 0.1 s: ~9,000 damage burst in 1 s); v21g Self Cast buff on basic shots (Lv 10 ≈ 6× a basic shot, Ruins DPS 407). v21h removes both.

## 3n. Aiming Shower
| | |
|---|---|
| MAX Lv | 10 |
| Skill Requirement | No Arrow Lv 5 |
| Skill Form | Active, Target Cast · Type Range (physical) |
| Target | 1 enemy |
| Critical Rate | No |
| **FCT 0.5 s · VCT 0.5 s · Global Delay 0.1 s · Cooldown 1 s** (v22a; v21h CD 2 s; v21f FCT 0.1, CD 0) · SP 20 (every level) |
| Detail | ยิงลูกธนู 1 ดอกออกไปผลักเป้าหมายให้ถอยหลังไป 2 ช่อง (สามารถใช้กับบอสได้) |

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ATK | 160% | 170% | 180% | 190% | 200% | 210% | 220% | 230% | 240% | 250% |

The push is straight away from the Ranger, 2 tiles, as a slide (12 tiles/s) that stops at a wall; bosses and Elites too. ⚠ "ATK +160%" read as 160% ATK. Idle (built-in choice) uses it when a monster is within 2.5 tiles.

### Balance check (simulator, v22a)
Game combat module in Node, 300 s, seeds 1–3, auto stats, no gear; the simulator counts **every** skill at max level (49 points cannot really buy all of them: the new five need 45). Kills · DPS · deaths. "Old" = v21e Ranger.

| | Fighter | Ranger old | v21f | v21g (buff) | v21h | **Ranger v22a** | Spellcaster |
|---|---|---|---|---|---|---|---|
| Lv 10, Field 01 | 59.3 · 46 | 54.0 · 39 | 58.7 · 43 | 58.7 · 44 | 58.0 · 43 | 58.7 · 44 | 47.7 · 26 |
| Lv 20, Field 02 | 53.3 · 75 | 50.0 · 67 | 51.3 · 76 | 50.7 · 80 | 49.7 · 73 | 50.7 · 77 | 46.0 · 53 |
| Lv 30, Field 03 | 42.3 · 130 | 39.7 · 116 | 46.0 · 136 | 49.0 · 148 | 43.0 · 130 | **44.0 · 136** | 42.0 · 117 |
| Lv 20, packs of 3 | 87 · 111 | 69 · 89 · 1 d | 83 · 102 | 83 · 103 | 82 · 101 | 84 · 101 | 108 · 123 |
| Lv 30, Geosyncline | 16.3 · 146 | 16.0 · 148 · 2 d | 18.7 · 182 · 1.7 d | 28.7 · 256 · 1 d | 15.7 · 156 · 1.7 d | **17.7 · 174 · 1.3 d** | 25.0 · 218 · 1 d |
| Lv 35, Ruins | 12.0 · 181 · 1 d | 13.0 · 192 · 3 d | 15.7 · 237 · 3 d | 28.0 · 407 · 1 d | 10.3 · 185 · 3 d | **12.0 · 200 · 3 d** | 13.7 · 200 · 1 d |
| **CP Lv 10 / 20 / 30** | 598 / 1,090 / 1,576 | 457 / 861 / 1,354 | 640 / 1,065 / 1,614 | 654 / 1,056 / 1,996 | 637 / 1,023 / 1,708 | **656 / 1,044 / 1,761** | 233 / 546 / 971 |

Gain by skill (Lv 35 Ruins DPS): old 192 → +Ranger Mastery 221 → +Focusing 220 → **+Aim Strike 215** → +Aiming Shower 200.

**v22a is balanced.** The Ranger sits level with the Fighter and with the Spellcaster on the Ruins (CP Lv 30 1,761, Ruins DPS 200). The shorter cast and 1 s delay alone barely moved the numbers, because the Ranger runs out of SP before it runs out of time (~1.9 SP/s regen at Lv 30); the AI order (Double Strafe before Aim Strike on one target) and **SP 20 → 10** did. Against one target Aim Strike is now close to just shooting (220 → 215 on the Ruins); it gains on packs through the splash. Aiming Shower costs a little DPS on the Ruins because the AI also spends 20 SP to push back every monster that comes close; that buys safety, not damage.

### Balance check (simulator, v22b: old Ranger skills removed)
Same method. The Ranger loses the distance bonus (+2% per tile beyond 3, up to +18%), range 12 → 9, +10 HIT, +5% crit, Double Strafe and Piercing Shot.

| | Fighter | Ranger v22a | **Ranger v22b** | Spellcaster |
|---|---|---|---|---|
| Lv 10, Field 01 | 59.3 · 46 | 58.7 · 44 | **52.0 · 32** | 47.7 · 26 |
| Lv 20, Field 02 | 53.3 · 75 | 50.7 · 77 | **44.0 · 55** | 46.0 · 53 |
| Lv 30, Field 03 | 42.3 · 130 | 44.0 · 136 | **34.3 · 99** | 42.0 · 117 |
| Lv 20, packs of 3 | 87 · 111 | 84 · 101 | **85 · 98** | 108 · 123 |
| Lv 30, Geosyncline | 16.3 · 146 | 17.7 · 174 · 1.3 d | **13.0 · 125 · 2 d** | 25.0 · 218 · 1 d |
| Lv 35, Ruins | 12.0 · 181 · 1 d | 12.0 · 200 · 3 d | **7.3 · 138 · 3.3 d** | 13.7 · 200 · 1 d |
| **CP Lv 10 / 20 / 30** | 598 / 1,090 / 1,576 | 656 / 1,044 / 1,761 | **510 / 789 / 1,196** | 233 / 546 / 971 |

**⚠ v22b leaves the Ranger weaker:** CP Lv 30 −32% (1,761 → 1,196; Fighter 1,576), Ruins DPS 200 → 138. Only packs hold up (splash). Scandium also gets worse, because more arrows are needed per kill (table below). Open for NIIQ: give some of it back (for example base range 12, the distance bonus as part of Ranger Mastery, or more ATK on Aim Strike).

### Balance check (simulator, v22d)
v22d changes (NIIQ): No Arrow 20 / 16 / 12 / 8 / 4 Sc per arrow; Ranger Mastery range +1 at Lv 1, 6, 10 (range 12 at Lv 10, the range Eagle Eye used to give). The spec sheet for this pass listed Aim Strike at SP 12–20; the game keeps **SP 10** (NIIQ's previous decision) until NIIQ confirms. With SP 12–20 the Ranger is weaker still: CP Lv 30 1,145, Ruins 5.0 kills · 123 DPS · 4 deaths, packs of 3 68 kills · 82 DPS.

Damage does not move (CP Lv 10 / 20 / 30 = 510 / 789 / 1,196, same as v22b): the simulator places a ranged fighter at min(range, 8) tiles, so range above 8 does not show there. In the game, range 12 gives about 1.3 more tiles of free shots before a monster arrives than range 9 did with the old distance bonus gone. **⚠ The Ranger stays about 24% below the Fighter (CP 1,196 vs 1,576; Ruins DPS 138 vs 181)**: what the old kit gave and v22d does not give back is the distance bonus (+2% per tile beyond 3, up to +18%), +5% crit, and Double Strafe / Piercing Shot as SP-cheap damage.

**Scandium is now positive everywhere at No Arrow Lv 5** (4 Sc per arrow): net per hour Field 01 +1.5k, Field 02 +4.2k, Field 03 +18.6k, Geosyncline +14.9k, Ruins +11.8k. At Lv 1 (20 Sc) it is still negative everywhere (table below).

**⚠ Scandium cost against income** (simulator, 600 s × 3 seeds, kills and arrows per hour; income = average monster Scandium, no drops sold):

| Map (Lv) | Kills/h | Arrows/h (per kill) | Income Sc/h | Net at 10 Sc/arrow (No Arrow 5) | Net at 20 Sc/arrow (No Arrow 1) |
|---|---|---|---|---|---|
| Field 01 (10) | 620 | 1,220 (2.0) | 6,407 | **−5,793** | **−17,993** |
| Field 02 (20) | 504 | 1,756 (3.5) | 11,256 | **−6,304** | **−23,864** |
| Field 03 (30) | 392 | 2,414 (6.2) | 28,224 | +4,084 | **−20,056** |
| Geosyncline (30) | 152 | 3,116 (20.5) | 27,360 | **−3,800** | **−34,960** |
| Ruins (35) | 82 | 3,022 (36.9) | 23,917 | **−6,303** | **−36,523** |

(v22b, old Ranger skills removed.) So a Ranger with No Arrow loses Scandium on Field 01–02 even at Lv 5, only just breaks even on the Geosyncline and Ruins at Lv 5, and loses on every map at Lv 1. Every other archetype keeps all of it. See `ECONOMY.md`.

## 3o. Fighter skills (v22e, from NIIQ)
Five Fighter skills. Weapon Mastery becomes **Weapons Mastery** (Lv 1–10). **v22g:** the old Fighter skills (Power Strike, Whirlwind Cleave, Crushing Blow, War Cry, Iron Body) and Momentum are removed (old saves get the points back; their hotbar slots clear). Forbear needs Gaslighting Lv 3 (`SKREQ`); the others need nothing. The five cost 50 points at max; a C1 Fighter has 49.

## 3p. Weapons Mastery (passive, Lv 1–10)
Master the knife and the sword and draw out what the weapon holds: **ATK +4 per level** (Lv 10: +40) while a knife or sword is held. The game has no knife / sword weapon types yet, so every Fighter weapon counts. Replaces the old Weapon Mastery (+20 ATK +5 HIT, one level): an old save keeps its one level (+4 ATK) and can raise it. `PASSIVE.weapon_mastery.atk` = 4 per level; the mastery ATK goes into `(statusATK + weapon + mastery)` (`COMBAT-FORMULAS.md` §2).

## 3q. Shield Mastery (passive, Lv 1–10)
A stronger guard for a slower swing, **only while a shield is worn** (`S.equip.shield`; the simulator assumes one: the Fighter set has a Tower Shield).

| Lv | STR / VIT | DEF | Attack speed |
|---|---|---|---|
| N | +N / +N | +2% × N (soft and hard DEF × (1 + 0.02N), hard DEF cap 70%) | −2% × N (attack delay × (1 + 0.02N)) |
| 10 | +10 / +10 | +20% | −20% |

## 3r. Timber!! (Active, Melee, Lv 1–10)
One blow on the target as heavy as a giant log falling on its head. **20% chance to Stun it for 3 s** (bosses are immune). The shock spreads: **70% ATK on every other enemy in the 3 × 3 square round the target**. Cannot crit. HIT bonus is added to the hit formula: `80 + HIT + bonus − FLEE`.

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ATK | 130% | 160% | 190% | 220% | 250% | 280% | 310% | 340% | 370% | 400% |
| HIT bonus | +5 | +10 | +15 | +20 | +25 | +30 | +35 | +40 | +45 | +50 |
| SP | 8 | 8 | 8 | 8 | 8 | 15 | 15 | 15 | 15 | 15 |

Every level: FCT 0, **VCT 0.5 s**, Global Delay 0.5 s, Cooldown 1.5 s. Range 1.8 tiles (the Fighter walks in first). The damage lands when the hologram log hits, 0.15 s after release (effect: `UI-UX.md` §27). Code: `TB_R`, `TB_SP`, `timber()`.

## 3s. Gaslighting (Active, Ground Debuff 3 × 3, Lv 1–10)
Lead and bend the minds of every enemy in a 3 × 3 square at the target so they turn on the caster (**not bosses**: they show "Immune"). A monster under it has **less DEF from VIT (soft DEF)** but **hits harder**. Range 9 tiles (⚠ not in the spec; RO Provoke range). A purple ring shows under each monster while it lasts.

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Soft DEF | −10% | −15% | −20% | −25% | −30% | −35% | −40% | −45% | −50% | −55% |
| Monster ATK | +5% | +8% | +11% | +14% | +17% | +20% | +23% | +26% | +29% | +32% |
| Time | 5 s | 5 s | 5 s | 5 s | 5 s | 10 s | 10 s | 10 s | 10 s | 10 s |
| SP | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

Every level: no cast, Global Delay 0.3 s, Cooldown 1 s. ⚠ "Def ลดลงตามค่า Vit" is read as **soft DEF only** (the part that comes from VIT); hard DEF (armor %) is not touched. Code: `GL_D`, `GL_A`, `mo.gas` / `mprof()`.

## 3t. Forbear (Self Cast, Buff, Lv 1–10) — needs Gaslighting Lv 3 — **removed in v22h (replaced by Logging, §3u)**
A mind steady as a bear: **physical hits do not make the Fighter flinch**, so they can run or strike back. Forbear holds for 7 hits; the 8th physical hit ends it (and that hit flinches). Magic hits do not count. **MDEF +1% per level** (⚠ read as %, the game's MDEF is a %).

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Time | 10 s | 13 s | 16 s | 19 s | 22 s | 25 s | 28 s | 31 s | 34 s | 37 s |
| MDEF | +1% | +2% | +3% | +4% | +5% | +6% | +7% | +8% | +9% | +10% |

Every level: SP 10, no cast, Global Delay 0, Cooldown 10 s.

**Flinch (new in v22e, every archetype):** a physical hit from a monster (basic attack or a non-magic monster skill) stops the player's feet for 0.3 s (`player.flinch`); attacks and skills are not stopped. Before v22e there was no flinch, so Forbear would have had nothing to remove.

### Balance check (simulator, v22e)
Same method as §3n (300 s × seeds 1–3, auto stats, no gear, every skill at max level; the simulator counts every skill, old and new, and assumes a shield). Fighter AI: Forbear while fighting, Gaslighting on a pack (not bosses), then Crushing Blow / Cleave as before, **Timber!! before Power Strike**. Kills · DPS · deaths.

| | Fighter v22d | **Fighter v22e** | Ranger | Spellcaster |
|---|---|---|---|---|
| Lv 10, Field 01 | 59.3 · 46 | **50.7 · 55** | 52.0 · 32 | 47.7 · 26 |
| Lv 20, Field 02 | 53.3 · 75 | **49.7 · 78** | 44.0 · 55 | 46.0 · 53 |
| Lv 30, Field 03 | 42.3 · 130 | **42.3 · 127** | 34.3 · 99 | 42.0 · 117 |
| Lv 20, packs of 3 | 87 · 111 | **72 · 100** | 85 · 98 | 108 · 123 |
| Lv 30, Geosyncline | 16.3 · 146 | **18.0 · 159 · 0 d** | 13.0 · 125 · 2 d | 25.0 · 218 · 1 d |
| Lv 35, Ruins | 12.0 · 181 · 1 d | **12.0 · 175 · 0 d** | 7.3 · 138 · 3.3 d | 13.7 · 200 · 1 d |
| **CP Lv 10 / 20 / 30** | 598 / 1,090 / 1,576 | **705 / 1,173 / 1,712** | 510 / 789 / 1,196 | 233 / 546 / 971 |

The Fighter is tougher (Shield Mastery DEF +20%, STR / VIT +10; no deaths on the Geosyncline or the Ruins) and hits harder per swing, but **Shield Mastery Lv 10 slows the basic attack by 20%**, which costs about as much as Timber!! adds: on packs of 3 the Fighter drops 87 → 72 kills (with attack speed unchanged it would be 84 kills · 119 DPS). CP still rises 1,576 → 1,712 (+9%), so the gap to the Ranger (1,196) grows. Per cast at Lv 30 against a neutral dummy: Timber!! Lv 10 ≈ 570 damage (+70% on each neighbour), Power Strike 272, Aim Strike 221, Fire Bolt Lv 5 (10 fireballs) 834. The flinch is not in the simulator.

### Balance check (simulator, v22g: old Fighter skills removed)
Same method. The Fighter now has only the five v22e skills; AI: Forbear while fighting, Gaslighting on a pack, then Timber!!.

| | Fighter v22e | **Fighter v22g** | Ranger | Spellcaster |
|---|---|---|---|---|
| Lv 10, Field 01 | 50.7 · 55 | **50.7 · 55** | 52.0 · 32 | 47.7 · 26 |
| Lv 20, Field 02 | 49.7 · 78 | **49.0 · 77** | 44.0 · 55 | 46.0 · 53 |
| Lv 30, Field 03 | 42.3 · 127 | **40.0 · 126** | 34.3 · 99 | 42.0 · 117 |
| Lv 20, packs of 3 | 72 · 100 | **66 · 96** | 85 · 98 | 108 · 123 |
| Lv 30, Geosyncline | 18.0 · 159 · 0 d | **17.0 · 150 · 0 d** | 13.0 · 125 · 2 d | 25.0 · 218 · 1 d |
| Lv 35, Ruins | 12.0 · 175 · 0 d | **11.7 · 174 · 1 d** | 7.3 · 138 · 3.3 d | 13.7 · 200 · 1 d |
| **CP Lv 10 / 20 / 30** | 705 / 1,173 / 1,712 | **634 / 1,038 / 1,469** | 510 / 789 / 1,196 | 233 / 546 / 971 |

The Fighter loses Iron Body (+15% Max HP) and Whirlwind Cleave (the old pack skill), so CP drops 1,712 → 1,469 (still above the Ranger's 1,196; v22d Fighter was 1,576). Packs of 3 drop to 66 kills: Timber!!'s 70% splash is the only area damage left and Shield Mastery Lv 10 still slows the basic attack 20%. Single targets barely change.

## 3u. Logging (Self Cast, Buff, Lv 1–10, v22h, from NIIQ) — needs Timber!! Lv 3
Gather **Timber Logging** from Timber!! hits. Once enough is gathered the logs are bound together and all of them are hurled at the target for a very heavy blow over a **5 × 5** area. Replaces Forbear; Momentum's idea (build with hits, spend in a finisher) now lives on Timber!!.

| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Time | 10 s | 20 s | 30 s | 40 s | 50 s | 60 s | 70 s | 80 s | 90 s | 100 s |
| ATK per log | +20% | +40% | +60% | +80% | +100% | +120% | +140% | +160% | +180% | +200% |
| Logs to bundle | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| Cooldown | 10 s | 20 s | 30 s | 40 s | 50 s | 60 s | 70 s | 80 s | 90 s | 100 s |

Every level: SP 20, FCT 0, **VCT 5 s**, Global Delay 0. Code: `SK.logging`, `addLog()`, `BF.logN`.

How it is read (⚠ to confirm):
- Each Timber!! that **hits** while Logging lasts adds 1 log (a miss adds none).
- When the logs reach the limit they fly at once at the Timber!! target: **one physical hit of logs × ATK-per-log** (Lv 10: 11 × 200% = **2,200% ATK**) on every monster in the 5 × 5 square round it, no crit. The damage lands 0.7 s later, when the bundle hits.
- The buff keeps running after a bundle, so another bundle can be built in the same buff (Lv 10: ~17 s of Timber!! per bundle). Logs not bundled when the buff ends are lost.

### Balance check (simulator, v22h: Forbear → Logging)
| | Fighter v22g | **Fighter v22h** | Ranger | Spellcaster |
|---|---|---|---|---|
| Lv 10, Field 01 | 50.7 · 55 | **49.7 · 56** | 52.0 · 32 | 47.7 · 26 |
| Lv 20, Field 02 | 49.0 · 77 | **47.0 · 78** | 44.0 · 55 | 46.0 · 53 |
| Lv 30, Field 03 | 40.0 · 126 | **38.7 · 124** | 34.3 · 99 | 42.0 · 117 |
| Lv 20, packs of 3 | 66 · 96 | **64 · 99** | 85 · 98 | 108 · 123 |
| Lv 30, Geosyncline | 17.0 · 150 · 0 d | **16.7 · 160 · 0 d** | 13.0 · 125 · 2 d | 25.0 · 218 · 1 d |
| Lv 35, Ruins | 11.7 · 174 · 1 d | **12.7 · 199 · 1 d** | 7.3 · 138 · 3.3 d | 13.7 · 200 · 1 d |
| **CP Lv 10 / 20 / 30** | 634 / 1,038 / 1,469 | **658 / 1,021 / 1,410** | 510 / 789 / 1,196 | 233 / 546 / 971 |

Logging pays off on long fights (Ruins DPS 174 → 199, level with the Spellcaster) but costs time on quick ones: the 5 s cast stops attacks, and the bundle needs 11 Timber!! hits at Lv 10. CP (a 3-minute fight against weak monsters) drops a little.

## 4. Skill levels and skill points
**Decided (NIIQ):**
- Skill points come from **Job Lv**: 1 Job Lv = 1 skill point. At Job Lv 1 a character has none; **Job Lv 2 gives the first point**.
- **Every skill of every archetype, active or passive, is raised by hand by the player.** Nothing is learned for free.
- When the class changes (Beginner → archetype) Job Lv resets to 1, so the character starts with **no points** and must gain Job Lv first (`JOBS.md`).

**In the game now:** every skill starts at Lv 0 (not learned) and costs 1 point per level. Since v20.10 points are spent in the **Skills Tree** as a draft: tap a skill, plan levels with ◀ ▶, then **Learn** (Reset drops the draft; `UI-UX.md` §26). A skill at Lv 0 cannot be used (a toast says so; Idle skips it; its hotbar slot is greyed). A C1 class (Job Lv cap 50) gets 49 points in total; Beginner (cap 10) gets 9.
- **Fire Bolt**, **Freezer**, **Lightning Spear** and **Petrifaction** have Lv 1–5 (§3, §3e–3g; v20.18). Saves from before v20.18: Frost Nova becomes Freezer and Stone Spike becomes Petrifaction (same level, same hotbar slots); Fire Bolt above Lv 5 drops to Lv 5 and the extra points come back.
- **Overload Energy** has Lv 1–5 (§3d); **Mana Flow** Lv 1–10 and **Elemental Attunement** Lv 1–5 (§3b, §3c): the first passives with levels.
- **Every other skill has one level** (1 point to learn it, the prototype numbers) until its levels are designed. ⚠ NIIQ has not given per-level effects for them yet.
- **Passives** are learned the same way (1 point each) and only work once learned.
- **Beginner (v20.4):** a Beginner spends points only on **Basic Skill** (Lv 1 given, Lv 2–10 cost 1 point each). First Aid and Heavy Strike come from Basic Skill Lv 3 and Lv 4 and stay learned after the Archetype choice (`JOBS.md` §1b).

**⚠ Still open:** points reset (respec), whether unspent points carry over on class change (the answer so far is no, because Job Lv resets), the max level and per-level effect of every skill except Fire Bolt.

## 5. Hotbar
The player chooses, for each hotbar slot, **which skill and which level** goes in it. v20.10: in the Skills Tree, ◀ ▶ under a learned skill pick the level and dragging the tile puts that level on the slot (`UI-UX.md` §26). The Hotbar setup drop-downs were removed in v20.10. A slot filled with no level picked uses the highest level learned. A slot uses that level’s own SP cost, cast time and number of hits, and a level above the one learned is not possible. Example: Fire Bolt Lv 3 on slot 1 and Fire Bolt Lv 10 on slot 2. The 10 slots are free: a slot holds a skill or a usable item, dragged from the bag or the Skills Tree (`UI-UX.md` §25). The default layout puts skills on 1–7 and Fly Wing, Red Potion and Blue Potion on 8, 9 and 0. Auto-potion uses the slot that holds Red Potion (HP below 35%) or Blue Potion (SP below 15%); if no slot holds it, it does nothing.

**Decided:** Fire Bolt has a 0 s cooldown, so levels do not block each other. After Lv 2 the player can cast Lv 5 straight away; only the Global Delay (1 s) has to pass.

**Built as (⚠ assumption, not stated):** Idle (auto-hunt) uses the level set on the **first hotbar slot that holds the skill**, and skips skills that are not learned. If NIIQ prefers “always the highest learned level”, it is a one-line change. The simulator (CP, offline estimate) picks the level itself (§3h balance check); Idle in the game does not.

**⚠ Not decided:** whether the two potion slots and the wing slot stay fixed.

## 6. Parked (homework for NIIQ)
**CP.** With a full set of tier-appropriate gear the Spellcaster is far ahead of the other roles in the simulator, **before and after** this draft. Full set, base rolls, no affixes: Lv 30 with ★2 gear, CP 20,761 vs Fighter 7,241 / Ranger 8,348 / Supporter 7,923; Lv 50 with ★3 gear, CP 101,558 vs 28,408 / 40,460 / 32,479. Kills stay close because respawn and travel time cap them.

Cause: every gear slot adds `m × 0.35` to the primary stat, and MATK has an `⌊INT/5⌋²` term (STR and DEX use `⌊/10⌋²`). At INT 225, max MATK is about 2,250. The staff’s `m × 2.2` (119 at tier 30 ★2) is only about 5% on top of that, so weaponMATK does not cause this. It matters for the CP gates (Geosyncline 2,000, Ruins 3,000).

New side effect of stopping fireballs when the target dies: CP counts damage dealt, and the old simulator counted overkill. With 2 common pieces the Spellcaster’s CP falls from 3,126 (old prototype) to about 2,140 with Fire Bolt Lv 5 and the staff × 1 (3,515 vs 6,698 with 5 pieces). Note that the CP simulation (and the Idle offline estimate) uses Fire Bolt Lv 5 and counts every skill and passive as learned. Nothing was changed for this.

## 7. ⚠ Open items
1. Max level and per-level effects of the Fighter and Supporter skills and the old Ranger prototype skills (one level each). Every Spellcaster skill and the five v21f Ranger skills have levels.
1d. Ranger v21f–v22b (§3i–3n): v22b Ranger is weaker after the old skills left (CP −32%); Scandium negative on most maps; Aim Strike "in total" read as shared between split arrows (single target it is slightly worse than shooting); the Scandium cost of No Arrow against monster Scandium; whether the old Ranger skills stay; "ATK +X%" read as X% ATK; free arrows without No Arrow.
1a. Freeze / Petrifaction / Burning time, the Burning damage over time (10% MATK/s, §3h; soft MDEF often cuts it to 1 on low-MATK characters), the exact MDEF / LUK resistance, boss immunity (§3h); the meaning of “Overload Damage ×0.5” (§3).
1c. Spellcaster CP fell about 20% with the v20.18 spells (§3h).
1b. Overload Energy: party members without combat stats (§3d).
2. Potion and wing slots (§5).
3. Respec (reset skill points).
4. Global Delay for the other skills (0 for now), and FCT values for every spell (0 for now). Items that lower VCT, FCT or Global Delay are still to be designed.
5. Fireball timing assumptions and the SP refund (§3).
6. Overload strength, the *Crit damage* ability (not applied to Overload in the game) and the label (OVERLOAD! / เกินพิกัด!, orange) (`COMBAT-FORMULAS.md` §3b).
7. Supporter staff: left as it is (+10% MATK, no weaponMATK) until classes are split.
8. CP and the gates (§6).
