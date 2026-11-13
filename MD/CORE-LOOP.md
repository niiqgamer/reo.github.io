# Core Loop & Progression

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`. Jobs and level caps: `JOBS.md`. Currencies: `ECONOMY.md`.

---

## 1. The loop

```
        ┌──────────────────────────────────────────────┐
        ▼                                              │
  1. Kill monsters                                     │
        │                                              │
        ▼                                              │
  2. Base EXP + Job EXP + Items + Coins                │
        │                                              │
        ▼                                              │
  3. Level up ──────────────► Job change (C0→C1→C2)    │
        │                                              │
        ▼                                              │
  4. Better equipment = higher CP                      │
     (refine · card slots · equipment options)         │
        │                                              │
        ├──► 5. Quests                                 │
        ├──► 6. Instance bosses                        │
        ├──► 7. Daily dungeons                         │
        └──► 8. Idle farming for materials ────────────┘
```

Every activity feeds the same outputs: **EXP, items, currency, materials** → which raise **level and CP** → which unlock **harder content** → which drops **better rewards**.

| # | Activity | Main output | Unlocked by |
|---|---|---|---|
| 1 | Kill monsters | Base/Job EXP, drops, Scandium | Start |
| 2 | Rewards | — | — |
| 3 | Level up | Stat & skill points, job change eligibility | EXP |
| 4 | Equipment upgrades | CP | Materials, Scandium, cards |
| 5 | Quests | EXP, items, story, job changes | Level / tier |
| 6 | Instance bosses | Rare equipment, cards | Level / CP gate |
| 7 | Daily dungeons | Materials, Yttrium | Level, daily entries |
| 8 | Idle farming | Materials | Unlocked area |

---

## 2. Monster kills (step 1–2)

Each kill grants:

| Reward | Notes |
|---|---|
| **Base EXP** | Raises Base Level |
| **Job EXP** | Raises Job Level of the current tier |
| **Items** | Drop table per monster (equipment, cards, materials, consumables) |
| **Coins** | Scandium (see `ECONOMY.md`) |

- Rewards are rolled **server-side**.
- Damage numbers and drops are shown in world space; drops are picked up by walking over them or by auto-loot (setting).

---

## 3. Leveling (step 3)

| Track | Cap | Notes |
|---|---|---|
| Base Level | **99** (will be raised in future updates) | Shared across all tiers |
| Job Level — C0 Beginner | 10 | |
| Job Level — C1 Class | 50 | |
| Job Level — C2 Job | 50 | |

- Base EXP and Job EXP are **separate pools** with separate bars in the HUD.
- Job change requirements are in `JOBS.md`.
- Code must read caps from data (`levelCaps.json` or equivalent), never hard-code `99`.

**Prototype formula (placeholder):** Base EXP to next level `round(60 × baseLv^1.5)`. Job EXP curve is **to be defined**.

---

## 4. Equipment & CP (step 4)

**Better equipment = better CP.** Three upgrade systems stack on top of an item’s base stats:

| System | What it does |
|---|---|
| **Refine** | Raises the item’s refine level (+1, +2, …) for more base stats |
| **Card slots** | Sockets that hold monster cards for extra effects |
| **Equipment options** | Bonus stat lines on the item |

**CP (Combat Power)** = one number derived from the character’s final stats, shown in the character window and used to gate content (instance bosses, dungeons).

```
CP = f( base stats, Base Lv, job, equipment base stats,
        refine bonuses, card effects, equipment options, skills )
```

The exact formula is an open question; implement CP as a single function so it can be tuned in one place.

---

## 5. Content (steps 5–8)

### 5. Quests
- **Main story** — guides the player between towns; includes job change quests.
- **Side quests** — town NPC requests.
- Starter quest “A New Beginning” in Gadolinium: see `GADOLINIUM.md`.

### 6. Instance bosses
- Private instanced map per player or party.
- Entry gated by Base Level and/or CP.
- Primary source of rare equipment and cards.

### 7. Daily dungeons
- Limited entries per day; resets at a fixed server time.
- Rewards focus on upgrade materials.

### 8. Idle farming for materials
- While idle auto-hunt is on (or offline), the character gathers **materials** from an unlocked area.
- Offline rewards are claimed on login.
- Prototype behavior: auto-hunt ON grants EXP and coins over time, random skill effects, and the character patrols the plaza with an “AUTO” badge. Manual clicks override patrol.

---

## Open questions

1. Job EXP curve per tier.
2. Is EXP from idle farming allowed, or is idle **materials only** (as step 8 suggests)?
3. Refine: max level, success rates, failure result (no change / downgrade / break), costs.
4. Card slots: max slots per item type; can cards be removed?
5. Equipment options: number of lines, reroll method and cost.
6. CP formula and weights.
7. Instance boss: solo or party, entry limits, CP requirement.
8. Daily dungeon: entries per day, reset time (server time zone), rewards.
9. Idle farming: hours cap for offline rewards, material tables per area.
10. ✅ Skill points come from **Job Lv**: 1 Job Lv = 1 skill point (the first at Job Lv 2), spent by the player on every skill, active or passive, which all start at Lv 0 (`SKILL-SPEC.md` §4). Stat points still come from Base Lv.


## Field boss (v6)
The first boss, **Gadolith** (Field 03, Lv 20), is a **field boss**: it stands in an open arena, respawns on a timer, and drops Crystal Hearts. Instance bosses (private maps) are still planned; see `FIELD-03.md` for the boss mechanics.

## Auto stat points (v13)

- With **Auto-assign** on (default), points are spent automatically on every level-up, on class change, on load, and after pressing Auto-assign.
- The Character window refreshes right away when the character levels up (before, it showed old stats until reopened).
- A stat raise costs at least 2 points, so one leftover point may wait for the next level-up. The window shows this as "แจกอัตโนมัติอยู่: เหลือ N แต้ม".
- Pressing a manual **+** turns Auto-assign off. Turn it on again with the button.
