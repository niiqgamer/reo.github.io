# Audio (8-bit chip music and sound effects)

> Part of the REO docs. Code: `AUDIO (v18)` section in `index.html` (`AUD`). Status: working; first pass, all sounds are generated live (no sound files).

## 1. How it works
- Everything is synthesized with the browser's WebAudio: square and pulse waves (25%, 12.5%), triangle bass, noise for drums. No files to download.
- Browsers do not allow sound before the player touches the page, so the music starts on the **first tap or key press**.
- Settings > Sound has two switches: **Sound effects** and **Music**. Both are saved.
- Music pauses while the tab is hidden and does not stack up when you come back.

## 2. Music per map
Each track is built from a scale, a chord progression (4 bars) and a seed, so it loops without repeating exactly.
| Track | Where | Tempo | Mood (scale) |
|---|---|---|---|
| town | Gadolinium | 112 | bright but strange (Lydian), light drums |
| field1 | Field 01 | 92 | calm, curious (Dorian), soft drums |
| field2 | Field 02 | 80 | dusk (Phrygian), long bass |
| field3 | Field 03 | 72 | icy, sparkling (whole tone), no drums |
| boss | Field 03 while Gadolith is fighting | 152 | tense (harmonic minor), driving drums, pulsing bass |
Changing map fades the new track in. The boss track plays while the boss is aggressive and the normal track returns when the fight ends.

## 3. Sound effects (25)
UI: click, window open, window close, error. Combat: hit, critical, miss, hurt, skill, kill, boss slam warning, boss slam, boss defeated, death. Progress: level up, quest accepted, quest done, announcement. Items: pickup, equipment drop, potion, equip, refine success, refine fail, coin (buy or sell). Travel: warp (map change and teleport), Idle on, Idle off.
Fast repeats are limited (for example hits at most every 60 ms) so it never turns into noise.

## 4. Open questions
1. Real music: replace the generated tracks with composed ones when available (same hook: `AUD.setMap`).
2. Volume sliders for music and effects (today: on or off).
3. Per-skill and per-monster voices; footsteps; ambient sounds.
