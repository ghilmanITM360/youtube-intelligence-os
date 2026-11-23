# V1 Rent: Casual Finance style-fidelity audit

Date 2026-11-21. Subject: `out/V1_RENT_segment_0-75s_take2.mp4`, sha256 `a40bbccc147368b49c7af10060c537225f4f6c1c1d25fb8e83ec8ba74577516c` (re-hashed this session, matches the `.sha256` sidecar).
Read-only audit: no render, no asset, renderer, storyboard or video change. New files only: this report and `style_audit/`.

## 1. Verdict

**The segment does not yet show that we learned Casual Finance's production principles. A viewer would read it as a generic animated explainer.**

It copies the channel's surface (thick black outlines, flat-ish colour, a red accent, a cartoon person, source tags). It does not copy the structure that makes the channel recognisable:

1. **Canvas.** CF is on a white or light canvas in about 83% of sampled long-form frames. V1 holds one full-bleed living room for all 75 s.
2. **Character.** CF's recurring host is a big round head (31-38% of figure height) on a thin line body. V1's host is a clothed, shaded man with a small head (16%) and legs about 3-4.5x thicker relative to height.
3. **Editing.** CF cuts hard 17-35 times in 75 s (one focal subject per beat). V1 has **zero** cuts: one persistent shot with a dashboard card that changes content.
4. **Graphics.** CF uses simple hand-drawn axes or real screenshots with a red hand-drawn arrow or circle, plus handwriting-style type. V1 uses a rounded UI card with Helvetica text and rolling counters.

Smallest effective correction (section 8): change the default canvas and the host rig, then re-block the same 75 s into about 20-30 hard-cut beats. Narration, timings, verified numbers and source tags stay.

## 2. Evidence base and limits

**Read:** `CHANNEL_001/05_VISUAL_DNA`, `06_STORYBOARD_GRAMMAR`, `08_ASSET_CREATION_BIBLE`, `09_CHARACTER_SYSTEM`, `10_LAYER_DEPTH`, `12_CAMERA`, `13_EDITING`, `21_MULTI_VIDEO_EVIDENCE` (incl. the 2026-11-20 viewed-pixel correction and independent review #1).

**Gap in that knowledge:** it is Shorts-centred (one deep video, 1080x1920, 22 frames, labelled PARTIAL). V1 is a landscape long-form, so I added a long-form sample. The folder has 34 landscape videos (26 at 1920x1080, 8 at 1280x720) and 138 vertical 1080x1920 Shorts.

**What I measured or viewed this session** (scripts and data in `style_audit/tools/`):
- Background class per frame: all 34 long-forms (first 300 s, one frame per 4 s, 2,544 frames) and 30 randomly drawn 1080x1920 Shorts (411 frames).
  - "light" = at least 55% of pixels with all channels >= 235.
  - "flat" = one quantised colour is at least 55% of the frame.
  - "full" = everything else.
  - "Full" therefore includes dark screenshot plates, grey-letterboxed screenshots and photos as well as illustrated environments, so it is an upper bound for "detailed environment".
- Contact sheets and frames viewed: 5 long-forms (Every Type of Investor, Drowning in Debt, Crypto Is a Brilliant Scam, Something Feels Off About 2026, Brace For Impact) and V1.
- Geometry measured on two reference stick figures, viewed as a normalised sheet with V1.
- Frame-difference motion statistics for V1 and 6 long-forms (first 75 s).
- Head-region temporal check of one reference stick figure over 8 s (Brace 0:06-0:14).

**Not done:** no frame-by-frame review of the other 29 long-forms (only pixel statistics). No audio. Sample timestamps are the ones named in the sheets; sheet 5 windows were chosen, not random.

## 3. Observed in the reference (long-form), separated from inferred

| # | OBSERVED | Evidence |
|---|---|---|
| O1 | Light canvas dominates: long-form 82.9% light / 4.6% flat colour / 12.5% full-bleed. Shorts 98.3% / 0.5% / 1.2%. | `tools/bgstat.json`; per-video light share 0.29-1.00 (median about 0.9) |
| O2 | Detailed environments exist but appear as separate beats (a city street, a nightclub, a party room, a restaurant). The host stays a thin-bodied stick figure inside them. | Off-2026 0:31 (`SHEET1`), Crypto restaurant (`LF_crypto_sheet`), Drowning club (`LF_drowning_sheet`) |
| O3 | The recurring host is one rig: big round peach head, dot eyes, line mouth, spiky hair, thin line body, stick arms and legs. Expression = a different head drawing on the same body (smile, flat mouth, worried, sunglasses). | `chars_normalized.jpg`; Brace 0:07 vs 0:46 and Investor 0:55 have the same body |
| O4 | Geometry at equal figure height: head height/H 0.38, 0.38, 0.31 (3 refs); body line about 1.6-2.5% of H. | `tools/chars2.py` output |
| O5 | Other, richer characters coexist (Uncle Sam, a hooded Satoshi, a teacher at a chalkboard). They carry a story role and are not the recurring narrator. | Drowning 0:02, Crypto 0:22/0:55 |
| O6 | Hard cuts, held frames. Head region changed 11 times in 8 s, all instant swaps with static frames between them. No continuous mouth motion. Staggered `?` pop-ins. | `ref/brace_mouth_strip.jpg`, d>0.5 change count |
| O7 | Frame change statistics (first 75 s): hard cuts (mean diff > 2) 17-35 in five long-forms (Brace 133, a fast map montage); exactly-still frames 84-96% in five of the six sampled long-forms (38% in one). | `tools/motion.py` |
| O8 | Graphics: hand-drawn axis line chart with two coloured lines and a hand-lettered legend; real chart screenshots with a red hand-drawn arrow and circle; real article or tweet screenshots on grey. | `SHEET3` |
| O9 | Type: hand-lettered or Comic-style labels and captions; screenshots carry their own source text. | `SHEET4` |

| # | INFERRED (not proven) |
|---|---|
| I1 | The thin-body rig is the host's design system and is reused across scene types. Supported by O2-O4; I only measured two host appearances. |
| I2 | Environments are inserted as one-off illustrated beats, not backdrops. Supported by O1/O2/O7; the "full" share includes non-illustration plates. |
| I3 | Rolling number counters are not part of the grammar. I did not see one in the sampled frames; not tested exhaustively. |
| I4 | Production tool: likely vector and image tools with 24 fps stepped holds (E42 in 21_MULTI_VIDEO_EVIDENCE). Not verified here. |

## 4. V1 as rendered (viewed, `style_audit/v1/V1_sheet.jpg`, `SHEET1/3/4/5`)

- One shot. The same living room (window, sofa, plant, rug, table) is visible from 0:00 to 1:15. A cream rounded card sits over it and its content changes: bars, headline text, tiles, a weights bar.
- One host, left third, standing. Two poses: bill-holding (0-16.4 s, 63.6-70.2 s) and open-hands shrug. Both have the same closed-mouth face. Three pose swaps in 75 s, hard cuts plus a continuous idle bob.
- Charts: rolling counters (e.g. 7.6% appears mid-roll at 0:47), grow-in bars, sans-serif labels, "Source:" lines in small grey text.
- Zero frame-to-frame jumps above diff 2.0; 31% exactly-still frames (the bob and counters keep it moving).

## 5. Side-by-side evidence

| Sheet | Shows |
|---|---|
| `style_audit/SHEET1_background.jpg` | White canvas (Investor 0:55, Brace 0:07) vs one full-bleed beat (Off-2026 0:31) vs V1 0:10 and 1:02 |
| `style_audit/chars_normalized.jpg` | Three reference stick figures vs V1 renter, all scaled to the same height |
| `style_audit/SHEET3_charts.jpg` | Hand-drawn line chart (Investor 1:04), real FRED chart with red circle (Off-2026 0:16), real bar screenshot with red circle (Drowning 1:22) vs V1 0:10, 0:36, 1:02 |
| `style_audit/SHEET4_typography_props.jpg` | Reference captions and lettered labels, props with source text (Brace 1:25) vs V1 headline and chart text |
| `style_audit/SHEET5_motion.jpg` | 20 s at 2 fps: Investor 0:36, Drowning 0:36, V1 0:40. References change scene every few frames; V1's row of frames is almost identical |

Geometry (measured on figure crops, same method for all):

| | head h / figure h | head w / figure h | body line or leg width / figure h | outline / figure h |
|---|---|---|---|---|
| Ref Brace 0:07 and 0:46 (same body) | 0.38 | 0.41 | 0.024 | 0.016 |
| Ref Investor 0:55 | 0.38 | 0.40 | 0.025 | 0.016 |
| Ref Investor 0:37 | 0.31 | 0.32 | 0.016 | not measured |
| **V1 renter sprite** | **0.16** | **0.14** | **0.072 per leg** | **0.0045** |

Reading: V1's head is 2-2.4x smaller relative to the body, the leg is about 3-4.5x thicker, and the outline about 3.5x thinner. Torso width and arm thickness for V1 were not measured separately (arms are spread in the sprite, so a torso-row measure would be wrong); I can see the jacket has substantial volume, the ref has a single line. Colour-count comparison was tried and dropped (video compression noise makes it meaningless).

## 6. Fidelity scorecard (no percentages)

| # | Category | Class | One-line basis |
|---|---|---|---|
| 1 | Background style | **MAJOR MISMATCH** as a persistent backdrop. An apartment used for single beats would be an ACCEPTABLE ORIGINAL ADAPTATION | O1, O2 vs V1 75 s one room |
| 2 | Character body geometry | **MAJOR MISMATCH** | head 0.16 vs 0.31-0.38; legs 0.072 vs line 0.02; clothed and shaded vs line |
| 3 | Character head originality | **MATCHES the intent** (original face, no copy of the channel's head) but the head's scale and style do not fit the rig | user requirement: original head |
| 4 | Facial expressions | **MAJOR MISMATCH** | one closed-mouth neutral face for 75 s vs head swaps in O3 |
| 5 | Body poses | **PARTIAL** | hard-cut pose swap matches O6, but only 2 poses, 3 swaps; ref has hands-on-hips, mug, pointing, etc. |
| 6 | Illustration stroke style | **PARTIAL** | thick outlines and rounded joins are in family; V1 is clean uniform vector, ref is wobbly hand-drawn and 3.5x heavier relative to figure |
| 7 | Colour and shading | **PARTIAL** | flat fills with a red accent are shared; V1 adds soft shading and muted earth tones on cream, the ref uses clean flats on white or one pastel block |
| 8 | Financial graphics | **PARTIAL** | data and sources are correct and simple bars suit the idea; the UI card container, rolling counters and no red arrow/circle annotation are not CF |
| 9 | Typography | **MAJOR MISMATCH** | Helvetica UI sans vs hand-lettered or Comic-style type (O9) |
| 10 | Motion and editing | **MAJOR MISMATCH** | 0 cuts vs 17-35; continuous bob and counters vs held frames and instant swaps |
| 11 | Storyboard decisions | **MAJOR MISMATCH** (as rendered) | 15 narration beats rendered as one persistent shot; ref is one focal subject per beat |
| 12 | Overall visual coherence | **PARTIAL** | internally consistent, but as a different style |

INSUFFICIENT EVIDENCE: whether CF ever uses rolling counters or eased motion (none seen, not exhaustively tested); host expression frequency across the whole channel (one 8 s window measured plus sheets).

### Detail for each PARTIAL / MAJOR MISMATCH

Priority: P1 high-impact design-system mismatch, P2 moderate, P3 cosmetic. Reuse: what existing V1 material survives.

| Item | Observed difference and evidence | Viewer-visible effect | Correction | Pri | Reuse |
|---|---|---|---|---|---|
| Background | 12.5% full-bleed in long-forms vs 100% in V1 (O1, `SHEET1`) | Reads as an interior explainer, not a CF canvas | Default `#FDFDFD`; apartment only for 1-3 s rent-life beats | P1 | `v1_bg_room` and table assets kept for those beats |
| Body | Head 0.16 vs 0.31-0.38; legs 0.072 vs about 0.02 (`chars_normalized`) | Looks like a stock illustrated man, not the channel's host | Thin line body with a large original head | P1 | Prop (bill), colours; not the sprite |
| Expressions | One face in all poses (`V1_sheet`) | No emotional beats | 4-5 head drawings swapped by hard cut | P1 | None (heads are new) |
| Editing and storyboard | 0 cuts, one room (O7, `SHEET5`) | Static dashboard feel | About 20-30 hard-cut beats over the same 75 s | P1 | Take 2 timings, claim register, chart data |
| Typography | Sans UI text vs lettered labels (`SHEET4`) | Corporate, not channel voice | Hand-style label font for labels and callouts; keep a small plain face for the source tag | P2 | Source text content |
| Charts | Card plus rolling counters vs drawn axes or screenshot plus red arrow (`SHEET3`) | Dashboard look | Drawn-style bars or line on white, red arrow/circle on the key number, numbers pop in (no roll) | P2 | Values 2.8, 2.7, 7.7, 25.9, 35.3 and source lines |
| Poses | Two poses vs a varied set | Repeated gesture | 3 arm poses (down, shrug, point) on the new body | P2 | Shrug and bill ideas |
| Stroke and colour | Clean uniform vector, soft shading | Slightly glossy | Follow in the new assets: flat fills, heavier wobbly line | P3 | Palette (olive, red, cream) as accents |

## 7. Answers

**Q1. Following CF's visual grammar or a generic animated finance video?** Mostly the second. The loose family look (outlined cartoon, red accent) is there. The canvas, the host rig, hard-cut beats, and drawn or screenshot-plus-arrow graphics are not.

**Q2. Thin stick body with an original head?** Yes. It is the strongest reusable, learnable, identity-neutral principle (O3-O5): a big expressive head on a line body. The head must still be a new drawing (not the channel's face or hair). The channel also uses richer characters (O5), but only as one-off story characters, not as the narrator.

**Q3. White or light default, apartment only when justified?** Yes. About 83% of sampled long-form frames are on a light canvas; full-bleed environments are single beats. Use the apartment for the rent-bill and "feels bigger than the number" beats, not as the background of the data scenes.

**Q4. Expressions and poses too limited?** Yes. One face, two poses, three swaps in 75 s. The reference shows no lip movement (O6), so do not add lip sync; add head and pose variety instead.

**Q5. Charts, typography, editing and motion consistent?** No on editing, motion and typography; partial on charts (O7-O9).

**Q6. Worth preserving.** Take 2 audio sync and word-timed reveals; verified numbers and the claim register; "Source:" lines (CF's real screenshots carry their own source text; ours need explicit tags because we are not using real screenshots yet); the bill prop idea; the render pipeline.

**Q7. Minimum correction before the full video.** Section 8.

## 8. Smallest effective correction plan

Do these in order and stop; no further reconstruction.

1. **Canvas default:** set the V1 background to `#FDFDFD`. Keep the room for at most 3 short beats (the bill beat and the "different question" beat). Cost: spec change only.
2. **Host rig (one new asset batch):** 1 thin body with 3 arm poses (down, shrug, point), plus 5 original head drawings (neutral, smile, worried, surprised or thinking, smirk). Heavier hand-style outline, flat fills, head about 0.33 of figure height. Do not copy the reference's hair or face. Optional shortcut: the existing `PRODUCTION_SYSTEM/assets/char_stick_{happy,neutral,worried}_{up,down,shrug}.png` set shows the 3x3 rig layout (head x arm pose), but those are recreations of the reference character, so reuse the structure only, not the art.
3. **Re-block, same audio:** split the 15 existing narration beats into about 20-30 hard-cut beats (reference range 17-35 per 75 s). One focal subject per beat. Staggered pop-ins about 0.6 s apart inside a beat. Remove the idle bob.
4. **Graphics:** white-canvas drawn-style bars and weights chart; red arrow or circle on 2.8% / 2.7% / 35.3%; numbers pop in (no rolling counters, which also removes the mid-roll wrong-value defect from the earlier QA); labels in a hand-style face. Real BLS/Zillow screenshots remain optional and must be real.
5. **One check:** render, then rerun `tools/bgstat.py`, `tools/motion.py`, `tools/chars2.py` on the new cut. Targets: light share above 70%, hard cuts 17-35, head ratio 0.3-0.4. Then one independent visual review against the same sheets.

Not recommended: re-drawing the room, redoing audio sync, or rebuilding the verified data work.

## 9. Honest limits and caveats

- This audit shows the **structure** differs; it does not prove viewers will reject the current look. No audience test.
- "Full" frames overstate illustrated environments (includes photos, dark screenshot plates, grey-letterbox screenshots).
- Rig geometry rests on two host appearances plus visual inspection of the contact sheets.
- The research docs (05, 09) were built from one Short; the long-form findings here are new and should be written back into the channel knowledge only after your approval.
- Nothing committed or pushed.
