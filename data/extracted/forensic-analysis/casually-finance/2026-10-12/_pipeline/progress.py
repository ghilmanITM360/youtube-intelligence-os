"""Atomic PROGRESS.json updater. Usage: python3 -B progress.py <OUT_DIR> <VIDEO_ID> <STATUS> [note]
Statuses: NOT_STARTED SOURCE_VERIFIED IN_PROGRESS QA_PENDING COMPLETE BLOCKED. Also recomputes next_video_id (first non-COMPLETE, non-BLOCKED in processing order).
"""
import csv, json, os, sys, time
from pathlib import Path

ORDER = ["roe3SgezmmU", "Uumnx2Fo6cE", "xtqbRt94TTw", "o3FQcd91MIs", "dlBhLhn8lL0", "kwMHrTFCWUE", "DgbHW0IqHrI", "5umJ63d3rzQ", "0ll9rEtoRrs", "-X6YzlY_8tM",
         "2EZzwupIa80", "YGC3ao005as", "PxgCsLSf-w4", "6S3PzAUFnXQ", "rSa2aziEsAI", "JsK53moCyZA", "turJ6VMfUjI", "Qof71Ef-3EU"]


def main(out, vid, status, note=""):
    out = Path(out); p = out / "00_MANIFEST/PROGRESS.json"
    prog = json.loads(p.read_text()); v = prog["videos"].setdefault(vid, {})
    v["status"] = status; v["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if note: v["note"] = note
    qp = out / "02_VIDEO_FORENSICS" / vid / "QA.json"
    if qp.exists():
        q = json.load(open(qp)); v["qa_status"] = q["status"]; v["counts"] = q["counts"]; v["stats"] = q["stats"]
    done = [k for k in ORDER if prog["videos"].get(k, {}).get("status") == "COMPLETE"]
    pend = [k for k in ORDER if prog["videos"].get(k, {}).get("status") not in ("COMPLETE", "BLOCKED")]
    prog["completed_count"] = len(done); prog["completed_videos"] = done; prog["next_video_id"] = pend[0] if pend else None
    prog["blocked"] = {k: prog["videos"][k].get("blocked_reason", "") for k in ORDER if prog["videos"].get(k, {}).get("status") == "BLOCKED"}
    prog["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tmp = p.with_suffix(".tmp"); tmp.write_text(json.dumps(prog, indent=1)); os.replace(tmp, p)
    print(vid, status, "| completed:", len(done), "| next:", prog["next_video_id"])


if __name__ == "__main__":
    main(*sys.argv[1:5])
