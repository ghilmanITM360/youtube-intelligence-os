# V8 deep audit (independent re-check, 2026-11-25)

Evidence used: V8 MP4 decoded and sampled every 2 s (40-frame sheet), V8 source `v8/tools/produce.py` + `rig_renderer.py` read in full, motion scores `M01–M12.json`, rig JSONs, asset files and provenance notes in V1–V8 manifests. V8 reports were read but not trusted: each claim below was re-checked against the file or frame.

## Cross-cutting findings (apply to every shot)

| Area | Verified finding | Evidence |
|---|---|---|
| Character provenance | **No character asset in V1–V8 was image-generated.** V1/V3–V6: Pillow-drawn PNGs ("not image-generated", "not AI generated"). V7/V8: Bézier SVGs emitted by `assets/character/build_rigs.py`. The owner's illustrated-asset requirement was never met. | `GhilmanProjects/skydiver-slowdown/ASSET_MANIFEST.md`, `v3/ASSET_MANIFEST_V3.md`, `v4/…V4.md`, `v8/RIG_MANIFEST.md` |
| Stationary character | Motion scores move joints by 1–3° (e.g. M10: head 0→1°, near_hand 0→−3°). 9 of 22 shots call the rig with `held=True` (frozen sample u=.32). | `motion_clips/compositions/M10.json`; `produce.py actor(... held)` |
| Environment | One reused composition: pale gradient + 4 scrolling clouds + `far_ridge`/`near_ridge` strip at the bottom. Ridge rises only 34 units over the whole film. No horizon, haze, terrain scale or altitude change. | `produce.py world()` |
| Descent speed | Clouds scroll 7–16 design units/s at every speed; travel is film time, not model speed. Fast and slow phases look the same. | `world(c,travel…)` |
| Force scale | Drag drawn at 91 vs weight 60 (≈1.5×) in "More drag than weight". A fixed-posture model from 10 km gives drag/weight ≈ 1.03 at most. Overstated by ~17×. | `force_pair(c,91)`; V9 `tools/model.py` |
| Force placement | Weight/drag arrows sit at fixed x=120/240 under the body, not at the centre of mass; on a separate white "paper" scene. | `force_pair()` |
| Velocity vs "DOWN" | The same dashed blue arrow is labelled "DOWN", "VELOCITY" and sits in place of weight in the hook; grammar shifts per shot. | `hook/slow/recap` branch |
| Instrument | Speed dial appears at 4 sizes (.66, .70, 1.25, .44) and positions with no motivating cut; needle 180→82 (hook), 12→167 (accelerate), 82→65 (insert), 65→50 (recap) — jumps between shots without a declared reset except S07. | `gauge()` calls |
| Text | Every shot has a 2-line 27-pt headline at the top; the picture reads as a slide deck. Footer disclaimers at 10 pt (~30 px) are unreadable on phone. | contact sheet |
| Sound | `AUDIO_MANIFEST.csv` lists two whooshes but `render()` maps only the narration track. **Zero SFX in V8.** | `produce.py render()` `-map 1:a` only |

## Shot-by-shot

| Shot | Time (s) | Observed defect | Scientific issue | Visual issue | Character issue | Camera issue | Sound issue | Required correction | Original asset required | Animation work | V9 status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 0–3.15 | Plane (top-view planform) + tiny figure on flat pale sky; "10 km" tag | Height not conveyed; no ground/horizon | No Earth, haze, depth | Figure scale .13, static | Static; no establishing → close progression | Silent | Wide with ground 10 km below, cloud deck, push-in | Side-view jump aircraft (Codex AC-01) | Camera push-in, figure drops below aircraft | **Rebuilt** (A1); aircraft is a procedural placeholder |
| S02 | 3.15–5.22 | Back view centred on blank sky | — | No ground below the rear view | Static replacement | Locked | Silent | Over-the-back view with terrain far below | Rear view illustrated (Codex CH-03) | Flutter, drift | **Rebuilt** (A2) |
| S03 | 5.22–11.15 | Needle rises then falls; "WEIGHT" arrow swaps to dashed "DOWN" | Hook claims slowdown with no time context | Floating gauge mid-frame | Held pose | Locked 6 s | Silent | Gravity arrow at CoM; wrist glance → insert labelled "later in the fall" | Wrist/forearm close-up (Codex CH-05) | Head/arm turn, insert push | **Rebuilt** (B1, B2) |
| S04 | 11.15–12.52 | Close-up OK | — | Blank sky | Small eye change | — | Silent | Keep; add blink/brow/head beat | — | Reaction curve | **Improved** (C1) |
| S05 | 12.52–16.8 | Front view + weight arrow below body | — | Slide headline | Static | Locked | Silent | Same weight arrow held identical across the question | — | Flutter, look | **Rebuilt** (D1) |
| S06 | 16.8–20.92 | Two faint curves, no relation to body | Airflow direction not legible | — | Static | Locked | Silent | Relative airflow streamlines around the body, moving upward | — | Animated dashes along potential-flow lines | **Rebuilt** (E1) |
| S07 | 20.92–23.14 | "Start from rest" with clouds | Reset OK | Text-only explanation | Held | — | Silent | MODEL frame, needle 0, altitude ruler, still world | — | Stillness (no streaks) | **Rebuilt** (F1) |
| S08 | 23.14–24.89 | Sparse marks | OK | Marks scattered, no region | Held | — | Silent | Equal-size air sample | — | Dots ∝ ρ from model | **Rebuilt** (G1) |
| S09 | 24.89–28.63 | Gauge rises | OK | Gauge large, floating | Small drift | — | Silent | Weight>drag at CoM, velocity lane, world streams faster | — | All driven by model v(t) | **Rebuilt** (H1) |
| S10 | 28.63–33.67 | More marks | No equal-area comparison | — | — | — | Silent | Two equal samples: at 10 km vs now | — | Dots from ρ(h) | **Rebuilt** (I1) |
| S11 | 33.67–38.72 | Drag grows on paper | Mixes density change with speed change | Detached from body | Held | — | Silent | Dedicated same-air, two-speed comparison (drag ∝ v²) | — | Panel build | **Rebuilt** (J1) |
| S12 | 38.72–47.71 | Drag grows to 1.5× weight | **Overstated** | Detached arrows | Held | Locked 9 s | Silent | One scale, weight-length reference tick, drag → 1.0 → 1.03×; 10× net inset labelled | — | Model-driven arrow lengths | **Rebuilt** (K1) |
| S13 | 47.71–49.41 | Velocity arrow alone | OK | Paper | Held | — | Silent | Velocity lane beside body, still down | — | — | **Rebuilt** (L1) |
| S14 | 49.41–52.19 | Net arrow ≈ weight length | **Net magnitude invented** (not drag−weight) | — | Held | — | Silent | Net = drag − weight, drawn 10× and labelled | — | — | **Rebuilt** (L1) |
| S15 | 52.19–55.57 | Gauge 180→82 | Different scale from S09 | Gauge size change | Small | — | Silent | Same card, same scale, needle monotone down | — | — | **Rebuilt** (M1) |
| S16 | 55.57–57.16 | Big floating dial | Unmotivated size jump | No hand/wrist | — | Unmotivated | Silent | Wrist insert (same dial) motivated by earlier glance | Wrist close-up (CH-05) | Slow push | **Rebuilt** (N1) |
| S17 | 57.16–59.35 | Map plane + gloves | OK | Map looks flat | — | Zoom only | Silent | Straight-down perspective terrain at model altitude | Codex EN-04 optional | Ground grows | **Rebuilt** (O1) |
| S18 | 59.35–61.93 | Back view on sky | — | No ground relation | Static | — | Silent | Over-the-back with near terrain | CH-03 | — | **Rebuilt** (P1) |
| S19 | 61.93–66.03 | Gauge 65→50 | Scale mismatch | — | — | — | Silent | Speed-vs-time sketch from model (rise, peak, ease, never zero) | — | Curve draws on | **Rebuilt** (Q1) |
| S20 | 66.03–70.53 | 1.5× drag | **Overstated** | Paper | Held | — | Silent | Same honest force scene as K1 | — | — | **Rebuilt** (Q2) |
| S21 | 70.53–74.52 | Framed front view | OK | Box on paper | — | — | Silent | Pull-back to tiny figure over landscape, MODEL frame | — | Camera pull | **Rebuilt** (R1) |
| S22 | 74.52–78.2 | Two density boxes | Implies density alone | — | — | — | Silent | Same model, other posture/conditions curves | — | Curves fade in | **Rebuilt** (S1) |

Verification status in the last column was checked by rendering V9 stills at each listed time and reviewing the full V9 contact sheet (`qa/V9_contact_1p5s.jpg`); see FINAL_VISUAL_AND_AUDIO_QA.md.
