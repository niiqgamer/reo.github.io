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

## Open questions

1. How is Lanthanum obtained — real-money purchase only, or also from play?
2. Is Yttrium bound per account or per character?
3. Trading channels: direct trade, player shops/vending, auction house/market — which exist and which currencies does each accept?
4. Fees/taxes on player trades (Scandium sink).
5. Exchange between currencies (e.g. La → Y, or none)?
6. What does each shop sell (NPC, Yttrium shop, premium shop)?
7. Thai display names for the three currencies.
