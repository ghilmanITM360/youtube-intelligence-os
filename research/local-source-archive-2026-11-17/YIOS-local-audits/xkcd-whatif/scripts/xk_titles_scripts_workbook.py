"""Build XKCD_What_If_Titles_and_Full_Scripts.xlsx from saved local sources only (read-only on sources).

Sources: census.csv (91 unique videos, exact titles), repo catalog DS-000017 caption texts (83),
local Whisper small.en segments (70). Then reopen and validate. Run: python3 -I <this> <out.xlsx>
"""
import csv, hashlib, json, os, sqlite3, sys
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

REPO = '/Users/ghilmankhan/workprojects/youtube-intelligence-os/'
XK = '/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/'
CENSUS = XK + 'census/census.csv'
DATASET = REPO + 'data/raw/competitors/DS-000017/dataset.json'
LIMIT = 32000  # Excel cell max is 32,767 chars; keep margin
OUT = sys.argv[1]

def ts(s):
    s = float(s); return '%02d:%05.2f' % (s // 60, s % 60)

def chunks(t):
    return [t[i:i + LIMIT] for i in range(0, len(t), LIMIT)] or ['']

cen = list(csv.DictReader(open(CENSUS, encoding='utf-8')))
ds = {d['id']: (i, d) for i, d in enumerate(json.load(open(DATASET, encoding='utf-8')))}
db = sqlite3.connect('file:' + REPO + 'data/catalog/youtube_inventory.db?mode=ro', uri=True)
cat = {r[0]: r for r in db.execute(
    "select v.youtube_video_id,t.transcript_id,t.canonical_reference,t.transcript_sha256,t.caption_type "
    "from transcripts t join videos v using(video_id) where v.channel_id='CH-000004'")}

rows, expected = [], {}
for n, c in enumerate(cen, 1):
    v = c['video_id']
    cap = asr = None
    if v in cat:
        b = open(REPO + cat[v][2], 'rb').read()
        assert hashlib.sha256(b).hexdigest() == cat[v][3], v
        cap = b.decode('utf-8')
        assert ds[v][1]['subtitles'][0]['plaintext'] == cap, v
    ap = XK + 'videos/%s/asr/asr_small_en_segments.csv' % v
    if os.path.exists(ap):
        seg = list(csv.DictReader(open(ap, encoding='utf-8')))
        asr = '\n'.join('[%s–%s] %s' % (ts(s['start']), ts(s['end']), s['text'].strip()) for s in seg)
        asr_words = sum(len(s['text'].split()) for s in seg)
    flags = []
    if cap is not None:
        kind = cat[v][4]
        status = 'FULL'
        src = 'YouTube %s captions (Apify capture, repo catalog)' % ('creator-uploaded' if kind == 'user_generated' else 'auto-generated')
        main = cap
        if asr:
            ratio = len(cap.split()) / max(asr_words, 1)
            if ratio < 0.85:
                status = 'PARTIAL'; flags.append('Caption has %.0f%% of the words in local ASR — may be truncated' % (ratio * 100))
        else:
            flags.append('No local audio/ASR to cross-check completeness')
        flags.append('Saved captions have no timestamps' + ('; Whisper timestamps in column K' if asr else ''))
    elif asr:
        status, src, main = 'FULL', 'Local Whisper small.en machine transcription of saved video (no saved captions)', asr
        flags.append('Machine ASR, not creator captions — wording may differ slightly from spoken audio')
    else:
        status, src, main = 'MISSING', '', ''
        flags.append('No saved captions, no local video/audio — title only')
    if c['title'] in [x['title'] for x in cen if x['video_id'] != v]:
        flags.append('Another video ID has the same title (separate upload, kept separate)')
    srcref = []
    if cap is not None:
        srcref.append('%s | catalog transcript %s | DS-000017/dataset.json item [%d]' % (cat[v][2], cat[v][1], ds[v][0]))
    if asr:
        srcref.append(ap.replace('/Users/ghilmankhan/', '~/'))
    srcref.append('census.csv row %d (snapshot %s)' % (n + 1, c['snapshot_utc']))
    rows.append(dict(v=v, url=c['canonical_url'], title=c['title'],
                     fmt='Long-form' if c['format_class'] == 'LONG_FORM' else 'Short',
                     dur=int(c['duration_s']) if c['duration_s'].isdigit() else c['duration_s'],
                     pub=c['publish_datetime'][:10], status=status, src=src, main=main, asr=asr or '',
                     ref='\n'.join(srcref), flags='; '.join(flags)))
    expected[v] = (c['title'], main, asr or '')

wb = Workbook()
ws = wb.active; ws.title = 'Titles and Scripts'
parts = wb.create_sheet('Script Parts')
hdr = ['#', 'Video ID', 'YouTube URL', 'Exact Video Title', 'Format', 'Duration (s)', 'Published',
       'Transcript Status', 'Transcript Source', 'Full Original Transcript',
       'Timestamped Transcript (local Whisper ASR)', 'Script Parts Link', 'Source File / Record Reference', 'Flags']
ws.append(hdr)
parts.append(['Video ID', 'Column', 'Part #', 'Part Count', 'Text'])
F = Font(name='Arial', size=10); B = Font(name='Arial', size=10, bold=True, color='FFFFFF')

def put(cell, val):
    cell.value = val
    if isinstance(val, str) and val.startswith('='):
        cell.data_type = 's'  # literal text, never a formula

for i, r in enumerate(rows, 2):
    vals = [i - 1, r['v'], r['url'], r['title'], r['fmt'], r['dur'], r['pub'], r['status'], r['src'],
            r['main'], r['asr'], '', r['ref'], r['flags']]
    for j, val in enumerate(vals, 1):
        put(ws.cell(i, j), val)
    links = []
    for col, key in (('J', 'main'), ('K', 'asr')):
        if len(r[key]) > LIMIT:
            cs = chunks(r[key]); first = parts.max_row + 1
            for k, t in enumerate(cs, 1):
                parts.append([r['v'], col, k, len(cs), None]); put(parts.cell(parts.max_row, 5), t)
            ws['%s%d' % (col, i)] = 'SEE SCRIPT PARTS (%d parts)' % len(cs)
            links.append(first)
    if links:
        ws.cell(i, 12).value = '=HYPERLINK("#\'Script Parts\'!A%d","Open parts")' % links[0]
    ws.cell(i, 3).hyperlink = r['url']
if parts.max_row == 1:
    parts.append(['(none)', '', '', '', 'Every transcript fits in one cell (max %d chars); no chunking needed.' % max(len(r['main']) for r in rows)])

for sh in (ws, parts):
    for row in sh.iter_rows():
        for c in row:
            c.font = F; c.alignment = Alignment(wrap_text=True, vertical='top')
    for c in sh[1]:
        c.font = B; c.fill = PatternFill('solid', fgColor='1F3864')
    sh.freeze_panes = 'A2'
for col, w in zip('ABCDEFGHIJKLMN', [5, 14, 30, 40, 10, 9, 11, 11, 30, 90, 70, 12, 50, 45]):
    ws.column_dimensions[col].width = w
parts.column_dimensions['E'].width = 100
ws.auto_filter.ref = ws.dimensions

s = wb.create_sheet('Summary')
for line in [
    ['xkcd What If? (@xkcd_whatif, UC6IxnFzHofFJ5X2PycSMsww) — titles and full original transcripts'],
    ['Built from saved local sources only; no new scraping or paid runs. Sources were read, not modified.'],
    [],
    ['Metric', 'Value'],
    ['Unique videos (by video ID)', '=COUNTA(\'Titles and Scripts\'!B2:B1000)'],
    ['FULL', '=COUNTIF(\'Titles and Scripts\'!H2:H1000,"FULL")'],
    ['  of which creator/auto captions', '=COUNTIFS(\'Titles and Scripts\'!H2:H1000,"FULL",\'Titles and Scripts\'!I2:I1000,"YouTube*")'],
    ['  of which local Whisper ASR only', '=COUNTIFS(\'Titles and Scripts\'!H2:H1000,"FULL",\'Titles and Scripts\'!I2:I1000,"Local Whisper*")'],
    ['PARTIAL', '=COUNTIF(\'Titles and Scripts\'!H2:H1000,"PARTIAL")'],
    ['MISSING', '=COUNTIF(\'Titles and Scripts\'!H2:H1000,"MISSING")'],
    ['Long-form', '=COUNTIF(\'Titles and Scripts\'!E2:E1000,"Long-form")'],
    ['Shorts', '=COUNTIF(\'Titles and Scripts\'!E2:E1000,"Short")'],
    [],
    ['Source', 'Path'],
    ['Video list + exact titles', CENSUS.replace('/Users/ghilmankhan/', '~/') + ' (channel tab snapshot 2026-11-04)'],
    ['Captions (plain text)', 'repo data/raw/competitors/DS-000017/ (Apify run mzl5dCHF81LbcBamS, SHA-256 verified vs catalog)'],
    ['Timestamps', '~/YIOS-local-audits/xkcd-whatif/videos/<id>/asr/asr_small_en_segments.csv (machine ASR)'],
    ['Not found', '"what if data .pdf" is not on this Mac; no PDF source used'],
    ['Excluded', 'Forensic analysis, production notes, Q&A and generated What If scripts are not in any transcript column'],
]:
    s.append(line)
for row in s.iter_rows():
    for c in row: c.font = F
s['A1'].font = Font(name='Arial', size=12, bold=True)
s.column_dimensions['A'].width = 36; s.column_dimensions['B'].width = 100
wb.move_sheet('Summary', offset=-2)
wb.calculation.fullCalcOnLoad = True  # no LibreOffice here; Excel/Numbers compute the COUNTIFs on open
wb.save(OUT)

# ---- validate: reopen and compare against sources ----
wb = load_workbook(OUT)
ws = wb['Titles and Scripts']
pm = {}
for r in wb['Script Parts'].iter_rows(min_row=2, values_only=True):
    if r[0] != '(none)': pm.setdefault((r[0], r[1]), []).append((r[2], r[3], r[4] or ''))
def text(v, col, cell):
    if (v, col) in pm:
        p = sorted(pm[(v, col)]); assert [x[0] for x in p] == list(range(1, p[0][1] + 1)), v
        return ''.join(x[2] for x in p)
    return cell or ''
ids = [r[1] for r in ws.iter_rows(min_row=2, values_only=True)]
assert len(ids) == len(set(ids)) == len(expected), (len(ids), len(set(ids)))
st = {}
for r in ws.iter_rows(min_row=2, values_only=True):
    t, m, a = expected[r[1]]
    assert r[3] == t, ('title', r[1])
    assert text(r[1], 'J', r[9]) == m, ('main', r[1])
    assert text(r[1], 'K', r[10]) == a, ('asr', r[1])
    st[r[7]] = st.get(r[7], 0) + 1
print(json.dumps({'unique_videos': len(ids), 'status': st, 'chunked_cells': len(pm),
                  'chars_checked': sum(len(e[1]) + len(e[2]) for e in expected.values()), 'validation': 'PASS'}))
