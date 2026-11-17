"""Concatenate per-video tables of COMPLETE videos into 03_MASTER_DATA/MASTER_*.csv (union of columns) and validate (video_id, id) uniqueness.
Usage: python3 -B aggregate_master.py <OUT_DIR>"""
import csv, json, sys
from pathlib import Path
out = Path(sys.argv[1]); prog = json.load(open(out / "00_MANIFEST/PROGRESS.json"))
ORDER = ["roe3SgezmmU", "Uumnx2Fo6cE", "xtqbRt94TTw", "o3FQcd91MIs", "dlBhLhn8lL0", "kwMHrTFCWUE", "DgbHW0IqHrI", "5umJ63d3rzQ", "0ll9rEtoRrs", "-X6YzlY_8tM",
         "2EZzwupIa80", "YGC3ao005as", "PxgCsLSf-w4", "6S3PzAUFnXQ", "rSa2aziEsAI", "JsK53moCyZA", "turJ6VMfUjI", "Qof71Ef-3EU"]
done = [v for v in ORDER if prog["videos"].get(v, {}).get("status") == "COMPLETE"]
MAP = {"MASTER_WORDS": ("TRANSCRIPT.csv", "word_id"), "MASTER_SENTENCES": ("SENTENCES.csv", "sentence_id"), "MASTER_SHOTS": ("SHOTS.csv", "shot_id"), "MASTER_STATES": ("STATES.csv", "state_id"),
       "MASTER_MOTIONS": ("MOTIONS.csv", "motion_id"), "MASTER_ASSETS": ("ASSETS.csv", None), "MASTER_AUDIO_EVENTS": ("AUDIO_EVENTS.csv", "audio_event_id"),
       "MASTER_AUDIO_VISUAL_SYNC": ("AUDIO_VISUAL_SYNC.csv", "sync_id"), "MASTER_SEMANTIC_BEATS": ("SEMANTIC_BEATS.csv", "beat_id"), "MASTER_FINANCE_CLAIMS": ("FINANCE_CLAIMS.csv", "claim_id")}
res = {"videos_included": done, "tables": {}}
for name, (fn, key) in MAP.items():
    cols, rows, seen, dup, per = ["video_id"], [], set(), 0, {}
    for v in done:
        p = out / "02_VIDEO_FORENSICS" / v / fn
        if not p.exists(): per[v] = "MISSING_FILE"; continue
        rs = list(csv.DictReader(open(p, newline="")))
        for r in rs:
            r.setdefault("video_id", v)
            for c in r:
                if c not in cols: cols.append(c)
            if key:
                k = (v, r[key])
                if k in seen: dup += 1
                seen.add(k)
            rows.append(r)
        per[v] = len(rs)
    with open(out / "03_MASTER_DATA" / f"{name}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); [w.writerow(r) for r in rows]
    res["tables"][name] = dict(rows=len(rows), duplicate_keys=dup, per_video=per)
    print(name, len(rows), "dup", dup)
json.dump(res, open(out / "03_MASTER_DATA/_AGGREGATION_SUMMARY.json", "w"), indent=1)
