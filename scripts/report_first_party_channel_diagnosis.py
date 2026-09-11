#!/usr/bin/env python3
"""Build own-channel diagnostics from normalized private Analytics exports."""
import argparse
import hashlib
import json
import sqlite3
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data/catalog/youtube_inventory.db"
OUTPUT_ROOT = ROOT / "data/intelligence/first-party/channels"
SCHEMA_VERSION = "first-party-channel-diagnosis-1"
PRIVATE_METRICS = {
    "IMPRESSIONS", "IMPRESSIONS_CTR", "WATCH_TIME_HOURS", "AVERAGE_VIEW_DURATION",
    "AVERAGE_PERCENTAGE_VIEWED", "UNIQUE_VIEWERS", "SUBSCRIBERS_GAINED",
    "SUBSCRIBERS_LOST", "SHARES", "NEW_VIEWERS", "CASUAL_VIEWERS",
    "REGULAR_VIEWERS", "RETURNING_VIEWERS", "RETENTION_PERCENTAGE",
    "INTRO_30S_PERCENTAGE", "TRAFFIC_SOURCE", "SEARCH_TERM",
}


class DiagnosisError(ValueError):
    pass


def load_public_context(channel_id, db_path=DB_PATH):
    uri = Path(db_path).resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT v.video_id,s.views,s.duration_seconds,"
            "MAX(CASE WHEN c.classification_dimension='CONTENT_TOPIC' THEN c.classification_value END) topic,"
            "MAX(CASE WHEN c.classification_dimension='CONTENT_FORMAT' THEN c.classification_value END) format "
            "FROM videos v LEFT JOIN video_snapshots s ON s.video_snapshot_id=("
            "SELECT x.video_snapshot_id FROM video_snapshots x WHERE x.video_id=v.video_id "
            "ORDER BY x.observed_at DESC,x.video_snapshot_id DESC LIMIT 1) "
            "LEFT JOIN content_classifications c ON c.video_id=v.video_id AND c.classification_status IN ('PROPOSED','VERIFIED') "
            "WHERE v.channel_id=? GROUP BY v.video_id ORDER BY v.video_id", (channel_id,),
        ).fetchall()
    return {row["video_id"]: {
        "FORMAT": row["format"] or ("SHORT_FORM" if row["duration_seconds"] is not None and row["duration_seconds"] <= 180 else "LONG_FORM"),
        "TOPIC": row["topic"], "PUBLIC_VIEWS": row["views"], "DURATION_SECONDS": row["duration_seconds"],
    } for row in rows}


def enrich_with_existing_intelligence(channel_id, context):
    channel_dir = ROOT / "data/intelligence/channels" / channel_id
    packaging_paths = sorted(path for path in channel_dir.glob("packaging-intelligence*.json") if "pilot" not in path.name)
    hook_paths = sorted(path for path in channel_dir.glob("hook-script-intelligence*.json") if "pilot" not in path.name)
    if packaging_paths:
        payload = json.loads(packaging_paths[-1].read_text(encoding="utf-8"))
        for row in payload.get("title_features", []):
            context.setdefault(row["video_id"], {}).update({
                "PACKAGE_PROMISE": {"TITLE": row.get("title"), "TITLE_ARCHETYPE": row.get("title_archetype")},
            })
    if hook_paths:
        payload = json.loads(hook_paths[-1].read_text(encoding="utf-8"))
        for row in payload.get("hook_features", []):
            context.setdefault(row["video_id"], {}).update({
                "HOOK_STRUCTURE": {"HOOK_ARCHETYPE": row.get("hook_archetype"), "TITLE_TO_HOOK": row.get("title_to_hook")},
            })
        for row in payload.get("script_features", []):
            context.setdefault(row["video_id"], {}).update({"SCRIPT_ARCHETYPE": row.get("script_archetype")})
    return context


def load_competitor_public_context(channel_ids, db_path=DB_PATH):
    context = {}
    uri = Path(db_path).resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as conn:
        conn.row_factory = sqlite3.Row
        for channel_id in sorted(channel_ids or []):
            rows = conn.execute(
                "SELECT s.views,MAX(CASE WHEN c.classification_dimension='CONTENT_TOPIC' THEN c.classification_value END) topic,"
                "MAX(CASE WHEN c.classification_dimension='CONTENT_FORMAT' THEN c.classification_value END) format "
                "FROM videos v LEFT JOIN video_snapshots s ON s.video_snapshot_id=(SELECT x.video_snapshot_id FROM video_snapshots x WHERE x.video_id=v.video_id ORDER BY x.observed_at DESC,x.video_snapshot_id DESC LIMIT 1) "
                "LEFT JOIN content_classifications c ON c.video_id=v.video_id AND c.classification_status IN ('PROPOSED','VERIFIED') "
                "WHERE v.channel_id=? GROUP BY v.video_id", (channel_id,),
            ).fetchall()
            views = [row["views"] for row in rows if row["views"] is not None]
            context[channel_id] = {
                "PUBLIC_VIDEO_COUNT": len(rows), "PUBLIC_MEDIAN_VIEWS": statistics.median(views) if views else None,
                "PUBLIC_TOPICS": sorted({row["topic"] for row in rows if row["topic"]}),
                "PUBLIC_FORMATS": sorted({row["format"] for row in rows if row["format"]}),
            }
    return context


def load_knowledge_context():
    training_path = ROOT / "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json"
    official_path = ROOT / "data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md"
    training = json.loads(training_path.read_text(encoding="utf-8"))
    applicable = [row["RULE_ID"] for row in training.get("rules", []) if row.get("DOMAIN") in {"TOPIC", "PACKAGING", "HOOK", "SCRIPT", "STRATEGY"}]
    return {
        "OFFICIAL_PRIMARY_EVIDENCE": {
            "PATH": str(official_path.relative_to(ROOT)), "SHA256": hashlib.sha256(official_path.read_bytes()).hexdigest(),
            "USE": "PLATFORM_BEHAVIOR_GUARDRAILS_ONLY",
        },
        "TRAINING_HEURISTIC": {
            "PATH": str(training_path.relative_to(ROOT)), "SCHEMA_VERSION": training.get("schema_version"),
            "APPLICABLE_RULE_IDS": applicable,
            "USE": "DIAGNOSTIC_LENSES_ONLY_NOT_PLATFORM_FACTS",
        },
    }


def _merge_payloads(payloads):
    if not payloads:
        raise DiagnosisError("at least one normalized analytics artifact is required")
    channels = {payload.get("CHANNEL_ID") for payload in payloads}
    ownership = {payload.get("CHANNEL_OWNERSHIP_CONTEXT") for payload in payloads}
    if len(channels) != 1 or ownership != {"FIRST_PARTY"}:
        raise DiagnosisError("analytics artifacts must belong to one FIRST_PARTY canonical channel")
    snapshots = [snapshot for payload in payloads for snapshot in payload.get("SNAPSHOTS", [])]
    snapshot_ids = [snapshot.get("ANALYTICS_SNAPSHOT_ID") for snapshot in snapshots]
    if len(snapshot_ids) != len(set(snapshot_ids)):
        raise DiagnosisError("duplicate analytics snapshot identity")
    return next(iter(channels)), snapshots


def _plain_metric(metric):
    return not metric.get("DIMENSIONS") or set(metric["DIMENSIONS"]) <= {"DATE", "TRAFFIC_SOURCE", "FORMAT"}


def _cohort_key(metric, public_context):
    context = public_context.get(metric.get("VIDEO_ID"), {})
    dimensions = metric.get("DIMENSIONS", {})
    return (
        metric.get("DATE_START"), metric.get("DATE_END"), metric.get("DATE_RANGE_KIND"),
        dimensions.get("FORMAT") or context.get("FORMAT", "UNKNOWN"),
        dimensions.get("TRAFFIC_SOURCE") or "ALL_TRAFFIC",
    )


def _values_by_video(metrics, public_context):
    grouped = defaultdict(lambda: defaultdict(list))
    for metric in metrics:
        if metric.get("VIDEO_ID") and _plain_metric(metric):
            grouped[(metric["VIDEO_ID"], _cohort_key(metric, public_context))][metric["METRIC_NAME"]].append(metric)
    return grouped


def _median_map(grouped, metric_name):
    by_cohort = defaultdict(list)
    for (video_id, cohort), metrics in grouped.items():
        if metric_name in metrics:
            by_cohort[cohort].append(metrics[metric_name][-1]["METRIC_VALUE"])
    return {cohort: statistics.median(values) for cohort, values in by_cohort.items() if len(values) >= 2}


def _band(value, median):
    return None if value is None or median is None else ("HIGH" if value >= median else "LOW")


def _single(metrics, name):
    values = metrics.get(name, [])
    return values[-1]["METRIC_VALUE"] if values else None


def _packaging_label(impressions_band, ctr_band):
    if not impressions_band or not ctr_band:
        return "INSUFFICIENT_CONTEXT"
    return f"{impressions_band}_IMPRESSIONS_{ctr_band}_CTR"


def _intro_label(ctr_band, intro_band):
    if not ctr_band or not intro_band:
        return "INSUFFICIENT_CONTEXT"
    return f"{'STRONG' if ctr_band == 'HIGH' else 'WEAK'}_PACKAGE_{'STRONG' if intro_band == 'HIGH' else 'WEAK'}_INTRO"


def _action(packaging_label, ctr_band, intro_band):
    if ctr_band == "HIGH" and intro_band == "LOW":
        return {"ACTION_TYPE": "FIX", "TARGET": "INTRO"}
    if packaging_label == "HIGH_IMPRESSIONS_LOW_CTR":
        return {"ACTION_TYPE": "FIX", "TARGET": "PACKAGE"}
    if packaging_label == "LOW_IMPRESSIONS_HIGH_CTR":
        return {"ACTION_TYPE": "WATCH", "TARGET": "IMPRESSION_OPPORTUNITY"}
    if packaging_label == "HIGH_IMPRESSIONS_HIGH_CTR" and intro_band == "HIGH":
        return {"ACTION_TYPE": "DOUBLE_DOWN", "TARGET": "PACKAGE_AND_INTRO_PATTERN"}
    if packaging_label == "LOW_IMPRESSIONS_LOW_CTR":
        return {"ACTION_TYPE": "TEST", "TARGET": "TOPIC_AND_PACKAGE"}
    return {"ACTION_TYPE": "WATCH", "TARGET": "EVIDENCE_GAP"}


def _issues(packaging_label, ctr_band, intro_band, metrics):
    issues = []
    if packaging_label == "HIGH_IMPRESSIONS_LOW_CTR":
        issues.append("WEAK_PACKAGING_RESPONSE")
    elif packaging_label == "LOW_IMPRESSIONS_HIGH_CTR":
        issues.append("LOW_IMPRESSION_OPPORTUNITY")
    elif packaging_label == "LOW_IMPRESSIONS_LOW_CTR":
        issues.append("TOPIC_DEMAND_OR_PACKAGING_RESPONSE")
    if ctr_band == "HIGH" and intro_band == "LOW":
        issues.append("HOOK_INTRO_DROP")
    if not issues:
        issues.append("INSUFFICIENT_EVIDENCE" if packaging_label == "INSUFFICIENT_CONTEXT" else "NO_SUPPORTED_FAILURE_CAUSE")
    return issues


def _confidence(metrics):
    groups = [
        bool(set(metrics) & {"IMPRESSIONS", "IMPRESSIONS_CTR"}),
        bool(set(metrics) & {"INTRO_30S_PERCENTAGE", "RETENTION_PERCENTAGE"}),
        bool(set(metrics) & {"WATCH_TIME_HOURS", "AVERAGE_VIEW_DURATION", "AVERAGE_PERCENTAGE_VIEWED"}),
    ]
    count = sum(groups)
    return "HIGH" if count == 3 else "MEDIUM" if count == 2 else "LOW"


def _confidence_explanation(metrics):
    present = []
    if set(metrics) & {"IMPRESSIONS", "IMPRESSIONS_CTR"}:
        present.append("PACKAGE_RESPONSE")
    if set(metrics) & {"INTRO_30S_PERCENTAGE", "RETENTION_PERCENTAGE"}:
        present.append("RETENTION")
    if set(metrics) & {"WATCH_TIME_HOURS", "AVERAGE_VIEW_DURATION", "AVERAGE_PERCENTAGE_VIEWED"}:
        present.append("WATCH_ENGAGEMENT")
    return f"{len(present)} of 3 first-party evidence dimensions present ({', '.join(present) or 'none'}); association only."


def _traffic_diagnosis(metrics):
    by_metric = {"VIEWS": defaultdict(float), "WATCH_TIME_HOURS": defaultdict(float)}
    for metric in metrics:
        source = metric.get("DIMENSIONS", {}).get("TRAFFIC_SOURCE")
        if source and metric["METRIC_NAME"] in {"VIEWS", "WATCH_TIME_HOURS"}:
            by_metric[metric["METRIC_NAME"]][source] += metric["METRIC_VALUE"]
    basis = "VIEWS" if by_metric["VIEWS"] else "WATCH_TIME_HOURS"
    values = by_metric[basis]
    total = sum(values.values())
    if not total:
        return "INSUFFICIENT_DATA", [], None
    ranked = sorted(values.items(), key=lambda row: (-row[1], row[0]))
    source, value = ranked[0]
    if value <= total / 2:
        return "MIXED", ranked, basis
    known = {
        "YouTube Search": "SEARCH_LED", "Browse features": "BROWSE_LED",
        "Suggested videos": "SUGGESTED_LED", "Shorts feed": "SHORTS_FEED_LED",
    }
    return known.get(source, f"{source.upper().replace(' ', '_')}_LED"), ranked, basis


def _audience_diagnosis(metrics):
    totals = defaultdict(float)
    for metric in metrics:
        if metric["METRIC_NAME"] in {"NEW_VIEWERS", "CASUAL_VIEWERS", "REGULAR_VIEWERS", "RETURNING_VIEWERS"}:
            totals[metric["METRIC_NAME"]] += metric["METRIC_VALUE"]
    if not totals.get("NEW_VIEWERS") or not totals.get("REGULAR_VIEWERS"):
        return "INSUFFICIENT_DATA", dict(totals)
    if totals["NEW_VIEWERS"] > totals["REGULAR_VIEWERS"]:
        return "NEW_VIEWER_LED", dict(totals)
    if totals["REGULAR_VIEWERS"] > totals["NEW_VIEWERS"]:
        return "LOYALTY_LED", dict(totals)
    return "BALANCED", dict(totals)


def _window_days(metric):
    try:
        start = datetime.fromisoformat(metric.get("DATE_START", "")).date()
        end = datetime.fromisoformat(metric.get("DATE_END", "")).date()
    except (TypeError, ValueError):
        return None
    return (end - start).days + 1


def _longitudinal_trajectories(metrics):
    groups = defaultdict(list)
    for metric in metrics:
        days = _window_days(metric)
        if days is None:
            continue
        key = (
            metric.get("VIDEO_ID"), metric["METRIC_NAME"], metric["UNIT"],
            metric.get("DATE_RANGE_KIND"), metric.get("DATE_GRANULARITY"), days,
            json.dumps(metric.get("DIMENSIONS", {}), sort_keys=True),
        )
        groups[key].append(metric)
    trajectories = []
    for key, rows in groups.items():
        points = sorted({
            (row["DATE_START"], row["DATE_END"], row["ANALYTICS_SNAPSHOT_ID"], row["METRIC_VALUE"])
            for row in rows
        })
        if len(points) < 2:
            continue
        changes = []
        for previous, current in zip(points, points[1:]):
            delta = current[3] - previous[3]
            changes.append({
                "FROM_SNAPSHOT": previous[2], "TO_SNAPSHOT": current[2], "DELTA": delta,
                "DIRECTION": "UP" if delta > 0 else "DOWN" if delta < 0 else "UNCHANGED",
            })
        trajectories.append({
            "VIDEO_ID": key[0], "METRIC_NAME": key[1], "UNIT": key[2],
            "DATE_RANGE_KIND": key[3], "DATE_GRANULARITY": key[4], "WINDOW_DAYS": key[5],
            "DIMENSIONS": json.loads(key[6]),
            "POINTS": [{"DATE_START": row[0], "DATE_END": row[1], "SNAPSHOT_ID": row[2], "VALUE": row[3]} for row in points],
            "CHANGES": changes,
        })
    return sorted(trajectories, key=lambda row: (row["VIDEO_ID"] or "", row["METRIC_NAME"], json.dumps(row["DIMENSIONS"], sort_keys=True)))


def build_diagnosis(payload, public_context=None, competitor_ids=None, generated_at=None,
                    source_artifacts=None, competitor_context=None, knowledge_context=None):
    payloads = payload if isinstance(payload, list) else [payload]
    channel_id, snapshots = _merge_payloads(payloads)
    public_context = public_context if public_context is not None else load_public_context(channel_id)
    metrics = [metric for snapshot in snapshots for metric in snapshot.get("METRICS", [])]
    grouped = _values_by_video(metrics, public_context)
    medians = {name: _median_map(grouped, name) for name in ("IMPRESSIONS", "IMPRESSIONS_CTR", "INTRO_30S_PERCENTAGE")}
    rows = []
    for (video_id, cohort), video_metrics in sorted(grouped.items()):
        impressions = _single(video_metrics, "IMPRESSIONS")
        ctr = _single(video_metrics, "IMPRESSIONS_CTR")
        intro = _single(video_metrics, "INTRO_30S_PERCENTAGE")
        impressions_band = _band(impressions, medians["IMPRESSIONS"].get(cohort))
        ctr_band = _band(ctr, medians["IMPRESSIONS_CTR"].get(cohort))
        intro_band = _band(intro, medians["INTRO_30S_PERCENTAGE"].get(cohort))
        packaging_label = _packaging_label(impressions_band, ctr_band)
        names = sorted(video_metrics)
        missing = sorted({
            "IMPRESSIONS", "IMPRESSIONS_CTR", "INTRO_30S_PERCENTAGE",
            "AVERAGE_PERCENTAGE_VIEWED", "TRAFFIC_SOURCE", "AUDIENCE_SEGMENTS",
        } - set(names))
        counter = []
        if packaging_label == "HIGH_IMPRESSIONS_LOW_CTR" and public_context.get(video_id, {}).get("PUBLIC_VIEWS"):
            counter.append("HIGH_PUBLIC_VIEWS_DO_NOT_ESTABLISH_STRONG_PACKAGING_RESPONSE")
        if packaging_label == "LOW_IMPRESSIONS_HIGH_CTR":
            counter.append("STRONG_RELATIVE_CTR_HAS_LOW_IMPRESSION_VOLUME")
        rows.append({
            "VIDEO_ID": video_id, "COHORT": {
                "DATE_START": cohort[0], "DATE_END": cohort[1], "DATE_RANGE_KIND": cohort[2],
                "FORMAT": cohort[3], "TRAFFIC_SOURCE": cohort[4],
            },
            "PACKAGING_DIAGNOSIS": packaging_label,
            "INTRO_DIAGNOSIS": _intro_label(ctr_band, intro_band),
            "LIKELY_ISSUES": _issues(packaging_label, ctr_band, intro_band, video_metrics),
            "ENGAGEMENT_DIMENSIONS": {name: _single(video_metrics, name) for name in (
                "WATCH_TIME_HOURS", "AVERAGE_VIEW_DURATION", "AVERAGE_PERCENTAGE_VIEWED", "RETENTION_PERCENTAGE"
            ) if name in video_metrics},
            "ACTION": _action(packaging_label, ctr_band, intro_band),
            "ACTION_REASON": _issues(packaging_label, ctr_band, intro_band, video_metrics),
            "PUBLIC_EVIDENCE": public_context.get(video_id, {}),
            "FIRST_PARTY_EVIDENCE": [{"METRIC": name, "VALUE": _single(video_metrics, name), "UNIT": video_metrics[name][-1]["UNIT"]} for name in names],
            "COMPETITOR_EVIDENCE": [{"CHANNEL_ID": value, "EVIDENCE": "PUBLIC_ONLY"} for value in sorted(competitor_ids or [])],
            "COUNTER_EVIDENCE": counter, "CONFIDENCE": _confidence(video_metrics),
            "CONFIDENCE_EXPLANATION": _confidence_explanation(video_metrics),
            "MISSING_EVIDENCE": missing,
            "CONCLUSION_TYPE": "OBSERVED_FIRST_PARTY_ASSOCIATION",
        })
    traffic_status, traffic_values, traffic_basis = _traffic_diagnosis(metrics)
    audience_status, audience_values = _audience_diagnosis(metrics)
    trajectories = _longitudinal_trajectories(metrics)
    first_party_names = sorted({metric["METRIC_NAME"] for metric in metrics} | ({"TRAFFIC_SOURCE"} if any(metric.get("DIMENSIONS", {}).get("TRAFFIC_SOURCE") for metric in metrics) else set()) | ({"SEARCH_TERM"} if any(metric.get("DIMENSIONS", {}).get("SEARCH_TERM") for metric in metrics) else set()))
    competitor_context = competitor_context or {}
    knowledge_context = knowledge_context or {}
    generated_at = generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": SCHEMA_VERSION, "generated_at": generated_at,
        "CHANNEL_ID": channel_id, "CHANNEL_OWNERSHIP_CONTEXT": "FIRST_PARTY",
        "ANALYTICS_SNAPSHOT_IDS": sorted(snapshot["ANALYTICS_SNAPSHOT_ID"] for snapshot in snapshots),
        "SOURCE_ANALYTICS_ARTIFACTS": sorted(source_artifacts or []),
        "REPORT_TYPES": sorted({snapshot["REPORT_TYPE"] for snapshot in snapshots}),
        "VIDEO_DIAGNOSES": rows,
        "TRAFFIC_SOURCE_DIAGNOSIS": traffic_status,
        "TRAFFIC_SOURCE_BASIS_METRIC": traffic_basis,
        "TRAFFIC_SOURCE_EVIDENCE": [{"SOURCE": key, "VALUE": value} for key, value in traffic_values],
        "SEARCH_TERM_EVIDENCE": sorted({metric["DIMENSIONS"]["SEARCH_TERM"] for metric in metrics if metric.get("DIMENSIONS", {}).get("SEARCH_TERM")}),
        "AUDIENCE_SEGMENT_DIAGNOSIS": audience_status, "AUDIENCE_SEGMENT_EVIDENCE": audience_values,
        "AUDIENCE_SEGMENT_NOTE": "New, casual, regular, and returning viewer measures are audience segments, not direct ranking signals.",
        "RETENTION_SUPPORT": {
            "CURVE_POINTS_PRESERVED": sum(metric["METRIC_NAME"] == "RETENTION_PERCENTAGE" and bool(metric.get("DIMENSIONS", {}).get("ELAPSED_VIDEO_TIME")) for metric in metrics),
            "INTRO_30S_VALUES": sum(metric["METRIC_NAME"] == "INTRO_30S_PERCENTAGE" for metric in metrics),
            "TRANSCRIPT_INFERENCE_USED": False,
        },
        "LONGITUDINAL_FIRST_PARTY_TREND": "AVAILABLE" if trajectories else "NOT_AVAILABLE",
        "LONGITUDINAL_TRAJECTORIES": trajectories,
        "OWN_VS_COMPETITOR": {
            "OWN_CHANNEL": channel_id, "SELECTED_COMPETITORS": sorted(competitor_ids or []),
            "SHARED_PUBLIC_DIMENSIONS": sorted({"FORMAT", "PUBLIC_VIEWS", "TOPIC"}),
            "COMPETITOR_PUBLIC_EVIDENCE": competitor_context,
            "PRIVATE_ONLY_DIMENSIONS": sorted(PRIVATE_METRICS & set(first_party_names)),
            "COMPETITOR_PRIVATE_METRICS": "NOT_AVAILABLE",
            "RULE": "Competitor comparison uses shared public dimensions only; private first-party evidence remains separate.",
        },
        "EVIDENCE_CLASSES": {
            "FIRST_PARTY_EVIDENCE": {"SNAPSHOT_IDS": sorted(snapshot["ANALYTICS_SNAPSHOT_ID"] for snapshot in snapshots)},
            "CORPUS_EVIDENCE": {"OWN_PUBLIC": bool(public_context), "COMPETITOR_PUBLIC": sorted(competitor_context)},
            **knowledge_context,
        },
        "METHODOLOGY": {
            "CTR_THRESHOLD": "CHANNEL_FORMAT_DATE_RANGE_RELATIVE_MEDIAN",
            "PERIOD_COMPARISON": "ONLY_EQUAL_DATE_RANGE_KIND_AND_FORMAT",
            "CAUSAL_CLAIMS": "NOT_MADE", "ENGAGEMENT_SCORE": "NOT_CREATED",
            "CTR_NOTE": "CTR is interpreted only with impressions inside comparable channel, format, and date-range cohorts.",
        },
    }


def build_from_paths(paths, competitor_ids=None, generated_at=None, db_path=DB_PATH):
    resolved = [Path(path).resolve() for path in paths]
    payloads = [json.loads(path.read_text(encoding="utf-8")) for path in resolved]
    if not payloads:
        raise DiagnosisError("at least one normalized analytics artifact is required")
    channel_id = payloads[0].get("CHANNEL_ID")
    public_context = enrich_with_existing_intelligence(channel_id, load_public_context(channel_id, db_path))
    return build_diagnosis(
        payloads, public_context, competitor_ids, generated_at,
        [str(path) for path in resolved], load_competitor_public_context(competitor_ids, db_path),
        load_knowledge_context(),
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analytics", action="append", required=True)
    parser.add_argument("--competitor", action="append")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    report = build_from_paths(args.analytics, args.competitor)
    version = hashlib.sha256("|".join(report["ANALYTICS_SNAPSHOT_IDS"]).encode()).hexdigest()[:12]
    output = Path(args.output) if args.output else OUTPUT_ROOT / report["CHANNEL_ID"] / f"first-party-channel-diagnosis-{datetime.now(timezone.utc).date().isoformat()}-{version}.json"
    if output.exists():
        raise FileExistsError(f"diagnosis artifact already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
