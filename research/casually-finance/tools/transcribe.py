#!/usr/bin/env python3
"""Usage: transcribe.py MODEL ID [ID...]  -- local openai-whisper, ASR_UNCERTIFIED, writes transcripts/<id>.{json,txt}. Skips existing."""
import csv, json, os, sys, time, hashlib
import whisper
model_name, ids = sys.argv[1], sys.argv[2:]
D = os.path.expanduser("~/YIOS-local-audits/CF_TRANSCRIPTS_ASR_20261109")
MEDIA = os.path.expanduser("~/Downloads/videos in mp3/CasuallyFinance")
rows = list(csv.DictReader(open(f"{D}/manifest.csv", encoding="utf-8")))
pri = {"ID_IN_NAME": 0, "MANUAL_TITLE+DUR": 1, "TITLE_PREFIX+DUR": 2}
os.makedirs(f"{D}/transcripts", exist_ok=True)
m = whisper.load_model(model_name, device="cpu")
for vid in ids:
    out = f"{D}/transcripts/{vid}.json"
    if os.path.exists(out):
        print(vid, "skip exists"); continue
    c = sorted([r for r in rows if r["video_id"] == vid and r["match"] in pri], key=lambda r: pri[r["match"]])
    if not c:
        print(vid, "NO_SOURCE"); continue
    r = c[0]; t0 = time.time()
    res = m.transcribe(f"{MEDIA}/{r['file']}", word_timestamps=True, fp16=False, language="en")
    el = time.time() - t0
    json.dump(dict(video_id=vid, source_file=r["file"], source_sha256=r["sha256"], local_dur=float(r["local_dur"]),
        model=model_name, engine="openai-whisper", status="ASR_UNCERTIFIED", device="cpu", elapsed_s=round(el, 1),
        language=res["language"], text=res["text"], segments=res["segments"]), open(out, "w"), ensure_ascii=False)
    open(f"{D}/transcripts/{vid}.txt", "w").write(res["text"].strip() + "\n")
    print(vid, f"{float(r['local_dur']):.0f}s audio in {el:.0f}s ({float(r['local_dur'])/el:.1f}x)", flush=True)
