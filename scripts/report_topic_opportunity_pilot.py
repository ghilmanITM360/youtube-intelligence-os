#!/usr/bin/env python3
"""Read-only public-performance report for the CH-000003 opportunity pilot."""

import argparse
import json
import math
import re
import statistics
from datetime import datetime, timezone
from itertools import combinations

from report_common import connect


CHANNEL_ID = "CH-000003"
DATASET_ID = "DS-000006"
EXPECTED_ITEMS = 32
UNAVAILABLE_METRICS = {
    "ctr",
    "impressions",
    "retention",
    "watch_time",
    "subscriber_conversion",
    "traffic_sources",
}
TITLE_STOPWORDS = {"a", "after", "and", "for", "in", "of", "on", "the", "to", "you", "your"}

# Derived channel-specific families. These do not replace catalog classifications.
TOPIC_FAMILY_BY_VIDEO = {
    "VID-000160": "FOOD_SAFETY_LONGEVITY",
    "VID-000161": "CARDIAC_WARNING_SELF_TESTS",
    "VID-000162": "MOBILITY_GAIT_FALL_PREVENTION",
    "VID-000163": "MOBILITY_GAIT_FALL_PREVENTION",
    "VID-000164": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000165": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000166": "FUNCTIONAL_AGING_SELF_ASSESSMENT",
    "VID-000167": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000168": "BLOOD_PRESSURE_LIFESTYLE_HOME",
    "VID-000169": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000170": "CARDIAC_WARNING_SELF_TESTS",
    "VID-000171": "BLOOD_PRESSURE_LIFESTYLE_HOME",
    "VID-000172": "BLOOD_PRESSURE_LIFESTYLE_HOME",
    "VID-000173": "METABOLIC_DIABETES",
    "VID-000174": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000175": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000176": "FUNCTIONAL_AGING_SELF_ASSESSMENT",
    "VID-000177": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000178": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000179": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000180": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000181": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000182": "FUNCTIONAL_AGING_SELF_ASSESSMENT",
    "VID-000183": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000184": "METABOLIC_DIABETES",
    "VID-000185": "MOBILITY_GAIT_FALL_PREVENTION",
    "VID-000186": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000187": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000188": "CARDIAC_WARNING_SELF_TESTS",
    "VID-000189": "BLOOD_PRESSURE_LIFESTYLE_HOME",
    "VID-000190": "BLOOD_PRESSURE_MEDICATION_SAFETY",
    "VID-000191": "BLOOD_PRESSURE_MEDICATION_SAFETY",
}


def parse_time(value):
    value = value.replace("Z", "+00:00")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def normalize_item(item, observed_at):
    """Return transparent public metrics; no private YouTube analytics."""
    result = dict(item)
    age_days = max(1.0, (parse_time(observed_at) - parse_time(item["published_at"])).total_seconds() / 86400)
    views = item["views"]
    result.update(
        age_days=round(age_days, 4),
        views_per_day=round(views / age_days, 4),
        like_rate=round(item["likes"] / views, 6) if views else None,
        comment_rate=round(item["comments"] / views, 6) if views else None,
    )
    return result


def robust_outlier_flags(values):
    """Apply 1.5 IQR Tukey fences to log1p velocity; preserve input order."""
    if len(values) < 4:
        return ["INSUFFICIENT_SAMPLE"] * len(values)
    logged = [math.log1p(value) for value in values]
    q1, _, q3 = statistics.quantiles(logged, n=4, method="inclusive")
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return ["NEGATIVE" if value < low else "POSITIVE" if value > high else "TYPICAL" for value in logged]


def require_exact_item_set(items, expected=EXPECTED_ITEMS):
    ids = [item["video_id"] for item in items]
    if len(ids) != expected or len(set(ids)) != expected:
        raise ValueError(f"expected {expected} unique items, found {len(ids)} rows / {len(set(ids))} unique")


def mean_title_token_jaccard(items):
    """Transparent lexical proxy for within-family semantic cohesion."""
    token_sets = [
        {token for token in re.findall(r"[a-z0-9]+", item.get("title", "").lower()) if token not in TITLE_STOPWORDS}
        for item in items
    ]
    pairs = list(combinations(token_sets, 2))
    if not pairs:
        return None
    similarities = [len(left & right) / len(left | right) if left | right else 1.0 for left, right in pairs]
    return round(statistics.mean(similarities), 4)


def aggregate_topic_families(items):
    grouped = {}
    for item in items:
        grouped.setdefault(item["family"], []).append(item)
    rows = []
    for family, members in grouped.items():
        ordered = sorted(members, key=lambda item: item["video_id"])
        velocities = [item["views_per_day"] for item in ordered]
        strongest = max(ordered, key=lambda item: item["views_per_day"])
        weakest = min(ordered, key=lambda item: item["views_per_day"])
        rows.append(
            {
                "family": family,
                "item_count": len(ordered),
                "video_ids": [item["video_id"] for item in ordered],
                "formats": sorted({item.get("format", "UNKNOWN") for item in ordered}),
                "median_views_per_day": round(statistics.median(velocities), 4),
                "mean_title_token_jaccard": mean_title_token_jaccard(ordered),
                "strongest_video_id": strongest["video_id"],
                "weakest_video_id": weakest["video_id"],
            }
        )
    return sorted(rows, key=lambda row: (-row["item_count"], row["family"]))


def render_json(payload):
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def load_items(conn, channel_id=CHANNEL_ID, dataset_id=DATASET_ID):
    rows = conn.execute(
        """
        SELECT v.video_id, v.youtube_video_id, v.channel_id, v.created_from_dataset_id,
               s.registration_run_id, s.observed_at, s.published_at, s.title,
               s.duration_seconds, s.views, s.likes, s.comments,
               topic.classification_value AS canonical_topic,
               format.classification_value AS format,
               t.availability_status AS transcript_status,
               t.word_count AS transcript_word_count,
               t.transcript_sha256, sf.canonical_path AS transcript_path
        FROM videos v
        JOIN video_snapshots s ON s.video_id = v.video_id AND s.dataset_id = ?
        LEFT JOIN content_classifications topic
          ON topic.video_id = v.video_id AND topic.classification_dimension = 'CONTENT_TOPIC'
         AND topic.classification_status IN ('PROPOSED', 'VERIFIED')
        LEFT JOIN content_classifications format
          ON format.video_id = v.video_id AND format.classification_dimension = 'CONTENT_FORMAT'
         AND format.classification_status IN ('PROPOSED', 'VERIFIED')
        LEFT JOIN transcripts t ON t.video_id = v.video_id AND t.dataset_id = ?
        LEFT JOIN source_files sf ON sf.file_id = t.archive_member_file_id
        WHERE v.channel_id = ?
        ORDER BY v.video_id
        """,
        (dataset_id, dataset_id, channel_id),
    ).fetchall()
    return [dict(row) for row in rows]


def build_report(conn, channel_id=CHANNEL_ID, dataset_id=DATASET_ID, expected=EXPECTED_ITEMS):
    source_items = load_items(conn, channel_id, dataset_id)
    require_exact_item_set(source_items, expected)
    if set(TOPIC_FAMILY_BY_VIDEO) != {item["video_id"] for item in source_items}:
        raise ValueError("derived topic-family map does not exactly cover canonical item set")
    observed_values = {item["observed_at"] for item in source_items}
    if len(observed_values) != 1:
        raise ValueError(f"expected one metric cutoff, found {sorted(observed_values)}")
    observed_at = observed_values.pop()
    items = []
    for source in source_items:
        item = normalize_item(source, observed_at)
        item["family"] = TOPIC_FAMILY_BY_VIDEO[item["video_id"]]
        items.append(item)
    velocities = [item["views_per_day"] for item in items]
    channel_median = statistics.median(velocities)
    flags = robust_outlier_flags(velocities)
    family_medians = {
        row["family"]: row["median_views_per_day"] for row in aggregate_topic_families(items)
    }
    for item, flag in zip(items, flags):
        item["channel_outlier"] = flag
        item["channel_median_ratio"] = round(item["views_per_day"] / channel_median, 4)
        item["family_median_ratio"] = round(item["views_per_day"] / family_medians[item["family"]], 4)
    return {
        "channel": channel_id,
        "dataset": dataset_id,
        "metric_cutoff": observed_at,
        "item_count": len(items),
        "transcript_coverage": sum(item["transcript_status"] == "AVAILABLE" for item in items),
        "public_metrics": ["views", "likes", "comments", "duration_seconds", "published_at"],
        "unavailable_metrics": sorted(UNAVAILABLE_METRICS),
        "normalization": "views / max(age_days, 1); Tukey 1.5-IQR fences on log1p(views_per_day)",
        "channel_median_views_per_day": round(channel_median, 4),
        "topic_families": aggregate_topic_families(items),
        "items": items,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db")
    parser.add_argument("--channel", default=CHANNEL_ID)
    parser.add_argument("--dataset", default=DATASET_ID)
    args = parser.parse_args(argv)
    with connect(args.db) as conn:
        print(render_json(build_report(conn, args.channel, args.dataset)), end="")


if __name__ == "__main__":
    main()
