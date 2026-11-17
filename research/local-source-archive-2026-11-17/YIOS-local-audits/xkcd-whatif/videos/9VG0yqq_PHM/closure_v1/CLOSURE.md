# 9VG0yqq_PHM: visual-only closure (contract v1; LOCAL ONLY) — fifth LONG closure

## Evidence base
- **Source:** sha re-computed = manifest, 3893 frames (CFR 24). Every frame measured and covered once (V2).
- **Reused:** rv1 ledger (145 segments: 73 holds, 72 activities), shot_ledger, measurements.
- **New in closure_v1/ (all viewed this pass, 2026-11-09):** holds_01..19.jpg (all 73 holds, 1/2 scale); 29 native strips (G0004, G0006, G0016, G0018, G0022, G0026, G0028, G0030, G0036 ×5, G0050, G0060, G0074, G0076, G0080, G0096 ×2, G0098, G0100, G0102 ×2, G0106 ×2, G0112, G0134, G0136); cuts_01..02.jpg (9 cuts, 1/4 scale); residue_crops_01..21.png (168 non-noise hold-residue frames, native + ×6 diff); diff_*.png; extra_checks.json; checks.json; activity_curves.csv; ad-hoc phase-correlation/ECC check f269–284.

## V3 cuts
All 9 cuts (f730, 1090, 1367, 1518, 1801, 2533, 2795, 3539, 3653) viewed before/after: all hard cuts.
**Correction:** hidden hard cut **f777|f778** inside rv1 G0036 (title card → open-freezer scene VS019), viewed in strip_G0036_05; px curve 2,014,561 at f778.

## V4/V5 resolutions
| Seg | rv1 | Resolution (native view) |
|---|---|---|
| G0004 f27–32 | HIGH | Attribution line typed left→right. Confirmed. |
| G0006 f85–90 | HIGH | Question typed left→right. Confirmed. |
| G0016 f262–270 | HIGH | One 9-f blurred camera push-in: Q card ghosts up and out, presenter slides off left, freezer cutaway grows; sharp at f269 (phase shift −3/−3.4 px at f269→270, 0 after). Confirmed. |
| G0018 f283 | LOW "DRIFT_SETTLE", UNRESOLVED | **Resolved:** no motion — phase shift 0.0/0.0 (response 0.995); every line edge re-rendered in place (87k px of sub-pixel edge change, diff_G0018). Treat as a render refresh, not a camera move. |
| G0022 f375–380 | HIGH | Heat lines fade out while frost specks/icicles fade in. Confirmed. |
| G0026 f579 | MEDIUM | **Resolved:** toast gone; grey water stains on ceiling/toaster; the "grey wedge" is a **towel** hanging over the outlet cord. |
| G0028 f648 | LOW | **Resolved:** 1-frame pop of black zigzag spark marks at the toaster corners and down the cord. |
| G0030 f660 | LOW | **Resolved:** 1-frame pop of spark zigzags around the outlet, outlet outline turns wobbly. |
| G0036 f730–778 | MEDIUM, 6/49 | Red series title card **animated every frame** f730–777 (mascot chews satellite; wordmark static); hidden hard cut f777\|f778. All frames viewed. |
| G0050, G0060, G0076, G0098, G0100 | HIGH | Handwritten write-ons (600°C; COLD (FOR TOASTER) bracket; ~1000W; ~100W; ~1000W). Confirmed frame by frame. |
| G0074 f1663–1668 | HIGH | Red glow halo fades in around the upper compartment and grey drips grow. Confirmed. |
| G0080 f1831–1837 | HIGH | Red arrow into fan, zigzag down the coil panel, then arrow + E_OUT. Confirmed. |
| G0096 f2229–2239 | HIGH | Red heat arrows radiate one per frame (1→12) while black input arrows add per frame. Confirmed. |
| G0102 f2458–2469, G0106 f2603–2614 | HIGH | Toaster red glow fades in (G0106 with 600°C label). Confirmed. |
| G0112 f2885–2890 | HIGH | Background darkens white → mid-grey with stars; (-20°C) fades in. Confirmed. |
| G0134 f3280–3285 | HIGH | Ghost-dissolve from standing (startled) to crouched shaking pose; AWOO... fades in; wolves' eyes go. Confirmed. |
| G0136 f3396 | LOW | **Resolved:** 1-frame swap — toast leaves the toaster into the crouched figure's hands. |

Other activities are 1-frame events seen in their before/after natives and rv1 tile view.
**Hidden event (new, from residue):** **f317–322 inside hold G0021/VS011** — red wavy heat lines fade in above the toaster over 6 frames (components 675–718 px). Recorded in corrections.json VS011; the rv1 ledger is not edited.
**INFERRED camera claims tested:** only same-shot hold shift >3 px is G0015→G0017 (dx −107, dy −69, response 0.0) = across the G0016 blurred push-in (a real camera move, confirmed by viewing). G0018 "drift" refuted (above).
**Hold residue:** 275 hold frames >50 px; 107 NOISE by component size; 168 viewed in crops. All edge/text re-encode flicker (incl. the f2641–2794 run: one line edge at (896,61), 21–59 px, repeating every 1–2 frames; f3706 end-card book-cover texture), except f317–322 (above). f1016 heat-line texture = encoder.

## V6 creative
- **Text (native/half-scale):** `Q. Would a toaster still work in a freezer? — My Brother, My Brother and Me (podcast)` (real podcast); `YOU MAY ALSO WANT TO RECONSIDER HAVING YOUR LIGHTING, TOASTER, AND REFRIGERATOR ALL ON ONE CIRCUIT`; `FOR COOLING`, `FOR HEATING`, `600°C`; axis `ABSOLUTE ZERO`, `200K -70°C -100°F` … `1000K 730°C 1340°F`, `TOASTER COILS`, `ROOM TEMPERATURE`, `FRIDGE`, `FREEZER`, `COLD (FOR TOASTER)`; `IF I WANTED A BURNER I WOULD HAVE USED THE STOVE.`; `~1000W`; `E_OUT`, `E_IN`, `COP ≈ 3 (E_OUT/E_IN)`, `COP ≈ 1`, `~100W`; `THAT'S NOT HOW YOU MAKE AN ICE CREAM SANDWICH`, `-18°C`; `WINNIPEG, CANADA (-20°C)`; `AWOO...`; `TOASTERS BEAT FREEZERS.`, `BUT WOLVES BEAT TOASTERS.`; title/end cards (source branding).
- **Palette:** off-white canvas, black line art; red for heat lines, arrows, glow halos, labels; orange coil inside red glow (GLOW plate); grey for stains, frost, towel, the electrified grey-toned scene (VS017–018), and the night scene (mid-grey sky, white stars, black trees, white wolf eyes); red title and end cards.
- **Continuity:** see corrections.json continuity.
- **Originality:** title card, mascot, end card, books, credits, URLs = source branding; replace entirely. Replace the real podcast attribution with an invented source; the three host figures and the podcast table appear to depict real people — use original character designs.

## V7
`reconstruction_blueprint_v2.md` (73 state prompts, motion, continuity, QA, originality).

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV out of scope, unsigned. Single model reviewer.
