"""Phase B (part 3): map local media -> YouTube IDs using exact title + duration + orientation evidence (never filename resemblance alone),
write SOURCE_FILES.csv, SELECTED_18.csv and initialise PROGRESS.json (does not overwrite existing per-video progress).
Usage: python3 -B reconcile_sources.py <OUT_DIR>
"""
import csv, json, re, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from compile_metadata import SELECTED, norm  # noqa: E402

DUR_TOL = 1.5


def main(out):
    out = Path(out)
    cat = {r["video_id"]: r for r in csv.DictReader(open(out / "01_CHANNEL_METADATA/all-videos-metadata.csv"))}
    by_title = {}
    for r in cat.values(): by_title.setdefault(norm(r["title"]), []).append(r)
    src = list(csv.DictReader(open(out / "00_MANIFEST/SOURCE_FILES_raw.csv")))
    sel_ids = {s[0]: s for s in SELECTED}
    rows, taken = [], {}
    for r in src:
        cands = by_title.get(norm(r["title_from_filename"]), [])
        dur = float(r["duration_sec"]); vertical = r["orientation"] == "VERTICAL_9x16"
        ok = [c for c in cands if abs(float(c["duration_sec"]) - dur) <= DUR_TOL and ((c["format_class"] == "SHORT") == vertical)]
        decode_ok = r["decode_rc"] == "0" and r["decode_error_lines"] == "0" and abs(float(r["decoded_duration_sec"] or 0) - dur) < 0.5
        if not decode_ok: status, vid, conf, why = "CORRUPT", "", "NONE", f"decode_rc={r['decode_rc']} errs={r['decode_error_lines']}"
        elif len(ok) == 1:
            c = ok[0]; vid = c["video_id"]
            status, conf = "SOURCE_VERIFIED", "HIGH"
            why = (f"exact normalized title match to public catalog; duration local {dur:.3f}s vs public {c['duration_sec']}s (|d|<={DUR_TOL}); "
                   f"orientation {r['orientation']} consistent with {c['format_class']}; full decode clean; content corroboration pending transcript")
        elif len(cands) >= 1:
            vid, status, conf, why = "", "DURATION_MISMATCH", "LOW", f"title matches {[c['video_id'] for c in cands]} but duration/orientation disagree (local {dur:.3f}s vs {[c['duration_sec'] for c in cands]})"
        else:
            vid, status, conf, why = "", "IDENTITY_UNCERTAIN", "NONE", "no exact normalized title match in public catalog"
        rows.append({**r, "candidate_youtube_id": ";".join(c["video_id"] for c in cands), "verified_youtube_id": vid, "identity_status": status,
                     "identity_confidence": conf, "identity_evidence": why, "in_selected_18": vid in sel_ids})
    # duplicate (same SHA) handling: first file canonical
    seen = {}
    for r in rows:
        if r["verified_youtube_id"] and r["sha256"] in seen:
            r["canonical_for_analysis"] = False; r["identity_evidence"] += f"; DUPLICATE_SHA of {seen[r['sha256']]}"
        else:
            r["canonical_for_analysis"] = True; seen.setdefault(r["sha256"], r["filename"])
    cols = list(rows[0].keys())
    with open(out / "00_MANIFEST/SOURCE_FILES.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    canon = {r["verified_youtube_id"]: r for r in rows if r["verified_youtube_id"] and r["canonical_for_analysis"]}
    sel_rows = []
    for vid, ut, uc in SELECTED:
        m, f = cat.get(vid), canon.get(vid)
        status = f["identity_status"] if f else "MISSING_LOCAL"
        sel_rows.append(dict(order=len(sel_rows) + 1, video_id=vid, user_supplied_title=ut, user_class=uc, public_title=m["title"], format_class=m["format_class"], published_at=m["published_at"],
                             duration_sec_public=m["duration_sec"], views=m["views"], likes=m["likes"], local_status=status, local_path=f["path"] if f else "", sha256=f["sha256"] if f else "",
                             local_duration_sec=f["duration_sec"] if f else "", width=f["width"] if f else "", height=f["height"] if f else "", fps=f["fps"] if f else "",
                             video_codec=f["video_codec"] if f else "", audio_codec=f["audio_codec"] if f else "", audio_tracks=f["audio_tracks"] if f else "",
                             identity_confidence=f["identity_confidence"] if f else "", identity_evidence=f["identity_evidence"] if f else "No local file with matching exact title found in ~/Downloads loose files or CasuallyFinance.zip"))
    with open(out / "00_MANIFEST/SELECTED_18.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sel_rows[0].keys())); w.writeheader(); w.writerows(sel_rows)
    # progress (preserve existing per-video state)
    pp = out / "00_MANIFEST/PROGRESS.json"
    prog = json.loads(pp.read_text()) if pp.exists() else {"videos": {}}
    for s in sel_rows:
        v = prog["videos"].setdefault(s["video_id"], {})
        if v.get("status") in (None, "NOT_STARTED", "SOURCE_VERIFIED", "BLOCKED"):
            v["status"] = "SOURCE_VERIFIED" if s["local_status"] == "SOURCE_VERIFIED" else "BLOCKED"
            v["blocked_reason"] = "" if s["local_status"] == "SOURCE_VERIFIED" else s["local_status"]
        v.update(format_class=s["format_class"], sha256=s["sha256"], source_path=s["local_path"])
    prog["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    pp.write_text(json.dumps(prog, indent=1))
    from collections import Counter
    print(Counter(s["local_status"] for s in sel_rows), "| non-selected verified:", [r["filename"][:40] for r in rows if r["verified_youtube_id"] and not r["in_selected_18"]])
    for s in sel_rows: print(s["order"], s["video_id"], s["local_status"], s["local_duration_sec"], s["duration_sec_public"])


if __name__ == "__main__":
    main(sys.argv[1])
