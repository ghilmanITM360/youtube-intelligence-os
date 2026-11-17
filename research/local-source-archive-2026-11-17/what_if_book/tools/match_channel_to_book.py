import csv
import json
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path('/Users/ghilmankhan/workprojects/what if book')
BOOK = ROOT / 'WhatIf_Complete_Extraction/01_ALL_QUESTIONS/all_questions.json'
VIDEOS = ROOT / 'XKCD_What_If_Titles_and_Full_Scripts.xlsx'
OUT = ROOT / 'WhatIf_Complete_Extraction/07_CHANNEL_BOOK_COMPARISON'

# Exact question/answer overlap reviewed against titles and the saved full scripts.
# One upload may cover several original book questions.
MATCH = {
    2:[91],4:[1],5:[2],7:[21],8:[3],9:[10],10:[82],11:[15],12:[66],
    13:[78],14:[67],16:[36],17:[75],18:[8],24:[77],28:[91],29:[91],
    31:[82],32:[21],33:[15],36:[11],43:[1],44:[1],45:[70],46:[2],
    49:[3],50:[10],52:[66],53:[67],54:[40],55:[78],57:[16],60:[17],
    64:[77],80:[4,18,29,13,14],82:[70],87:[30,42,74,48,49,63],
    88:[40],89:[17],
}
EXCERPT = {28,29,31,32,33}
COMPILATION = {80,87}
TITLE_ONLY = {89}

questions = {int(q['question_id'][3:]):q for q in json.loads(BOOK.read_text())}
ws = load_workbook(VIDEOS, read_only=True, data_only=True)['Titles and Scripts']
rows = []
for cells in list(ws.values)[1:]:
    n, video_id, url, title, fmt, _, _, transcript_status, source, transcript, *_ = cells
    ids = MATCH.get(n, [])
    if n in COMPILATION:
        kind = 'BOOK_2014_COMPILATION'
    elif n in EXCERPT:
        kind = 'BOOK_2014_ANSWER_EXCERPT'
    elif ids:
        kind = 'BOOK_2014_QUESTION_ANSWER'
    else:
        kind = 'NO_IDENTIFIED_BOOK_2014_MATCH'
    confidence = 'TITLE_ONLY_PROBABLE' if n in TITLE_ONLY else ('SCRIPT_CHECKED' if transcript else 'NO_TRANSCRIPT')
    rows.append({
        'video_number':n,'video_id':video_id,'youtube_url':url,'video_title':title,
        'format':fmt,'classification':kind,'book_question_ids':'; '.join(f'WI-{i:04}' for i in ids),
        'book_chapter_titles':'; '.join(dict.fromkeys(questions[i]['chapter_title'] for i in ids)),
        'transcript_status':transcript_status,'match_evidence':confidence,
        'source_workbook':str(VIDEOS),
    })

OUT.mkdir(exist_ok=True)
with (OUT/'all_91_video_matches.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
matched=[r for r in rows if r['book_question_ids']]
unique_ids={i for ids in MATCH.values() for i in ids}
count_by_format={fmt:sum(r['format']==fmt for r in matched) for fmt in ('Long-form','Short')}
report=f'''# xkcd What If? channel versus the 2014 book

## Count

- Channel census: **{len(rows)} public videos** (snapshot 2026-11-04; 45 long-form and 46 Shorts).
- **{len(matched)} videos** contain an identifiable question, answer, or answer excerpt from the **2014 book**: {count_by_format}.
- These videos cover **{len(unique_ids)} distinct book question records**. A video can cover multiple questions; several videos can cover one question.
- **{len(rows)-len(matched)} videos** have no identified match among the 91 extracted book questions.
- **Video 89** has a matching title but no transcript in the saved workbook: count is probable, pending script verification. Thus the script-confirmed count is **{len(matched)-1}**.

This establishes **content overlap** with the 2014 book. Since many chapters were also published on the What If? website, overlap alone does not establish that the production team adapted the printed book rather than the original web article. The channel describes its series as an adaptation of the *What If? books*.

## Method and limitations

Compared the 91-video public channel census with the saved workbook of titles and full scripts, then matched submitted-question wording and answer content to the local 91-question book extraction. Counted each upload once, including Shorts, even when two Shorts retell one chapter. Two Weird and Worrying compilations collectively cover 11 book questions but count as two videos. The 10th-anniversary-only “MORE power” chapter was excluded from this 2014-edition match.

The saved workbook has one missing transcript for a matching video. Live public channel counts can change after the census snapshot. The underlying book OCR still has unresolved proofreading, so this is an evidence-based content classification rather than a certified edition provenance audit.

## Matching videos

| # | Format | Video | Book ID(s) | Evidence |
|---:|---|---|---|---|
'''
for r in matched:
    report+=f"| {r['video_number']} | {r['format']} | [{r['video_title']}]({r['youtube_url']}) | {r['book_question_ids']} | {r['match_evidence']} |\n"
report+='\nFull 91-video classification: `all_91_video_matches.csv`.\n'
(OUT/'comparison_report.md').write_text(report)
print(json.dumps({'channel_videos':len(rows),'matched_videos':len(matched),'script_confirmed':len(matched)-1,'distinct_book_questions':len(unique_ids),'matched_by_format':count_by_format,'output':str(OUT)},indent=2))
