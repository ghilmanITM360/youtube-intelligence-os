# CH001 novel-scene tests (2026-11-20) — SELF-CHECK, NOT INDEPENDENT QA
Script: render_novel.py (imports helpers from render_10nEByVLya0_v6.py). Outputs: RENDERED_OUTPUTS/novel_scene/NS1_inflation_cash.mp4, NS2_compound_growth.mp4 (270 frames, 1080x1920, 30 fps, silent).
| Test | Family | Brief | Storyboard (frames) |
|---|---|---|---|
| NS1 | character scene | cash loses value as prices rise | f0 man + cash pop (f6) / f60 price tag $5->$7 red arrow, cash shrinks / f140 sweat + ? pop / f200 hard cut to "cash value" red arrow |
| NS2 | chart/data scene | compound growth | title / f20 axes + bars grow x1.38 per year / f190 "10x" |
Checks run: content stays inside y 655-1265 (measured bbox 685-1263 NS2, 760-1195 NS1 after fixing an overflow found on first render); caption block uses v4 rule (centre y1353, wrap 800); palette and outline rules from 05_VISUAL_DNA.md; same helper functions (stick, qmark, bag) as the reconstruction, which shows reuse, not that the style is indistinguishable from the channel.
Limits: no independent reviewer ran; no side-by-side against channel footage beyond the numeric layout checks; captions are evenly timed placeholders (no voiceover); characters limited to the measured brown stick man; no new character families tested. Rulebook asks for two tests across different families: done as prototypes (interim milestone), not final-GO evidence until reviewed.

## Round 2 (2026-11-20): family-conditional tests, measured with the SAME tools as the references (MULTI_VIDEO_MEASUREMENTS/measure.py)
Renderer `render_novel2.py`; outputs `RENDERED_OUTPUTS/NS3_emergency_fund_uncaptioned.mp4` (24 s) and `NS4_emergencies_captioned.mp4` (18 s). Original art/topics; silent; caption text for NS4 is placeholder wording with evenly spaced word timing (not real ASR).
| Check | NS3 (family B target: 33NV/zLv) | NS4 (family A target: 10nE/1eTw) |
|---|---|---|
| Bg #FDFDFD, art in 35-65% band | PASS (rows 688-1088) | PASS (736-1384 incl. caption) |
| Bottom caption presence per family rule | PASS (none; OCR bins 6-7 = 0) | PASS (OCR bin 7 = 16 words) |
| Mean state duration vs family (B 1.8-1.9 s; A 0.7-0.9 s) | 2.67 s: slower than target (merged states), FAIL by ~1.4x | 0.46 s: busier than target (caption changes count as states), FAIL by ~0.6x |
| Cuts/10 s (B 0.4-0.8; A 0.9-1.6) | 0.0 (borderline for B) | 0.0 FAIL (my scenes change little ink per cut) |
| Visual fidelity vs a real video | NOT measurable: no reference for these topics; no human/blind review | same |
Verdict: structural rules (bg, band, caption presence) transfer; pacing parameters do NOT yet transfer (state rate off by 0.6-1.4x, cut metric off). This is a proxy test against numeric family stats, not visual quality validation. Independent review still not done.

### Round 2b (2026-11-20): pacing retune (NS4 beat 28 f, bigger art; NS3 beat 42 f, bigger art)
| Metric | NS3 | NS4 |
|---|---|---|
| Mean state s (target B 1.8-1.9 / A 0.7-0.9) | 2.67 (unchanged; additive text beats merge into one state) FAIL | **0.69 PASS** |
| Cuts/10 s (mean-diff>18) | 0.0 | 0.0 |
Finding: the cuts metric needs ~30% of the frame area to change, which a 610-px flat-art band rarely does even with large art; in the references it is driven by large Earth/clip panels. It measures art area, not editing pace, so it is **deprecated as a pacing parameter**; use state rate (states/s) instead. NS3 remains FAIL on state rate (beats add text to existing art instead of changing it).
Round 2c: NS3 beats now replace art (stick left/right, one word per beat): 11 states, mean 2.18 s vs target 1.77-1.91 (+14-23%): **near-pass, still outside +-10%**. NS4 0.69 s PASS (target 0.7-0.9). Pacing is parameterised only by hand-tuned beat length; no automatic rule yet. Score unchanged at 51/100.

## Round 3 (2026-11-20): NS5 family B panel-fill (`render_novel3.py` -> `RENDERED_OUTPUTS/NS5_retire_early_panelfill.mp4`, 24.3 s, silent, original art/topic)
Targets from T3 of 33NV/zLv/xdF8. Measured with the same tools:
| Check | Target | NS5 v1 | NS5 v2 |
|---|---|---|---|
| Bottom caption absent | none | PASS | PASS |
| Content band | y ~712-1263 | 744-1200 PASS | 696-1216 PASS |
| Mean state s | 1.77-1.91 | 4.06 FAIL (full-width panels keep the ink mask constant; only small black art changed) | **1.87 PASS** |
| Panel colours | green #309050 / orange #F09010 | exact by construction | same |
| Black ink share 11-44% of ink | 11-44% | ~3-15% (low) | not re-measured |
v2 changes: panel geometry varied per beat (inset/half-width panels) and two dark-panel beats added. **Caveat: this was tuned to the state-rate metric; the geometry variation is my assumption, not a measured rule from the references.** No blind visual comparison, no audio, dialogue text is placeholder, black-ink share not verified, hand-font differs from the source's lettering (UNVERIFIED). Counts as a structural/pacing proxy pass for family B only.
