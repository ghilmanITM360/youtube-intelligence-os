#!/usr/bin/env python3
"""Read-only extraction of DS-000011/018/031 knowledge + Senior Health channel/video
data + own-channel data + existing knowledge-video mappings into one master_data.json.

Never writes to any path under data/ or docs/ — output goes to exports/ only.
Source files read are listed in each _extract_* function's docstring.
"""
import json
import re
import subprocess
import sqlite3
import zipfile
from pathlib import Path

import openpyxl

REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1] / "master_data.json"
ARCHIVE_DIR = Path(__file__).resolve().parents[1] / "supplemental-data-archive"


def parse_md_table(text, start_marker=None, end_marker=None):
    """Generic pipe-table parser. Returns list of dicts keyed by header row."""
    if start_marker:
        idx = text.find(start_marker)
        text = text[idx:] if idx >= 0 else text
    if end_marker:
        idx = text.find(end_marker, 1)
        text = text[:idx] if idx > 0 else text
    lines = [l for l in text.splitlines() if l.strip().startswith("|")]
    rows = []
    header = None
    for l in lines:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue  # separator row
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def _pdf_to_text(path):
    r = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def _docx_to_text(path):
    import docx as _docx
    d = _docx.Document(str(path))
    return "\n".join(p.text for p in d.paragraphs)


def _extract_ds000011_fulltext():
    """Full original text of every DS-000011 raw source file, extracted read-only via
    pdftotext (poppler) / python-docx / direct read. Never writes back into data/."""
    import hashlib
    src_dir = REPO / "data/raw/global-youtube-knowledge/DS-000011"
    out = []
    seen_hashes = {}
    for fpath in sorted(src_dir.iterdir()):
        if not fpath.is_file():
            continue
        if fpath.suffix.lower() == ".pdf":
            text = _pdf_to_text(fpath)
        elif fpath.suffix.lower() == ".docx":
            text = _docx_to_text(fpath)
        elif fpath.suffix.lower() == ".md":
            text = fpath.read_text(encoding="utf-8")
        else:
            text = None
        raw_bytes = fpath.read_bytes()
        sha = hashlib.sha256(raw_bytes).hexdigest()
        dup_of = seen_hashes.get(sha)
        if dup_of is None:
            seen_hashes[sha] = fpath.name
        out.append({
            "filename": fpath.name,
            "sha256": sha,
            "byte_size": len(raw_bytes),
            "duplicate_of": dup_of,
            "full_text": text,
            "full_text_char_count": len(text) if text else 0,
            "extraction_status": "OK" if text else "UNREADABLE_FORMAT",
        })
    return out


def _extract_ds000011():
    """Sources: data/manifests/DS-000011.md, data/catalog/youtube_inventory.db
    (document_records where dataset_id='DS-000011'),
    data/intelligence/system/youtube-strategy-training-knowledge-2026-09-24.json
    (rows where SOURCE_ID='DS-000011'), and full original text of all 17 raw files
    (data/raw/global-youtube-knowledge/DS-000011/*)."""
    manifest = (REPO / "data/manifests/DS-000011.md").read_text()

    con = sqlite3.connect(REPO / "data/catalog/youtube_inventory.db")
    con.row_factory = sqlite3.Row
    docs = [dict(r) for r in con.execute(
        "SELECT * FROM document_records WHERE dataset_id='DS-000011' ORDER BY document_id"
    )]
    con.close()

    training = json.loads(
        (REPO / "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-24.json").read_text()
    )
    rules_key = "rules" if "rules" in training else next(k for k, v in training.items() if isinstance(v, list))
    rules = [r for r in training[rules_key] if r.get("SOURCE_ID") == "DS-000011"]

    fulltext_sources = _extract_ds000011_fulltext()
    unique_sources = [s for s in fulltext_sources if s["duplicate_of"] is None]

    return {
        "dataset_id": "DS-000011",
        "manifest_raw": manifest,
        "source_documents": docs,
        "source_document_count": len(docs),
        "knowledge_rules": rules,
        "knowledge_rule_count": len(rules),
        "fulltext_sources": fulltext_sources,
        "fulltext_source_count": len(fulltext_sources),
        "fulltext_unique_source_count": len(unique_sources),
    }


def _extract_ds000018_tab_fulltext():
    """Full original markdown text of all 63 DS-000018 research tabs, read in-memory
    straight from the zip (never extracted to disk under data/)."""
    zip_path = next((REPO / "data/raw/global-youtube-knowledge/DS-000018").glob("*.zip"))
    out = {}
    with zipfile.ZipFile(zip_path) as z:
        for m in z.namelist():
            if m.startswith("tabs/") and m.endswith(".md"):
                out[m] = z.read(m).decode("utf-8", errors="replace")
    return out


def _load_additional_ds000018_claims():
    """Loads the AI-extracted claims for the 56 previously-unprocessed DS-000018 tabs.
    These were extracted by grounded read-through of each tab's full original text
    (batches in scripts/ds18_additional_claims/*.json). Unlike the original 33 claims,
    these have NOT been through a human validation pass — marked accordingly. Absent
    the batch files, returns an empty list (does not fail the whole export)."""
    batch_dir = Path(__file__).resolve().parent / "ds18_additional_claims"
    if not batch_dir.exists():
        return []
    out = []
    for f in sorted(batch_dir.glob("*.json")):
        items = json.loads(f.read_text())
        for it in items:
            it["assertion_type"] = it.get("assertion_type", "SOURCE_CLAIM")
            it["extraction_method"] = "AI_GROUNDED_EXTRACTION_UNVALIDATED"
            it["prior_status_at_validation"] = "NOT_CURRENTLY_VERIFIABLE"
            it["validation_note"] = "Extracted by AI read-through of full source text; no independent human validation pass performed (unlike the original 33 claims)."
        out.extend(items)
    return out


def _extract_ds000018():
    """Sources: data/manifests/DS-000018.md,
    data/raw/global-youtube-knowledge/DS-000018/*.zip -> source-manifest.json (63 tabs) AND
    full text of all 63 tabs/*.md members (read in-memory, never extracted to disk),
    data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md (33 claims across 3 subsections),
    data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md (validation status per claim),
    scripts/ds18_additional_claims/*.json (grounded AI extraction of the remaining 56 tabs)."""
    manifest = (REPO / "data/manifests/DS-000018.md").read_text()

    zip_path = next((REPO / "data/raw/global-youtube-knowledge/DS-000018").glob("*.zip"))
    with zipfile.ZipFile(zip_path) as z:
        source_manifest = json.loads(z.read("source-manifest.json"))
    tabs = source_manifest["tabs"]
    tab_fulltext = _extract_ds000018_tab_fulltext()
    for t in tabs:
        t["full_text"] = tab_fulltext.get(t["snapshot_member"])

    claims_text = (REPO / "data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md").read_text()
    claim_rows = parse_md_table(claims_text, start_marker="## Extracted Algorithm Claims", end_marker="## Source Interpretations")
    interp_rows = parse_md_table(claims_text, start_marker="## Source Interpretations", end_marker="## Source Recommendations")
    rec_rows = parse_md_table(claims_text, start_marker="## Source Recommendations", end_marker="## Themes Covered")
    for r in claim_rows:
        r["assertion_type"] = "SOURCE_CLAIM"
    for r in interp_rows:
        r["assertion_type"] = "SOURCE_INTERPRETATION"
    for r in rec_rows:
        r["assertion_type"] = "SOURCE_RECOMMENDATION"
    all_claims = claim_rows + interp_rows + rec_rows

    validation_text = (REPO / "data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md").read_text()
    validation_rows = parse_md_table(validation_text, start_marker="| Claim ID | Prior status | Current official basis | Audit outcome |")
    val_by_id = {r["Claim ID"]: r for r in validation_rows}
    for c in all_claims:
        cid = c.get("Claim ID", "")
        c["extraction_method"] = "HUMAN_AUDITED_ORIGINAL_33"
        # BUG FIX (2026-09-27 correction): "validated_status" previously held reference
        # citation codes (e.g. "[R1], [R2]") copied from the wrong source column, not the
        # actual validation status. That column is now "evidence_citation_codes"; the real
        # status lives in "prior_status_at_validation" / "audit_outcome" below.
        c["evidence_citation_codes"] = val_by_id.get(cid, {}).get("Current official basis", "")
        if cid in val_by_id:
            c["audit_outcome"] = val_by_id[cid].get("Audit outcome", "")
            c["prior_status_at_validation"] = val_by_id[cid].get("Prior status", "")
        else:
            c["audit_outcome"] = ""
            c["prior_status_at_validation"] = "NOT_CURRENTLY_VERIFIABLE"

    additional_claims = _load_additional_ds000018_claims()

    return {
        "dataset_id": "DS-000018",
        "manifest_raw": manifest,
        "source_manifest": source_manifest,
        "tabs": tabs,
        "tab_count": len(tabs),
        "claims": all_claims,
        "claim_count": len(all_claims),
        "additional_claims": additional_claims,
        "additional_claim_count": len(additional_claims),
        "all_claims_combined_count": len(all_claims) + len(additional_claims),
        "validation_row_count": len(validation_rows),
    }


def _extract_ds000031():
    """Sources: data/manifests/DS-000031.md,
    data/intelligence/global/creator-strategy-knowledge-DS-000031.json (segments/concepts/formulas/
    numeric_heuristics/scorecard/examples/relationships),
    data/raw/global-youtube-knowledge/DS-000031/creator-strategy-audience-psychology-experimentation-corpus.txt
    (raw corpus — full original text sliced per segment's own line range, then re-attached to
    every concept/framework that cites that segment, per the correction request: replace the
    one-sentence "summary" field with the actual original source text alongside it)."""
    manifest = (REPO / "data/manifests/DS-000031.md").read_text()
    idx = json.loads((REPO / "data/intelligence/global/creator-strategy-knowledge-DS-000031.json").read_text())

    corpus_path = REPO / "data/raw/global-youtube-knowledge/DS-000031/creator-strategy-audience-psychology-experimentation-corpus.txt"
    corpus_lines = corpus_path.read_text(encoding="utf-8").splitlines(keepends=True)

    segments = idx["segments"]
    seg_text_by_id = {}
    for s in segments:
        a, b = s["lines"]
        text = "".join(corpus_lines[a - 1:b])
        s["full_text"] = text
        s["full_text_char_count"] = len(text)
        seg_text_by_id[s["id"]] = text

    concepts = idx["concepts"]
    for c in concepts:
        c["source_segment_full_text"] = {sid: seg_text_by_id.get(sid, "") for sid in c.get("segments", [])}

    return {
        "dataset_id": "DS-000031",
        "manifest_raw": manifest,
        "segments": segments,
        "concepts": concepts,
        "formulas": idx["formulas"],
        "numeric_heuristics": idx["numeric_heuristics"],
        "scorecard": idx["scorecard"],
        "examples": idx["examples"],
        "relationships": idx["relationships"],
        "counts": {
            "segments": len(idx["segments"]),
            "concepts": len(idx["concepts"]),
            "formulas": len(idx["formulas"]),
            "numeric_heuristics": len(idx["numeric_heuristics"]),
            "scorecard": 1,
            "examples": len(idx["examples"]),
            "relationships": len(idx["relationships"]),
        },
    }


SENIOR_HEALTH_CHANNEL_IDS = {
    "UCFpxvukIqCAUA7YizI-q9Dw": "Better Health While Aging",
    "UCQIzqH7QZ9viBYpOFqgSXMg": "Decode Your Heart - Dr. Rehan",  # OWN_CHANNEL
    "UCFuGMi0idGeyXl6wYK9hg7Q": "Doctor Thomas",
    "UCMJxAeBJ0d1JC937de1eZ0Q": "Dr. Okoro",
    "UC356D-NzdnznBOftTpYoBLw": "Dr. Ares Senior",
    "UCQcBYZxFW7YwNMU8-DsT3Uw": "Dr. Elias Senior Health",
    "UCAYG0fzUyxv6OevH88qA45w": "Senior Health Hub",
    "UCXZi5JVeuTluazF-fYqQgNA": "Dr. Aliza Wright | Advice",
}
OWN_CHANNEL_ID = "UCQIzqH7QZ9viBYpOFqgSXMg"

# Thumbnail-recovery sources: the DB's `videos.thumbnail_url` column is sparsely populated
# (64/460 for this cohort) even though the *raw* Apify acquisition output has thumbnailUrl
# for nearly every video. This maps each channel to its raw source file(s) so the export can
# backfill thumbnail URLs (and, where they exist, already-downloaded local image paths)
# without touching the database. Read-only against data/raw and data/manifests.
THUMBNAIL_SOURCES = {
    "UCFpxvukIqCAUA7YizI-q9Dw": [  # Better Health While Aging
        ("apify_list", "data/raw/competitors/DS-000033/dataset.json"),
        ("apify_list", "data/raw/competitors/DS-000033/apify/Ll3gKxE3dXEeG4SDd/dataset.json"),
        ("apify_list", "data/raw/competitors/DS-000033/apify/AuZ65QkXBmVIXcOn9/raw/dataset.json"),
    ],
    "UCQIzqH7QZ9viBYpOFqgSXMg": [("apify_list", "data/raw/competitors/DS-000032/dataset.json")],  # Dr. Rehan
    "UCFuGMi0idGeyXl6wYK9hg7Q": [("apify_list", "data/raw/competitors/DS-000029/dataset.json")],  # Doctor Thomas
    "UCMJxAeBJ0d1JC937de1eZ0Q": [("apify_list", "data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/raw/dataset.json")],  # Dr. Okoro
    "UC356D-NzdnznBOftTpYoBLw": [("apify_list", "data/raw/channel-data/DS-000027/apify/dqMkTSwYwRir4QfUM/youtube_actor_raw.json")],  # Dr. Ares
    "UCQcBYZxFW7YwNMU8-DsT3Uw": [  # Dr. Elias Senior Health
        ("elias_xlsx", "data/raw/competitors/DS-000019/DrElias_Master_Data.xlsx"),
        ("snapshot_manifest", "data/manifests/DS-000019-thumbnail-snapshot-2026-09-10.json"),
    ],
    "UCAYG0fzUyxv6OevH88qA45w": [("apify_list", "data/raw/competitors/DS-000030/dataset.json")],  # Senior Health Hub
    "UCXZi5JVeuTluazF-fYqQgNA": [("snapshot_manifest", "data/manifests/DS-000006-thumbnail-snapshot-2026-09-10.json")],  # Dr. Aliza
}


def _thumb_from_apify_list(path):
    d = json.loads((REPO / path).read_text())
    return {x["id"]: x["thumbnailUrl"] for x in d if x.get("id") and x.get("thumbnailUrl")}


def _thumb_from_elias_xlsx(path):
    wb = openpyxl.load_workbook(REPO / path, read_only=True)
    ws = wb["All Videos"]
    rows = list(ws.iter_rows(min_row=4, values_only=True))
    header = rows[0]
    idx_vid = header.index("Video ID")
    idx_thumb = header.index("Thumbnail URL")
    return {r[idx_vid]: r[idx_thumb] for r in rows[1:] if r and r[idx_vid]}


def _thumb_from_snapshot_manifest(path):
    d = json.loads((REPO / path).read_text())
    urls, local_paths = {}, {}
    for s in d.get("snapshots", []):
        url = s.get("final_url") or s.get("original_registered_url")
        if not url:
            continue
        m = re.search(r"/vi/([A-Za-z0-9_-]{11})/", url)
        if not m:
            continue
        vid = m.group(1)
        urls[vid] = url
        lp = s.get("local_path")
        if lp:
            idx = lp.find("data/raw/")
            if idx >= 0:
                local_paths[vid] = lp[idx:]
    return urls, local_paths


def _build_thumbnail_lookup():
    """Returns {channel_id: {video_id: {"thumbnail_url":..., "downloaded_local_path":... or None}}}."""
    lookup = {}
    for cid, sources in THUMBNAIL_SOURCES.items():
        urls, local_paths = {}, {}
        for kind, path in sources:
            if kind == "apify_list":
                urls.update(_thumb_from_apify_list(path))
            elif kind == "elias_xlsx":
                urls.update(_thumb_from_elias_xlsx(path))
            elif kind == "snapshot_manifest":
                u, l = _thumb_from_snapshot_manifest(path)
                urls.update(u)
                local_paths.update(l)
        lookup[cid] = {vid: {"thumbnail_url": u, "downloaded_local_path": local_paths.get(vid)}
                       for vid, u in urls.items()}
    return lookup


def _extract_channels_and_videos():
    """Source: data/catalog/youtube_channel_registry.db (channels/videos/transcripts/dataset_channels/datasets)."""
    con = sqlite3.connect(REPO / "data/catalog/youtube_channel_registry.db")
    con.row_factory = sqlite3.Row
    ids = tuple(SENIOR_HEALTH_CHANNEL_IDS)
    q = f"SELECT * FROM channels WHERE canonical_channel_id IN ({','.join('?' * len(ids))})"
    channels = [dict(r) for r in con.execute(q, ids)]

    for ch in channels:
        cid = ch["canonical_channel_id"]
        ch["classification"] = "OWN_CHANNEL" if cid == OWN_CHANNEL_ID else "ACQUIRED_DIRECT_COMPETITOR"
        ch["dataset_links"] = [dict(r) for r in con.execute(
            "SELECT * FROM dataset_channels WHERE canonical_channel_id=?", (cid,)
        )]

    thumb_lookup = _build_thumbnail_lookup()

    videos_by_channel = {}
    for cid in ids:
        vids = [dict(r) for r in con.execute(
            "SELECT * FROM videos WHERE canonical_channel_id=? ORDER BY published_at", (cid,)
        )]
        for v in vids:
            vid = v["youtube_video_id"]
            v["transcripts"] = [dict(r) for r in con.execute(
                "SELECT transcript_id, dataset_id, word_count, language, caption_type, is_placeholder, "
                "unavailable_reason, evidence_locator, transcript_sha256 FROM transcripts WHERE youtube_video_id=?",
                (vid,)
            )]
            raw = v.pop("raw_json", None)
            if raw:
                try:
                    rj = json.loads(raw)
                    v["subscribers_at_capture"] = rj.get("numberOfSubscribers")
                    v["channel_total_views_at_capture"] = rj.get("channelTotalViews")
                    v["channel_total_videos_at_capture"] = rj.get("channelTotalVideos")
                    v["comments_count_raw"] = rj.get("commentsCount")
                except (json.JSONDecodeError, TypeError):
                    pass

            # Thumbnail recovery (read-only join against raw acquisition source files;
            # DB thumbnail_url column is sparse — see THUMBNAIL_SOURCES docstring above).
            if v.get("thumbnail_url"):
                v["thumbnail_url_source"] = "DATABASE_COLUMN"
            else:
                hit = thumb_lookup.get(cid, {}).get(vid)
                if hit and hit["thumbnail_url"]:
                    v["thumbnail_url"] = hit["thumbnail_url"]
                    v["thumbnail_url_source"] = "RECOVERED_FROM_RAW_ACQUISITION_SOURCE"
                else:
                    v["thumbnail_url_source"] = "SOURCE_DATA_GENUINELY_UNAVAILABLE"
            v["downloaded_thumbnail_local_path"] = thumb_lookup.get(cid, {}).get(vid, {}).get("downloaded_local_path")
        videos_by_channel[cid] = vids
    con.close()
    return channels, videos_by_channel


def _extract_master_inventory():
    """Source: docs/research/senior-health-2026-09-25/forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY.json
    (69 total known Senior Health leads: acquired + pending + identity-only + removed + own)."""
    d = json.loads((REPO / "docs/research/senior-health-2026-09-25/forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY.json").read_text())
    from collections import Counter
    class_counts = Counter(c["class"] for c in d["channels"])
    return {
        "generated_by": d["generated_by"],
        "channels": d["channels"],
        "total_known_leads": len(d["channels"]),
        "class_distribution": dict(class_counts),
        "class_legend": {
            "A": "ACQUIRED_DIRECT_COMPETITOR (complete dataset, pre-existing)",
            "B": "ACQUIRED_DIRECT_COMPETITOR (complete dataset, acquired via recent backfill/run)",
            "C": "PARTIALLY_ACQUIRED_COMPETITOR (metadata only, no full package) — currently empty",
            "D": "QUALIFIED_PENDING_COMPETITOR (registered, awaiting paid acquisition) — currently empty at this level",
            "E": "QUALIFIED_PENDING_COMPETITOR or IDENTITY_ONLY (48 = 14 qualified-pending + 34 identity-only)",
            "F": "REMOVED_OR_UNVERIFIABLE (terminated by YouTube, empty shell, or excluded content-mill clone)",
            "OWN": "OWN_CHANNEL",
        },
    }


def _extract_knowledge_video_mappings():
    """Sources: docs/research/senior-health-2026-09-25/forensic-v2/DS-000011-TRACE-MATRIX.json,
    .../DS-000018-CLAIM-MATRIX.json, .../DS-000031-FRAMEWORK-MATRIX.json — existing
    project-authored mappings between knowledge units and Senior Health videos."""
    base = REPO / "docs/research/senior-health-2026-09-25/forensic-v2"
    ds011 = json.loads((base / "DS-000011-TRACE-MATRIX.json").read_text())
    ds018 = json.loads((base / "DS-000018-CLAIM-MATRIX.json").read_text())
    ds031 = json.loads((base / "DS-000031-FRAMEWORK-MATRIX.json").read_text())
    return {
        "DS-000011_trace_matrix": ds011,
        "DS-000018_claim_matrix": ds018,
        "DS-000031_framework_matrix": ds031,
        "counts": {"DS-000011": len(ds011), "DS-000018": len(ds018), "DS-000031": len(ds031)},
    }


def _reconciliation(ds011, ds018, ds031, channels, videos_by_channel, inventory):
    total_videos = sum(len(v) for v in videos_by_channel.values())
    total_real_transcripts = sum(
        1 for vids in videos_by_channel.values() for v in vids
        for t in v["transcripts"] if not t["is_placeholder"]
    )
    total_with_desc = sum(
        1 for vids in videos_by_channel.values() for v in vids if v.get("description")
    )
    total_with_thumb = sum(
        1 for vids in videos_by_channel.values() for v in vids if v.get("thumbnail_url")
    )
    total_with_downloaded_thumb = sum(
        1 for vids in videos_by_channel.values() for v in vids if v.get("downloaded_thumbnail_local_path")
    )
    tabs_with_fulltext = sum(1 for t in ds018["tabs"] if t.get("full_text"))
    tabs_claim_atomized = len({
        c["tab_file"] for c in ds018["additional_claims"] if c.get("tab_file")
    }) + 7  # + the original 7 human-audited tabs
    return {
        "DS-000011": {
            "prior_audit_files": 17, "prior_audit_unique": 16,
            "observed_files": ds011["source_document_count"], "observed_rules": ds011["knowledge_rule_count"],
            "fulltext_sources_extracted": ds011["fulltext_source_count"],
            "fulltext_unique_sources": ds011["fulltext_unique_source_count"],
            "drift": ds011["source_document_count"] != 17,
        },
        "DS-000018": {
            "prior_audit_tabs": 63, "prior_audit_unique": 61,
            "observed_tabs": ds018["tab_count"], "observed_claims": ds018["claim_count"],
            "tabs_with_fulltext_recovered": tabs_with_fulltext,
            "tabs_claim_atomized": tabs_claim_atomized,
            "original_human_audited_claims": ds018["claim_count"],
            "additional_ai_extracted_claims": ds018["additional_claim_count"],
            "all_claims_combined": ds018["all_claims_combined_count"],
            "drift": ds018["tab_count"] != 63,
        },
        "DS-000031": {
            "prior_audit": {"segments": 15, "concepts": 63, "frameworks": 11, "formulas": 15, "scorecard": 1, "examples": 9},
            "observed": ds031["counts"],
            "segments_with_fulltext_recovered": sum(1 for s in ds031["segments"] if s.get("full_text")),
            "drift": ds031["counts"]["segments"] != 15 or ds031["counts"]["concepts"] != 63,
        },
        "senior_health": {
            "acquired_channels_incl_own": len(channels),
            "total_unique_video_records": total_videos,
            "total_real_transcripts": total_real_transcripts,
            "total_descriptions_exported": total_with_desc,
            "total_thumbnail_urls_recovered": total_with_thumb,
            "total_downloaded_thumbnail_files": total_with_downloaded_thumb,
            "known_leads_total": inventory["total_known_leads"],
            "class_distribution": inventory["class_distribution"],
        },
    }


def main():
    ds011 = _extract_ds000011()
    ds018 = _extract_ds000018()
    ds031 = _extract_ds000031()
    channels, videos_by_channel = _extract_channels_and_videos()
    inventory = _extract_master_inventory()
    mappings = _extract_knowledge_video_mappings()
    recon = _reconciliation(ds011, ds018, ds031, channels, videos_by_channel, inventory)

    master = {
        "generated_at": "2026-09-27",
        "repo_branch": "research/senior-health-acquisition-phase-2",
        "note": "Read-only export. No source dataset under data/ or docs/ was modified to produce this file.",
        "DS-000011": ds011,
        "DS-000018": ds018,
        "DS-000031": ds031,
        "senior_health_channels": channels,
        "senior_health_videos_by_channel": videos_by_channel,
        "senior_health_master_inventory": inventory,
        "knowledge_video_mappings": mappings,
        "reconciliation": recon,
    }
    OUT.write_text(json.dumps(master, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    print(json.dumps(recon, indent=2))


if __name__ == "__main__":
    main()
