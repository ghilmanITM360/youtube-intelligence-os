#!/usr/bin/env python3
"""Build read-only, channel-scoped Topic Opportunity Intelligence from catalog evidence."""

import argparse
import json
import math
import re
import statistics
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

from report_common import connect


UNAVAILABLE_METRICS = {
    "audience_overlap",
    "ctr",
    "impressions",
    "retention",
    "subscriber_conversion",
    "traffic_sources",
    "unique_viewers",
    "watch_time",
}
STOPWORDS = {
    "a", "about", "actually", "after", "all", "also", "always", "an", "and", "answer", "are", "around", "as", "at", "be", "because", "before", "but",
    "by", "can", "caption", "channel", "com", "comments", "could", "count", "description", "did", "do", "does", "duration", "enough", "even", "for", "from", "get", "gets", "had", "has", "have", "how",
    "every", "first", "going", "here", "if", "in", "into", "is", "it", "its", "just", "let", "like", "more", "most", "no", "not", "now", "of", "on",
    "one", "or", "other", "our", "out", "over", "people", "pretty", "probably", "really", "say", "should", "so", "some", "something", "start", "than", "that", "the", "their", "them", "there", "these", "they", "thing", "things", "this", "time", "times", "transcript", "two",
    "to", "up", "use", "very", "video", "was", "we", "were", "what", "when", "where", "which", "who", "why",
    "will", "with", "would", "you", "your",
}
PATTERN_MARKERS = {
    "audience_problem": {"danger", "difficult", "failure", "mistake", "problem", "risk", "struggle", "worry"},
    "comparison": {"better", "compare", "difference", "less", "more", "versus", "vs", "worse"},
    "decision": {"choose", "decision", "option", "plan", "should"},
    "life_stage": {"age", "aging", "early", "later", "old", "older"},
    "misconception": {"false", "lie", "myth", "wrong"},
    "question": {"can", "could", "how", "what", "when", "where", "which", "who", "why", "would"},
    "warning": {"avoid", "danger", "never", "risk", "warning", "worst"},
}


def parse_time(value):
    if not value:
        raise ValueError("missing timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def normalize_item(item, observed_at):
    """Add public, age-normalized observations without inventing missing metrics."""
    result = dict(item)
    try:
        age_days = max(1.0, (parse_time(observed_at) - parse_time(item.get("published_at"))).total_seconds() / 86400)
        status = "NORMALIZED_FROM_REGISTERED_OBSERVATION"
    except (TypeError, ValueError):
        age_days = None
        status = "INVALID_PUBLISHED_AT"
    views = item.get("views")
    likes = item.get("likes")
    comments = item.get("comments")
    result.update(
        age_days=round(age_days, 4) if age_days is not None else None,
        views_per_day=round(views / age_days, 4) if views is not None and age_days is not None else None,
        like_rate=round(likes / views, 6) if likes is not None and views else None,
        comment_rate=round(comments / views, 6) if comments is not None and views else None,
        normalization_status=status,
    )
    return result


def robust_outlier_flags(values):
    """Return Tukey 1.5-IQR bands on log1p velocity, preserving input order."""
    valid = [value for value in values if value is not None and value >= 0]
    if len(valid) < 4:
        return ["INSUFFICIENT_SAMPLE" if value is not None else "METRIC_UNAVAILABLE" for value in values]
    logged = [math.log1p(value) for value in valid]
    q1, _, q3 = statistics.quantiles(logged, n=4, method="inclusive")
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    flags = []
    for value in values:
        if value is None:
            flags.append("METRIC_UNAVAILABLE")
        elif math.log1p(value) < low:
            flags.append("NEGATIVE_OUTLIER")
        elif math.log1p(value) > high:
            flags.append("POSITIVE_OUTLIER")
        else:
            flags.append("NORMAL_RANGE")
    return flags


def words(value):
    return [token for token in re.findall(r"[a-z0-9]+", (value or "").lower()) if len(token) > 2 and token[0].isalpha() and token not in STOPWORDS]


def phrases(value):
    tokens = words(value)
    return set(tokens) | {" ".join(tokens[index:index + 2]) for index in range(len(tokens) - 1)}


def family_key(value):
    return re.sub(r"[^A-Z0-9]+", "_", value.upper()).strip("_") or "UNCLASSIFIED"


def assign_topic_families(items):
    """Assign one derived family per item from recurring title evidence."""
    document_frequency = Counter(feature for item in items for feature in phrases(item.get("title")))
    maximum_frequency = max(2, math.floor(len(items) * 0.6))
    eligible = {
        feature: count for feature, count in document_frequency.items()
        if 2 <= count <= maximum_frequency
    }
    for item in items:
        candidates = [feature for feature in phrases(item.get("title")) if feature in eligible]
        if candidates:
            selected = max(candidates, key=lambda feature: (len(feature.split()), eligible[feature], len(feature), feature))
            source = "RECURRING_TITLE_PHRASE"
        else:
            selected = (item.get("canonical_topic") or "UNCLASSIFIED").lower().replace("_", " ")
            source = "CANONICAL_TOPIC_FALLBACK"
        item["family_key"] = family_key(selected)
        item["topic_family"] = family_key(selected)
        item["family_derivation"] = source
    return items


def mean_title_token_jaccard(items):
    token_sets = [set(words(item.get("title"))) for item in items]
    pairs = combinations(token_sets, 2)
    similarities = [len(left & right) / len(left | right) if left | right else 1.0 for left, right in pairs]
    return round(statistics.mean(similarities), 4) if similarities else None


def repeatability(members, channel_median):
    velocities = [item["views_per_day"] for item in members if item.get("views_per_day") is not None]
    if len(velocities) < 3 or not channel_median:
        return "INSUFFICIENT_SAMPLE"
    median_ratio = statistics.median(velocities) / channel_median
    high_count = sum(value >= channel_median * 1.5 for value in velocities)
    extreme_count = sum(value >= channel_median * 3 for value in velocities)
    if median_ratio >= 1.5 and high_count >= 2:
        return "REPEATABLE_WINNER"
    if median_ratio < 0.67:
        return "WEAK_FAMILY"
    if extreme_count == 1 and median_ratio < 1.5:
        return "ONE_OFF_OUTLIER"
    return "MIXED_FAMILY"


def aggregate_topic_families(items, channel_median):
    grouped = defaultdict(list)
    for item in items:
        grouped[item["topic_family"]].append(item)
    rows = []
    for name, members in grouped.items():
        ordered = sorted(members, key=lambda item: item["video_id"])
        measured = [item for item in ordered if item.get("views_per_day") is not None]
        velocities = [item["views_per_day"] for item in measured]
        strongest = sorted(measured, key=lambda item: (-item["views_per_day"], item["video_id"]))[:3]
        weakest = sorted(measured, key=lambda item: (item["views_per_day"], item["video_id"]))[:3]
        latest = max((item.get("published_at") or "" for item in ordered), default="") or None
        family_median = statistics.median(velocities) if velocities else None
        transcript_frequency = Counter(
            token
            for item in ordered if item.get("transcript_text")
            for token in set(words(item["transcript_text"]))
        )
        rows.append({
            "evidence_state": "OBSERVATION",
            "topic_family": name,
            "family_key": ordered[0]["family_key"],
            "derivation": sorted({item["family_derivation"] for item in ordered}),
            "item_count": len(ordered),
            "video_ids": [item["video_id"] for item in ordered],
            "median_views_per_day": round(family_median, 4) if family_median is not None else None,
            "channel_median_ratio": round(family_median / channel_median, 4) if family_median is not None and channel_median else None,
            "strongest_examples": [{"video_id": item["video_id"], "views_per_day": item["views_per_day"]} for item in strongest],
            "weakest_examples": [{"video_id": item["video_id"], "views_per_day": item["views_per_day"]} for item in weakest],
            "latest_published_at": latest,
            "format_mix": dict(sorted(Counter(item.get("format") or "UNCLASSIFIED" for item in ordered).items())),
            "mean_title_token_jaccard": mean_title_token_jaccard(ordered),
            "recurring_transcript_terms": [
                {"term": term, "item_count": count}
                for term, count in sorted(transcript_frequency.items(), key=lambda pair: (-pair[1], pair[0]))
                if count >= 2
            ][:8],
            "repeatability": repeatability(ordered, channel_median),
        })
    return sorted(rows, key=lambda row: (-row["item_count"], row["topic_family"]))


def transcript_topic_patterns(items):
    available = [item for item in items if item.get("transcript_text")]
    document_frequency = Counter()
    marker_counts = Counter()
    for item in available:
        tokens = words(item["transcript_text"])
        raw_tokens = re.findall(r"[a-z0-9]+", item["transcript_text"].lower())
        token_set = set(tokens)
        document_frequency.update(token_set)
        for name, markers in PATTERN_MARKERS.items():
            marker_counts[name] += sum(raw_tokens.count(marker) for marker in markers)
    minimum = max(2, math.ceil(len(available) * 0.2)) if available else 2
    maximum = max(minimum, math.floor(len(available) * 0.85)) if available else 0
    recurring = [
        {"term": term, "item_count": count}
        for term, count in sorted(document_frequency.items(), key=lambda pair: (-pair[1], pair[0]))
        if minimum <= count <= maximum
    ][:20]
    return {
        "evidence_state": "OBSERVATION",
        "available_items": len(available),
        "method": "document frequency over supplied transcript tokens; lexical markers are discovery aids, not semantic facts",
        "recurring_terms": recurring,
        "pattern_marker_counts": dict(sorted(marker_counts.items())),
    }


def performance_band(flag, ratio):
    if flag in {"POSITIVE_OUTLIER", "NEGATIVE_OUTLIER", "METRIC_UNAVAILABLE", "INSUFFICIENT_SAMPLE"}:
        return flag
    if ratio is not None and ratio >= 1.5:
        return "HIGH_RELATIVE_PERFORMER"
    if ratio is not None and ratio <= 0.67:
        return "LOW_RELATIVE_PERFORMER"
    return "NORMAL_RANGE"


def internal_candidates(channel_id, items, families, limit=12):
    family_by_name = {family["topic_family"]: family for family in families}
    status_order = {"REPEATABLE_WINNER": 0, "MIXED_FAMILY": 1, "ONE_OFF_OUTLIER": 2, "INSUFFICIENT_SAMPLE": 3, "WEAK_FAMILY": 4}
    ordered = sorted(
        families,
        key=lambda family: (
            status_order[family["repeatability"]],
            -family["item_count"],
            -(family["channel_median_ratio"] or 0),
            family["topic_family"],
        ),
    )
    selected = ordered[:limit]
    if len(selected) < min(limit, len(items)):
        represented = {family["topic_family"] for family in selected}
        for item in sorted(items, key=lambda row: (-(row.get("views_per_day") or -1), row["video_id"])):
            if item["topic_family"] not in represented:
                selected.append(family_by_name[item["topic_family"]])
                represented.add(item["topic_family"])
            if len(selected) == limit:
                break
    candidates = []
    for index, family in enumerate(selected, 1):
        members = [item for item in items if item["topic_family"] == family["topic_family"]]
        strongest = max(members, key=lambda item: (item.get("views_per_day") or -1, item["video_id"]), default=None)
        ratio = family["channel_median_ratio"]
        if family["repeatability"] == "REPEATABLE_WINNER":
            confidence = "HIGH"
        elif family["item_count"] >= 2 and ratio is not None and ratio >= 1:
            confidence = "MEDIUM"
        else:
            confidence = "LOW"
        counter = {
            "REPEATABLE_WINNER": "Family signal remains observational; no private demand or causal data.",
            "ONE_OFF_OUTLIER": "One strong item does not establish repeatability.",
            "WEAK_FAMILY": "Family median trails channel median.",
            "INSUFFICIENT_SAMPLE": "Fewer than three measured family items.",
            "MIXED_FAMILY": "Family includes conflicting relative-performance evidence.",
        }[family["repeatability"]]
        candidates.append({
            "evidence_state": "HYPOTHESIS",
            "candidate_id": f"{channel_id}-CAND-{index:03d}",
            "channel_id": channel_id,
            "topic": family["family_key"].replace("_", " ").title(),
            "specific_angle": f"Source-derived concept represented by {strongest['video_id']}: {strongest['title']}" if strongest else "No measured exemplar",
            "topic_family": family["topic_family"],
            "supporting_video_ids": [entry["video_id"] for entry in family["strongest_examples"]],
            "performance_signal": f"Family median/channel median ratio: {ratio}" if ratio is not None else "Normalized views unavailable",
            "repeatability": family["repeatability"],
            "coverage_signal": "SPARSE" if family["item_count"] < 3 else "DENSE" if family["item_count"] >= 8 else "MODERATE",
            "counter_evidence": counter,
            "initial_confidence": confidence,
            "dimensions": {
                "internal_performance_signal": "HIGH" if ratio is not None and ratio >= 1.5 else "LOW" if ratio is not None and ratio < 0.67 else "MEDIUM",
                "repeatability": "HIGH" if family["repeatability"] == "REPEATABLE_WINNER" else "LOW" if family["repeatability"] in {"WEAK_FAMILY", "INSUFFICIENT_SAMPLE"} else "MEDIUM",
                "channel_fit": "HIGH" if family["item_count"] >= 3 else "MEDIUM" if family["item_count"] == 2 else "LOW",
                "coverage_gap": "HIGH" if family["item_count"] < 3 else "MEDIUM",
                "evidence_quality": "HIGH" if len(family["strongest_examples"]) >= 3 else "MEDIUM" if len(family["strongest_examples"]) == 2 else "LOW",
            },
        })
    return candidates


def read_transcript(item):
    if item.get("transcript_status") != "AVAILABLE":
        return None
    if item.get("transcript_path"):
        text = Path(item["transcript_path"]).read_text(encoding="utf-8", errors="replace")
        return clean_transcript(text)
    if item.get("transcript_archive_path") and item.get("transcript_member_path"):
        with zipfile.ZipFile(item["transcript_archive_path"]) as archive:
            text = archive.read(item["transcript_member_path"]).decode("utf-8", errors="replace")
            return clean_transcript(text)
    return None


def clean_transcript(text):
    """Remove supplied archive metadata/description wrapper when present."""
    parts = re.split(r"\n(?:CONTENT|TRANSCRIPT)\s*\n", text, maxsplit=1)
    return parts[-1]


def load_channel(conn, channel_id):
    row = conn.execute(
        """SELECT c.*, d.dataset_name, d.semantic_class, d.source_type, d.ingestion_mode,
                  d.status AS dataset_status,
                  a.apify_source_run_id, a.actor_run_id, a.run_status AS acquisition_status
           FROM channels c
           JOIN datasets d ON d.dataset_id = c.created_from_dataset_id
           LEFT JOIN apify_source_runs a ON a.dataset_id = d.dataset_id
           WHERE c.channel_id = ?""",
        (channel_id,),
    ).fetchone()
    if not row:
        raise ValueError(f"unknown canonical channel: {channel_id}")
    return dict(row)


def load_items(conn, channel_id, dataset_id):
    rows = conn.execute(
        """SELECT v.video_id, v.youtube_video_id, v.channel_id, v.created_from_dataset_id,
                  s.registration_run_id, s.observed_at, s.published_at, s.title,
                  s.duration_seconds, s.views, s.likes, s.comments,
                  COALESCE((SELECT classification_value FROM content_classifications c
                            WHERE c.video_id = v.video_id AND c.classification_dimension = 'CONTENT_TOPIC'
                              AND c.classification_status IN ('PROPOSED', 'VERIFIED')
                            ORDER BY CASE c.classification_status WHEN 'VERIFIED' THEN 0 ELSE 1 END, c.classification_id LIMIT 1), 'UNCLASSIFIED') AS canonical_topic,
                  COALESCE((SELECT classification_value FROM content_classifications c
                            WHERE c.video_id = v.video_id AND c.classification_dimension = 'CONTENT_FORMAT'
                              AND c.classification_status IN ('PROPOSED', 'VERIFIED')
                            ORDER BY CASE c.classification_status WHEN 'VERIFIED' THEN 0 ELSE 1 END, c.classification_id LIMIT 1), 'UNCLASSIFIED') AS format,
                  t.availability_status AS transcript_status, t.word_count AS transcript_word_count,
                  t.transcript_sha256,
                  sf.storage_kind AS transcript_storage_kind, sf.canonical_path AS transcript_path,
                  sf.archive_member_path AS transcript_member_path,
                  parent.canonical_path AS transcript_archive_path
           FROM videos v
           JOIN video_snapshots s ON s.video_id = v.video_id AND s.dataset_id = ?
           LEFT JOIN transcripts t ON t.video_id = v.video_id AND t.dataset_id = ?
           LEFT JOIN source_files sf ON sf.file_id = t.archive_member_file_id
           LEFT JOIN source_files parent ON parent.file_id = sf.parent_file_id
           WHERE v.channel_id = ?
           ORDER BY v.video_id""",
        (dataset_id, dataset_id, channel_id),
    ).fetchall()
    return [dict(row) for row in rows]


def metric_availability(items):
    metric_fields = ["views", "likes", "comments", "duration_seconds", "published_at", "observed_at"]
    return {
        metric: {"available": sum(item.get(metric) is not None for item in items), "total": len(items)}
        for metric in metric_fields
    }


def source_provenance(conn, channel, item_count):
    dataset_id = channel["created_from_dataset_id"]
    files = conn.execute(
        """SELECT storage_kind, file_role, verification_status, evidence_layer, COUNT(*) AS item_count
           FROM source_files WHERE dataset_id = ?
           GROUP BY storage_kind, file_role, verification_status, evidence_layer
           ORDER BY storage_kind, file_role""",
        (dataset_id,),
    ).fetchall()
    return {
        "evidence_state": "CANONICAL_FACT",
        "dataset_id": dataset_id,
        "dataset_name": channel["dataset_name"],
        "semantic_class": channel["semantic_class"],
        "source_type": channel["source_type"],
        "ingestion_mode": channel["ingestion_mode"],
        "dataset_status": channel["dataset_status"],
        "manifest": f"data/manifests/{dataset_id}.md",
        "source_acquisition": "DIRECT_APIFY" if channel.get("apify_source_run_id") else "SUPPLIED_REGISTERED_DATASET",
        "acquisition_run_id": channel.get("apify_source_run_id"),
        "actor_run_id": channel.get("actor_run_id"),
        "canonical_item_count": item_count,
        "source_file_summary": [dict(row) for row in files],
    }


def build_report(conn, channel_id, generated_on=None):
    channel = load_channel(conn, channel_id)
    dataset_id = channel["created_from_dataset_id"]
    source_items = load_items(conn, channel_id, dataset_id)
    if not source_items:
        raise ValueError(f"channel has no canonical items: {channel_id}")
    item_ids = [item["video_id"] for item in source_items]
    if len(item_ids) != len(set(item_ids)):
        raise ValueError(f"duplicate canonical item rows for {channel_id}")
    observed_values = {item["observed_at"] for item in source_items}
    if len(observed_values) != 1:
        raise ValueError(f"expected one registered observation cutoff for {channel_id}, found {sorted(observed_values)}")
    observed_at = observed_values.pop()
    items = []
    for source in source_items:
        item = normalize_item(source, observed_at)
        item["transcript_text"] = read_transcript(item)
        items.append(item)
    assign_topic_families(items)
    velocities = [item.get("views_per_day") for item in items]
    valid_velocities = [value for value in velocities if value is not None]
    channel_median = statistics.median(valid_velocities) if valid_velocities else None
    flags = robust_outlier_flags(velocities)
    for item, flag in zip(items, flags):
        ratio = item["views_per_day"] / channel_median if item.get("views_per_day") is not None and channel_median else None
        item["channel_median_ratio"] = round(ratio, 4) if ratio is not None else None
        item["performance_band"] = performance_band(flag, ratio)
    families = aggregate_topic_families(items, channel_median)
    family_medians = {family["topic_family"]: family["median_views_per_day"] for family in families}
    for item in items:
        family_median = family_medians[item["topic_family"]]
        item["family_median_ratio"] = round(item["views_per_day"] / family_median, 4) if item.get("views_per_day") is not None and family_median else None
    patterns = transcript_topic_patterns(items)
    candidates = internal_candidates(channel_id, items, families)
    formats = Counter(item.get("format") or "UNCLASSIFIED" for item in items)
    topics = Counter(item.get("canonical_topic") or "UNCLASSIFIED" for item in items)
    public_items = []
    for item in items:
        public_items.append({
            "canonical_fact": {
                "video_id": item["video_id"],
                "youtube_video_id": item["youtube_video_id"],
                "title": item["title"],
                "published_at": item["published_at"],
                "observed_at": item["observed_at"],
                "duration_seconds": item["duration_seconds"],
                "views": item["views"],
                "likes": item["likes"],
                "comments": item["comments"],
                "canonical_topic": item["canonical_topic"],
                "format": item["format"],
                "transcript_status": item["transcript_status"],
                "transcript_word_count": item["transcript_word_count"],
                "transcript_sha256": item["transcript_sha256"],
            },
            "derived_metric": {
                "age_days": item["age_days"],
                "views_per_day": item["views_per_day"],
                "like_rate": item["like_rate"],
                "comment_rate": item["comment_rate"],
                "channel_median_ratio": item["channel_median_ratio"],
                "family_median_ratio": item["family_median_ratio"],
                "normalization_status": item["normalization_status"],
            },
            "observation": {
                "topic_family": item["topic_family"],
                "family_derivation": item["family_derivation"],
                "performance_band": item["performance_band"],
            },
        })
    return {
        "schema_version": "topic-opportunity-1",
        "generated_on": generated_on or datetime.now(timezone.utc).date().isoformat(),
        "channel": {
            "evidence_state": "CANONICAL_FACT",
            "channel_id": channel_id,
            "display_name": channel["display_name"],
            "handle": channel["handle"],
            "dataset_id": dataset_id,
        },
        "provenance": source_provenance(conn, channel, len(items)),
        "evidence_snapshot": {
            "evidence_state": "CANONICAL_FACT",
            "metric_cutoff": observed_at,
            "canonical_item_count": len(items),
            "canonical_item_ids": item_ids,
            "transcripts_available": sum(item.get("transcript_status") == "AVAILABLE" for item in items),
            "transcript_words": sum(item.get("transcript_word_count") or 0 for item in items),
            "formats": dict(sorted(formats.items())),
            "canonical_topics": dict(sorted(topics.items())),
            "metric_availability": metric_availability(items),
            "unavailable_private_metrics": sorted(UNAVAILABLE_METRICS),
        },
        "normalization": {
            "evidence_state": "DERIVED_METRIC",
            "age": "registered observed_at minus published_at; minimum 1 day",
            "views_per_day": "views / age_days; observational heuristic, not intrinsic quality",
            "channel_relative": "views_per_day / channel median views_per_day",
            "outlier_rule": "Tukey 1.5-IQR fences on log1p(views_per_day), minimum n=4",
            "small_sample_fallback": "INSUFFICIENT_SAMPLE; relative bands omitted",
            "channel_median_views_per_day": round(channel_median, 4) if channel_median is not None else None,
            "composite_score": None,
        },
        "outliers": {
            "evidence_state": "OBSERVATION",
            "counts": dict(sorted(Counter(item["performance_band"] for item in items).items())),
            "positive_video_ids": [item["video_id"] for item in items if item["performance_band"] == "POSITIVE_OUTLIER"],
            "negative_video_ids": [item["video_id"] for item in items if item["performance_band"] == "NEGATIVE_OUTLIER"],
        },
        "topic_families": families,
        "transcript_topic_patterns": patterns,
        "internal_candidates": candidates,
        "items": public_items,
        "guardrails": {
            "evidence_state": "CANONICAL_FACT",
            "primary_validation": "data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md",
            "youtube_principles": [
                "Recommendations are personalized and recommendation surfaces differ.",
                "Interests across formats can inform recommendations, while viewer format preferences may differ.",
                "No single universal ranking metric is encoded.",
                "Content groups are analytical buckets, not documented algorithm buckets.",
                "Topic interest and competition are context, not hidden ranking weights.",
            ],
            "private_metrics_not_inferred": sorted(UNAVAILABLE_METRICS),
            "prohibited_scores": ["ALGORITHM_SCORE", "SUCCESS_PROBABILITY", "VIRAL_SCORE"],
            "classification_mutation": False,
            "candidate_status": "HYPOTHESIS_UNTIL_VALIDATED",
        },
    }


def build_cross_channel_comparison(reports):
    channels = {report["channel"]["channel_id"]: report for report in reports}
    pairs = []
    for left_id, right_id in combinations(sorted(channels), 2):
        left, right = channels[left_id], channels[right_id]
        left_families = {row["family_key"]: row for row in left["topic_families"]}
        right_families = {row["family_key"]: row for row in right["topic_families"]}
        shared = sorted(set(left_families) & set(right_families))
        left_terms = {row["term"] for row in left["transcript_topic_patterns"]["recurring_terms"]}
        right_terms = {row["term"] for row in right["transcript_topic_patterns"]["recurring_terms"]}
        pairs.append({
            "left_channel_id": left_id,
            "right_channel_id": right_id,
            "shared_topic_families": shared,
            "shared_recurring_transcript_terms": sorted(left_terms & right_terms),
            "shared_family_evidence": [
                {
                    "family_key": key,
                    left_id: {"item_count": left_families[key]["item_count"], "repeatability": left_families[key]["repeatability"]},
                    right_id: {"item_count": right_families[key]["item_count"], "repeatability": right_families[key]["repeatability"]},
                }
                for key in shared
            ],
            "warning": "Channel-relative metrics remain separate and are not pooled.",
        })
    return {
        "schema_version": "topic-opportunity-comparison-1",
        "evidence_state": "OBSERVATION",
        "channel_ids": sorted(channels),
        "pairwise_comparisons": pairs,
        "metric_pooling": False,
    }


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db")
    parser.add_argument("--channel", action="append")
    parser.add_argument("--compare", action="store_true")
    parser.add_argument("--generated-on")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    if not args.channel:
        parser.error("at least one --channel is required")
    with connect(args.db) as conn:
        reports = [build_report(conn, channel_id, args.generated_on) for channel_id in args.channel]
    payload = build_cross_channel_comparison(reports) if args.compare else reports[0] if len(reports) == 1 else reports
    rendered = render_json(payload)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
