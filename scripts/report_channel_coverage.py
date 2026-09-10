#!/usr/bin/env python3
"""Channel coverage report — answers "which channels are in the system", "which
channels have scripts/transcripts", "which channels only have screenshots", "which
channels have packaging-style evidence", "which channels have editing-style evidence".

Read-only. Two distinct identity tiers are reported, and never merged, because they
carry different evidence strength (AGENTS.md rule 6 — never silently convert an
inference into a fact):

  Tier A — REGISTERED_CHANNEL: a real row in the `channels` table (Decision 015
           structured registration), with videos/snapshots/transcripts linked to it
           by foreign key. A linked screenshot dataset remains visible as evidence.
  Tier B — DATASET_EVIDENCED_COMPETITOR: no `channels` row exists. The "channel" is
           only known because one dataset's own recorded `dataset_name` literally
           says "<Name> — Competitor Channel Screenshots" and it carries screenshot
           evidence (`entity_classifications`, `visual_assets`). No transcript/video
           identity has been registered for these — once a strong identity link exists,
           that dataset is reported with Tier A instead of duplicated here.

Usage:
    python3 scripts/report_channel_coverage.py
    python3 scripts/report_channel_coverage.py --json
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import report_common as rc  # noqa: E402

COMPETITOR_SUFFIX = " — Competitor Channel Screenshots"


def _tier_a_registered_channels(conn):
    channels = conn.execute(
        "SELECT channel_id, youtube_channel_id, display_name, handle, channel_url, "
        "created_from_dataset_id FROM channels ORDER BY channel_id;"
    ).fetchall()
    out = []
    for ch in channels:
        transcript_rows = conn.execute(
            "SELECT t.availability_status, COUNT(*) c FROM videos v "
            "JOIN transcripts t ON t.transcript_id = ("
            " SELECT t2.transcript_id FROM transcripts t2 WHERE t2.video_id=v.video_id "
            " ORDER BY t2.created_at DESC, t2.transcript_id DESC LIMIT 1"
            ") WHERE v.channel_id = ? "
            "GROUP BY t.availability_status;",
            (ch["channel_id"],),
        ).fetchall()
        transcripts = {row["availability_status"]: row["c"] for row in transcript_rows}
        videos = conn.execute("SELECT COUNT(*) FROM videos WHERE channel_id = ?;", (ch["channel_id"],)).fetchone()[0]
        type_rows = conn.execute(
            "SELECT CASE LOWER(COALESCE(vs.video_type, '')) "
            " WHEN 'video' THEN 'regular' "
            " WHEN 'short' THEN 'shorts' WHEN 'shorts' THEN 'shorts' "
            " WHEN 'live' THEN 'streams' WHEN 'stream' THEN 'streams' WHEN 'streams' THEN 'streams' "
            " ELSE 'unknown' END content_type, COUNT(*) c FROM videos v "
            "LEFT JOIN video_snapshots vs ON vs.video_snapshot_id = ("
            " SELECT vs2.video_snapshot_id FROM video_snapshots vs2 WHERE vs2.video_id=v.video_id "
            " ORDER BY vs2.observed_at DESC, vs2.video_snapshot_id DESC LIMIT 1"
            ") WHERE v.channel_id=? GROUP BY content_type;",
            (ch["channel_id"],),
        ).fetchall()
        content_counts = {row["content_type"]: row["c"] for row in type_rows}
        dataset_rows = conn.execute(
            "SELECT dataset_id FROM (SELECT dataset_id FROM channel_dataset_links WHERE channel_id=? "
            "UNION SELECT ?) ORDER BY dataset_id;",
            (ch["channel_id"], ch["created_from_dataset_id"]),
        ).fetchall()
        dataset_ids = [row["dataset_id"] for row in dataset_rows]
        placeholders = ",".join("?" for _ in dataset_ids)
        visual_assets = conn.execute(
            "SELECT COUNT(*) FROM visual_assets WHERE dataset_id IN ({}) "
            "AND frame_sequence_id IS NULL;".format(placeholders), dataset_ids
        ).fetchone()[0]
        semantic_rows = conn.execute(
            "SELECT vo.structured_json FROM visual_observations vo "
            "JOIN visual_assets va ON va.visual_asset_id=vo.visual_asset_id "
            "WHERE va.dataset_id IN ({}) AND vo.observation_type='SEMANTIC_INSPECTION';".format(placeholders),
            dataset_ids,
        ).fetchall()
        packaging = False
        for row in semantic_rows:
            try:
                value = json.loads(row["structured_json"] or "null")
            except json.JSONDecodeError:
                value = None
            packaging = packaging or bool(isinstance(value, dict) and value.get("visual_packaging_pattern_notes"))
        classifications = conn.execute(
            "SELECT content_domain, packaging_style, editing_style FROM entity_classifications "
            "WHERE dataset_id IN ({});".format(placeholders), dataset_ids,
        ).fetchall()
        packaging = packaging or any(row["packaging_style"] for row in classifications)
        editing_styles = {row["editing_style"] for row in classifications if row["editing_style"] not in (None, "UNKNOWN")}
        forensic_rows = conn.execute(
            "SELECT d.dataset_id, d.dataset_name, COUNT(DISTINCT fp.video_id) proven_videos, "
            "COUNT(DISTINCT va.visual_asset_id) frame_assets, "
            "COUNT(DISTINCT va.visual_state_cluster_id) visual_state_clusters "
            "FROM channel_dataset_links cdl JOIN datasets d ON d.dataset_id=cdl.dataset_id "
            "JOIN field_provenance fp ON fp.dataset_id=cdl.dataset_id "
            " AND fp.extraction_method='xattr_plist_base64url_media_id' "
            "JOIN videos fv ON fv.video_id=fp.video_id AND fv.channel_id=cdl.channel_id "
            "JOIN visual_assets va ON va.dataset_id=cdl.dataset_id AND va.frame_sequence_id IS NOT NULL "
            "WHERE cdl.channel_id=? AND cdl.relationship_type='IDENTITY_EVIDENCE' "
            "GROUP BY d.dataset_id, d.dataset_name ORDER BY d.dataset_id;",
            (ch["channel_id"],),
        ).fetchall()
        related_forensic_datasets = [dict(row) for row in forensic_rows]
        thumbnail_row = conn.execute(
            "SELECT COALESCE(SUM(url_count),0) references_count, COUNT(*) video_count FROM ("
            " SELECT video_id,COUNT(DISTINCT thumbnail_url) url_count FROM ("
            "  SELECT te.video_id,te.thumbnail_url FROM thumbnail_evidence te JOIN videos v ON v.video_id=te.video_id WHERE v.channel_id=? "
            "  UNION ALL "
            "  SELECT vs.video_id,vs.thumbnail_url FROM video_snapshots vs JOIN videos v ON v.video_id=vs.video_id WHERE v.channel_id=? AND vs.thumbnail_url IS NOT NULL"
            " ) GROUP BY video_id);",
            (ch["channel_id"], ch["channel_id"]),
        ).fetchone()
        packaging = packaging or thumbnail_row["video_count"] > 0
        newest_snapshot = conn.execute(
            "SELECT MAX(observed_at) FROM ("
            "SELECT observed_at FROM channel_snapshots WHERE channel_id=? UNION ALL "
            "SELECT vs.observed_at FROM video_snapshots vs JOIN videos v ON v.video_id=vs.video_id WHERE v.channel_id=?"
            ");", (ch["channel_id"], ch["channel_id"]),
        ).fetchone()[0]
        apify_rows = conn.execute(
            "SELECT source, extraction_provider, actor_name, actor_id, actor_run_id, run_status, "
            "run_cost_usd, observed_at, result_record_count FROM apify_source_runs "
            "WHERE dataset_id IN ({}) ORDER BY observed_at, actor_run_id;".format(placeholders),
            dataset_ids,
        ).fetchall()
        apify_runs = [dict(row) for row in apify_rows]
        sources = []
        if visual_assets:
            sources.append("SCREENSHOT")
        if related_forensic_datasets:
            sources.append("FORENSIC_VIDEO")
        if apify_runs:
            sources.append("APIFY")
        if conn.execute(
            "SELECT 1 FROM datasets WHERE dataset_id IN ({}) AND source_type='EXTERNAL_FILES' LIMIT 1".format(placeholders),
            dataset_ids,
        ).fetchone():
            sources.append("SUPPLIED_FILES")
        out.append({
            "tier": "REGISTERED_CHANNEL",
            "channel_id": ch["channel_id"],
            "youtube_channel_id": ch["youtube_channel_id"],
            "display_name": ch["display_name"],
            "handle": ch["handle"],
            "channel_url": ch["channel_url"],
            "dataset_ids": dataset_ids,
            "videos": videos,
            "regular_videos": content_counts.get("regular", 0),
            "shorts": content_counts.get("shorts", 0),
            "streams": content_counts.get("streams", 0),
            "unknown_content_type": content_counts.get("unknown", 0),
            "transcripts_available": transcripts.get("AVAILABLE", 0),
            "transcripts_unavailable": transcripts.get("UNAVAILABLE", 0),
            "screenshot_evidence_count": visual_assets,
            "thumbnail_reference_count": thumbnail_row["references_count"],
            "videos_with_thumbnail_evidence": thumbnail_row["video_count"],
            "has_packaging_evidence": packaging,
            "has_forensic_editing_evidence": bool(related_forensic_datasets),
            "has_editing_evidence": bool(editing_styles or related_forensic_datasets),
            "editing_style": ", ".join(sorted(editing_styles)) if editing_styles else "UNKNOWN",
            "related_forensic_datasets": related_forensic_datasets,
            "content_domain": next((row["content_domain"] for row in classifications if row["content_domain"]), None),
            "newest_structured_snapshot": newest_snapshot,
            "apify_provenance": apify_runs,
            "evidence_sources": sources,
        })
    return out


def _tier_b_dataset_evidenced_competitors(conn):
    datasets = conn.execute(
        "SELECT dataset_id, dataset_name FROM datasets WHERE dataset_name LIKE ? "
        "AND NOT EXISTS (SELECT 1 FROM channel_dataset_links cdl WHERE cdl.dataset_id=datasets.dataset_id) "
        "ORDER BY dataset_id;",
        ("%" + COMPETITOR_SUFFIX.strip() + "%",),
    ).fetchall()
    out = []
    for d in datasets:
        display_name = d["dataset_name"].split(COMPETITOR_SUFFIX)[0].strip()
        cls = conn.execute(
            "SELECT content_domain, packaging_style, editing_style FROM entity_classifications "
            "WHERE dataset_id = ? LIMIT 1;", (d["dataset_id"],)
        ).fetchone()
        visual_assets = conn.execute(
            "SELECT COUNT(*) FROM visual_assets WHERE dataset_id = ?;", (d["dataset_id"],)
        ).fetchone()[0]
        transcripts = conn.execute(
            "SELECT COUNT(*) FROM transcripts WHERE dataset_id = ?;", (d["dataset_id"],)
        ).fetchone()[0]
        out.append({
            "tier": "DATASET_EVIDENCED_COMPETITOR",
            "channel_id": None,
            "display_name": display_name,
            "handle": None,
            "dataset_id": d["dataset_id"],
            "videos": None,
            "regular_videos": None,
            "shorts": None,
            "streams": None,
            "unknown_content_type": None,
            "transcripts_available": transcripts,
            "transcripts_unavailable": 0,
            "screenshot_evidence_count": visual_assets,
            "thumbnail_reference_count": 0,
            "videos_with_thumbnail_evidence": 0,
            "has_packaging_evidence": bool(cls and cls["packaging_style"]),
            "has_forensic_editing_evidence": False,
            "has_editing_evidence": bool(cls and cls["editing_style"] not in (None, "UNKNOWN")),
            "editing_style": cls["editing_style"] if cls else "UNKNOWN",
            "related_forensic_datasets": [],
            "content_domain": cls["content_domain"] if cls else None,
            "newest_structured_snapshot": None,
            "apify_provenance": [],
            "evidence_sources": ["SCREENSHOT"] if visual_assets else [],
        })
    return out


def build_report(conn):
    tier_a = _tier_a_registered_channels(conn)
    tier_b = _tier_b_dataset_evidenced_competitors(conn)
    all_entities = tier_a + tier_b

    with_transcripts = [e for e in all_entities if e["transcripts_available"]]
    screenshots_only = [e for e in all_entities if e["screenshot_evidence_count"] > 0 and not e["transcripts_available"]]
    with_packaging = [e for e in all_entities if e["has_packaging_evidence"]]
    with_editing = [e for e in all_entities if e["has_editing_evidence"]]

    payload = {
        "registered_channels": tier_a,
        "dataset_evidenced_competitors": tier_b,
        "answers": {
            "channels_with_transcripts": [e["display_name"] for e in with_transcripts],
            "channels_with_screenshots_only": [e["display_name"] for e in screenshots_only],
            "channels_with_packaging_evidence": [e["display_name"] for e in with_packaging],
            "channels_with_editing_evidence": [e["display_name"] for e in with_editing],
        },
    }

    lines = []
    lines.append("# Channel Coverage Report")
    lines.append("")
    lines.append("Read-only. Generated by `scripts/report_channel_coverage.py`. See "
                  "`docs/STATUS_QUERIES.md` for the identity-tier caveat before treating "
                  "Tier B rows as equivalent to a registered channel.")
    lines.append("")
    lines.append("## Tier A — Registered channels (`channels` table, has video/transcript identity)")
    lines.append("")
    lines.extend(rc.md_table(
        ["Channel ID", "YouTube ID", "Display Name", "Handle", "Datasets", "Total (Regular/Shorts/Streams/Unknown)",
         "Transcripts A/U", "Thumbnail Items/Refs", "Packaging", "Editing Evidence", "Related Forensics",
         "Newest Snapshot", "Sources"],
        [(e["channel_id"], e["youtube_channel_id"], e["display_name"], e["handle"],
          ", ".join(e["dataset_ids"]),
          "{} ({}/{}/{}/{})".format(e["videos"], e["regular_videos"], e["shorts"], e["streams"],
                                     e["unknown_content_type"]),
          "{}/{}".format(e["transcripts_available"], e["transcripts_unavailable"]),
          "{}/{}".format(e["videos_with_thumbnail_evidence"], e["thumbnail_reference_count"]),
          "YES" if e["has_packaging_evidence"] else "no",
          e["editing_style"] if e["editing_style"] != "UNKNOWN" else
          ("FORENSIC (unclassified)" if e["has_forensic_editing_evidence"] else "UNKNOWN"),
          ", ".join(row["dataset_id"] for row in e["related_forensic_datasets"]) or "none",
          e["newest_structured_snapshot"], ", ".join(e["evidence_sources"]))
         for e in tier_a]))
    lines.append("")
    lines.append("## Tier B — Dataset-evidenced competitor channels (screenshot evidence only, "
                  "no registered channel/video identity)")
    lines.append("")
    lines.extend(rc.md_table(
        ["Dataset ID", "Display Name (from dataset_name)", "Content Domain", "Screenshot Count",
         "Packaging Evidence", "Editing Evidence"],
        [(e["dataset_id"], e["display_name"], e["content_domain"] or "UNCLASSIFIED", e["screenshot_evidence_count"],
          "YES" if e["has_packaging_evidence"] else "no", "YES" if e["has_editing_evidence"] else "no")
         for e in tier_b]))
    lines.append("")
    lines.append("## Answers")
    lines.append("")
    lines.append("- **Channels with scripts/transcripts:** {}".format(
        ", ".join(e["display_name"] for e in with_transcripts) or "none"))
    lines.append("- **Channels with screenshots only (no transcript/video identity):** {}".format(
        ", ".join(e["display_name"] for e in screenshots_only) or "none"))
    lines.append("- **Channels with packaging-style evidence:** {}".format(
        ", ".join(e["display_name"] for e in with_packaging) or "none"))
    lines.append("- **Channels with classified editing style or strongly linked forensic moving-image evidence:** {}".format(
        ", ".join(e["display_name"] for e in with_editing) or "none (Decision 016: editing_style requires real "
        "moving-image/frame evidence; transcripts, thumbnails, and screenshots do not establish it)"))
    apify_runs = [(e["display_name"], run) for e in tier_a for run in e["apify_provenance"]]
    if apify_runs:
        lines.append("")
        lines.append("## Apify Provenance")
        lines.append("")
        lines.extend(rc.md_table(
            ["Channel", "Actor", "Actor ID", "Run ID", "Status", "Records", "Cost USD", "Observed At"],
            [(name, run["actor_name"], run["actor_id"], run["actor_run_id"], run["run_status"],
              run["result_record_count"], run["run_cost_usd"], run["observed_at"])
             for name, run in apify_runs]))
    lines.append("")
    lines.append("## Caveat")
    lines.append("")
    lines.append("Tier B display names are derived by stripping the literal `{}` suffix off each dataset's own "
                  "`dataset_name` — they are not a registered channel identity (no `channel_id`, no YouTube channel "
                  "ID, no video/transcript linkage). Treat Tier A and Tier B as different confidence levels, "
                  "never as interchangeable rows.".format(COMPETITOR_SUFFIX.strip()))
    lines.append("")

    return payload, lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", default=None)
    parser.add_argument("--json", action="store_true", help="emit structured JSON instead of Markdown")
    args = parser.parse_args()

    conn = rc.connect(args.db_path)
    payload, lines = build_report(conn)
    rc.emit(payload, lines, args.json)


if __name__ == "__main__":
    main()
