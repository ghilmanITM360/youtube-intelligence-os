#!/usr/bin/env python3
"""Phase 1 reconciliation: enrich the media inventory, grade prior research coverage, list gaps.

Usage: python3 -I build_phase1_discovery.py <source_dir> <repo_root> <out_dir>

Read-only on <source_dir> and on git (uses `git show` / `git ls-tree` against refs).
Inputs  : <out_dir>/SOURCE_MEDIA_INVENTORY.csv (from build_source_inventory.py)
Outputs : SOURCE_MEDIA_INVENTORY.csv (enriched in place), PRIOR_RESEARCH_COVERAGE.csv,
          RESEARCH_GAP_REGISTER.csv, evidence/phase1_facts.json
"""
import csv
import io
import json
import os
import subprocess
import sys
import zipfile
import zlib
from collections import Counter, defaultdict

INV_REF = "origin/research/casually-finance-video-inventory"
INV_DIR = "research/casually-finance-video-inventory"
PRIOR_REF = "codex/casually-finance-forensic-research"
PRIOR = "data/extracted/forensic-analysis/casually-finance/2026-10-12"
PER_VIDEO_TABLES = ["SHOTS", "STATES", "MOTIONS", "ASSETS", "AUDIO_EVENTS",
                    "AUDIO_VISUAL_SYNC", "SEMANTIC_BEATS", "TRANSCRIPT"]
ZIPS = ["CasuallyFinance.zip", "CasuallyFinance (1).zip"]


def git(repo, *args):
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)
    return r.stdout


def gcsv(repo, ref, path):
    return list(csv.DictReader(io.StringIO(git(repo, "show", "%s:%s" % (ref, path)))))


def crc32_file(p):
    c = 0
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            c = zlib.crc32(chunk, c)
    return c & 0xFFFFFFFF


def ahash_signature(path, duration):
    """5 normalized-position frames -> 256-bit average hashes (content fingerprint)."""
    sig = []
    for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", "%.3f" % (duration * frac), "-i", path,
                            "-frames:v", "1", "-vf", "scale=16:16,format=gray", "-f", "rawvideo", "-"],
                           capture_output=True)
        b = r.stdout
        if len(b) != 256:
            sig.append(None)
            continue
        m = sum(b) / 256.0
        sig.append([1 if x > m else 0 for x in b])
    return sig


def hamming(a, b):
    d = [sum(x != y for x, y in zip(p, q)) for p, q in zip(a, b) if p and q]
    return round(sum(d) / len(d), 1) if d else ""


def grade_prior(vid, row, qa, mat, nrows):
    """Return dict of dimension -> (status, note). Only demonstrated evidence earns more than PARTIAL."""
    NF = ("NOT_FOUND", "no record in any inspected ref")
    if not row:
        return {k: NF for k in DIMS}
    ind = mat.get("independent_visual_qa", "")
    ind_status = "PARTIAL" if ind in ("PARTIAL", "SAMPLED_VISUAL_QA_COMPLETE") else "UNVERIFIED"
    return {
        "Metadata": ("VERIFIED_COMPLETE", "Oct-19 inventory snapshot; core fields present; language unavailable"),
        "Transcript": ("PARTIAL", "word-level Whisper-base ASR; names/numbers uncertified; no YouTube captions"),
        "Scene_Segmentation": ("PARTIAL", "%s shots; every frame decoded for change detection; boundaries set by frame review; not re-reviewed over whole duration" % nrows["SHOTS"]),
        "Still_Frame_Evidence": ("PARTIAL", "one representative frame per stable state on labelled contact sheets; not exhaustive"),
        "Motion_Sequences": ("PARTIAL", "%s motion rows; flagged candidates reviewed (%s/%s); easing NOT_ASSESSED; non-flagged not certified" % (nrows["MOTIONS"], mat.get("motion_candidates_reviewed", "?"), mat.get("original_motion_candidates", "?"))),
        "Asset_Taxonomy": ("PARTIAL", "%s asset-appearance labels; analyst labels not verified unique artwork" % nrows["ASSETS"]),
        "Typography_Analysis": ("NOT_FOUND", "visible_text transcribed per state only; no typeface/weight/size/position/entrance analysis"),
        "Audio_Analysis": ("PARTIAL", "signal-processing + ASR timing (%s events); NOT auditory listening" % nrows["AUDIO_EVENTS"]),
        "Full_Visual_Timeline": ("PARTIAL", "state timeline + transition gaps cover duration (structural PASS); matrix: full_duration_continuous_visual_review=%s" % mat.get("full_duration_continuous_visual_review", "?")),
        "Narration_Visual_Sync": ("PARTIAL", "%s sync rows; ASR (+/-100ms) vs frame-exact visual times; not listened" % nrows["AUDIO_VISUAL_SYNC"]),
        "Independent_QA": (ind_status, "matrix independent_visual_qa=%s (sampled, not whole-duration)" % ind),
        "Complete_Audiovisual_Review": ("BLOCKED", "direct audio listening unavailable in prior environment; matrix full_av_signoff_eligibility=%s" % mat.get("full_av_signoff_eligibility", "?")),
    }


DIMS = ["Metadata", "Transcript", "Scene_Segmentation", "Still_Frame_Evidence", "Motion_Sequences",
        "Asset_Taxonomy", "Typography_Analysis", "Audio_Analysis", "Full_Visual_Timeline",
        "Narration_Visual_Sync", "Independent_QA", "Complete_Audiovisual_Review"]


def main(src, repo, out):
    inv_path = os.path.join(out, "SOURCE_MEDIA_INVENTORY.csv")
    rows = list(csv.DictReader(open(inv_path)))
    base_fields = list(rows[0].keys())
    for r in rows:
        r.setdefault("Record_Kind", "LOOSE_FILE")

    # ---- identity from the Oct-19 inventory branch (re-verified against my own SHA256)
    scan = [r for r in gcsv(repo, INV_REF, INV_DIR + "/LOCAL_MEDIA_SCAN.csv") if r["kind"] == "FOLDER"]
    scan_by_sha = {r["sha256"]: r for r in scan}
    meta = {r["Video ID"]: r for r in gcsv(repo, INV_REF, INV_DIR + "/CASUALLY_FINANCE_VIDEO_INVENTORY.csv")}
    sel18 = {r["video_id"]: r for r in gcsv(repo, PRIOR_REF, PRIOR + "/00_MANIFEST/SELECTED_18.csv")}
    prior_sha = {r["sha256"]: vid for vid, r in sel18.items() if r["sha256"]}
    inv_commit = git(repo, "rev-parse", INV_REF).strip()
    prior_commit = git(repo, "rev-parse", PRIOR_REF).strip()

    # ---- zip CRC cross-check (read-only)
    loose_crc = {}
    for r in rows:
        loose_crc[(crc32_file(os.path.join(src, r["Relative_Path"])), int(r["Size_Bytes"]))] = r["Source_ID"]
    zip_rows, zip_hits = [], defaultdict(list)
    parent = os.path.dirname(src.rstrip("/"))
    for zn in ZIPS:
        zp = os.path.join(parent, zn)
        if not os.path.exists(zp):
            continue
        zf = zipfile.ZipFile(zp)
        ents = [i for i in zf.infolist() if not i.filename.startswith("__MACOSX") and i.filename.lower().endswith(".mp4")]
        matched = 0
        for i in ents:
            sid = loose_crc.get((i.CRC, i.file_size))
            if sid:
                zip_hits[sid].append(zn)
                matched += 1
        import hashlib
        h = hashlib.sha256()
        with open(zp, "rb") as f:
            for ch in iter(lambda: f.read(1 << 20), b""):
                h.update(ch)
        zip_rows.append({"Source_ID": "CFARC-%02d" % (len(zip_rows) + 1), "Relative_Path": "../" + zn, "Filename": zn,
                         "Size_Bytes": os.path.getsize(zp), "SHA256": h.hexdigest(), "Container_Format": "zip",
                         "Has_Video": False, "Has_Audio": False, "Decode_Status": "N/A_ARCHIVE",
                         "Decode_Errors": "%d mp4 entries; %d CRC32+size matched to loose files; %d unmatched" % (len(ents), matched, len(ents) - matched),
                         "Record_Kind": "ADJACENT_ARCHIVE"})

    # ---- content fingerprints for duplicate / variant verification
    for r in rows:
        r["_sig"] = ahash_signature(os.path.join(src, r["Relative_Path"]), float(r["Duration_S"]))

    groups = defaultdict(list)
    for r in rows:
        s = scan_by_sha.get(r["SHA256"])
        vid = s["video_id"] if s else ""
        r["Video_ID"] = vid
        m = meta.get(vid, {})
        r["ID_Match_Method"] = (s["method"] if s else "UNMATCHED")
        prior_ok = r["SHA256"] in prior_sha
        r["ID_Confidence"] = "HIGH_SHA256_ALSO_VERIFIED_IN_PRIOR_BRANCH" if prior_ok else "STRONG_NORMALIZED_TITLE_PLUS_DURATION_NOT_CRYPTOGRAPHIC"
        r["Public_Title"] = m.get("Video Title", "")
        r["Video_Type"] = m.get("Video Type", "")
        r["Upload_Date"] = m.get("Upload Date", "")
        r["Public_Views_Snapshot"] = m.get("Views", "")
        r["Public_Duration_S"] = m.get("Duration (sec)", "")
        r["Associated_Transcript"] = "NONE_FOUND_IN_SOURCE_DIR" + ("; prior Whisper ASR in %s" % PRIOR_REF if vid in sel18 and sel18[vid].get("local_status") == "SOURCE_VERIFIED" else "")
        r["Associated_Metadata"] = "%s:%s (snapshot %s)" % (INV_REF, INV_DIR, (m.get("Metadata Retrieved At", "") or "")[:10])
        r["Archive_Copies"] = ";".join(zip_hits.get(r["Source_ID"], []))
        groups[vid].append(r)

    for vid, g in groups.items():
        def key(r):
            return (r["SHA256"] in prior_sha, int(r["Width"]) * int(r["Height"]), int(r["Video_Bitrate"] or 0), -len(r["Filename"]))
        g.sort(key=key, reverse=True)
        canon = g[0]
        for i, r in enumerate(g):
            r["Duplicate_Group"] = vid if len(g) > 1 else ""
            if r is canon:
                r["Variant_Role"] = "CANONICAL" if len(g) > 1 else "SOLE_COPY"
                r["Canonical_For_Analysis"] = True
                r["Content_Hamming_To_Canonical"] = 0.0 if len(g) > 1 else ""
            else:
                same_sha = r["SHA256"] == canon["SHA256"]
                ham = hamming(r["_sig"], canon["_sig"])
                r["Content_Hamming_To_Canonical"] = ham
                r["Canonical_For_Analysis"] = False
                if same_sha:
                    r["Variant_Role"] = "BYTE_IDENTICAL_DUPLICATE"
                elif r["Width"] != canon["Width"]:
                    r["Variant_Role"] = "ALTERNATE_LOWER_RESOLUTION_REENCODE"
                else:
                    r["Variant_Role"] = "ALTERNATE_ENCODE_SAME_RESOLUTION_BYTES_DIFFER"
    # cross-ID accidental duplicates check
    cross = []
    canon_rows = [g[0] for g in groups.values()]
    for i, a in enumerate(canon_rows):
        for b in canon_rows[i + 1:]:
            h = hamming(a["_sig"], b["_sig"])
            if h != "" and h < 12:
                cross.append((a["Video_ID"], b["Video_ID"], h))

    # ---- prior coverage rows
    mats = {r["video_id"]: r for r in gcsv(repo, PRIOR_REF, PRIOR + "/07_VALIDATION/VIDEO_QA_COMPLETION_MATRIX.csv")}
    tree = git(repo, "ls-tree", "-r", "--name-only", PRIOR_REF, "--", PRIOR + "/02_VIDEO_FORENSICS").splitlines()
    sheets = Counter()
    for p in tree:
        parts = p.split("/")
        if "/sheets/" in p or "/evidence/" in p:
            if p.lower().endswith((".jpg", ".png")):
                sheets[parts[7]] += 1
    ts = git(repo, "log", "-1", "--format=%cI", PRIOR_REF, "--", PRIOR + "/02_VIDEO_FORENSICS").strip()
    cov_fields = ["Video_ID", "Public_Title", "Video_Type", "Local_File_Count", "Canonical_Local_File", "Canonical_SHA256",
                  "Canonical_Resolution", "Canonical_Duration_S", "Resolution_Limited_Source"] + \
                 DIMS + ["Prior_Rows_SHOTS", "Prior_Rows_STATES", "Prior_Rows_MOTIONS", "Prior_Rows_ASSETS",
                         "Prior_Rows_AUDIO_EVENTS", "Prior_Rows_SYNC", "Prior_Rows_TRANSCRIPT_WORDS", "Prior_Evidence_Images",
                         "Prior_SHA256", "Prior_SHA256_Matches_Current_Canonical", "Prior_Git_Ref", "Prior_Git_Commit",
                         "Prior_Evidence_Root", "Prior_Last_Commit_Timestamp", "Dimension_Notes", "Other_Related_Research",
                         "Overall_Prior_Coverage"]
    cov = []
    all_ids = list(groups.keys())
    for vid in all_ids + [v for v in sel18 if v not in groups]:
        g = groups.get(vid)
        m = meta.get(vid, {})
        c = g[0] if g else None
        in_prior = vid in sel18 and sel18[vid].get("local_status") == "SOURCE_VERIFIED"
        nrows = {}
        if in_prior:
            for t in PER_VIDEO_TABLES:
                nrows[t] = len(gcsv(repo, PRIOR_REF, "%s/02_VIDEO_FORENSICS/%s/%s.csv" % (PRIOR, vid, t)))
        grade = grade_prior(vid, in_prior, None, mats.get(vid, {}), nrows) if in_prior else None
        if not g:
            grade = {k: ("BLOCKED", "source file not present locally (prior status %s)" % sel18[vid].get("local_status")) for k in DIMS}
            grade["Metadata"] = ("VERIFIED_COMPLETE", "Oct-19 inventory snapshot")
        elif not in_prior:
            grade = {k: ("NOT_FOUND", "no per-video record in any inspected ref") for k in DIMS}
            grade["Metadata"] = ("VERIFIED_COMPLETE", "Oct-19 inventory snapshot; core fields present; language unavailable")
            grade["Complete_Audiovisual_Review"] = ("NOT_FOUND", "no per-video record; audio listening unavailable in this environment")
        row = {"Video_ID": vid, "Public_Title": m.get("Video Title", sel18.get(vid, {}).get("public_title", "")),
               "Video_Type": m.get("Video Type", sel18.get(vid, {}).get("format_class", "")),
               "Local_File_Count": len(g) if g else 0,
               "Canonical_Local_File": c["Relative_Path"] if c else "", "Canonical_SHA256": c["SHA256"] if c else "",
               "Canonical_Resolution": "%sx%s" % (c["Width"], c["Height"]) if c else "",
               "Canonical_Duration_S": c["Duration_S"] if c else "",
               "Resolution_Limited_Source": (int(c["Width"]) <= 360) if c else ""}
        for d in DIMS:
            row[d] = grade[d][0]
        row["Dimension_Notes"] = " | ".join("%s: %s" % (d, grade[d][1]) for d in DIMS if grade[d][0] != "NOT_FOUND")
        row["Prior_Rows_SHOTS"] = nrows.get("SHOTS", "")
        row["Prior_Rows_STATES"] = nrows.get("STATES", "")
        row["Prior_Rows_MOTIONS"] = nrows.get("MOTIONS", "")
        row["Prior_Rows_ASSETS"] = nrows.get("ASSETS", "")
        row["Prior_Rows_AUDIO_EVENTS"] = nrows.get("AUDIO_EVENTS", "")
        row["Prior_Rows_SYNC"] = nrows.get("AUDIO_VISUAL_SYNC", "")
        row["Prior_Rows_TRANSCRIPT_WORDS"] = nrows.get("TRANSCRIPT", "")
        row["Prior_Evidence_Images"] = sheets.get(vid, 0) if in_prior else ""
        row["Prior_SHA256"] = sel18[vid]["sha256"] if in_prior else ""
        row["Prior_SHA256_Matches_Current_Canonical"] = (sel18[vid]["sha256"] == c["SHA256"]) if (in_prior and c) else ""
        row["Prior_Git_Ref"] = PRIOR_REF if vid in sel18 else ""
        row["Prior_Git_Commit"] = prior_commit if vid in sel18 else ""
        row["Prior_Evidence_Root"] = "%s/02_VIDEO_FORENSICS/%s" % (PRIOR, vid) if vid in sel18 else ""
        row["Prior_Last_Commit_Timestamp"] = ts if vid in sel18 else ""
        related = []
        if vid in ("roe3SgezmmU", "5umJ63d3rzQ", "rSa2aziEsAI"):
            related.append("origin/research/casually-finance-success-playbook PILOT_REMOTION reference sequence")
        row["Other_Related_Research"] = "; ".join(related)
        row["Overall_Prior_Coverage"] = ("PARTIAL_STRUCTURAL_ONLY" if in_prior else ("BLOCKED_SOURCE_MISSING" if not g else "NONE"))
        cov.append(row)
        if g:
            for r in g:
                r["Prior_Research_Status"] = row["Overall_Prior_Coverage"]
    for r in rows:
        r.pop("_sig", None)

    new_cols = ["Record_Kind", "Video_ID", "ID_Match_Method", "ID_Confidence", "Public_Title", "Video_Type", "Upload_Date",
                "Public_Views_Snapshot", "Public_Duration_S", "Duplicate_Group", "Variant_Role", "Canonical_For_Analysis",
                "Content_Hamming_To_Canonical", "Associated_Transcript", "Associated_Metadata", "Archive_Copies",
                "Prior_Research_Status"]
    fields = [f for f in base_fields if f not in new_cols] + new_cols
    with open(inv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
        w.writerows(zip_rows)
    with open(os.path.join(out, "PRIOR_RESEARCH_COVERAGE.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cov_fields)
        w.writeheader()
        w.writerows(cov)

    # ---- gap register
    cnt = Counter(c["Overall_Prior_Coverage"] for c in cov)
    none_ids = [c["Video_ID"] for c in cov if c["Overall_Prior_Coverage"] == "NONE"]
    prior_ids = [c["Video_ID"] for c in cov if c["Overall_Prior_Coverage"] == "PARTIAL_STRUCTURAL_ONLY"]
    miss_ids = [c["Video_ID"] for c in cov if c["Overall_Prior_Coverage"] == "BLOCKED_SOURCE_MISSING"]
    low = [c["Video_ID"] for c in cov if c["Resolution_Limited_Source"] is True]
    longs = [c["Video_ID"] for c in cov if c["Video_Type"] == "VIDEO" and c["Local_File_Count"]]
    gaps = [
        ("GAP-001", "NO_PRIOR_FORENSICS", "HIGH", "; ".join(none_ids), len(none_ids), "No per-video scene/state/motion/asset/audio/sync record exists in any inspected ref", "Phase 2-7 full per-video forensics", "OPEN"),
        ("GAP-002", "FULL_CHRONOLOGICAL_REVIEW", "HIGH", "; ".join(prior_ids), len(prior_ids), "Prior matrix: full_duration_continuous_visual_review=NOT_STARTED; one representative frame per state, not continuous review", "Phase 2 Pass C/E", "OPEN"),
        ("GAP-003", "EASING_AND_KEYFRAME_MEASUREMENT", "HIGH", "ALL", len(cov) - len(miss_ids), "Prior easing = NOT_ASSESSED (needs tracked element positions); only changed-pixel episodes measured", "Phase 4 tracked-geometry measurement", "OPEN"),
        ("GAP-004", "TYPOGRAPHY_ANALYSIS", "MEDIUM", "ALL", len(cov) - len(miss_ids), "Only visible_text transcribed per state; no typeface/weight/size/position/entrance-animation measurements", "Phase 5", "OPEN"),
        ("GAP-005", "ASSET_UNIQUENESS_AND_REUSE", "HIGH", "ALL", len(cov) - len(miss_ids), "Asset rows are per-appearance analyst labels (2,196 master rows are not unique illustrations); no pose/variant/crop de-duplication", "Phase 5", "OPEN"),
        ("GAP-006", "DIRECT_AUDIO_LISTENING", "BLOCKED", "ALL", len(cov) - len(miss_ids), "No auditory capability in this environment (images/text only); only signal measurement + ASR available. Cannot be closed by this agent", "Owner/human listening review; Phase 7 limited to measured signal", "BLOCKED"),
        ("GAP-007", "ASR_NAMES_NUMBERS_UNCERTIFIED", "MEDIUM", "; ".join(prior_ids), len(prior_ids), "Whisper-base transcripts; proper nouns and numbers uncertified; on-screen text preferred", "Phase 2/6 per-video verification vs on-screen text", "OPEN"),
        ("GAP-008", "NO_TRANSCRIPT_FOR_NEW_SHORTS", "MEDIUM", "; ".join(none_ids), len(none_ids), "No YouTube captions downloaded and no ASR for these videos", "Run local Whisper (cached models) per video", "OPEN"),
        ("GAP-009", "RESOLUTION_LIMITED_SOURCES", "MEDIUM", "; ".join(low), len(low), "Only a 360x640 copy exists locally; fine linework, text weight and small-motion measurement limited", "Flag confidence; do not redownload without owner direction", "OPEN"),
        ("GAP-010", "MISSING_LOCAL_SOURCES_PRIOR_SELECTED", "BLOCKED", "; ".join(miss_ids), len(miss_ids), "Prior-selected Short has no local media (turJ6VMfUjI). Qof71Ef-3EU, also MISSING_LOCAL in the prior bundle, is now present locally only as a 360x640 SnapYT copy and is counted under GAP-001/GAP-009", "Owner to supply media; do not redownload", "BLOCKED"),
        ("GAP-011", "UNDOWNLOADED_CHANNEL_VIDEOS", "INFO", "162 of 210 public videos", 162, "Oct-19 inventory: 24 regular + 138 Shorts not downloaded; population claims must state eligible denominator 48", "Owner decision; out of scope", "OPEN"),
        ("GAP-012", "MOTION_METHOD_CLASSIFICATION", "HIGH", "ALL", len(cov) - len(miss_ids), "No duration-weighted classification of conventional keyframe vs complex/generated motion exists; user 70-80/10-20 hypothesis untested", "Phase 4", "OPEN"),
        ("GAP-013", "NON_FLAGGED_MOTION_UNCERTIFIED", "MEDIUM", "; ".join(prior_ids), len(prior_ids), "Only pixel-flagged motion candidates were reviewed; unflagged micro-changes (e.g. 49 un-tabulated episodes in 6S3PzAUFnXQ) not certified", "Phase 3", "OPEN"),
        ("GAP-014", "PRODUCTION_BLUEPRINT_RECIPES", "HIGH", "ALL", len(cov) - len(miss_ids), "Existing blueprint is channel-level; per-recipe keyframe/easing/timing specs with reference timestamps absent; Remotion pilot has documented acting/illustration gaps", "Phase 9", "OPEN"),
    ]
    with open(os.path.join(out, "RESEARCH_GAP_REGISTER.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Gap_ID", "Gap_Class", "Severity", "Affected_Video_IDs", "Affected_Count", "Description", "Planned_Resolution", "Status"])
        w.writerows(gaps)
    facts = {"prior_commit": prior_commit, "inventory_commit": inv_commit, "coverage_counts": dict(cnt),
             "cross_id_near_duplicates": cross, "unique_ids": len(groups), "files": len(rows),
             "zip_rows": [{k: z[k] for k in ("Filename", "SHA256", "Size_Bytes", "Decode_Errors")} for z in zip_rows],
             "variant_roles": dict(Counter(r["Variant_Role"] for r in rows)),
             "ids_none": none_ids, "ids_prior": prior_ids, "ids_missing": miss_ids, "ids_low_res": low, "ids_long": longs}
    json.dump(facts, open(os.path.join(out, "evidence", "phase1_facts.json"), "w"), indent=1)
    print(json.dumps({k: facts[k] for k in ("coverage_counts", "variant_roles", "cross_id_near_duplicates", "zip_rows")}, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:4])
