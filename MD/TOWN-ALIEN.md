# Gadolinium: alien look and NPC spots (v18)

## 1. Look
- **Ground** violet to magenta with teal blades and glowing flowers; plaza stone is lilac. Cliff edge dark purple with a teal rim.
- **Sky** (behind the town): stars, a ringed planet, a teal moon and nebula glows that move slowly with the camera.
- **Buildings** pale lilac and mint walls, magenta, teal, violet and lime roofs, cyan glowing windows, and three floating crystals over every roof.
- **Lamps** glow cyan. **Trees** are teal, purple or pink. Glowing mushrooms fill the edges.
- **New props:** Rune Monolith (floating slab with glowing runes), Eye Stalk (its eye follows the player), Spore Pod, Tentacle Bloom, Floating Rock with crystals. Placement is by a fixed hash, so the town looks the same every time.
- **Air:** glowing spores drift up across the screen while you are in town.

## 2. NPC spots (nothing may cover an NPC)
- On start the game finds, for each NPC, the nearest open road or plaza tile where **no prop drawn later overlaps the NPC's sprite or name plate** (checked with each prop's screen box). NPCs stay at least 4.5 tiles from each other, outside the crystal circle and away from the portal.
- Wandering townspeople never pick a target near an NPC, stop if they get within 2 tiles, and are moved away at the start. Measured closest approach over 40 s: 1.96 tiles.
- **Name plate:** a bigger gold-edged plate above the head with the NPC name and a role tag (GUIDE, SHOP, QUESTS, ARCHETYPE). The quest "!" sits above it.

## 3. If you add props or NPCs
Give every new prop kind a depth key `k` and an entry in `staticBox` (screen box). The NPC spot search then avoids it automatically.
