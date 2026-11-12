# Status Icons & Live Stats

> Part of the REO docs. Build status: effect icons = mockup; network/device strip = live on device, ping/players simulated until a server exists.

## 1. Effect icons (under the character card)

- A row of round icons with countdown timers sits directly under the player ID card (top-left).
- Hover (desktop) or tap (phone) shows the name and description.
- Debuffs get a red border.
- **v5:** icons are real buffs only: Momentum (stacks), War Cry, Evasive Leap, empowered shot, Blessing, Grace shield (amount), Sanctuary. The earlier mockup icons were removed.
- Future: buffs/debuffs come from the skill and item system; the row shows max 8 icons, then wraps.

## 2. Status readout (top-right, above the minimap) — v5

Ultra-minimal, two lines, no icons:

```
52 FPS / 15 ms / 12:55 PM
User Online: 579 | This map: 2
```

| Item | Source |
|---|---|
| FPS | measured every 0.5 s from the game loop |
| Ping (ms) | `REO_SERVER` round trip; simulated until a server exists |
| Local time | device clock, locale format (Thai: 24-hour) |
| User Online | server count; simulated now |
| This map | players on the current map; simulated now (town: you + wandering players, fields: you) |

Signal, Wi-Fi and battery were removed in v5. Hovering the readout says when values are simulated.

## 3. Rules

- Stats update in the HUD about 8 times per second; the strip is only re-rendered when a value changes.
- Colors use the same thresholds on phone and desktop.
- Never show private data (no account names in the strip).

## Open questions

1. Should the battery/signal strip be hideable in settings?
2. Ping source in production: WebSocket heartbeat or HTTP HEAD on the game server?
