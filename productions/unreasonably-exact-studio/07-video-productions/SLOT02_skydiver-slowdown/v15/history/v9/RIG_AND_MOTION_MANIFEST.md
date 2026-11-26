# V9 rig and motion manifest

## Rigs

The rigs are unchanged from V8 and live in `rigs/<view>/rig.json`. They are forward-kinematic hierarchies with clamped joint limits, evaluated per frame by `tools/rig_renderer.py`. The views are side, three_quarter, back, front (front is unused in V9), closeup, pov and instrument. See `v8/RIG_MANIFEST.md` for the full pivot table. All character art is a **procedural placeholder**; see CODEX_MISSING_ASSET_REQUEST_V9.md.

## Why V8 looked static (verified)

V8 motion scores moved joints by only 1–3° per shot, and 9 of 22 shots froze the rig at a single sample (`held=True`). V9 does not use the V8 motion scores; they are copied to `motion_scores/` for reference only.

## V9 motion system (tools/v9.py)

| Layer | Function | What it does | Amplitude |
|---|---|---|---|
| Airflow flutter (secondary) | `perf_flutter(t, amt, seed)` | Two-frequency, non-repeating sinusoid per joint. Hands and feet flutter fastest (0.8–1.3 Hz), forearms and shins at 0.3–0.5 Hz, upper limbs, thighs and head slowest (0.13–0.3 Hz), so motion follows through from parent to child. The seed differs per shot, so no loop repeats across shots. | hand/foot ±7°/±6°, forearm/shin ±5°/±4°, upper arm ±3°, thigh ±2°, head ±2.5°, torso ±0.8° (× amt) |
| Intentional acting | per-shot `extra` dict | B1: head settles −3°. B2: glance at the wrist (head +14°, upper arm +18°, forearm −30°, hand +12°, ease-out 0.9 s). D1: head searches ±5°. E1: head sway ±4°. A2: arms spread out ±6°. P1: head lifts. | as listed |
| Reaction (closeup) | C1 | Eyes lead (+4 px), brows lift (−6 px) 0.3 s later, blink at 55–62% of the shot, head tilt −4°, mouth opens 4°. | — |
| Model-section restraint | `model_scene` | **Body posture held fixed.** Only flutter is applied, with amt = 0.25 + 0.45·(v/80), so it calms as the modelled speed falls. At the rest reset amt = 0.12. The causal story is never carried by a posture change. | ≤ 0.7 of hook amplitude |
| Camera | `Cam` + per-shot keys | Push-in (A1 ×3.6, ease-in-out), wrist insert push ×1.06, pull-back (R1: 0.9 → 7 km behind, F 700 → 380), final drift (S1). | — |
| World travel | `air_streaks`, `passing_wisps` | Speck speed = 4.8·v + 20 units/s and wisp speed = 2.2·v, so a faster model speed reads as faster world motion. Both are 0 at model rest. | — |

## Instrument

- **One identity:** the same `instrument` rig (plate plus pointer, pivot 140,139) is used everywhere. Needle angle is −72° + 144°·v/90 m/s on a qualitative scale, with no numerals.
- **Placement:** a fixed-size card at a fixed position (306,118) for the whole model section, and the wrist insert (B2, N1), reached by a motivated cut from the glance.
- **Continuity:** the needle goes to 0 at the declared model reset (F1). After 47.7 s it only moves down, which `--check` asserts.

## Verification performed

- `python tools/v9.py --check` passes. It confirms 22 contiguous shots, monotonic model time, v ≥ 0, altitude never rising, the needle monotonic after 47.7 s, and a minimum altitude of 445 m (no ground contact).
- `ffmpeg freezedetect` (noise 0.0008, ≥0.75 s) on the final MP4 found only the intended model-rest stillness at 21.9–22.7 s after the S1 drift fix. See the QA file for the re-run.
