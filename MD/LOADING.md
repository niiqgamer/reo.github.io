# Loading & Cut Scenes

> Part of the REO docs.

## Rule

Assets load in the background. The player only sees a loading screen when something they asked for needs an asset that is not ready yet. Gameplay is never paused for background loading.

## When loading may appear

| Moment | Behavior |
|---|---|
| Game start | Loading screen until the starting map’s ground is ready (“Loading Gadolinium…”) |
| Change map (portal, return to town) | Ready neighbors are instant. If not ready: loading screen with progress, then fade and travel |
| Cut scene (e.g. crystal scene) | Required maps are prepared first; the dialog opens when ready (“Preparing scene…”) |
| Anything else | Background only. No loading screen |

## How it works

- Each map has a **ground texture** (the expensive asset). It is built in **slices of about 4 ms per frame** in the background, so gameplay keeps running.
- While someone is waiting (loading screen visible), the build budget rises to about 40 ms per frame.
- After boot, the **neighbor maps** of the current map are prefetched. On phones (Lite mode), only the **current map and the one map ahead** stay in memory (`AHEAD`: Town→01→02→03, and 03→02); every other ground is freed. That keeps phones at about 39 MB for ground textures. Going back one map can show the loading screen for a moment. Desktops keep the neighbors.
- The loading screen shows a title, a progress bar, and a rotating tip. Tips are in both languages.
- Clicks are blocked only while the loading screen is visible.

## Helper API (prototype)

- `whenReady(maps, callback, labelKey)` — run callback when those maps are ready; shows the loader only if needed.
- `cutscene(maps, fn)` — same as whenReady, labelled as a cut scene.
- `queueBuild(map, priority)` — schedule background building.

## Open questions

1. In production, which assets are streamed: sprite atlases per map, monster sprites, audio?
2. Should the loader show a tip about the current map (e.g. Field 02 recommended CP 900)?
