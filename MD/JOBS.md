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

### C0 → C1: the Archetype Trial (built in v5.1)

| Step | What happens |
|---|---|
| 1 | Every new character is a **Beginner (C0)**, Job Lv cap 10. |
| 2 | Talk to **Archetype Helper Sera** in Gadolinium plaza (tile 28, 27). She explains the 4 archetypes. Before Job Lv 10 she only teaches and says to come back. |
| 3 | At **Job Lv 10** she offers the quest **Archetype Trial**: defeat **10 Elite monsters** in any field. The quest is only given by her (it never appears in the Quests window list). |
| 4 | Return to her. A choice window shows the 4 archetypes; the player picks **exactly one** (Choose → Confirm). |
| 5 | The character becomes that archetype (**C1**). **Job Lv resets to 1** with a new cap of **50**. Reward: 500 Base EXP, 30 Yttrium. |
| 6 | The choice is **permanent**. Talking to her again only gives encouragement. |

- Requirement used: **Job Lv 10**. The earlier draft also required Base Lv 10; it was dropped to match the latest direction.
- The archetype is the C1 tier for now. When each archetype gets its 4 classes, the same trial picks the archetype and a later step picks the class.
- Elites per field: 1 per monster type (6 total in Fields 01–02), respawn 45–60 s. Expect the trial to take a while; Elites wear a golden circle at their feet.

### C1 → C2 (planned)

| Step | Requirement | Result |
|---|---|---|
| 1 | Base Lv **50+** and Job Lv **50 (max)** | Eligible |
| 2 | Complete the **upper class change quest** | Becomes a **Job (C2)** |
| 3 | Level to Base Lv **99** and Job Lv **50** | Current cap |

Implementation rules:
- Requirements are checked when the quest is offered and when it is turned in.
- Store `arch` on the character. `jcap()` = 10 for Beginner, 50 for an archetype.
- Saves from v5 (when classes could be switched freely for testing) keep their class, and the trial is marked done.

## 5. Prototype mapping

- v5: one **baseline prototype per archetype** is playable (see `ARCHETYPES.md`). It stands in for that archetype's classes until each class gets its own kit.

- Prototype label **“Novice / ผู้ฝึกหัด”** must become **“Beginner”** (Thai name TBD, see below).
- The prototype hotbar skills are **placeholders**; real skill lists will be defined per class/job.

---

## Open questions

1. Names for Spellcaster class 3.2 and its two jobs (the draft repeated Wizard/Warlock).
2. All 4 Supporter classes and 8 jobs.
3. Is the archetype chosen separately before the class, or implied by the class choice? (This doc assumes implied.)
4. ✅ Job Lv resets to 1 on the C0 → C1 change (v5.1). Still open: do unspent skill points carry over?
5. Thai display names for archetypes, classes and jobs, or keep English names in both languages?
6. Spelling check: “Swordman” (kept as written) vs “Swordsman”.
7. Archetype accent colors for UI (job icons, name tags, skill effects).
8. Can a character ever change class/job again (job reset item)?
