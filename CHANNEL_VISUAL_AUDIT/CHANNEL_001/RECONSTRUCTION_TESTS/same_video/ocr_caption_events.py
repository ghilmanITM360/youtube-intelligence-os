"""OCR the reference caption band (y1280-1440) at every caption_event_ledger frame -> caption_ocr_10nE.json [{f, text(lines list)}]. Reads reference TEXT (internal use). Usage: ocr_caption_events.py REF.mp4 LEDGER.csv OUT.json"""
import csv, json, subprocess, sys, os, tempfile
ref, led, out = sys.argv[1:4]
ev = [int(r['start_frame']) for r in csv.DictReader(open(led))]
res = []; td = tempfile.mkdtemp()
for e in ev:
    png = os.path.join(td, 'c.png')
    subprocess.run(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-i', ref, '-vf', f'select=eq(n\\,{e+1}),crop=1080:170:0:1270,scale=2160:-1', '-frames:v', '1', png], check=True)
    t = subprocess.run(['tesseract', png, '-', '--psm', '6'], capture_output=True, text=True).stdout
    res.append({'f': e, 'lines': [l.strip() for l in t.splitlines() if l.strip()]})
json.dump(res, open(out, 'w'), indent=0); print(len(res), res[:5])
