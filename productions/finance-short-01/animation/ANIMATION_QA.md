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
| Captions fit one line at ≥ 40 px inside x 50–890 (updated phone-safe metrics) | PASS (one chunk auto-shrinks to 45.7 px) |
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
- **Captions.** Updated default y1530, S01A/B y720, S02A y560, S07B y200, S09 y1335; x470/max-width840. All chunks satisfy the simulated UI mask. Actual phone/app review remains pending.
- **Font.** Avenir Next comes from macOS. Fallback strategy and tested second-PC scope are in PORTABILITY.md; fallback widths/pixels need review.
- **Associate.** Their acting is limited to two pose blends (stand → present, offer → present).
- **Hands and in-betweens.** Hands remain stylised mittens. Hand-shape and expression changes are step switches by design. There's no smear or motion blur.
- **Still needed:** human review of acting, timing feel, phone readability, and owner sign-off on the remy-2 hair.

## Second-PC targeted QA (2026-10-13)

Fresh Node 24.14.0 install, rig/timeline tests and typecheck PASS. All 244 SVG / 196 PNG manifest hashes match. Bundle rebuild bytes match; Python parity-fixture numeric differences max 4.55e-13 (tolerance 1e-6), original fixture preserved. Local Sharp renderer smoke test passes from an unrelated cwd. Renderer and font strategy: `PORTABILITY.md`.

**Fixed S10 contact discontinuity:** S10A+61 / S10B+0 (absolute 1375→1376). The 1.08-turn stroke ends beyond the zero-angle start; the old retreat incorrectly jumped back to that start. Retreat now begins at the drawn endpoint. A continuity test failed before the fix and passes afterward, including backward seek checks. Five before/after stills inspected; no full render repeated. Existing committed full preview predates this fix; it remains a provisional reference, not the updated master.

**Fixed caption timing and UI overlaps:** source-shot holds now stop at the cut (observed at S11+2 with old S10B wording). All 21 boundaries/gaps/end-of-timeline are covered by regression tests. Captions use shared x470/max-width840/default-y1530/S07B-y200 metrics. Every current chunk remains >=40px and outside the test mask (top100, bottom320, right180px from y850–1600). The test mask is a simulation, not a universal YouTube UI specification. Native stills for 21 shots and 320/160px stress sheets reviewed, followed by 11 updated caption samples. Supporting labels/qualifiers remain very small at 160px; approved right-side scene content can be obscured by the mask. Actual-device/human review is pending.

Contact boundary samples: S01B+12/13/15, S02A+49/50/51, S03+20/21/25, S05A+13/14/26, S06B+30/31/32, S07B+69/70, S11+2/11/19. No new defect confirmed in these samples; automated rig tests remain separate from artistic review. Associate gesture range remains limited; adding motion without demonstrated communication benefit is deferred to human direction.

## Remaining-work classification after consolidated QA

| Category | Item / disposition |
|---|---|
| CONFIRMED DEFECT | Marker retreat jump, caption spill across cuts and caption simulated-UI overlaps: fixed and regression tested. No other defect confirmed by this session's sampled frames. |
| ALREADY VERIFIED | All 21 shots render; asset resolution and hashes; native bundle rebuild; rig parity; actual two walk trajectories; contact samples; updated caption layout; muted preview decode health. |
| REPRODUCIBLE QUALITY GAP | 20–24px supporting labels/qualifiers become 3–4px at 160px stress scale. Right-side approved diagram/scene content intersects the conservative simulated UI rail. Requires owner review of message hierarchy and approved composition before broad redesign. |
| TECHNICAL RISK | Cross-platform font/raster differences. Second macOS ARM64 checkout verified; Linux/Windows not executed (no container runtime available). |
| DOCUMENTATION / PORTABILITY GAP | Owner-PC Sharp path and macOS-only QA font path resolved. Local dependency lock/smoke test and font strategy documented. |
| OWNER APPROVAL REQUIRED | Associate gesture/art direction; Remy-2 hair; phone/device readability; human motion review; final export. Existing approved art retained. |
| AUDIO BLOCKED | Only original MP3 present; APR→April correction absent. No replacement voice generated, no publication gate bypass. |

### Approved near-arm perspective exceptions: exact owner review samples

These are three-quarter approved artwork, not side-view anatomical flexion measurements. The automated envelope accepts them; this is not human art-direction approval.

| Pose | Near elbow | Representative frame |
|---|---:|---|
| shrug | +117.89° | S01A+30, absolute30 |
| hold_bill | +132.38° | S01B+15, absolute56 |
| hold_sheet | +136.41° | S02B+40, absolute215 |
| open_hands | +129.53° | S09A+17, absolute1114 |
| shocked | +154.51° | S06B+38, absolute757 |

Actual walk test trajectories now include S02A travel550/0.62 over64 frames with170-unit step target and S07B travel760 over48 frames with170-unit step target (in addition to prior generic cases). Both report planted slide~1.1e-12px, knees19.8–53.4°, hips−35.0…11.6°. Stop samples S02A+49/50/51/58 and S07B+115/116/118 inspected. Seated contact remains sampled at S11+2/11/19; no human physics/acting certification is implied.

Consolidated updated preview: 1080×1920 H.264,30fps,1590frames,53.0s, no audio stream. Full-frame joint-warning capture:0. FFmpeg decode exit0/no stderr; blackdetect0 segments. Five fresh forward/backward frame pairs byte-identical (81,1297,1375,1376,1439). Preview SHA256 `9d83fa32ed662a3933dbaa8122e48716b321f73b521ca3e1fd8b67cddbe78df0`. Committed machine-readable evidence: `qa/second_pc_validation.json`; targeted visual evidence: `qa/marker_retreat_before_after.png`, `qa/caption_simulated_UI_stress.png`. Two scratch registered-PNG rebuilds match manifest hashes without overwriting registered assets. Updated preview includes all session visual fixes and remains muted/watermarked.
