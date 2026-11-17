# HumanCraft Video Studio V2 guide, applied to the xkcd-style clone (P5, 2026-11-08, LOCAL ONLY)

Source: `~/Downloads/HumanCraft_Video_Studio_V2_Complete_Guide.pdf` (35 pages; read in full this session via text extraction). Evidence: `model_sheets/MODEL_SHEETS_XKCD_WHATIF.md`, `motion_windows/MOTION_WINDOWS.md`, `CATEGORY_AUDIT.md`.

## 1. What the guide requires (with page refs)
- Motion from editable layered assets + authored keyframes, masks, rigs, cameras; text-to-video / image-to-video OFF by default for main shots; AI stills only if the owner approves (p.4–5, 18–19).
- No mandatory skill; choose a real, tested renderer and prove it with a tiny render; if none works, deliver assets + blocker note and never claim a video (p.1, 10, 17–18).
- Narration (MP3) is the timing authority; transcript times are suggestions; absolute frame = round(t × fps) (p.11).
- References teach grammar, not frames: STYLE_BIBLE, REFERENCE_BREAKDOWN with SEEN vs INFERRED, ANIMATION_GRAMMAR, FEEDBACK_MEMORY (p.8–10).
- Process: style still → moving 5–12 s proof with real narration → 10-dimension scorecard, worst 3 issues → fix → chapters → whole-video rhythm pass (p.16).
- "Intentional simplicity often looks more professional than adding more animation" (p.34); 1–4 motion mechanisms per shot (p.25).

## 2. Why xkcd-style fits the guide well (INFERRED)
The measured style is almost entirely 1-frame drawing swaps on a flat canvas (POP_ON 38%, CUT 23%, POSE_SWAP 3.5%), linear 6-frame dissolves, constant-speed write-ons and a few blurred camera moves (MOTION_WINDOWS). That is "scientific motion graphics" + "illustration and character craft" in the guide's terms (p.7), with very little interpolation. A layered, keyframed build can reproduce it closely; generated video would add motion the reference does not have.

## 3. Layer and rig plan (original assets; none exist yet)
- **Canvas layer:** off-white plate (#F7–F9 grey-white), 1920x1080 and 1080x1920 masters; alternates: black space plate, grey night plate with vignette, flat colour/gradient plates, map plates.
- **Narrator rig (original character, see PROMPT_PACK):** separate transparent layers: head (unfilled outline shape), torso line, 2 arms, 2 legs, modifier slots (hair/hat/glasses/headphones), held-prop slot (paper, pointer). Pivots: neck, shoulders, hips. Poses are DRAWN SWAPS (pose library PNG/SVG per pose), matching the measured 1-frame POSE_SWAP; an optional 6-frame linear dissolve between poses (measured once, 2LSyizrk8-0 G0092). No walk cycles unless a beat needs one.
- **Set pieces:** whiteboard frame + ledge (empty, so contents swap inside), question card box (text layer on top), desk/chair/computer, globe-on-stand, notebook page, end card and title card plates (original design).
- **Props/diagrams:** one transparent PNG or SVG per object; labels as separate text layers; red annotation strokes as vector paths (for write-on).
- **Text layers:** hand-print caps font (original near-match), serif for the question card and footnotes, red for marks. Every word an editable layer, not baked into art.
- **Anchors:** ruler/scale bar, black timer banner, map band as persistent top layers that survive cuts.
- **Shorts:** same assets, re-laid: board panel upper half, narrator below; map panel over black lower area with a white-outline narrator variant; wide diagrams panned as one layer.

## 4. Candidate motion mapping per entering class (all INFERRED until a render is tested; timings MEASURED where noted)
| Entering class (share long) | Guide technique (# in library) | Authored spec |
|---|---|---|
| POP_ON (37.9%) | #37 transform keyframe as a hold-step, #56 staged reveal and hold | opacity 0→1 in 1 frame, no scale, no overshoot (MEASURED 2/2) |
| CUT (22.6%) | #59 hard cut for contrast | 1-frame canvas swap |
| DISSOLVE/FADE (6.6%) | #41 linear opacity, cross-fade | exactly 6 frames, linear (MEASURED 3/3) |
| STATE_SWAP (6.4%) | #39 stepped curve | 1 frame (median 1, p90 3) |
| DRAW_ON_STROKE (6.4%) | #85 trim-path write-on | ≈constant speed, 4 frames median (p90 13); optional 2-frame slow start |
| DRAW_ON_TYPE (4.9%) | #78 typewriter | ≈1 letter per frame, median 6 frames |
| PAN/SLIDE/SCROLL (3.9%) | #08 pan, #09 whip pan, #55 motion blur | 8–12 frames, ease-in-out, directional blur peaking mid-move, hard landing |
| POSE_SWAP (3.5%) | #66 pose-to-pose (stepped), #54 on-ones | 1-frame swap; or 6-frame linear dissolve |
| ZOOM (2.0%) | #04 push-in / #05 pull-out, #55 blur | 9–10 frames; zoom-out S-curve, zoom-in ease-out |
| Rejected for this style | #43 overshoot/settle, #44 squash/stretch, #53 idle loops, #60 shake, #98 light leaks | 0/13 windows showed overshoot or bounce; holds are dead still |

## 5. The tiny proof the guide requires (not started; needs owner go-ahead)
- One 5–12 s ORIGINAL beat (original script line, original narrator), 1920x1080 at 24 fps: lecture frame → question card types on → board receives an object pop-on → red circle write-on → 6-frame dissolve to a dark scene. Then the same beat re-laid at 1080x1920.
- It needs real narration as the timing authority. Audio is BLOCKED here (no listening capability; ASR only). A silent proof can test motion only; sync must wait for owner-supplied narration and a human listen.
- Score it with the 10-dimension scorecard below; list the worst 3 issues; fix; re-render.

## 6. 10-dimension scorecard (guide p.16), with xkcd-specific "5" anchors (INFERRED)
| Criterion | What a 5 looks like for this style |
|---|---|
| Editorial purpose | every pop-on names the thing the narration just said; no decoration |
| Visual individuality | original narrator and set pieces, same grammar; not the source's lecture frame or mascot |
| Motion craftsmanship | 1-frame swaps crisp; no stray easing on pops; blurred moves land hard |
| Technical layering | clean alpha, no halos on the off-white canvas, consistent 8-px-at-1080 stroke |
| Camera direction | locked by default; ≤4% of events are pans/zooms, each motivated |
| Timing & narration | event every ~1.4–2.9 s, busy or calm by beat type; pops on the spoken word (needs audio) |
| Cohesion | one line weight, one hand font, red only for marks |
| Readability & restraint | ≤1 new object and ≤1 label per beat; holds long enough to read |
| Audio mix | BLOCKED / not ratable here |
| Reliability | render exists, ffprobe + decode pass, frames sampled and watched |

## 7. Reference breakdown: SEEN vs INFERRED
- SEEN (opened as images this pass): 240 clusters in 10 sheets across all 44 videos; 32 opening frames with measurement boxes; 12 title/end-card neighbourhood frames; 24 modifier frames; 2 full motion strips (22 frames). Plus the campaign's earlier reviewer views (recorded in each video's `review/`), not re-done here.
- MEASURED without viewing: rhythm and entering classes from all 5,458 ledger rows; palettes from sampled pixels; 13 motion windows' per-frame metrics.
- INFERRED: style rules, motion mapping, busy/calm drivers, font classes, layer plan.
- UNAVAILABLE: sound grammar, narration timing, music/SFX, true software curves, title-card animation detail.

## 8. Local renderer facts (re-checked 2026-11-08 ~18:05Z; nothing installed)
- Node v24.14.0, `npx` present. ffmpeg 9.0.1 with overlay, xfade, zoompan, gblur, boxblur; **no drawtext** (text must be pre-rendered as image layers).
- Python venv `~/YIOS-local-audits/tooling/visual-ct-scan-venv` has PIL + OpenCV 5.0.0 (frame compositing possible; the campaign's RT1–RT4 animatics were made with Python/ffmpeg drawing).
- NOT found on PATH: `remotion`, `hyperframes` CLI, Blender, ImageMagick. A `hyperframes` skill is listed in this Claude session, but its CLI is not installed or verified. CapCut.app exists (manual tool, not scriptable here).
- Per the guide no "video" claim is possible until a tiny test render passes. Installs need owner approval.

## 9. Timing authority
Narration is the timing authority (guide p.11). For xkcd evidence, audio is `BLOCKED_CAPABILITY` (`campaign/AUDIO_LISTENING_CAPABILITY.json`); all narration relations here are ASR_UNCERTIFIED. A clone must take its timing from the owner's own narration file, checked by a human listener.
