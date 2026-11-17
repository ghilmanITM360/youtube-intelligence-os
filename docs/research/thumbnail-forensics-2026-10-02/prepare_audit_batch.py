"""Prepare one audit batch: ordered thumbnail list, viewable JPEGs (native, 320x180, 160x90 sheets) and input.json.

Queue order = SHA-256 of Thumbnail_ID (deterministic pseudo-random mix of channels/niches/formats), excluding
the six B001 thumbnails. Batch B002-NN is slice NN (size 24) of that fixed queue. Views are JPEG derivatives for the
reviewer only; the evidence files are never modified. Mobile sheets are kept in the repo for QA replay.
Usage: prepare_audit_batch.py B002-01 [size=24]
"""
import csv, hashlib, json, sys
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCRATCH = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/audit')
SHEETS = HERE / 'audit-sheets'


def queue():
    done = {r['Thumbnail_ID'] for r in csv.DictReader((HERE / 'individual-audit-batch-001.csv').open())}
    feats = {r['Thumbnail_ID']: r for r in csv.DictReader((HERE / 'visual-features.csv').open())}
    allr = [r for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID'] and r['Audit_Required'] == 'Y']
    key = lambda r: hashlib.sha256(r['Thumbnail_ID'].encode()).hexdigest()
    cur = sorted([r for r in allr if r['Evidence_Class'] in ('REGISTERED_LOCAL_THUMBNAIL', 'CURRENT_PUBLIC_THUMBNAIL')], key=key)
    shot = sorted([r for r in allr if r['Evidence_Class'] == 'SCREENSHOT_EMBEDDED_THUMBNAIL'], key=key)  # appended after the registry thumbnails so earlier batches stay stable
    return [(r, feats[r['Thumbnail_ID']]) for r in cur + shot if r['Thumbnail_ID'] not in done]


def load(path):
    im = Image.open(ROOT / path).convert('RGB')
    if abs(im.width / im.height - 4 / 3) < 0.05:  # letterboxed 4:3 hqdefault: keep native view but note it
        pass
    return im


if __name__ == '__main__':
    bid = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    k = int(bid.split('-')[1]); q = queue()[(k - 1) * n:k * n]  # batch NN = slice NN of the fixed queue
    out = SCRATCH / bid; out.mkdir(parents=True, exist_ok=True); SHEETS.mkdir(exist_ok=True)
    items = []
    for i, (r, f) in enumerate(q, 1):
        im = load(r['Source_Path'])
        view = out / f'{i:02d}.jpg'
        v = im.copy(); v.thumbnail((1280, 720)); v.save(view, quality=93)
        items.append(dict(Seq=i, Thumbnail_ID=r['Thumbnail_ID'], View_Path=str(view), Video_ID=r['Video_ID'], Channel_ID=r['Channel_ID'],
                          Channel_Name=r['Channel_Name'], Niche_Label=r['Niche_Label'], Format=r['Format'], Title=r['Title'], Published_At=r['Published_At'],
                          Dataset_IDs=r['Dataset_IDs'], Source_Path=r['Source_Path'], Native_Size=f"{r['Width']}x{r['Height']}",
                          Observation_Context=r['Notes'], Mapping_Confidence=r['Mapping_Confidence'], Evidence_Class=r['Evidence_Class'], Creative_Temporal_Alignment=r['Creative_Temporal_Alignment'], Source_Observation_Date=r['Source_Observation_Date'],
                          Letterbox_Cropped=f['Letterbox_Cropped'],
                          Objective_Features={k: f[k] for k in ('Mean_Luminance', 'Contrast_Std', 'Mean_Saturation', 'Dominant_Colors', 'Color_Count_Proxy', 'Edge_Density',
                                                                  'Background_Edge_Density', 'Strong_Edge_Block_Ratio', 'Face_Count_Haar', 'Largest_Face_Area_Ratio')}))
    for tag, (w, h, cols) in {'320': (320, 180, 4), '160': (160, 90, 6)}.items():
        rows = (len(q) + cols - 1) // cols
        sh = Image.new('RGB', (cols * (w + 6), rows * (h + 16)), (20, 20, 20)); d = ImageDraw.Draw(sh)
        for i, (r, f) in enumerate(q):
            im = load(r['Source_Path']); im = im.crop((0, (im.height - int(im.width * 9 / 16)) // 2, im.width, (im.height + int(im.width * 9 / 16)) // 2)) if abs(im.width / im.height - 4 / 3) < 0.05 else im
            x, y = (i % cols) * (w + 6), (i // cols) * (h + 16)
            sh.paste(im.resize((w, h), Image.LANCZOS), (x, y + 14)); d.text((x + 2, y + 1), f'#{i+1:02d}', fill=(255, 255, 0))
        sh.save(out / f'sheet_{tag}.jpg', quality=92)
        sh.save(SHEETS / f'{bid}-mobile-{tag}.jpg', quality=85)
    (out / 'input.json').write_text(json.dumps(items, indent=1))
    print(bid, len(items), 'items ->', out)
