# Asset factory and Codex feasibility

**Yes: Codex can produce many consistent useful assets when the design rules and components are explicit.** It cannot guarantee hundreds of distinct, art-directed organic illustrations at a fixed speed. The source corpus demonstrates recurring character/prop appearances, not the competitor's internal asset factory or AI usage. Everything below is our original implementation plan.

## What scales and what costs design time

| Category | Feasibility | Required control |
|---|---|---|
| Icons, arrows, labels, chart axes, simple diagrams | Programmatically straightforward | Unit/date semantics, spacing, legibility and consistent stroke/fill tokens |
| Reusable props, color variants, layouts, keyframe presets | Programmatically straightforward | Stable dimensions, pivots, schema and deterministic evaluation |
| Character poses/expressions/clothes | Possible with reusable design system | Approved original bible, joint limits, silhouette comparison, human face review |
| Repeated environment / arrangement variations | Possible with reusable design system | Fixed perspective, compositional hierarchy, layer/mask tests |
| Scene-specific original illustrations | Possible, with art direction | A reviewed sketch and integration into the style system |
| Organic anatomy, sophisticated acting, unique complex scenes | Additional design effort | Skilled manual drawing, pose correction and frame-by-frame review where needed |

A render is not a new authored illustration. Three poses × three expressions = nine character states from shared components, not nine wholly independent artworks. Recoloring 50 props into ten palettes yields 500 exports but only 50 base prop designs. Budget authored components, derived variants and meaningful shot compositions separately.

## Proposed taxonomy and first-library estimate

| Category | Authored items | Derived variants / use |
|---|---:|---|
| Original host rig | 1 | 8 poses × 6 expressions × 3 clothing palettes = 144 combinations before invalid-pose filtering |
| Supporting character silhouettes | 3 | Limited pose subsets; do not promise all 144 combinations per character |
| Finance/household props | 25–40 | Size/color/count variants; loan, bond, wallet, home, bank, calendar, fund, document |
| Icons / arrows / brackets | 15–25 | Stroke/shape variants and semantic direction |
| Chart/diagram/source-card templates | 8–12 | Data-bound instantiations; each dataset is checked independently |
| Environment kits | 3 | Desk/study, street/bank, simplified house interior; 5–8 modules each |
| Motion presets | 8–10 | Reused timings retimed to narration, not new illustrations |
| Unique scene illustrations per 6–8m episode | 2–6 | Budget separately after storyboard; never auto-generate every scene |

Approximately 55–85 base visual components plus environments/rigs can support hundreds of exported variants and dozens of distinct explanation shots. These are proposed planning counts, not measured competitor inventory or throughput guarantees. Reject combinations with occlusion, impossible hands or missing perspective.

## Original character bible

Demo character: **Mira**, rounded-square warm-ochre face, plum side-part hair, teal jacket, cream shirt, broad rounded torso, solid trousers/shoes and rounded limbs. This differs from the competitor's peach round stick-figure narrator. Neutral stance is 360×540 local units; face center near (180,135), shoulders at (115,240)/(245,240). Preserve face width/height, eye spacing, nose anchor and hair contour across expressions. Proportions and hex colors are our tokens, not source measurements.

Token set: ink #243247, jacket #157A78, face #EDB76A, accent #D55B47, paper #FFF9EC, violet #7358A6. Use labels/shapes as well as color. Source cards remain sober and readable; commercial cards have an explicit sponsorship label.

| Pose | Neutral | Concerned | Curious | Joy / further expansion |
|---|---|---|---|---|
| Stand | Demo | Demo | Demo | Planned, not authored |
| Point | Demo | Demo | Demo | Planned |
| Explain / open hand | Demo | Demo | Demo | Planned |
| Sit / carry / lean / compare / shrug | Planned | Planned | Planned | Needs approved joint silhouettes |

Expressions change mouth/eyebrow only after eyes/head/hair are locked. Concerned does not mean panicked. Pointing target must align with fingertip/pointer. Clothing recolor cannot change anatomy. Save approved full-size silhouette, expression contact grid and pivot specification. Human review remains mandatory before expanding beyond the demo's nine states.

## Environment kit

One editable demo study: wall, floor, desk, lamp and wall frame. Stable geometry/perspective; character and diagram use distinct clear regions. Three production kits should share palette/stroke scale but differ in function, not only hue. Store backgrounds without captions or finance facts. Never draw unexplained chart data into decoration. Check empty space for captions/source strips at both aspect ratios.

## Reusable SVG architecture

Use one symbols.svg or component generator with named IDs, consistent viewBoxes and explicit fill/stroke tokens. Character root contains hair/head/face/torso and separate arms/hands/legs. Props are separate symbols. World parent handles camera; character parent handles position/scale; joints own local rotation. Masks and gradients get namespace-prefixed IDs per instance. Charts consume actual values/units/date and have truthful axis metadata. PNG exports are derived deliverables; editable SVG stays canonical.

Asset request schema (original example):

```json
{
  "asset_id": "mira_point_concerned_v1",
  "category": "character",
  "design_version": "mira-1",
  "pose": "point",
  "expression": "concerned",
  "palette": "base",
  "viewBox": [0, 0, 360, 540],
  "pivot": [180, 300],
  "layers": ["hair", "face", "torso", "arm_left", "arm_right"],
  "usage": "point at loan comparison",
  "fact_ids": [],
  "rights": "original authored SVG",
  "qa_status": "pending"
}
```

Record path/hash, authoring method, revision, approved pose/expression, constraints and dependencies in an asset ledger. A screenshot/reference is evidence, never automatic permission to reuse its artwork. AI bitmap generation is optional for selected original scenes and needs consistent art direction; no tool is assumed in the demo.

## Keyframe timing specification

30fps, integer frame indices; root duration 240 frames (8s) for demo. Production frame rate can differ, but all events use one declared timebase. Source timestamps and ASR beats remain seconds until deliberately mapped to frames. Animation evaluation is pure time/frame seeking; no accumulated physics, wall-clock-dependent randomness or uncontrolled CSS transitions.

| Preset | Proposed timing | Properties / purpose |
|---|---|---|
| REVEAL_STEP | Instant at assigned frame | Visibility of the next meaningful fact |
| POP_IN | 6–10 frames | Inner scale 0.85→1, opacity 0→1; optional small overshoot only with clearance |
| SLIDE_IN | 10–18 frames | Inner translation and opacity; no jump in parent transform |
| CUT_THEN_PUSH | Cut at N, 12–24-frame push | Separate replacement from camera/local scale |
| COMPARE_BUILD | 12–30 frames per item | Bar/mask grows from same zero baseline; common units preserved |
| TRACE_REVEAL | 15–45 frames | Stroke dash offset or clip; data geometry never altered |
| SOURCE_HIGHLIGHT | 8–12 frames, readable hold | Bounding box/color highlight around exact cited fragment |
| POSE_EXPRESSION_SWITCH | Step or 4–8-frame blend | Local rig parts; no fake lip-sync claim |
| CAMERA_REFIT | 18–30 frames | World parent translate/scale; UI stays fixed |
| SCENE_EXIT | 8–15 frames, when needed | Inner opacity/translation before next clip; no gratuitous exit loop |

Durations are our starting defaults, not recovered competitor easing. A shot's hold depends on reading/comprehension, not a universal cuts/min quota. Data charts never overshoot a numerical endpoint. Shape interpolation requires equal path topology; otherwise use a supported swap/dissolve. Expression swaps do not certify nuanced character acting.

## Asset-generation QA

- Match original silhouette, face anchors, proportions, palette and outline width to the bible.
- Check all requested pose/expression combinations and mirrored directional meaning.
- Inspect hands/joints/pivots, clipping, layer order, transforms and independent masks.
- Confirm transparent margins, export resolution and crisp scaling at intended sizes.
- Separate real data charts from illustrative diagrams; label units, date, source and scenario.
- Reject invalid anatomy, unreadable labels, non-original character resemblance and unrelated decorative facts.
- Seek start/middle/end and backward/random frame order; identical frame yields identical rendered output.
- Review at target aspect ratio and mobile scale; make all assets editable and record provenance/hash.

## Effort ranges with explicit assumptions

Planning estimates for one solo creator, already comfortable with SVG/code, no complex anatomy, existing rendering tools, one revision round, and a 6–8m original explainer. These are not observed channel times or speed guarantees.

| Work | Initial episode / system | Later episode, established kit |
|---|---|---|
| Original character/palette/environment foundations | 12–30 hours | 1–4 hours repairs/extensions |
| 25–40 simple props and templates | 8–20 hours | 2–6 hours new components |
| Research and source checking | 6–16 hours | 6–16 hours; cannot skip for reuse |
| Script and narrative beats | 4–10 hours | 4–10 hours |
| Storyboard / layout | 4–8 hours | 3–6 hours |
| Animation, narration, edit and audio QA | 10–24 hours | 8–18 hours |
| Final review / revisions / publish | 3–8 hours | 3–8 hours |

Initial total roughly 47–116 person-hours; established-kit episode 27–68. Parallel team work changes elapsed time, not total labor automatically. Highly unique documentary scenes, licensed media, complex acting or poor source access expand these ranges. The small silent demo proves deterministic reuse, not a full production cycle, professional art quality or hundreds-of-assets throughput. Demo status and reproduction appear in DEMO/README.md.
