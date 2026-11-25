# Economy & Currencies

> Part of the REO docs. Rules and glossary live in `REO-INSTRUCTIONS.md`.

---

## 1. Major currencies

All three are named after rare-earth elements.

| Currency | Symbol | Type | Tradable | Used for |
|---|---|---|---|---|
| **Scandium** | `Sc` | Common in-game gold | Yes | General trading, NPC fees |
| **Yttrium** | `Y` | In-game cash, **earnable** | **No** (bound to account/character) | Bound cash purchases |
| **Lanthanum** | `La` | Premium cash | Yes | Player trading, premium shop |

### Scandium (Sc)
- Main currency from monster kills, quests and selling to NPCs.
- Spent on NPC shops and fees (e.g. refine fees, teleports, repairs, job change fees if any).
- Can be traded between players.

### Yttrium (Y)
- Earned through play (e.g. dailies, achievements, events).
- **Cannot be traded** — bound to the owner.
- Spent in a dedicated shop.

### Lanthanum (La)
- Premium currency.
- **Can be traded** between players.
- Spent in the premium shop.

---

## 2. Display rules

- Wallet shows all three, in order: **Scandium · Yttrium · Lanthanum**.
- Each has its own icon and color; never show a bare number without the icon or symbol.
- Numbers use locale formatting (`th-TH` / `en-US`).
- Currency names stay in English in both languages unless Thai names are approved.

| Currency | Suggested color |
|---|---|
| Scandium | Silver-gold `#D9C27A` |
| Yttrium | Teal `#3FC6A8` |
| Lanthanum | Violet `#8A78FF` |

---

## 3. Implementation rules

- All balance changes happen **server-side** with a transaction log (source, amount, before, after, timestamp).
- Bound currency (Yttrium) must never move between accounts through any path: trade, mail, market, guild storage.
- Prototype rename: `S.gold` → `S.sc`; add `S.y` and `S.la`. Labels “Gold / ทอง” → “Scandium”.

---

## 4. Party rewards (v20.3)

Applies to monster kills (`killMon`). Idle and offline rewards are not changed yet.

- **Size bonus** (EXP, Items and Scandium you receive): each extra member adds to the bonus. 2 people +5% · 3 +12% · 4 +21% · 5 +32% · 6 +47% (the step per member is +5, +7, +9, +11, +15, added together). The bonus applies even when nothing is shared. Table: `PT_BONUS` in `index.html`.
- **Level gap**: a party needs `max level − min level ≤ 20`. The invite is refused if it would break this. If a level-up breaks it later, the bonus and sharing pause until it is back in range (the Party tab says so).
- **EXP sharing** (leader setting):
  - *Off*: you get `EXP × (1 + bonus)`.
  - *Split equally*: the party pool is `EXP × (1 + bonus)`, split evenly, so you get `EXP × (1 + bonus) ÷ members`. Example, 2 people, 20 EXP: Off → 21 · Split → 10.5 each.
- **Item & Scandium sharing** (leader setting; Scandium follows this setting):
  - *Off*: you keep your own drops. In the simulation the simulated members deal no damage, so you always have the top damage and get the loot.
  - *On*: drops rotate through `[you, members…]`, one item or Scandium pile at a time. Turns that belong to a member go to that member (shown in the Party chat).
- **Item quantity bonus**: a stack `q` becomes `q × (1 + bonus)`, rounded stochastically so the average is exact. Gear gets one extra piece with chance = bonus.

---

## Open questions

1. How is Lanthanum obtained — real-money purchase only, or also from play?
2. Is Yttrium bound per account or per character?
3. Trading channels: direct trade, player shops/vending, auction house/market — which exist and which currencies does each accept?
4. Fees/taxes on player trades (Scandium sink).
5. Exchange between currencies (e.g. La → Y, or none)?
6. What does each shop sell (NPC, Yttrium shop, premium shop)?
7. Thai display names for the three currencies.

## 5. Scandium sink: No Arrow (v21f)
A Ranger who learned **No Arrow** pays Scandium for every arrow shot: 20 / 18 / 15 / 13 / 10 Sc by skill level (`SKILL-SPEC.md` §3j). With too little Scandium the bow does not shoot. Offline idle subtracts the arrows too (the net can be negative; the wallet stops at 0). Simulated net per hour at Lv 5: Field 01 −4.7k, Field 02 −3.2k, Field 03 +14.9k, Geosyncline +7.5k, Ruins +17.9k; at Lv 1 every map is negative (table in `SKILL-SPEC.md` §3n). ⚠ Open: this is the first big Scandium sink tied to fighting, and it hits one archetype only.
