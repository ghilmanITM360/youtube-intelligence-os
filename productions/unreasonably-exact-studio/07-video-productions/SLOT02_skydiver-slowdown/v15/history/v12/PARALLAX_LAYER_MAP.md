# V12 parallax layer map

Depth in V12 comes from one **world camera**, not from sliding flat pictures. `Cam` in `tools/v12.py` is a pinhole camera over a terrain mesh measured in metres. Every layer is placed at a real distance, so apparent motion falls off with depth automatically. Overlays (figure, aircraft, drop line) are positioned through `cam.proj()`, the same world-to-screen function, so they stay attached during camera moves.

| # | Layer | How it is built | Depth / motion rate |
|---|---|---|---|
| 01 | Sky gradient | `sky()`: deeper blue only at altitude | infinite (static) |
| 02 | Far haze | `haze_k`: exponential distance haze (about 40 km scale) plus a horizon haze band | follows the horizon only |
| 03 | Distant terrain and hills | `far_patches()`: widening depth bands of irregular fields, out to 240 km; low-contrast hill line | very slow |
| 04 | Mid terrain | `near_patches()`: jittered field mesh in the Codex landscape palette, crop rows close up, 220 forest clumps, 3 roads, river | slow → fast as altitude falls (O1, P1) |
| 05 | Distant cloud deck | 240 Codex cloud sprites at 1.9–2.3 km height, depth-sorted and hazed | moves with the camera; z-sorted |
| 06 | Character environment | `passing_wisps()`: Codex wisp sprites passing at 2.2 × model speed | fast |
| 07 | Character rig | `side_rig()` / `body()` | subject |
| 08 | Near clouds | `near_clouds()`: three large Codex cumulus sprites crossing the lens (A1 wipe) | fastest; occludes everything |
| 09 | Foreground air | `air_streaks()` (relative-air specks, rate = model speed) and streamlines (`airflow`, back + front passes) | rate = model speed |
| 10 | Science graphics | arrows, lens, ruler, trail, graph | screen-locked or body-attached |
| 11 | Labels / captions | `chip()` small labels. Captions are a separate overlay pass (`--out qa/caption_overlay.mov`). | screen |

## Per shot

| Shot | Layers | Camera |
|---|---|---|
| **A1** | 01–05, aircraft (world-positioned), figure (world-positioned), 08 | Dolly 1.1 km → 150 m toward the figure, descending 250 m, tilting 4°→10°. The near-cloud wipe covers the cut. |
| **A2** | 01, 03–05, 07 (back), 09, drop line | Looking down 62°; settle-in push 1.08 → 1.0 |
| **B–D, model shots** | 01–07, 09–10 | Tracking at the body's height; terrain and wisps run at the model speed |
| **E1** | 01–07, 09 back (behind the body), 07, 09 front (outer lines only) | Locked off: occlusion shows the body sits *inside* the flow |
| **N1/O1** | 01–05, own forearm (screen) | First-person tilt 64° → 86°; the arm exits and the ground approaches |
| **R1** | 01–05, figure | Pull-back 870 m → 7 km behind and 700 m above |

Not used: a separate painted-horizon plane. The Codex landscape is used only as the palette source, because the painted image cannot parallax against the mesh without visible sliding.
