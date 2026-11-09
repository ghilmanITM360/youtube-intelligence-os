# Visual, motion and production DNA

Scope: inherited observations from ten long-form and six Shorts; source tables remain untouched. Assets are appearances/labels, not verified unique artwork files. Exact software, rigs, easing, AI usage and authoring labor are unknown. Below, OBSERVED means the existing visual QA records; ENGINEERING METHOD means our independent implementation.

## Character and design language

OBSERVED: recurring peach round face, black spiky hair/contours, thin limbs and small eyebrow/mouth changes. White fields, outlined buildings, green money/country props, red warnings, hand-lettered annotations and conventional chart/document type recur. Head/body proportions appear stable enough to identify a narrator, but no measured universal ratio, exact font or palette hex is established. Props such as banknotes, bonds, maps, buildings, pointers and labeled boxes turn systems into actors. Host facing/pose changes add emphasis.

Counterexamples: dark evidence panels, full trading-floor/lab/bedroom/van environments, logos, photographs, imported memes and pixel imagery. Therefore “everything is white-background vector animation” is false. Typography varies with handwritten labels, printed source excerpts and bold thumbnail judgments; do not assert one font. Source visibility/rights are unverified for imported material.

References: [visual DNA](../../data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/VISUAL_DNA.md); [asset master](../../data/extracted/forensic-analysis/casually-finance/2026-10-12/03_MASTER_DATA/MASTER_ASSETS.csv); sampled state IDs in [independent continuation](../../data/extracted/forensic-analysis/casually-finance/2026-10-12/07_VALIDATION/NEW_MAC_TARGETED_VISUAL_QA_2026-10-12.json). Exact object dimensions/pivots are our future specification, not competitor measurements.

## Timeline rhythm: measured units kept separate

| Format | Runtime s | Reviewed shots | Stable states | Mean / median shot s | Shots/min | States/min |
|---|---:|---:|---:|---|---:|---:|
| Long-form selected 10 | 7,503.2 | 1,401 | 4,194 | 5.356 / 4.333 | 11.203 | 33.458 |
| Shorts selected 6 | 375.575 | 45 | 314 | 8.346 / 6.434 | 7.189 | 49.205 |

Source: [editing DNA](../../data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/EDITING_DNA.md) and SHOTS/STATES master tables. Shot-duration distribution varies: bond mean/median 3.58/2.96s; housing 7.67/6.58s; MicroStrategy 7.27/6.55s. No ideal duration is identified. SpaceX Short has only 4.2 shots/min but 79.5 states/min; captions create frequent changes inside a held composition. States/min is a count of labeled information changes, not continuous motion density, cuts or attention. Scene complexity is qualitative in reviewed descriptions, not a certified pixel/object complexity score. Per-video ASR speeds approximately 152–199 words/min long-form, 186.5–212.5 Shorts; exact vocal tempo is unverified.

Long-form alternates sparse narrator/prop scenes with dense source/comparison panels. SpaceX 110–129s relatively sparse versus 173–189s comparisons and 732–750s source excerpts. Dense evidence should be simplified or held longer, not automatically cut faster. Narration-to-visual overlap derives from ASR, not listened intentional sync.

## Source-confirmed motion sequences and independent methods

| Exact source locator | Observed result / confidence boundary | Independent implementation |
|---|---|---|
| -X6YzlY_8tM M0026, 12.833–13.25s; disposition register | Existing composition persists; consumer comparison added. Original CUT label corrected | Reveal child bar/logo groups on unchanged scene; do not replace root |
| 0ll9rEtoRrs M0004, M0020; reviewed motion JSON | Progressive counter entrance; chart replacement followed by enlargement | Separate reveal and scale phases; active-pixel interval is not entrance duration |
| -X6YzlY_8tM M0047; reviewed motion JSON | Cut followed by paper enlargement | Step clip switch at frame N, animate paper group's local scale afterward |
| JsK53moCyZA M0032, 16.967–20.633s | Scene replacement then rising head | Switch visible scene; translate head/character group from below; parent inherits camera |
| JsK53moCyZA M0046, 30.4–32.867s | Cut then paper enlargement | Local document pivot and scale; do not claim source used camera zoom |
| rSa2aziEsAI M0010, 20.333–21.1s; M0027, 38.8–39.633s | Character rises; banknote transfers upward | Y-translation with start/end positions; separate hand and prop layers |
| 6S3PzAUFnXQ M0030, 33.667–34.333s; M0045, 51.75–52.542s | Cut then host entrance; chart slide plus comparison build | Sequence step, translation, masked reveal on independent lanes |
| 2EZzwupIa80 M0040, 47.125–48.583s | Scene replacement then trace reveal | Replace composition then reveal SVG stroke using dash offset |
| roe3SgezmmU M0001, 0.042–0.667s; M0005, 9.708–10.292s | Chart exposes progressively; company characters added in stages | Clip/mask growth; one child visibility track per company |

Evidence: [664-candidate disposition register](../../data/extracted/forensic-analysis/casually-finance/2026-10-12/07_VALIDATION/MOTION_QA_DISPOSITION.csv), per-video MOTIONS.csv and review JSONs. All 664 candidates triaged, two exact mechanisms unresolved. The larger 4,484-row label census includes unreviewed/provisional labels; counts such as CUT 1,721/POP_IN 685 are label frequencies, not fully certified mechanisms. Do not count every active-pixel episode as a cut. Precise interpolation/easing and camera-versus-object transforms remain unverified.

## Shape, layer and rig architecture: our design

SVG root has world coordinates 1920×1080. Scene camera wraps environment, props and characters; fixed caption/source UI lives outside camera. Character root owns torso/head/arm groups. Shoulder/elbow pivots are local, transforms compose parent-first. Use vector paths with stable point topology for expression/shape interpolation; swap paths when topology differs. A mask belongs to the revealed content, not the entire scene unless the transition calls for it. Order: background, environment, diagram, character, pointer, highlights, source UI/captions. PNG layers are appropriate for authorized raster imports, never a reason to flatten an editable rig.

For original keyframes store integer frame, target ID, property, value and easing. A pure evaluate(frame) derives every transform and visibility directly from time; no accumulated random increments. Pop-in uses visibility plus an explicit short scale envelope; position changes interpolate local coordinates; reveal clips content or advances stroke length; camera push changes only world parent; pose/expression switches change relevant children. Export start/middle/end states before rendering. Imported footage playback belongs to the selected renderer and cannot be replaced by a CSS opacity simulation.

The same outcome can be represented by an FFmpeg expression/filter timeline, an SVG/HTML composition, a Remotion frame function or After Effects transform/mask keyframes. Tool choice does not tell us what the competitor used. For a solo creator, an editable deterministic SVG rig plus frame-based composition is sufficient for this demo; use an NLE for authorized voice/music mix and final sound QA. Retain stems, source dates and project settings.

## Reuse: observed versus proposed

HOST appears repeatedly in many states (e.g. roe3SgezmmU asset HOST: 186 state appearances, 99 shots, 262.8 recorded on-screen seconds). This supports visual recurrence; cross-video binary reuse is unknown. Buildings/money/maps/arrows and comparable object arrangements recur. Assets identified as REUSED within a video are analyst labels; 2,196 master asset rows must not be called 2,196 unique illustrations.

Our reusable modules: one original host rig, one bank/building family, three environments, chart axes/data styles, source-card/date/unit component, cash/loan/bond props, arrows, labels, comparison panels and timing presets. Distinct shots come from different argument relationships, layout and timing, not only recoloring files. A new shot must communicate a new beat. See asset factory for authored component versus export counts.

## Visual weaknesses and repair policy

Dense source text cannot be assumed readable on mobile; enlarge the exact supported fragment and carry title/date/unit to a persistent citation strip. Qualify projections on screen. Use predictable color meanings but not color alone. Name dates and denominators before animating a comparison. Sponsor UI and meme imports need authorized provenance. Expressions should support narration, not assert a real person's emotions. Continuous easing/sync and full audio still need human QA; no universal “high motion makes videos win” finding.

## Existing production technology, inspected read-only

Dr Rehan branch frozen at `8daa1c831834ff30f2b72180a2e233b566b36468`: `projects/dr-rehan-test-videos/project/src/rig.tsx` separates look/pose records, local joint points, interpolated angles and parent transforms; `src/lib.ts` evaluates keyframes from absolute time. The established project also records full-listening and fine-motion limits. Our method uses these technical principles independently; no medical art, scripts, narration or implementation is copied or modified. [Read-only rig reference](https://github.com/ghilmanITM360/youtube-intelligence-os/blob/8daa1c831834ff30f2b72180a2e233b566b36468/projects/dr-rehan-test-videos/project/src/rig.tsx).

## Rendered follow-up and attribution correction (2026-10-13)

The archived YouTube description for roe3SgezmmU credits original hand-drawn illustrations, visuals and animation to a freelance artist. This verifies the channel's self-report, not its actual software, artist workload or AI usage. Budget custom illustration and acting separately from keyframe engineering. The new [42-second original Remotion pilot](PILOT_REMOTION/README.md) demonstrates rig consistency and real animation but shows [illustration/acting quality gaps](PILOT_REMOTION/QUALITY_REVIEW.md); it does not certify parity or publication readiness. The prior Word/Excel reports are the earlier research snapshot; this follow-up supplies the corrected feasibility evidence.
