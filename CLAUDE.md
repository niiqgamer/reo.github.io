# CLAUDE.md — Rare Earth Online (REO)

Talk to the user in Thai. Code, comments and commit messages stay in English.

## What this repo is
- The whole game is one file: `index.html` (HTML + CSS + JS, art drawn in canvas). There is no build step.
- `wiki.html` is the player wiki.
- `MD/` holds the design docs. Start with `MD/README.md` (the index) and `MD/REO-INSTRUCTIONS.md` (the rulebook). Read the rulebook before big changes.
- `images/` holds item, monster and map images used by the wiki. `reo/` is an unused Godot stub.

## Rules for every change (do these yourself; the user should never have to)
1. **Keep the copies in sync.** `MD/index.html` must be a byte-for-byte copy of `index.html`, and `MD/wiki.html` a copy of `wiki.html`. After editing, run `cp index.html MD/index.html` and `cp wiki.html MD/wiki.html`.
2. **Update the docs in the same commit as the code.** Find the doc for the area you changed in the `MD/README.md` index (towns → `GADOLINIUM.md` / `TOWN-ALIEN.md`, fields → `FIELD-*.md`, items → `ITEMS.md`, quests → `QUESTS.md`, combat → `COMBAT-FORMULAS.md`, UI → `UI-UX.md`, and so on). Fix every number, coordinate and rule that changed. If player-facing info changed, update `wiki.html` (and `MD/REO-Wiki.md`) too.
3. **If a request conflicts with `MD/REO-INSTRUCTIONS.md`,** follow the request, then update that file so it stays accurate.
4. **Log the change** in a short "Changes in …" entry at the top of the changes list in `MD/README.md`.
5. **Every user-facing string goes through `t(key)`,** with both `en` and `th` text. Never hard-code UI text.

## Code facts that are easy to get wrong
- Maps: every map is 98 × 98 tiles. The old 49 × 49 design grid is scaled by `MAPK` (all 2). `N` is the size of the **current** map; code that works on another map must use `m.N` (or local `I` / `inb` helpers built from it). Change the current map with `setCur(m)`, never `cur=` directly.
- Fields are laid out in the old 49-grid coordinates inside `FCFG` and scaled in `buildField`. Monster `zone`s are also in 49-grid coordinates. Field portals sit 2 tiles from the edge.
- The town layout is hand-placed in `buildTown` using `TC`, `PLAZA_R`, `CRY`, `CRY_R`, `TOWN_SPAWN`, `TOWN_GATES`.
- The ground is drawn in chunks (`groundGen` / `groundChunk`) under a memory budget (`groundScale`). Only the current map and the one ahead (`AHEAD`) stay in memory.
- Saves carry `mv` (map version). If map coordinates change again, bump it and migrate old positions on load.

## Testing
Chromium + Playwright are preinstalled. Open `file:///…/index.html` directly (no server needed) and skip the login by seeding a guest session first:
```js
await page.addInitScript(()=>{localStorage.setItem('reo.session.v1',JSON.stringify({v:1,t:Date.now(),type:'guest',uid:'g1',name:'Guest1',charName:'Arin'}));localStorage.setItem('reo.authLang','th')});
```
Then wait for `window.__reo.cur.ground`. `window.__reo` exposes the game state and helpers (`goMap`, `startNav`, `player`, `MAPS`, `S`, …). Before committing, check for page errors and take a screenshot of what you changed.
