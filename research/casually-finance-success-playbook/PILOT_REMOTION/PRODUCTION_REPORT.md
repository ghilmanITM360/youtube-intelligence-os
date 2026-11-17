# Asset factory and production timing

This is one authored original character, not fifteen independently drawn characters. [Measured inventory](evidence/asset-and-motion-inventory.json) counts 14 artwork/layout modules: one rig, one environment, five reusable finance props, two diagram-specific glyphs, one chart, three explanatory diagrams and one shared arrow. Text/card components are reusable code and are not additional unique illustrations.

| Output | Count / meaning |
|---|---|
| Character body poses | 3: shrug, point, hold; jointed upper/lower arms, hands, hips, knees and fixed feet |
| Expressions | 5: curious, concerned, explaining, pleased, neutral; fixed face/hair/glasses geometry |
| Exported SVGs | 21: 15 combinations from one rig, 5 finance props, 1 environment |
| Distinct scene layouts | 8 over 42 seconds; mean 5.25s; all reuse host/environment |
| Explicit object-property tracks | 28, containing 76 value knots; [frame catalog](evidence/motion-events.csv) |
| Other animation events | 8 camera pushes, 6 articulated pose transitions, 3 delayed grip visibility ramps; expressions/blinks/caption changes counted separately |
| Reused finance props | Contract across 4 layouts, lock across 5, explicit arrow across 3; multiple appearances are not new artwork |
| Custom episode assets | Policy/contract connector, rate/payment schematic, old/new-loan comparison, escrow breakdown; approval/calendar glyphs |
| Source evidence touched | Read-only: selected reports/tables, archived description and 3 existing video files; no extraction pipeline rerun |

The actual assembly/generation/render timings are recorded in the inventory and supporting JSON. Local TTS generation took **36.12 seconds**, including loading/downloading the cached model; voice content totals **38.175 seconds**. Audio stem scheduling/mixing took **2.18 seconds** in its recorded pass. The final corrected render took **131.18 seconds** including bundling, nine sample stills, two asset boards and 1,260 video frames. These are local machine measurements, not guarantees or paid-production labor rates. The inventory's checkpoint elapsed time is measured from creation of PLAN.md, includes implementation/corrections/waits/review, and excludes earlier source exploration. It is not a human animator's billable time.

No paid generator, cloud render or new paid scrape was invoked: **incremental service payments $0**. Account subscription/token cost, electricity, hardware depreciation, existing software cost and a future artist's fee are not measured.

## What worked and what required correction

Pure frame evaluation and a shared SVG rig preserve identity without regenerating a separate image per scene. Parent shoulder/elbow transforms provide actual articulation. Two-bone leg solving maintains 95px bone lengths and fixed local foot anchors at every frame. Camera movement intentionally moves the whole world; it is not local foot sliding. The actual backwards-seek test, full decode, native samples and temporal excerpts support reproducibility and working motion.

Eight manual code/art corrections were needed, recorded in the inventory. No independently drifting face was found among inspected outputs. Current consistency limitations are a stylized contract grip, limited wrist/body rotation, an open mouth without phoneme timing, and repeated staging. Automated frame/geometry checks cannot classify every hand shape as anatomically natural.

## Scale estimate: 5–8-minute explainer

Assumptions: refined Nori kit, roughly 55–90 meaningful layouts, 12–25 new props, 10–20 custom illustrated arrangements, a solo creator using a reused renderer, one factual topic, one voice, and two revision rounds. This is a planning estimate, not a measured production benchmark or guarantee. A dedicated designer/animator is valuable for the custom scenes and acting; code supplies rig consistency, charts, layout variants, transforms and exports.

| Work | Estimated person-hours |
|---|---:|
| Research, claim ledger and original script | 6–12 |
| Storyboards and staging across reused/custom scenes | 8–16 |
| New props/custom illustration and acting refinement | 10–26 |
| Keyframe timing, narration/edit and sound decisions | 10–22 |
| Full QA and two revision rounds | 6–14 |
| **Episode total, rounded** | **40–90** |

Before scaling, budget an additional **6–16 person-hours** to refine this pilot's hands, acting, shot variety and audiovisual cues. That is estimated work, not work already performed. More scenes, detailed illustration or extra review rounds increase the range.

Cost should be calculated from the actual artist/creator quote. An **assumed budgeting rate of $25–$75/person-hour** gives **$1,000–$6,750** for the 40–90-hour episode, plus any commercial software/license or voice services chosen later. These are hypothetical internal planning rates, not verified market prices or a vendor offer. The current build itself required no such service purchase. A solo owner can substitute their own time, but it still consumes that time.

A naive frame-count extrapolation of this simple render is roughly **16–25 minutes** for 5–8 minutes on the same setup; it is not a benchmark. More SVG detail, footage, concurrency limits, font changes, RAM pressure and sound processing can materially increase it. Generation/render minutes should not be confused with story/illustration/review hours.

## Reusable system versus unique art

A hundred exported views can come from pose/expression combinations, camera choices and different arrangements of the same assets. They are useful production states, not a hundred genuinely new illustrations. Original scene metaphors, expressive acting and unusual organic poses remain design work. Maintaining the same mathematical face is straightforward; maintaining engaging varied storytelling over 90 shots is the unproven part. The next valuable test is a small designer-refined revision of this pilot, followed by a one-minute sequence with more custom staging, not a batch export of hundreds of PNGs.
