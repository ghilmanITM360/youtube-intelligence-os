# Animation QA: Finance Short 01 (provisional timing)

QA date 2026-10-13. Reviewer: one agent (Claude). **No human motion or art-direction review has happened yet.**

**Status:** all 21 shots are animated. Every timing is anchored to narration words, but the timing is **provisional**: the supplied MP3 says "April" for APR, so the gate fails and no final export is allowed.

## Automated checks

| Check | Result |
|---|---|
| Rig parity with the Python reference (`npm test`): 22 library poses, eye shapes, arm IK | PASS (exact to 1e-6) |
| Rigid limbs (bone lengths preserved): every limb matrix has \|det\| = 1 in all library poses | PASS |
| Walk solver: planted feet never slide or leave the ground; knee and hip stay in range | PASS (slide < 1e-11 px; knee 20–53°, hip −34…8°) |
| Leg IK round trip: the ankle lands on its target and the shoe stays flat | PASS |
| Joint angles on every rendered frame (1590 frames), against the rig's suggested limits ∪ the angles the approved poses use | PASS: 0 violations after the fix below |
| Timeline: 21 shots, 21 phrases, contiguous coverage, every word inside its phrase, narration not truncated, audio frames + end hold | PASS |
| Captions fit one line at ≥ 40 px inside x 70–1010 | PASS (one chunk auto-shrinks to 45.7 px) |
| Every scene instance resolves to a registered asset or its own generator markup | PASS |
| Final sync is blocked while the pronunciation gate fails | PASS (BLOCKED) |
| Deterministic seeking: 6 frames rendered forward and in reverse are byte-identical | PASS |
| `bundle.json` rebuild is byte-identical | PASS |
| Preview: H.264, 1080×1920, 30 fps, 1590 frames, 53.0 s; `ffmpeg` decodes with 0 errors; `blackdetect` finds 0 black segments | PASS |

**Fixed during QA:**
- **Joint interpolation.** Shortest-path interpolation spun the near wrist past ±180° during S01B, outside every approved pose. Joints now interpolate linearly between normalized keys, so every in-between stays inside the interval of its two keys.
- **Suggested limits vs. approved poses.** The rig's "suggested" elbow limit [−150, 20] is a side-view flexion range. Five approved 3/4-view poses fold the near arm with the elbow out, to +118…+155°: hold_sheet, hold_bill, open_hands, shrug, shocked. They were approved visually in Phase 2. The check accepts their range, and they are listed here for human review.

## Visual review (contact sheets and motion strips in `qa/`)

| Area | Finding |
|---|---|
| Opening hook (S01A/B) | The sign drops with a small pendulum settle. Remy rises, dips and shrugs. The statement rises into open hands, and the grip switches 2 frames after contact using the same prop matrix (no pop). |
| Walk (S02A, S07B) | Planted feet, counter-swinging arms and a physical pelvis bob. Remy stops with his feet together and his upper body settles. The foreground plant occludes him correctly. |
| Hand–object contact | The S03 fingertip lands on the IF lever and the press moves finger and lever together. The S10 marker tip traces the circle, and the drawn stroke is the tip's own path. In S05A the coins leave the release hand and slip behind the card edge. |
| Seated transition (S11) | Stand to sit with both ankles pinned by IK: forward counter-lean, pelvis down onto the seat, a 1.5 % cushion compression, no bounce. |
| Prop transfers | S06B: the receipt flies on a gravity arc and lands on the statement header. At contact the statement swaps from empty to charged. |
| Charts (S05A, S07B, S08) | The fill steps and bar growth never overshoot. Interest chips scale with no overshoot, so the proportions stay honest. The SCHEMATIC qualifier stays visible above Remy. |
| Qualifiers | F2 shows in S02, F6 in S07B, F8 in S09B (on until the cut) and F10 in S12. No "0%" appears on deferred assets, and there are no amounts, rates or dates. |
| Ending (S12) | The camera refits to the approved C14 close-up. The receipt and clock reveal, the minute hand ticks back once, Remy switches to sit_notice, and the qualifier fades in. |

## Deviations from the approved hero frames (deliberate)

- **S03:** the fingertip contact moves from the switch plate edge (610, 1010) to the IF lever face (712, 742), so the press is physical.
- **S10:** the static coral circle on the PROMO ENDS page is removed and drawn live by the marker tip, using the same geometry and colour.
- **S11:** a stand-to-sit action is added at the start; the hero frame starts seated.
- **Remy's walk** uses a footstep or IK solver instead of alternating walk_a/walk_b. The upper body still comes from the library poses.

## Known limitations and open items

- **Audio.** Timings are word-anchored but PROVISIONAL until a corrected MP3 is aligned. The audio track isn't wired into the composition yet, by design.
- **Captions.** Default y is 1550 (plate ≈ 1500–1600). That's above the Shorts UI band but below the handoff's "essential text ≤ 1520" guideline. S01A/B and S02A use 720/560, S07B uses 100 and S09 uses 1335. Check on a phone.
- **Font.** Avenir Next comes from macOS. Other operating systems fall back to a different font, so widths change.
- **Associate.** Their acting is limited to two pose blends (stand → present, offer → present).
- **Hands and in-betweens.** Hands remain stylised mittens. Hand-shape and expression changes are step switches by design. There's no smear or motion blur.
- **Still needed:** human review of acting, timing feel, phone readability, and owner sign-off on the remy-2 hair.

## Second-PC targeted QA (2026-10-13)

Fresh Node 24.14.0 install, rig/timeline tests and typecheck PASS. All 244 SVG / 196 PNG manifest hashes match. Bundle rebuild bytes match; Python parity-fixture numeric differences max 4.55e-13 (tolerance 1e-6), original fixture preserved. Local Sharp renderer smoke test passes from an unrelated cwd. Renderer and font strategy: `PORTABILITY.md`.

**Fixed S10 contact discontinuity:** S10A+61 / S10B+0 (absolute 1375→1376). The 1.08-turn stroke ends beyond the zero-angle start; the old retreat incorrectly jumped back to that start. Retreat now begins at the drawn endpoint. A continuity test failed before the fix and passes afterward, including backward seek checks. Five before/after stills inspected; no full render repeated. Existing committed full preview predates this fix; it remains a provisional reference, not the updated master.

**Fixed caption timing and UI overlaps:** source-shot holds now stop at the cut (observed at S11+2 with old S10B wording). All 21 boundaries/gaps/end-of-timeline are covered by regression tests. Captions use shared x470/max-width840/default-y1530/S07B-y200 metrics. Every current chunk remains >=40px and outside the test mask (top100, bottom320, right180px from y850–1600). The test mask is a simulation, not a universal YouTube UI specification. Native stills for 21 shots and 320/160px stress sheets reviewed, followed by 11 updated caption samples. Supporting labels/qualifiers remain very small at 160px; approved right-side scene content can be obscured by the mask. Actual-device/human review is pending.

Contact boundary samples: S01B+12/13/15, S02A+49/50/51, S03+20/21/25, S05A+13/14/26, S06B+30/31/32, S07B+69/70, S11+2/11/19. No new defect confirmed in these samples; automated rig tests remain separate from artistic review. Associate gesture range remains limited; adding motion without demonstrated communication benefit is deferred to human direction.
