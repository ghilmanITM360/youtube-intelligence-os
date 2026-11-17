# Primitive Education — channel production manual v1 (DEV set, pre-held-out)
Channel UCsuQtyrMiUPdHUQ8WaqsFvQ (not Primate Economics). Supersedes v0.1 (kept unchanged).
Evidence: 11 DEV videos, all VISUAL_ANALYSIS_PARTIAL. LONG 16:9 n=6 (qB_EKkMyuUE, 3AsDdMQr_nQ, KyBWJPaF1KI, RmTdnXHbI8s, DekaeZPzTAQ, RM_KBLDLsnQ). SHORT 9:16 n=5 (IUur04eOd4A, f1vIzsTFrp4, uIG2U_1xynQ, W8AVd7RhTME, Nv4xJ_NsFdo).
Metrics: campaign/aggregate_dev_final.{json,csv}. Reuse: campaign/reuse_dev.json. Per-video locators: videos/<id>/tables/state_ledger.csv (seg IDs Gnnnn), review/rv1_<id>/annotations.csv, review/native_art_review.md.
Limits: no listening (BLOCKED_CAPABILITY). Narration relations are ASR_UNCERTIFIED. Public views are snapshots; no retention/CTR claims. Held-out videos were not opened when this was written.
Confidence: HIGH = ≥9/11 videos and MEASURED; MEDIUM = OBSERVED in ≥5 videos or MEASURED with exceptions; LOW = ≤4 videos or INFERRED.

## A. Observed source features
| Feature | LONG n=6: median (min–max) | SHORT n=5: median (min–max) | Label | Conf. |
|---|---|---|---|---|
| Duration s | 150.1 (68.5–211.4) | 40.8 (17.1–60.2) | MEASURED | HIGH |
| Events/min | 42.1 (34.1–59.7) | 45.6 (35.7–47.9) | reviewer classes + MEASURED timing | MEDIUM |
| Scene cuts/min | 23.7 (18.4–32.4) | 21.9 (18.9–25.3) | reviewer classes | MEDIUM |
| Median hold s | 1.30 (0.50–1.57) | 1.14 (0.89–1.34) | MEASURED | HIGH |
| Activity frame share | 0.034 (0.021–0.223) | 0.054 (0.012–0.076) | MEASURED | MEDIUM |
| Mean dark-ink fraction | 0.087 (0.071–0.104) | 0.098 (0.079–0.129) | MEASURED | HIGH |
| Holds containing yellow | 0.50 (0.24–0.62) | 0.64 (0.43–0.75) | MEASURED | MEDIUM |
| Single-frame share of activities | 0.903 (0.833–0.978) | 0.977 (0.923–1.0) | MEASURED | HIGH |

1. **Format (HIGH, MEASURED census).** All local videos are 50 fps CFR. 16:9 is 1920x1080 and 9:16 is 1080x1920, with no letterbox. The canvas is near-white #FDFDFD in 10/11 videos (Nv4xJ_NsFdo #FCFCFC). Counterexample: KyBWJPaF1KI has a measured #000000 background because it is a night/space video.
2. **Motion grammar (HIGH).** States change by single-frame replacement in 83–100% of activities. Multi-frame exceptions:
   - fade to white and fade-in of a new pose (RM_KBLDLsnQ G0050–G0052; end fade G0157);
   - gradual colour drift during a hold (3AsDdMQr_nQ hue rotation; RmTdnXHbI8s G0071 cloud fade, G0187 ghost fade-in — D4C MEASURED);
   - fall/slide (qB G0132), tumble and shrink (KyB G0140), pan with slide-on (IUur G0060), and text fade (RmT G0050).

   Zooms are stepped re-scales of one drawing (KyB G0074–G0078). The reviewer could not separate zoom from new drawing in RM_KBLDLsnQ G0100/G0106 (MEDIUM). A montage tile position is never treated as a camera move.
3. **Outlier pacing (counterexample).** RM_KBLDLsnQ (dinosaur tornado) has 59.7 events/min, a 0.50 s median hold and 0.223 activity share, driven by 26 effect events (fades, jitter alternation of two drawings). That gives 205 self-matching holds in the dHash reuse test. One video can therefore break the "about 1 s hold" norm.
4. **Character (HIGH, native crops in 11 videos).** The bearded caveman has:
   - a heavy black brow bar, single-dot eyes, a bulbous nose and a solid scribbled black beard;
   - a yellow tunic with black ovals and a zig-zag hem, and forearm tick marks;
   - mitt hands with finger lines and scalloped toes.

   Line art is a thick, even black outline: stroke median 10–14 px on landscape (pe_stroke) and about 20 px on portrait (Nv4 G0073). Fills are flat, with no gradient and no cast shadow.
   - Variants: brown tunic (DekaeZPzTAQ G0123–G0127), other-tribe green tunic + headdress (IUur), brain overlay as a "smart" metaphor (Dekae NATIVE_006028), and the bald moustached suited banker (RmT G0054, G0066).
   - Non-caveman subjects keep the same line system: a dinosaur in black line only (RM_KBL NATIVE_000949), and a goat in a softer "kawaii" style with glossy eyes (Nv4 G0070–G0073; MEDIUM style break).
5. **Literalisation (MEDIUM; relations ASR_UNCERTIFIED).** Narrated words become a picture on screen:
   - "goated" → quoted word → trophy → goat (Nv4 G0066–G0070);
   - money vs time → coins + alarm clock (RmT G0062–G0065);
   - "muscular dystrophy" / "HIV/AIDS" → word list beside a small caveman (Dekae G0132–G0134).
6. **Text (MEDIUM).** Rounded handwritten-style lower/upper case on white, built word by word with space reserved for the next item (Dekae G0132→G0134; uIG G0040–G0042). Coloured quote marks or red are used for emphasis. There is no captions track.
7. **Negation mark (MEDIUM).** A thick flat red X over the subject appears in uIG, W8A and Nv4 (G0073 native, with the black line drawn over the red).
8. **Blank beats (MEDIUM).** Blank white frames or holds appear between ideas (RmT G0051, RM_KBL G0051 end), and full-black frames occur (qB G0100).
9. **Ending (MEDIUM).** No CTA or end card is observed in 11/11. Videos end on a final joke or a fade (RM_KBL G0157).
10. **Short ↔ long reuse (HIGH for text, MEDIUM for images).** The ASR text overlap for each Short against its long sibling is:

    | Short | Long sibling | ASR overlap | Hold dHash matches |
    |---|---|---|---|
    | W8AVd7RhTME | RmTdnXHbI8s | 0.959 | 21 |
    | f1vIzsTFrp4 | qB_EKkMyuUE | 0.952 | 12 |
    | uIG2U_1xynQ | KyBWJPaF1KI | 0.849 | 31 |

    The dHash matches are candidates, not pixel-verified.
    - IUur04eOd4A (nuclear part 2) and Nv4xJ_NsFdo (Gen Z slang) have no DEV long sibling above 0.12.
    - Near-duplicate Shorts are not independent evidence of production rules. Unique-production evidence for portrait rests mainly on IUur04eOd4A and Nv4xJ_NsFdo.
    - Within-video re-use of the same drawing is common (Dekae 25, KyB 22 self-pairs).
11. **Landscape vs portrait (MEDIUM, n=6/5).**
    - The same drawing system is recomposed vertically, with heavier relative stroke on portrait.
    - Portrait has higher single-frame share, higher yellow share and slightly shorter holds.
    - Landscape has wider ranges, including the outliers KyB (dark) and RM_KBL (fast effects).
    - Cut rates overlap.
12. **Loudness** was MEASURED by ebur128 per video in evidence/ebur128.txt. Voice, music and SFX are UNAVAILABLE without listening.

## B. Open items
- Unresolved segments are listed per video in quality_gate.json. RM_KBL has many LOW jitter rows (even G0056–G0090).
- Multi-frame activities are sampled by strips, not all-frame-verified.
- Assets are aliased per video in asset_inventory.csv; cross-video identity is only a dHash candidate.

## C. Proposed original production choices (NOT source facts; new character, script, art)
- Build your own mascot with one signature flat colour on a near-white canvas and a thick even outline.
- Show one idea per drawing for about 1–1.3 s, and replace the drawing in a single frame by default.
- Use a dip-to-white only for scene/era breaks.
- Picture the narrated word at the moment it is said.
- Build text word by word with space reserved for the next word.
- Use a red X for negation, end on a joke state, and add no end card.
- Before adopting any timing rule, verify sync by listening.
