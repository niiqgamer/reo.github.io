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

## 1b. Basic Skill: the Beginner skill tree (v20.4)

Every Beginner has one skill, **Basic Skill**, with **10 levels**. Lv 1 is given at the start. Each next level costs **1 skill point** (1 Job Lv = 1 point, the first at Job Lv 2) and teaches one ability. Beginner Job Lv is capped at 10, which gives exactly **9 points**, so Basic Skill Lv 10 uses all of them. Raise it in the Skills window (the + on the Basic Skill row).

| Lv | Teaches | Rule in the game |
|---|---|---|
| 1 | Talk, fight, use skills, use items, Idle | Given; nothing is locked |
| 2 | Sit (HP / SP regen ×3), stand up, set a status sign | Sit and *Set status* are disabled in the right-click menu until Lv 2 |
| 3 | **First Aid** (skill) | Restore **50 HP** · SP **10** · cooldown **5 s** · no cast time |
| 4 | **Heavy Strike** (skill, id `bash`) | **200% ATK** on one enemy · SP **5** · cooldown **5 s** · range **1.6 tiles** (same as the Beginner basic attack) · no cast time. On a target further away (up to 7.6 tiles) the character walks in first and then strikes (gives up after 4 s; Idle then skips it for 3 s) |
| 5 | **Pocket Dimension** | Personal storage (300 slots) through **Narvis**, an NPC in every main town (`ITEMS.md` §7) |
| 6 | Friends | *Add friend* is disabled and Social → Friends is locked until Lv 6 |
| 7 | Party | *Create a party* and Social → Party are locked until Lv 7 |
| 8 | Trade | Player trade and stalls (both still *Soon*) show the Lv 8 requirement until then |
| 9 | Guild | Social → Guild and guild invites are locked until Lv 9 |
| 10 | Archetype | The Archetype Trial **starts automatically** once Basic Skill Lv 10 and Job Lv 10 are both reached (§4) |

- **Kept for good.** Choosing an Archetype never removes Basic Skill or anything it taught. First Aid and Heavy Strike stay in the Skills window and can go on any hotbar slot (on a new archetype's hotbar they fill the empty skill slots after its 4 archetype skills). An Archetype's own points start from 0 as before; Basic Skill does not use them.
- First Aid and Heavy Strike cannot be planned on their own in the Skills Tree (v20.9, `UI-UX.md` §26): their level comes from Basic Skill (Lv 3 / Lv 4); before that their tile is grey with "Basic Lv 3 / 4". A locked one says "Requires Basic Skill Lv N" when used.
- Code: `S.basicLv` (1–10), `BASIC_UNLOCK`, `hasBasic(k)`, `basicRaise()`. Older saves: a Beginner starts at Basic Skill Lv 1 and gets back the points spent on Bash / First Aid; an Archetype gets Lv 10.

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
| 3 | **v20.5: automatic.** The moment the character has both **Job Lv 10** and **Basic Skill Lv 10** (§1b), whichever comes last, the quest **Archetype Trial** starts by itself and is tracked: defeat **1 Elite monster** in any field. No visit to Sera is needed to start it (talking to her still starts it as a fallback). It never appears in the Quests window list and cannot be abandoned. Older saves that already meet both requirements get it when loaded. |
| 4 | Return to her. A choice window shows the 4 archetypes; the player picks **exactly one** (Choose → Confirm). |
| 5 | The character becomes that archetype (**C1**). **Job Lv resets to 1** with a new cap of **50**. Reward: 500 Base EXP, 30 Yttrium and the full **10-piece class set** of that archetype (**Lv 10**, Common ✪, no random options), equipped at once; the Beginner pieces go to the bag (v20.7). |
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
4. ✅ Job Lv resets to 1 on the C0 → C1 change (v5.1). Beginner points all go into Basic Skill (§1b), which is kept; Archetype points start again from 0.
5. Thai display names for archetypes, classes and jobs, or keep English names in both languages?
6. Spelling check: “Swordman” (kept as written) vs “Swordsman”.
7. Archetype accent colors for UI (job icons, name tags, skill effects).
8. Can a character ever change class/job again (job reset item)?
