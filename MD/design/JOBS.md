# Jobs & Job Change

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.
> *Future jobs, availability and details may change.*

---

## 1. Structure

**1 Beginner → 4 Archetypes → 16 Classes → 32 Jobs**

| Tier | Code | Count | Example |
|---|---|---|---|
| Beginner | C0 | 1 | Beginner |
| Class | C1 | 16 | Swordman |
| Job | C2 | 32 | Knight |

The **archetype** is the role family. A player picks a **class** at C1, which places them in that class’s archetype, and later picks one of that class’s two **jobs** at C2.

---

## 2. Archetypes

| # | Archetype | Type | Range (tiles) | Role |
|---|---|---|---|---|
| 1 | **Fighter** | `MELEE` | 1–3 | Physical close-quarters combat |
| 2 | **Ranger** | `RANGED` | 1–12 | Physical long-range engagements |
| 3 | **Spellcaster** | `MAGIC` | 1–7 | Combat spells at medium range |
| 4 | **Supporter** | `SUPPORT` | 1–15 | Team assistance over a massive range |

---

## 3. Job tree

### 1. Fighter — MELEE (1–3 tiles)

| Class (C1) | Job (C2) | Job (C2) |
|---|---|---|
| 1.1 Tanker | 1.1.1 Defender | 1.1.2 Paladin |
| 1.2 Swordman | 1.2.1 Knight | 1.2.2 Duelist |
| 1.3 Thief | 1.3.1 Assassin | 1.3.2 Pirate |
| 1.4 Monk | 1.4.1 Hermit | 1.4.2 Inquisitor |

### 2. Ranger — RANGED (1–12 tiles)

| Class (C1) | Job (C2) | Job (C2) |
|---|---|---|
| 2.1 Hunter | 2.1.1 Warden | 2.1.2 Artillerist |
| 2.2 Gunslinger | 2.2.1 Pistoleer | 2.2.2 Sniper |
| 2.3 Ninja | 2.3.1 Shinobi | 2.3.2 Zephyr |
| 2.4 Robotic | 2.4.1 Juggernaut | 2.4.2 Programmer |

### 3. Spellcaster — MAGIC (1–7 tiles)

| Class (C1) | Job (C2) | Job (C2) |
|---|---|---|
| 3.1 Magician | 3.1.1 Wizard | 3.1.2 Warlock |
| 3.2 *TBD* | 3.2.1 *TBD* | 3.2.2 *TBD* |
| 3.3 Witch | 3.3.1 Shaman | 3.3.2 Necromancer |
| 3.4 Illusionist | 3.4.1 Creator | 3.4.2 Summoner |

### 4. Supporter — SUPPORT (1–15 tiles)

| Class (C1) | Job (C2) | Job (C2) |
|---|---|---|
| 4.1 *TBD* | 4.1.1 *TBD* | 4.1.2 *TBD* |
| 4.2 *TBD* | 4.2.1 *TBD* | 4.2.2 *TBD* |
| 4.3 *TBD* | 4.3.1 *TBD* | 4.3.2 *TBD* |
| 4.4 *TBD* | 4.4.1 *TBD* | 4.4.2 *TBD* |

**Defined so far:** 13 of 16 classes and 26 of 32 jobs.

### Data IDs

Use stable lowercase IDs in code and data; display names come from localization.

```
beginner
fighter:  tanker(defender, paladin) · swordman(knight, duelist) · thief(assassin, pirate) · monk(hermit, inquisitor)
ranger:   hunter(warden, artillerist) · gunslinger(pistoleer, sniper) · ninja(shinobi, zephyr) · robotic(juggernaut, programmer)
spellcaster: magician(wizard, warlock) · tbd_3_2(tbd, tbd) · witch(shaman, necromancer) · illusionist(creator, summoner)
supporter: tbd_4_1 … tbd_4_4
```

---

## 4. How to change jobs

```
 C0 Beginner ──(Base Lv ≥ 10, Job Lv 10/10, archetype change quest)──► C1 Class
 C1 Class    ──(Base Lv ≥ 50, Job Lv 50/50, upper class change quest)─► C2 Job
 C2 Job      ──► level to Base Lv 99 (cap), Job Lv 50 (cap)
```

| Step | Requirement | Result |
|---|---|---|
| 1 | New character | **Beginner (C0)** |
| 2 | Base Lv **10+** and Job Lv **10 (max)** | Eligible for C1 |
| 3 | Complete the **archetype change quest** | Becomes a **Class (C1)** |
| 4 | Base Lv **50+** and Job Lv **50 (max)** | Eligible for C2 |
| 5 | Complete the **upper class change quest** | Becomes a **Job (C2)** |
| 6 | Level to Base Lv **99** and Job Lv **50** | Current cap (will be raised later) |

Implementation rules:
- Requirements are checked **server-side** when the quest is started and when it is completed.
- Store `tier`, `archetype`, `class`, `job` on the character; derive range type and skill list from data.
- UI shows the requirement checklist in the quest window with current progress (e.g. “Job Lv 7 / 10”).

---

## 5. Prototype mapping

- Prototype label **“Novice / ผู้ฝึกหัด”** must become **“Beginner”** (Thai name TBD, see below).
- The prototype hotbar skills are **placeholders**; real skill lists will be defined per class/job.

---

## Open questions

1. Names for Spellcaster class 3.2 and its two jobs (the draft repeated Wizard/Warlock).
2. All 4 Supporter classes and 8 jobs.
3. Is the archetype chosen separately before the class, or implied by the class choice? (This doc assumes implied.)
4. Does Job Lv reset to 1 on each job change? Do unspent skill points carry over?
5. Thai display names for archetypes, classes and jobs, or keep English names in both languages?
6. Spelling check: “Swordman” (kept as written) vs “Swordsman”.
7. Archetype accent colors for UI (job icons, name tags, skill effects).
8. Can a character ever change class/job again (job reset item)?
