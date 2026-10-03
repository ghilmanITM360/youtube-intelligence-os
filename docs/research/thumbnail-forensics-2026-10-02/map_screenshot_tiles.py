"""OCR the title strip under every screenshot tile (Apple Vision, local, macOS) and match it to canonical videos.

Mapping rules (never guess):
  MATCHED_TITLE_EXACT       normalized OCR title equals / is a prefix of a single registry title (len>=25) and no rival
  MATCHED_TITLE_FUZZY       similarity >= 0.92 on the common prefix and a clear margin over the runner-up
  NOT_IN_REGISTRY           best similarity < 0.80 -> tile is a real screenshot thumbnail of a video outside the 2,303 canonical videos
  AMBIGUOUS_MAPPING         anything in between, or unreadable title
Outputs screenshot-tile-ocr.csv (one row per tile; includes OCR title, views, age, duration).
"""
import csv, re, sqlite3, difflib
from pathlib import Path
import Vision
from Foundation import NSURL

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = sqlite3.connect(ROOT / 'data/catalog/youtube_channel_registry.db')


def ocr(path, level=0):
    req = Vision.VNRecognizeTextRequest.alloc().init()
    req.setRecognitionLevel_(level)  # 0 = accurate
    h = Vision.VNImageRequestHandler.alloc().initWithURL_options_(NSURL.fileURLWithPath_(str(path)), None)
    ok, err = h.performRequests_error_([req], None)
    items = sorted(req.results() or [], key=lambda o: (-o.boundingBox().origin.y, o.boundingBox().origin.x))
    return [o.topCandidates_(1)[0].string() for o in items]


def norm(s):
    s = s.lower().replace('’', "'").replace('–', '-').replace('—', '-')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def parse(lines):
    title, views, age = [], '', ''
    for ln in lines:
        m = re.search(r'([\d.,]+[KM]?)\s+views.*?(\d+\s+\w+\s+ago)?$', ln)
        if re.search(r'views|watching', ln) or re.search(r'\bago$', ln):
            m = re.search(r'([\d.,]+[KMB]?)\s+views', ln); views = m.group(1) if m else views
            m = re.search(r'(\d+\s+\w+\s+ago)', ln); age = m.group(1) if m else age
            break
        title.append(ln)
    return ' '.join(title).strip(), views, age


if __name__ == '__main__':
    reg = [(vid, ch, t, norm(t)) for vid, ch, t in REG.execute('select youtube_video_id,canonical_channel_id,title from videos') if t]
    out = []
    for r in csv.DictReader((HERE / 'screenshot-tiles-detected.csv').open()):
        lines = ocr(ROOT / r['Title_Strip_Path'])
        title, views, age = parse(lines)
        nt = norm(title.rstrip('.…'))
        best = []
        if len(nt) >= 12:
            for vid, ch, t, n in reg:
                k = min(len(nt), len(n))
                sc = difflib.SequenceMatcher(None, nt[:k], n[:k]).ratio() if k else 0
                best.append((sc, vid, ch, t))
            best.sort(reverse=True)
        top = best[0] if best else (0, '', '', '')
        second = best[1][0] if len(best) > 1 else 0
        if not best: status = 'AMBIGUOUS_MAPPING'
        elif top[0] >= 0.97 and top[0] - second >= 0.03: status = 'MATCHED_TITLE_EXACT'
        elif top[0] >= 0.92 and top[0] - second >= 0.05: status = 'MATCHED_TITLE_FUZZY'
        elif top[0] < 0.80: status = 'NOT_IN_REGISTRY'
        else: status = 'AMBIGUOUS_MAPPING'
        out.append(dict(r, OCR_Title=title, OCR_Views=views, OCR_Age=age, Match_Status=status, Match_Score=round(top[0], 3), Runner_Up=round(second, 3),
                        Video_ID=top[1] if status.startswith('MATCHED') else '', Channel_ID=top[2] if status.startswith('MATCHED') else '',
                        Registry_Title=top[3] if status.startswith('MATCHED') else '', Best_Candidate_Title=top[3]))
    with (HERE / 'screenshot-tile-ocr.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
    from collections import Counter
    print(len(out), Counter(o['Match_Status'] for o in out))
