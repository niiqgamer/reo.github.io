# Status Icons & Status Islands

> Part of the REO docs. Build status: effect icons = real buffs; status islands = FPS and clock live on device, ping/online simulated until a server exists.

## 1. Effect icons (under the character card)

- A row of round icons with countdown timers sits directly under the player ID card (top-left).
- Hover (desktop) or tap (phone) shows the name and description.
- Debuffs get a red border.
- **v5:** icons are real buffs only: Momentum (stacks), War Cry, Evasive Leap, empowered shot, Blessing, Grace shield (amount), Sanctuary. The earlier mockup icons were removed.
- Future: buffs/debuffs come from the skill and item system; the row shows max 8 icons, then wraps.

## 2. Status islands (left of the minimap) — v18.3

Four separate islands in a column beside the minimap (portrait: one row at the very top). No SERVER TIME label and no USER ON MAP.

```
🎮 60 FPS   |   📡 25 ms   |   🌏 1,286 ONLINE   |   ⏱ 12:25 PM
```

| Island | Source |
|---|---|
| FPS | measured every 0.5 s from the game loop; green ≥ 50, amber ≥ 30, red below |
| ms (ping) | `REO_SERVER` round trip; simulated until a server exists; green < 40, amber < 120, red above, `—` if unknown |
| ONLINE | server count; simulated now |
| Clock | device clock, locale format (Thai: 24-hour) |

The islands are always visible (the old 30 second expand and collapse is gone). Layout details are in `UI-UX.md` §13. Hovering the column says when values are simulated.

## 3. Rules

- Stats update in the HUD about 8 times per second; the islands are only re-rendered when a value changes.
- Colors use the same thresholds on phone and desktop.
- Never show private data (no account names in the strip).

## Open questions

1. Should the islands be hideable in settings?
2. Ping source in production: WebSocket heartbeat or HTTP HEAD on the game server?
