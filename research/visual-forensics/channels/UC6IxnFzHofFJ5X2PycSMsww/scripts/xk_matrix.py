"""Campaign matrix: per video, per requirement status + evidence locator. Re-run after each checkpoint.
Statuses: VERIFIED_DONE, PARTIAL, PENDING, BLOCKED, NOT_APPLICABLE. python3 -I xk_matrix.py <ws>"""
import csv, json, sys, pathlib

W = pathlib.Path(sys.argv[1]); C = W / "census"
census = list(csv.DictReader(open(C / "census.csv")))
sel = json.load(open(W / "selection" / "selection_v1.json"))
role = {**{i: "LONG_DEV" for i in sel["long_dev"]}, **{i: "LONG_HELDOUT" for i in sel["long_heldout"]},
        **{i: "SHORT_DEV" for i in sel["short_dev"]}, **{i: "SHORT_HELDOUT" for i in sel["short_heldout"]}}
CORPUS = "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output"
corpus_ids = {r["candidate_youtube_video_id"]: r for r in json.load(open(
    "/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/manifests/what-if-forensic-source-v1.json"))["sources"]
    if r.get("candidate_youtube_video_id")}
COLS = ["source_identity", "frame_timestamp_measurement", "candidate_state_segmentation", "native_visual_art_review",
        "motion_event_inspection", "transcript_asr", "listening_av_alignment", "production_specs", "independent_review",
        "reconstruction_test", "kit_gates", "publication_evidence"]

def st(vid, key):
    v = W / "videos" / vid
    if key == "source_identity":
        if (v / "evidence/source_sha256.txt").exists(): return "VERIFIED_DONE", f"videos/{vid}/evidence/source_sha256.txt"
        return ("PENDING", "census local_sha256") if role.get(vid) else ("PENDING", "census local_sha256 (hashed, not selected)")
    if key == "frame_timestamp_measurement":
        if (v / "tables/FULL_FRAME_MEASUREMENTS.csv").exists(): return "VERIFIED_DONE", f"videos/{vid}/tables/FULL_FRAME_MEASUREMENTS.csv"
    if key == "candidate_state_segmentation":
        if (v / "tables/state_ledger.csv").exists():
            q = json.load(open(v / "quality_gate.json")) if (v / "quality_gate.json").exists() else {}
            ok = q.get("gates", {}).get("meaningful_state_timing") == "PASS"
            return ("VERIFIED_DONE" if ok else "PARTIAL"), f"videos/{vid}/tables/state_ledger.csv (all segments classified; unresolved listed in quality_gate.json)"
        if (v / "tables/boundary_candidates.csv").exists(): return "PARTIAL", f"videos/{vid}/tables/boundary_candidates.csv (candidates only)"
    if key == "native_visual_art_review" and (v / "tables/palette_measured.json").exists() and (v / "visual_ct_scan_report.md").exists(): return "PARTIAL", f"videos/{vid}/visual_ct_scan_report.md §4 + tables/palette_measured.json (tile-scale review)"
    if key == "motion_event_inspection" and (v / "visual_event_ledger.csv").exists():
        c = json.load(open(v / "coverage.json")); full = c["activities_fully_viewed"] == c["activities"]
        return ("VERIFIED_DONE" if full else "PARTIAL"), f"videos/{vid}/visual_event_ledger.csv ({c['activities_fully_viewed']}/{c['activities']} events all frames viewed)"
    if key == "transcript_asr":
        if (v / "asr/asr_small_en.json").exists(): return "PARTIAL", f"videos/{vid}/asr/asr_small_en.json (PROVISIONAL_ASR_NOT_LISTENING) + catalog plaintext captions"
        r = next(r for r in census if r["video_id"] == vid)
        if int(r["catalog_transcript_rows"] or 0): return "PARTIAL", "catalog transcripts (untimed plaintext captions, DS-000017)"
    if key == "listening_av_alignment":
        return "BLOCKED", "no audio perception capability in this session (see campaign/AUDIO_LISTENING_CAPABILITY.json); ASR is not listening"
    if key == "production_specs" and (v / "reconstruction_blueprint.md").exists(): return "PARTIAL", f"videos/{vid}/reconstruction_blueprint.md"
    if key == "independent_review":
        vals = list((v / "review").glob("*/validation.json"))
        if vals:
            d = json.load(open(vals[0]))
            if not d["errors"]: return "PARTIAL", f"videos/{vid}/review/{d['reviewer']}/validation.json (same-family model reviewer, transcript-audited; primary spot-check review/primary_spotcheck.json)"
        if (v / "review/primary_annotations_v1.csv").exists(): return "PENDING", "primary analyst review only; no independent reviewer yet"
    if key == "kit_gates" and (v / "quality_gate.json").exists():
        g = json.load(open(v / "quality_gate.json")); return g.get("overall", "PARTIAL"), f"videos/{vid}/quality_gate.json"
    if key == "publication_evidence" and (v / "PUBLISHED").exists(): return "PARTIAL", (v / "PUBLISHED").read_text().strip()
    if vid in corpus_ids and key in ("candidate_state_segmentation", "native_visual_art_review", "motion_event_inspection", "production_specs"):
        return "PARTIAL", f"HISTORICAL_UNVERIFIED corpus {corpus_ids[vid]['source_video_id']} {CORPUS}/{corpus_ids[vid]['forensic_slug']} (different encode sha {corpus_ids[vid]['sha256'][:12]})"
    return "PENDING", ""

rows = []
for r in census:
    vid = r["video_id"]; row = dict(video_id=vid, format=r["format_class"], publish=r["publish_datetime"][:10], role=role.get(vid, "NOT_SELECTED"),
                                    local_source="YES" if r["local_files"] != "0" else "NO")
    for k in COLS:
        s, e = st(vid, k)
        if row["role"] == "NOT_SELECTED" and s == "PENDING": s = "NOT_APPLICABLE"; e = "not in selection_v1 (population member, not analysed)"
        if row["local_source"] == "NO" and k != "listening_av_alignment" and s in ("PENDING", "NOT_APPLICABLE"): s = "BLOCKED"; e = "no local source"
        row[k] = s; row[k + "_evidence"] = e
    rows.append(row)
(W / "campaign").mkdir(exist_ok=True)
with open(W / "campaign/campaign_matrix.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
sel_rows = [r for r in rows if r["role"] != "NOT_SELECTED"]
print({k: dict(Counter(r[k] for r in sel_rows)) for k in COLS})
