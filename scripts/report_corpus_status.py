#!/usr/bin/env python3
"""Corpus status report — answers "what data has arrived so far" and "what is
still missing" by querying the existing catalog (data/catalog/youtube_inventory.db).

Read-only. Does not ingest, does not modify the database, does not perform
competitor strategy analysis or topic recommendations (see docs/STATUS_QUERIES.md
and .codex/skills/multimodal-source-ingestion/SKILL.md "Phase boundary").

Usage:
    python3 scripts/report_corpus_status.py            # Markdown to stdout
    python3 scripts/report_corpus_status.py --json      # structured JSON for agents
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import report_common as rc  # noqa: E402


def _dataset_counts(conn):
    total = conn.execute("SELECT COUNT(*) FROM datasets;").fetchone()[0]
    by_status = conn.execute(
        "SELECT status, COUNT(*) c FROM datasets GROUP BY status ORDER BY status;"
    ).fetchall()
    classified = conn.execute(
        "SELECT COUNT(DISTINCT dataset_id) FROM entity_classifications;"
    ).fetchone()[0]
    return total, by_status, classified


def _batches(conn):
    return conn.execute(
        "SELECT batch_id, batch_name, status, root_count FROM source_batches ORDER BY batch_id;"
    ).fetchall()


def _discovered_files(conn):
    total = conn.execute("SELECT COUNT(*) FROM discovered_files;").fetchone()[0]
    by_disp = conn.execute(
        "SELECT disposition, COUNT(*) c FROM discovered_files GROUP BY disposition ORDER BY disposition;"
    ).fetchall()
    return total, by_disp


def _structured_registration(conn):
    channels = conn.execute("SELECT COUNT(*) FROM channels;").fetchone()[0]
    videos = conn.execute("SELECT COUNT(*) FROM videos;").fetchone()[0]
    transcripts_by_status = conn.execute(
        "SELECT availability_status, COUNT(*) c FROM transcripts GROUP BY availability_status;"
    ).fetchall()
    return channels, videos, transcripts_by_status


def _visual_evidence(conn):
    visual_assets = conn.execute("SELECT COUNT(*) FROM visual_assets;").fetchone()[0]
    ocr = conn.execute("SELECT COUNT(*) FROM visual_observations WHERE observation_type='OCR';").fetchone()[0]
    semantic = conn.execute(
        "SELECT COUNT(*) FROM visual_observations WHERE observation_type='SEMANTIC_INSPECTION';"
    ).fetchone()[0]
    clusters = conn.execute(
        "SELECT COUNT(DISTINCT visual_state_cluster_id) FROM visual_assets WHERE visual_state_cluster_id IS NOT NULL;"
    ).fetchone()[0]
    forensic_datasets = conn.execute(
        "SELECT DISTINCT dataset_id FROM visual_assets WHERE visual_state_cluster_id IS NOT NULL ORDER BY dataset_id;"
    ).fetchall()
    return visual_assets, ocr, semantic, clusters, [r["dataset_id"] for r in forensic_datasets]


def _documents(conn):
    total = conn.execute("SELECT COUNT(*) FROM document_records;").fetchone()[0]
    datasets = conn.execute("SELECT DISTINCT dataset_id FROM document_records ORDER BY dataset_id;").fetchall()
    return total, [r["dataset_id"] for r in datasets]


def _gap_unclassified_datasets(conn):
    return conn.execute(
        "SELECT dataset_id, dataset_name FROM datasets d "
        "WHERE NOT EXISTS (SELECT 1 FROM entity_classifications ec WHERE ec.dataset_id = d.dataset_id) "
        "ORDER BY dataset_id;"
    ).fetchall()


def _gap_editing_style_missing_despite_visual_evidence(conn):
    rows = conn.execute(
        "SELECT d.dataset_id, d.dataset_name, "
        "(SELECT COUNT(*) FROM visual_assets va WHERE va.dataset_id = d.dataset_id) AS visual_asset_count, "
        "(SELECT editing_style FROM entity_classifications ec WHERE ec.dataset_id = d.dataset_id LIMIT 1) AS editing_style "
        "FROM datasets d ORDER BY d.dataset_id;"
    ).fetchall()
    return [r for r in rows if r["visual_asset_count"] > 0 and (r["editing_style"] is None or r["editing_style"] == "UNKNOWN")]


def _gap_packaging_style_missing_despite_semantic_inspection(conn):
    rows = conn.execute(
        "SELECT d.dataset_id, d.dataset_name, "
        "(SELECT COUNT(*) FROM visual_observations vo JOIN visual_assets va ON va.visual_asset_id = vo.visual_asset_id "
        " WHERE va.dataset_id = d.dataset_id AND vo.observation_type = 'SEMANTIC_INSPECTION') AS semantic_obs_count, "
        "(SELECT packaging_style FROM entity_classifications ec WHERE ec.dataset_id = d.dataset_id LIMIT 1) AS packaging_style "
        "FROM datasets d ORDER BY d.dataset_id;"
    ).fetchall()
    return [r for r in rows if r["semantic_obs_count"] > 0 and not r["packaging_style"]]


def _gap_provenance_locator_mismatch(conn):
    """entity_classifications.source_locator is free text written at classification
    time (e.g. "aggregated from N screenshot semantic inspections"). This checks that
    claimed N against the semantic-inspection count actually recorded now, and flags
    any disagreement — a genuine provenance inconsistency, not something to silently fix."""
    rows = conn.execute(
        "SELECT ec.dataset_id, ec.source_locator, "
        "(SELECT COUNT(*) FROM visual_observations vo JOIN visual_assets va ON va.visual_asset_id = vo.visual_asset_id "
        " WHERE va.dataset_id = ec.dataset_id AND vo.observation_type = 'SEMANTIC_INSPECTION') AS actual_semantic_obs_count "
        "FROM entity_classifications ec ORDER BY ec.dataset_id;"
    ).fetchall()
    mismatches = []
    for r in rows:
        m = re.search(r"aggregated from (\d+) screenshot semantic inspections", r["source_locator"] or "")
        if m and int(m.group(1)) != r["actual_semantic_obs_count"]:
            mismatches.append({
                "dataset_id": r["dataset_id"],
                "source_locator": r["source_locator"],
                "claimed_count": int(m.group(1)),
                "actual_semantic_obs_count": r["actual_semantic_obs_count"],
            })
    return mismatches


def build_report(conn):
    ds_total, ds_by_status, ds_classified = _dataset_counts(conn)
    batches = _batches(conn)
    df_total, df_by_disp = _discovered_files(conn)
    channels, videos, transcripts_by_status = _structured_registration(conn)
    visual_assets, ocr, semantic, clusters, forensic_datasets = _visual_evidence(conn)
    doc_total, doc_datasets = _documents(conn)

    gap_unclassified = _gap_unclassified_datasets(conn)
    gap_editing = _gap_editing_style_missing_despite_visual_evidence(conn)
    gap_packaging = _gap_packaging_style_missing_despite_semantic_inspection(conn)
    gap_provenance = _gap_provenance_locator_mismatch(conn)
    transcripts_unavailable = next((r["c"] for r in transcripts_by_status if r["availability_status"] == "UNAVAILABLE"), 0)

    payload = {
        "datasets": {
            "total": ds_total,
            "by_status": {r["status"]: r["c"] for r in ds_by_status},
            "with_entity_classification": ds_classified,
            "without_entity_classification": ds_total - ds_classified,
        },
        "batches": [dict(r) for r in batches],
        "discovered_files": {
            "total": df_total,
            "by_disposition": {r["disposition"]: r["c"] for r in df_by_disp},
        },
        "structured_registration": {
            "channels": channels,
            "videos": videos,
            "transcripts_by_availability": {r["availability_status"]: r["c"] for r in transcripts_by_status},
        },
        "visual_evidence": {
            "unique_visual_assets": visual_assets,
            "ocr_observations": ocr,
            "semantic_inspection_observations": semantic,
            "distinct_visual_state_clusters": clusters,
            "forensic_video_datasets": forensic_datasets,
        },
        "document_corpus": {
            "document_records": doc_total,
            "datasets": doc_datasets,
        },
        "gaps": {
            "datasets_never_classified": [dict(r) for r in gap_unclassified],
            "editing_style_unknown_despite_visual_evidence": [dict(r) for r in gap_editing],
            "packaging_style_missing_despite_semantic_inspection": [dict(r) for r in gap_packaging],
            "provenance_source_locator_mismatches": gap_provenance,
            "transcripts_unavailable": transcripts_unavailable,
        },
    }

    lines = []
    lines.append("# Corpus Status Report")
    lines.append("")
    lines.append("Read-only snapshot generated from `data/catalog/youtube_inventory.db` by "
                  "`scripts/report_corpus_status.py`. No ingestion, no strategy analysis, no "
                  "topic recommendations — see `docs/STATUS_QUERIES.md`.")
    lines.append("")
    lines.append("## Datasets")
    lines.append("")
    lines.append("- Total registered datasets: **{}**".format(ds_total))
    for r in ds_by_status:
        lines.append("  - {}: {}".format(r["status"], r["c"]))
    lines.append("- With a classification record (`entity_classifications`): {}".format(ds_classified))
    lines.append("- With **no** classification record at all: {}".format(ds_total - ds_classified))
    lines.append("")
    lines.append("## Source Batches")
    lines.append("")
    lines.extend(rc.md_table(["Batch ID", "Name", "Status", "Roots"],
                              [(r["batch_id"], r["batch_name"], r["status"], r["root_count"]) for r in batches]))
    lines.append("")
    lines.append("## Discovered Files (all batches)")
    lines.append("")
    lines.append("- Total discovered filesystem items: **{}**".format(df_total))
    lines.extend(rc.md_table(["Disposition", "Count"], [(r["disposition"], r["c"]) for r in df_by_disp]))
    lines.append("")
    lines.append("## Structured Registration (scripts/transcripts)")
    lines.append("")
    lines.append("- Registered channels: **{}**".format(channels))
    lines.append("- Registered videos: **{}**".format(videos))
    for r in transcripts_by_status:
        lines.append("- Transcripts {}: {}".format(r["availability_status"], r["c"]))
    lines.append("")
    lines.append("## Visual Evidence (screenshots + forensic video frames)")
    lines.append("")
    lines.append("- Unique visual assets: **{}**".format(visual_assets))
    lines.append("- OCR observations: {}".format(ocr))
    lines.append("- Native semantic-inspection observations: {}".format(semantic))
    lines.append("- Distinct forensic visual-state clusters: {}".format(clusters))
    lines.append("- Datasets with forensic-video frame-cluster evidence: {}".format(", ".join(forensic_datasets) or "none"))
    lines.append("")
    lines.append("## Document Corpus")
    lines.append("")
    lines.append("- Document records: **{}**".format(doc_total))
    lines.append("- Datasets: {}".format(", ".join(doc_datasets) or "none"))
    lines.append("")
    lines.append("## What is still missing (computed gaps, not a fixed list)")
    lines.append("")
    if gap_unclassified:
        lines.append("**Datasets with no classification record at all** ({}):".format(len(gap_unclassified)))
        for r in gap_unclassified:
            lines.append("  - {} — {}".format(r["dataset_id"], r["dataset_name"]))
    else:
        lines.append("- Every dataset has at least one classification record.")
    if gap_editing:
        lines.append("")
        lines.append("**Datasets with visual evidence but `editing_style` still UNKNOWN/unset** ({}):".format(len(gap_editing)))
        for r in gap_editing:
            lines.append("  - {} — {} ({} visual assets)".format(r["dataset_id"], r["dataset_name"], r["visual_asset_count"]))
    if gap_packaging:
        lines.append("")
        lines.append("**Datasets with semantic screenshot inspection but no `packaging_style` recorded** ({}):".format(len(gap_packaging)))
        for r in gap_packaging:
            lines.append("  - {} — {} ({} semantic observations)".format(r["dataset_id"], r["dataset_name"], r["semantic_obs_count"]))
    if gap_provenance:
        lines.append("")
        lines.append("**Provenance text inconsistencies** (`entity_classifications.source_locator` claims a count that "
                      "does not match the observations actually recorded) ({}):".format(len(gap_provenance)))
        for r in gap_provenance:
            lines.append("  - {}: locator says \"{}\", actual semantic-inspection count is {}".format(
                r["dataset_id"], r["source_locator"], r["actual_semantic_obs_count"]))
    if transcripts_unavailable:
        lines.append("")
        lines.append("- {} transcript(s) recorded as UNAVAILABLE.".format(transcripts_unavailable))
    lines.append("")
    lines.append("See also `data/manifests/batches/BATCH-000001_VISUAL_STATE_COVERAGE.md` for the related, already-"
                  "documented finding that DS-000012 and DS-000015 are suspected to share the same source video.")
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
