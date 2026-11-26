# Asset generation failure: root-cause audit (Batches 0, 0b, 1, 2)

Written 2026-11-26 by Claude (production director) after reading the four Codex run logs (`/private/tmp/claude-501/codex_batch{0,0b,1,2}.log`), `~/.codex/config.toml`, Codex's imagegen skill (`~/.codex/skills/.system/imagegen/SKILL.md`), every `deliveries/batch*/ARTWORK_QA.md` and `IMAGE_GENERATION_PROMPTS.md`, and by **viewing every Batch 1 and Batch 2 PNG myself on a magenta backing** (magenta exposes any stray alpha).

## Summary: the failures were mostly ours (the process), not the generator's

| # | Root cause | Evidence | Which failures it explains |
|---|---|---|---|
| R1 | **No reference image ever reached the generator.** Codex's built-in `image_gen` can only edit/condition on an image that was first loaded with `view_image`; our prompts never required that, and nothing was attached with `codex exec -i`. | batch2 `IMAGE_GENERATION_PROMPTS.md`: "No source image was passed to generator"; imagegen SKILL.md line 417 | geometry differs from the photos; views disagree; tilt wrong |
| R2 | **Every view was generated independently from text.** There was no master image, so each call re-invented the hardware. | batch2 prompts: 3/4, top and side each = "common prompt + view sentence" | object geometry changes between views; layers cannot register |
| R3 | **Overloaded runs.** One run = independent research + 3-4 images + 9 required documents + validation + contact sheet, at **reasoning effort `low`** (the config default). | `~/.codex/config.toml`: `model_reasoning_effort = "low"`; batch2 prompt lines 16-18 | shallow research, 1 attempt per item, self-QA "blocked" with no retry |
| R4 | **Comparative wording invites a reference sheet.** "Orthographic top view of *the same* supported instrument" asks the model to show the thing it is "the same" as. | batch2 top-view prompt; the result shows a 3/4 view and a front view side by side | multiple perspectives in one image |
| R5 | **Numbers the generator cannot measure.** "tilted 30 degrees", "apex exactly at canvas centre", "depth 6 %" are not controllable by text. | side view delivered at ~35-39 deg; apex 2-8 px off centre | incorrect tilt; misaligned apex |
| R6 | **Canvas sizes the generator does not produce.** Briefs asked for 3000x2000, 4096x4096, 2160x3840; the generator's native outputs were 1254x1254, 1536x1024, 1774x887, 1672x941. | batch0/1/2 `ASSET_MANIFEST.csv` `generation_px` | resolution mismatch; forced resampling |
| R7 | **Transparency is generated, not authored.** The generator's alpha leaves colour under alpha 0 and soft fringes; Codex repaired the RGB-under-zero-alpha afterwards, but fringes stay. | batch1 QA (RGB under zero alpha in 8 files), batch2 validator `semi_transparent_share` 2-24 % | unwanted pixels in alpha |
| R8 | **Asking the generator for things that are measurement or code.** Pivots, face-plane corners, recess centres and polar geography were requested from an image model. | batch2 PIVOTS.json null; batch1 polar patches with invented coastlines | rigging data missing; uncertified geography |
| R10 | **Our brief was scientifically wrong about the tilt.** RETRO_004 asked for "30 deg back from vertical" (= 60 deg from the ground); the research note computes the face normal ~23 deg from vertical (panel ~23 deg from the ground), and AS11-40-5952 shows a low panel. | batch2 prompt vs `deliveries/batch2/RESEARCH_NOTES.md`; photo viewed 2026-11-26 | "incorrect tilt" was partly the brief's fault; guide now drawn at 23 deg |
| R9 | **Self-report was taken as the verdict.** Codex marked everything "blocked" and stopped after one attempt; nobody checked whether the delivered file still had the defect. | my inspection below: the 3/4 frame has **no** backdrop in the delivered file | good candidates discarded; no correction loop |

## Failure by failure: cause, corrective strategy, acceptance test

| Failure | Cause | Corrective strategy | Acceptance test (who runs it) |
|---|---|---|---|
| Unwanted backgrounds | R7, plus scene words in the prompt ("resting on", "lunar") make the model paint a floor | Prompt says *isolated object, transparent background, no ground, no shadow*; Claude's composite adds ground and shadow. If a backdrop still appears, one **edit** call on the same image: "remove the background only", never a regeneration | corner alpha = 0 at all 4 corners; one large alpha component; < 0.5 % of opaque pixels outside the object's convex hull (Claude, `tools/validate_asset.py` + magenta preview) |
| Multiple perspectives in one image | R4 | One call = one view. Never say "same as"/"matching"; attach the master image instead and say "redraw THIS object from the side". Prompt ends with "one single view, no inset, no second drawing" | alpha has exactly one large connected component (Claude, validator `components.large` length = 1) |
| Geometry changes between views | R1, R2 | **Master first.** One approved master per object; every other view/layer is an *edit* of the master (`view_image` master, then `image_gen` edit) | Claude overlays a silhouette of the derived view on the master's construction guide; handle, legs, panel proportions within 5 % |
| Incorrect tilt / angles | R5 | Claude draws a **construction guide** (thin-line side silhouette at the true angle, a compositing aid, not artwork) and Codex edits the master to follow it | Claude measures the panel edge angle on the alpha: within +-3 deg of target |
| Alpha with unwanted pixels | R7 | Codex runs the existing alpha repair (zero RGB under alpha 0); Claude's compositor premultiplies and erodes 1 px on import (documented, non-destructive: source file untouched) | `rgb_under_zero_alpha_px` = 0; no magenta halo visible at 200 % (Claude) |
| Layers do not register | R2, R8 | Layers are cut **from the master canvas** (same size, same origin), hidden areas extended by an edit call with the layer mask; Claude supplies the masks | Claude re-composites the layers and diffs against the master: mean abs diff < 3/255 inside the master alpha |
| Resolution | R6 | Ask only for native generator sizes: 1024x1024, 1536x1024, 1024x1536 (state which). Large maps come from public-domain NASA data, not from the generator. Up-scaling is Claude's documented step | file size equals one of the three native sizes, `resampled=False` |
| Rigging failures | R8, R2 | Pivots, overlap and registration are **measured by Claude** on the delivered master and its layers; Codex supplies overlap artwork (the hidden part of each limb drawn past the joint) | rig test in code: rotate each part +-25 deg about its pivot, no gap or tear visible in a rendered moving test |
| Overloaded prompts | R3 | One run = one deliverable (+ a 5-line notes file). Reasoning effort `high` on every run (`-c model_reasoning_effort="high"`) | run log shows `view_image` for every cited reference before the first `image_gen` call (Claude greps the log) |
| References unused | R1 | Attach the 2-3 decisive photographs with `codex exec -i` and require `view_image` of them; a run whose log has no `view_image` is rejected unread | as above |

## What my own inspection changed (2026-11-26)

| Asset | Codex said | I see (magenta backing, full size) | Decision |
|---|---|---|---|
| `retro_frame_34.png` (1500x1000) | opaque grey backdrop | corners alpha 0; one object; no backdrop in the delivered file | **Master candidate** for RETRO_004 (proportions read as the Apollo 11 LRRR: silver frame, white base rails, rear bail, tilted dark panel) |
| `retro_frame_top.png` | two views | confirmed: a 3/4 view and a front view side by side | reject. **No storyboard shot uses a top view** (manifest: B17/B18 = 3/4 hero + low surface): the top view is dropped, not regenerated |
| `retro_frame_side.png` | ~39 deg | panel edge measured ~35 deg from vertical; handle and support differ from the 3/4 | reject; one focused edit of the 3/4 master with a construction guide |
| `retro_cube_3face.png` (1254) | apex ~(625,631) | edge centroid ~(619-625, 629): 2-8 px from centre (< 0.7 %) | **Candidate**: Claude re-centres by translation (documented minor repair); no regeneration |
| Batch 1 cloud tiles (4) | grey relief in alpha | clean on magenta; read as clouds | **Candidates**: Claude composites them into the equirectangular cloud layer (compositing is Claude's role) |
| Batch 1 atmosphere slices (3) | sizes off | usable layers | candidates; Claude scales them in the composite |
| Batch 1 polar patches (2) | geography uncertified | invented coastlines (Arctic islands and Antarctic coast do not match NASA maps) | reject as geography. Poles come from the NASA base map; Codex repaints only if the polar render test fails |
| Claude's procedural cloud layer `assets/earth/earth_clouds_proc_4096x2048.png` | (Claude's own) | blobby hard-edged masses; colour smears the land at partial alpha | **rejected**, and it was outside Claude's role (clouds are Codex artwork). Kept on disk as a rejected file, not used |

## New run protocol (applies from Batch 2R onward)

1. `codex exec -C codex_handoff -c model_reasoning_effort="high" -i <master or 2-3 decisive refs> "<one deliverable>"`.
2. Prompt states: one deliverable, native size, single view, isolated, what to look at in each attached image, and the exact acceptance test.
3. Codex writes `deliveries/<run>/` = the image + `NOTES.md` (<= 10 lines: references viewed, what was assumed). Nothing else.
4. Claude: grep the log for `view_image`; validator; magenta preview; measured test; then verdict in `qa/asset_tracker.csv`.
5. On fail: one *edit* call naming the single defect. Never regenerate a whole family for one defect.

## Results of the new protocol (same day, runs R2a, B3M, B4M, B5M, B5L, R2b, B1c, B5L2)

All runs: Codex bundled CLI 0.171 (`/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex`; the `codex` on PATH is 0.153 and cannot use the configured model), `-c model_reasoning_effort="high"`, references attached with `-i`, prompt after `--`, stdin closed. Every log shows `view_image` on the references before generation (grep count 4 per run).

| Run | Ask | Result (Claude-measured) | Verdict |
|---|---|---|---|
| R2a | RETRO_004 side view, edit of the 3/4 master + 23-deg guide | one component, corners 0, **tilt 23.6 deg** | candidate (base/handle differ from master) |
| B3M | lunar environment master | horizon at row 398 (26 %), foreground clear, shadows to the right | master candidate; used in P13 and P05 |
| B4M | observatory exterior master | one dome, two open leaves, top third clear sky | master candidate |
| B5M | astronaut master | one figure, visor down, anonymous, corners 0 | master candidate |
| B5L | torso + 2 arm layers from the master | silhouette IoU 0.978; layers coherent; arms carry overlap | candidate; rigged in P05 |
| B1c | 2 cyclone variants | edges alpha <= 1; distinct shapes | candidate; in the cloud composite |
| R2b | one-defect fix of R2a (base/handle) | **regressed**: tilt 23.6 -> 14.7 deg; base unchanged | rejected (`runs/_rejected/`) |
| B5L2 | small shoulder-cap layer on the full canvas | **no alpha = 0 anywhere**, noise over the canvas, cap tiny | rejected |

Seven of eight single-deliverable runs produced usable images on the first attempt, against zero approved images in Batches 0-2. New lessons:

| # | Finding | Rule from now on |
|---|---|---|
| R11 | The generator fails when asked for a small piece on a mostly empty transparent canvas (B5L2) | small parts are generated **filling their own tight canvas**; Claude registers them to the master by measured offset/scale |
| R12 | Edit mode keeps geometry but re-renders texture (B5L: 15/255 mean difference, IoU 0.978) | layer acceptance = silhouette IoU >= 0.97 + stacked layers coherent with each other; the master is a reference, not a pixel target |
| R13 | A one-defect edit can break an earlier pass (R2b tilt) | after every edit, Claude re-measures all earlier passes, not only the named defect |
| R14 | Square native size is 1254x1254 (B1c, and Batch 0) | briefs ask for 1254x1254, 1536x1024 or 1024x1536 |

## Production pass 2 (2026-11-26 afternoon): runs B4L2, B4P, B5C, B5P, B5PA, B5PR, B5PR2

| Run | Ask | Result (Claude-measured) | Verdict |
|---|---|---|---|
| B4L2 | slit-open building (one-defect edit of B4L) | IoU 0.992 vs closed layer; slit open and dark | candidate; RIG_002 |
| B4P | clean sky + mountains plate (edit of B4M) | top 500 rows differ by 2.98/255; no building trace | candidate; parallax plate |
| B5C | shoulder piece on its own tight canvas (R11) | clean sleeve dome; arrived at 1254 px, not the 1024 px asked (R14 confirmed again) | spare: rig v2 skinning made it unnecessary |
| B5P | astronaut + reflector interaction, one composition | grip on the handle; reflector matches the master | master candidate |
| B5PA / B5PR | layer cut of B5P (astronaut only / reflector only), hidden parts painted | restack IoU 0.983 | candidates; rigged in P06 |
| B5PR2 | one-defect edit: draw the 10x10 cube grid on the panel | **IoU 0.327**: the whole object was re-rendered larger and moved | rejected (R13); Claude composited the existing Codex cube-array assembly instead |

Lessons:

| # | Finding | Rule |
|---|---|---|
| R15 | Layer cuts of an approved composition work on the first try when both layers are asked for in separate runs (B5PA, B5PR) | interactions are generated as one composition, then cut into one run per layer |
| R16 | Asking for small repeated detail (100 cubes) inside an existing object makes the generator redraw the object | repeated technical detail comes from an already approved part (cube instances) composited by Claude; Codex is not asked for it again |
| R17 | Some art fixes are rig fixes: the shoulder gap came from a rigid swing about one pivot, not from missing art | before commissioning corrective art, test a deformation fix in the rig (P05 v2) |
