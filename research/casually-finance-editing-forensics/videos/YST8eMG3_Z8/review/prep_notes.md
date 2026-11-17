# YST8eMG3_Z8 prep notes (partial, NOT validated; written 2026-10-20 before handover)

Banded, headline 'Everybody's Fighting Over the Same Pile of Debt', 2624 frames, 30 fps (= inventory). `prep_banded.sh` has been run (auto/bands.json, STAGE_EVENTS_AUTO.csv). Sheets are in `../yio-cf-editing-forensics-local-evidence/YST8eMG3_Z8/sheets/` (`overview_1s.png`, `ev_01`, `ev_02`; regenerate with `scripts/make_sheet.py` if absent). Nothing authored yet; frames below are from reviewed sheets (`DIRECTLY_OBSERVED`), frame = native index.

## Scene candidates (start frame -> content)
- S01 f0: OECD report cover infographic (dark blue, centred, small); zoom in f27-54, shrinks and moves left f63-82 (55-frame move, measure with `measure_motion.py camera`); red '29T' + money bag pop at f148; rotated handwritten note writes on f148-168 and a second segment f176-189; f266 the 29T/note group is removed (1 frame) just before the cut.
- S02 f267: host at a desk with laptop beside a shelf-like frame with a window. Window shows a map picture f267-299, empties at f300, then report pages/charts change in the window f307-409 (102 frames), f419-451, f459-483, f495-506, f515-527, f575-580, f589-601, f607-615 (page flick/scroll; mechanism unresolved, classify INDET unless frame-by-frame inspection resolves it). Host face slumps f533-561.
- S03 f616: stick figure with magnifier (static to f677).
- S04 f678: OECD text page ('Nearly 80%') with yellow highlight; small host appears bottom-right ~f814.
- S05 f887: US-map character 'Actual useful things'; bubble 'Boring!' pops ~f917-938.
- S06 f939: old bearded man holding a 'DEBT' paper; slow move/scale f952-1010 (59 frames).
- S07 f1011: text page 'last year the borrowing cost ... $13.5 trillion' with highlight growth; host appears bottom-right ~f1154.
- S08 f1298: host at a blackboard; 'NOT even!' text pops ~f1315.
- S09 f1347: three 'DEBT' papers; red 'PAY IN 2027' paper pops f1374, text swap ~f1428.
- S10 f1477: thinking figure.
- S11 f1538: line chart with two lines ('similar to the United States situation').
- S12 f1623: text page with orange highlight and small DEBT-paper icons at both sides.
- S13 f1904: OECD stacked-area/bar chart; zoom/pan f1938-1990 (53 frames); host pops f1991.
- S14 f2119: text page ('a third of the developed world's debt'); host with pointer pops f2138-2146.
- (inside S14) DEBT paper icon pops f2272; money bag pops f2302.
- S15 f2338: worried host alone ('and we're already seeing it happen').
- S16 f2387: text page with two yellow sticky notes to the end (f2624), static after the cut.
Narration: OECD report on 2026 borrowing (~29 trillion), refinancing share (~80 %), $13.5 -> $14.5 trillion, one third of fixed-rate debt due by 2027, 60 % issued 2021 or earlier, +2 percentage points on new debt, 1/5 of fixed-rate bonds issued above 4 %.

## To do
Measure: S01 zoom/shrink (camera), S13 chart zoom (camera), S06 old-man move (blob/extent), note write-on (extent). Author scenes/events with `scripts/author_lib.py` (copy `videos/ji2qFfcgSB4/review/author_review.py`), set `depth_label` in `auto/bands.json`, run `build_video_tables.py`, write STORY_STRUCTURE.md/findings.md, `write_review.py`.
