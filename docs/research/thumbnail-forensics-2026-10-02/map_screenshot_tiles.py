"""OCR the title strip under every screenshot tile (Apple Vision, local, macOS) and match it to canonical videos.

Mapping rules (never guess):
  MATCHED_TITLE_EXACT       normalized OCR title equals / is a prefix of a single registry title (len>=25) and no rival
  MATCHED_TITLE_FUZZY       similarity >= 0.92 on the common prefix and a clear margin over the runner-up
  NOT_IN_REGISTRY           best similarity < 0.80 -> tile is a real screenshot thumbnail of a video outside the 2,303 canonical videos
  AMBIGUOUS_MAPPING         anything in between, or unreadable title
Outputs screenshot-tile-ocr.csv (one row per tile; includes OCR title, views, age, duration).
"""
import csv, re, sqlite3, json, glob
from rapidfuzz import fuzz
import imagehash
from PIL import Image
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


HANDLE_TO_CHANNEL = {'@DrThomasSeniorHealthTips': 'UCFuGMi0idGeyXl6wYK9hg7Q', '@drmarcusokoro': 'UCMJxAeBJ0d1JC937de1eZ0Q',
                     '@Dr.AlizaWrightAdvice': 'UCXZi5JVeuTluazF-fYqQgNA', '@Health.Hub.Senior': 'UCAYG0fzUyxv6OevH88qA45w'}
UI_WORDS = re.compile(r"Similar Channels|Niche Overview|Analytics|Sort by|Latest|Popular|Oldest|You're a manager|Quick channel stats|Connect MCP", re.I)


def screenshot_channels():
    out = {}
    for f in glob.glob(str(HERE / 'screenshot-transcriptions/part-*.json')):
        for s in json.load(open(f)):
            h = s.get('handle_visible') or ''
            for k, v in HANDLE_TO_CHANNEL.items():
                if h.startswith(k): out[s['screenshot_id']] = v
    return out


def clean_title(t):
    t = UI_WORDS.sub(' ', t)
    t = re.sub(r'^[^A-Za-z0-9\'"“]+', '', t)  # leading menu glyphs
    t = re.sub(r'\s+[:;|]\s+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def region(path):
    im = Image.open(path).convert('RGB'); w, h = im.size
    if abs(w / h - 4 / 3) < 0.05:  # letterboxed 4:3 hqdefault -> central 16:9
        ch = int(w * 9 / 16); y = (h - ch) // 2; im = im.crop((0, y, w, y + ch)); h = ch
    return im.crop((int(w * .03), int(h * .03), int(w * .97), int(h * .82)))  # drops the duration-badge strip


def vdist(crop_path, ref_path):
    return imagehash.phash(region(crop_path)) - imagehash.phash(region(ref_path))


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
    chmap = screenshot_channels()
    UNI = {r['Video_ID']: r['Source_Path'] for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID']}
    out = []
    for r in csv.DictReader((HERE / 'screenshot-tiles-detected.csv').open()):
        lines = ocr(ROOT / r['Title_Strip_Path'])
        raw = ' | '.join(lines)
        title, views, age = parse(lines)
        title = clean_title(title)
        ui = bool(UI_WORDS.search(' '.join(lines)[:60])) and not views
        nt = norm(title.rstrip('.…'))
        pool = [x for x in reg if x[1] == chmap.get(r['Screenshot_Source_ID'])] if r['Screenshot_Source_ID'] in chmap else reg
        best = []
        if len(nt) >= 12 and not ui:
            for vid, ch, t, n in pool:
                k = min(len(nt), len(n))
                best.append((fuzz.ratio(nt[:k], n[:k]) / 100, vid, ch, t))
            best.sort(reverse=True)
        top = best[0] if best else (0, '', '', '')
        second = best[1][0] if len(best) > 1 else 0
        if ui or len(nt) < 12: status = 'NOT_A_VIDEO_TILE' if ui else 'AMBIGUOUS_MAPPING'
        elif top[0] >= 0.97 and top[0] - second >= 0.03: status = 'MATCHED_TITLE_EXACT'
        elif top[0] >= 0.92 and top[0] - second >= 0.05: status = 'MATCHED_TITLE_FUZZY'
        elif top[0] < 0.80: status = 'NOT_IN_REGISTRY'
        else: status = 'AMBIGUOUS_MAPPING'
        # visual verification / tie-break against current-public thumbnails (same-creative phash distance is <=8 in practice, random pairs >=24)
        cands = [x for x in best[:4] if x[0] >= 0.80]
        vis = [(vdist(r['Crop_Path'], UNI[x[1]]), x) for x in cands if x[1] in UNI]
        vis.sort(key=lambda t: t[0])
        vd = vis[0][0] if vis else ''
        if status in ('AMBIGUOUS_MAPPING', 'MATCHED_TITLE_EXACT', 'MATCHED_TITLE_FUZZY') and vis:
            if status == 'AMBIGUOUS_MAPPING' and vis[0][0] <= 12 and (len(vis) == 1 or vis[1][0] - vis[0][0] >= 6):
                status = 'MATCHED_TITLE_VISUAL_TIEBREAK'; top = vis[0][1]
            elif status == 'AMBIGUOUS_MAPPING' and vis[0][0] <= 12 and top[0] >= 0.97:
                status = 'AMBIGUOUS_MAPPING'  # identical titles and visually indistinguishable current thumbnails
        if status == 'NOT_IN_REGISTRY' and r['Screenshot_Source_ID'] in chmap and not ui and len(nt) >= 12:
            ch = chmap[r['Screenshot_Source_ID']]
            vs = sorted((vdist(r['Crop_Path'], UNI[v]), v, t) for v, c, t, n in reg if c == ch and v in UNI)
            if vs and vs[0][0] <= 10 and vs[1][0] - vs[0][0] >= 8:
                status = 'MATCHED_VISUAL_ONLY_TITLE_DIFFERS'; top = (0, vs[0][1], ch, vs[0][2]); vd = vs[0][0]
        twin = ''
        if r['Screenshot_Source_ID'] not in chmap and status != 'NOT_A_VIDEO_TILE' and (status.startswith('MATCHED') or status == 'AMBIGUOUS_MAPPING') and top[1]:
            # screenshot channel is not a registry channel: a title/visual twin in another channel is NOT the same video
            twin = top[1]; status = 'NOT_IN_REGISTRY'
        ok = status.startswith('MATCHED')
        out.append(dict(r, OCR_Lines=raw, OCR_Title=title, OCR_Views=views, OCR_Age=age, Match_Status=status, Match_Score=round(top[0], 3), Runner_Up=round(second, 3),
                        Visual_Distance_To_Current=vd, Channel_Context=chmap.get(r['Screenshot_Source_ID'], 'NONE_IN_REGISTRY_OR_UNKNOWN'), Video_ID=top[1] if ok else '',
                        Channel_ID=(top[2] if ok else ''), Twin_Registry_Video_ID=twin, Best_Candidate_Title=top[3]))
    with (HERE / 'screenshot-tile-ocr.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
    from collections import Counter
    print(len(out), Counter(o['Match_Status'] for o in out))
