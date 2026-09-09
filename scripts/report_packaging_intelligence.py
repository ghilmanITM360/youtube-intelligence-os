#!/usr/bin/env python3
"""Build deterministic, read-only historical packaging evidence from Topic Intelligence."""

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from report_common import connect


WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)?")
NUMBER_RE = re.compile(
    r"\d|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|"
    r"hundred|thousand|million|billion|trillion)\b",
    re.I,
)
EXTREME_RE = re.compile(
    r"\b(?:all|every|entirely|largest|fastest|highest|lowest|billion|trillion|"
    r"nanosecond|light speed|black hole|suddenly|last|no rules|world'?s?)\b",
    re.I,
)
COMPARISON_RE = re.compile(
    r"\b(?:versus|vs\.?|than|compared|except|half|instead|as an?|made of|turned into)\b|%",
    re.I,
)
CONTRADICTION_RE = re.compile(
    r"\b(?:but|except|actually|only|literally|no|without|impossible)\b", re.I
)
SCALE_RE = re.compile(
    r"\b(?:magnitude|scale|how (?:fast|high|long|many|much|detailed)|speed|"
    r"distance|size|largest|billion|percent)\b|%|\d",
    re.I,
)
CONSEQUENCE_RE = re.compile(
    r"\b(?:what would happen|would .* be like|if .* died|disappear|vanish|"
    r"stopped|went out|go out|survive|collapse|destroy)\b",
    re.I,
)
SCIENCE_TERMS = {
    "antimatter", "baseball", "climate", "computer", "dna", "earth",
    "earthquake", "electron", "energy", "hubble", "laser", "lightning",
    "mars", "microwave", "moon", "ocean", "planet", "power", "proton",
    "radiation", "radioactivity", "space", "sun", "water", "wikipedia",
}
FIRST_PERSON_RE = re.compile(r"\b(?:i|me|my|mine|we|us|our|ours)\b", re.I)
SECOND_PERSON_RE = re.compile(r"\b(?:you|your|yours)\b", re.I)

BOOLEAN_FEATURES = (
    "question_form", "statement_form", "what_if_construction", "has_number",
    "has_entity_candidate", "has_scientific_object", "extreme_condition",
    "comparison", "contradiction", "scale_magnitude_framing",
    "consequence_framing", "curiosity_gap", "parenthetical", "first_person",
    "second_person",
)

LIMITATIONS = [
    "One registered public-metric snapshot per item; no performance trajectory.",
    "No impressions, CTR, watch time, retention, traffic source, subscriber conversion, unique viewers, or audience overlap.",
    "Title associations are observational and confounded by topic, thumbnail, format, release context, and content.",
    "Registered thumbnail URLs are references, not locally preserved images; no visual attributes are inferred from them.",
    "Long-form and Shorts evidence remains separated; transfer between formats is unproven.",
]


def extract_title_features(title):
    title = title or ""
    words = WORD_RE.findall(title)
    lower_words = [word.lower().replace("’", "'") for word in words]
    question = title.rstrip().endswith("?")
    entity_candidates = [
        word for index, word in enumerate(words)
        if index > 0 and word[:1].isupper() and word.lower() not in {"all", "except", "if", "what", "which", "why", "would"}
    ]
    science = sorted({word for word in lower_words if word.rstrip("s") in SCIENCE_TERMS})
    return {
        "character_length": len(title),
        "word_count": len(words),
        "question_form": question,
        "statement_form": bool(title) and not question,
        "what_if_construction": bool(re.match(r"^what if\b", title, re.I)),
        "has_number": bool(NUMBER_RE.search(title)),
        "capitalized_entity_candidates": entity_candidates,
        "has_entity_candidate": bool(entity_candidates),
        "scientific_objects": science,
        "has_scientific_object": bool(science),
        "extreme_condition": bool(EXTREME_RE.search(title)),
        "comparison": bool(COMPARISON_RE.search(title)),
        "contradiction": bool(CONTRADICTION_RE.search(title)),
        "scale_magnitude_framing": bool(SCALE_RE.search(title)),
        "consequence_framing": bool(CONSEQUENCE_RE.search(title)),
        "curiosity_gap": question,
        "specificity": "HIGH" if NUMBER_RE.search(title) or science or entity_candidates else "MEDIUM" if len(words) >= 6 else "LOW",
        "question_marks": title.count("?"),
        "exclamation_marks": title.count("!"),
        "colon_count": title.count(":"),
        "dash_count": len(re.findall(r"[-–—]", title)),
        "parenthetical": bool(re.search(r"\([^)]*\)", title)),
        "first_person": bool(FIRST_PERSON_RE.search(title)),
        "second_person": bool(SECOND_PERSON_RE.search(title)),
    }


def title_archetype(title):
    lower = (title or "").lower()
    if lower.startswith("what if"):
        return "WHAT_IF_SCENARIO"
    if lower.startswith("how ") or lower.startswith("is there"):
        return "LIMIT_OR_MEASUREMENT"
    if lower.startswith(("could ", "can ", "would a", "would an")):
        return "FEASIBILITY_TEST"
    if lower.startswith("what would") or lower.startswith("if "):
        return "CONSEQUENCE_QUESTION"
    return "DIRECT_QUESTION_OR_STATEMENT"


def title_item(video_id, title, format_name, channel_median_ratio, **metrics):
    return {
        "video_id": video_id,
        "title": title,
        "format": format_name,
        "title_archetype": title_archetype(title),
        "features": extract_title_features(title),
        "views": metrics.get("views"),
        "views_per_day": metrics.get("views_per_day"),
        "channel_median_ratio": channel_median_ratio,
        "family_median_ratio": metrics.get("family_median_ratio"),
        "like_rate": metrics.get("like_rate"),
        "comment_rate": metrics.get("comment_rate"),
        "performance_band": metrics.get("performance_band"),
        "topic_family": metrics.get("topic_family"),
        "published_at": metrics.get("published_at"),
        "age_days": metrics.get("age_days"),
        "transcript_status": metrics.get("transcript_status"),
        "thumbnail_url": metrics.get("thumbnail_url"),
        "thumbnail_local_path": metrics.get("thumbnail_local_path"),
        "thumbnail_inspectable": bool(metrics.get("thumbnail_local_path")),
        "packaging_screenshot_evidence": False,
    }


def _median(values):
    values = [value for value in values if value is not None]
    return round(statistics.median(values), 4) if values else None


def _repeatability(members):
    measured = [row for row in members if row["channel_median_ratio"] is not None]
    if len(measured) < 3:
        return "INSUFFICIENT_SAMPLE"
    high = sum(row["channel_median_ratio"] >= 1.25 for row in measured)
    low = sum(row["channel_median_ratio"] < 0.75 for row in measured)
    if high >= 2 and high / len(measured) >= 0.5 and low / len(measured) < 0.25:
        return "REPEATED_HIGH_ASSOCIATION"
    if low >= 2 and low / len(measured) >= 0.5 and high / len(measured) < 0.25:
        return "REPEATED_LOW_ASSOCIATION"
    return "MIXED_ASSOCIATION"


def _performance_by_format(members):
    groups = defaultdict(list)
    for member in members:
        groups[member["format"]].append(member)
    return {
        format_name: {
            "item_count": len(rows),
            "median_raw_views": _median(row["views"] for row in rows),
            "median_views_per_day": _median(row["views_per_day"] for row in rows),
            "median_channel_relative_performance": _median(row["channel_median_ratio"] for row in rows),
        }
        for format_name, rows in sorted(groups.items())
    }


def aggregate_title_archetypes(items):
    groups = defaultdict(list)
    for item in items:
        groups[item["title_archetype"]].append(item)
    rows = []
    for archetype_id, members in sorted(groups.items()):
        ranked = sorted(
            members,
            key=lambda row: (row["channel_median_ratio"] is not None, row["channel_median_ratio"] or float("-inf")),
            reverse=True,
        )
        rows.append({
            "archetype_id": archetype_id,
            "definition": {
                "WHAT_IF_SCENARIO": "Counterfactual title beginning with 'What if'.",
                "LIMIT_OR_MEASUREMENT": "Question asks for a limit, duration, quantity, detail, or existence boundary.",
                "FEASIBILITY_TEST": "Could/Can/Would construction tests whether a premise works.",
                "CONSEQUENCE_QUESTION": "Title asks what follows from a stated condition.",
                "DIRECT_QUESTION_OR_STATEMENT": "Other direct question or declarative packaging.",
            }[archetype_id],
            "evidence_state": "OBSERVATION",
            "item_count": len(members),
            "supporting_video_ids": sorted(row["video_id"] for row in members),
            "median_raw_views": _median(row["views"] for row in members),
            "median_views_per_day": _median(row["views_per_day"] for row in members),
            "median_channel_relative_performance": _median(row["channel_median_ratio"] for row in members),
            "median_family_relative_performance": _median(row["family_median_ratio"] for row in members),
            "median_like_rate": _median(row["like_rate"] for row in members),
            "median_comment_rate": _median(row["comment_rate"] for row in members),
            "format_mix": dict(sorted(Counter(row["format"] for row in members).items())),
            "performance_by_format": _performance_by_format(members),
            "topic_contexts": sorted({row["topic_family"] for row in members if row["topic_family"]}),
            "strongest_examples": [row["video_id"] for row in ranked[:3]],
            "weakest_examples": [row["video_id"] for row in reversed(ranked[-3:])],
            "repeatability": _repeatability(members),
            "confidence": "HIGH" if len(members) >= 10 else "MEDIUM" if len(members) >= 3 else "LOW",
        })
    return rows


def summarize_title_features(items):
    summaries = []
    for feature in BOOLEAN_FEATURES:
        members = [row for row in items if row["features"][feature]]
        summaries.append({
            "feature": feature,
            "evidence_state": "DERIVED_METRIC",
            "item_count": len(members),
            "frequency": round(len(members) / len(items), 4) if items else None,
            "median_raw_views": _median(row["views"] for row in members),
            "median_views_per_day": _median(row["views_per_day"] for row in members),
            "median_channel_relative_performance": _median(row["channel_median_ratio"] for row in members),
            "format_mix": dict(sorted(Counter(row["format"] for row in members).items())),
            "performance_by_format": _performance_by_format(members),
        })
    return summaries


def thumbnail_record(video_id, url, local_path):
    if local_path and Path(local_path).is_file():
        return {
            "video_id": video_id,
            "thumbnail_url": url,
            "local_path": str(local_path),
            "inspectable": True,
            "visual_observation_status": "LOCAL_IMAGE_AVAILABLE",
        }
    return {
        "video_id": video_id,
        "thumbnail_url": url,
        "local_path": None,
        "inspectable": False,
        "visual_observation_status": "REMOTE_REFERENCE_ONLY" if url else "NOT_AVAILABLE",
    }


def recursive_keys(value):
    keys = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key).lower())
            keys.update(recursive_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(recursive_keys(child))
    return keys


def validate_package_evidence(packages, canonical_video_ids, title_archetype_ids):
    for package in packages:
        support = package.get("historical_support", {})
        unknown_videos = set(support.get("canonical_video_ids", ())) - set(canonical_video_ids)
        if unknown_videos:
            raise ValueError("unknown canonical video: " + ", ".join(sorted(unknown_videos)))
        unknown_archetypes = set(support.get("title_archetype_ids", ())) - set(title_archetype_ids)
        if unknown_archetypes:
            raise ValueError("unknown title archetype: " + ", ".join(sorted(unknown_archetypes)))
    return packages


def build_historical_report(conn, topic_artifact):
    topic_path = Path(topic_artifact)
    topic = json.loads(topic_path.read_text(encoding="utf-8"))
    channel = topic["channel"]
    canonical_items = topic["items"]
    video_ids = [row["canonical_fact"]["video_id"] for row in canonical_items]
    if len(video_ids) != len(set(video_ids)):
        raise ValueError("duplicate canonical video ID in Topic Intelligence artifact")
    placeholders = ",".join("?" for _ in video_ids)
    thumbnail_rows = conn.execute(
        "SELECT te.video_id, te.thumbnail_url FROM thumbnail_evidence te "
        "WHERE te.video_id IN ({}) "
        "ORDER BY te.video_id, te.observed_at DESC, te.thumbnail_evidence_id DESC".format(placeholders),
        video_ids,
    ).fetchall() if video_ids else []
    urls = {}
    for row in thumbnail_rows:
        urls.setdefault(row["video_id"], row["thumbnail_url"])
    thumbnails = [thumbnail_record(video_id, urls.get(video_id), None) for video_id in sorted(video_ids)]
    title_items = []
    for row in canonical_items:
        fact, metric, observation = row["canonical_fact"], row["derived_metric"], row["observation"]
        title_items.append(title_item(
            fact["video_id"], fact["title"], fact["format"], metric["channel_median_ratio"],
            views=fact["views"], views_per_day=metric["views_per_day"],
            family_median_ratio=metric["family_median_ratio"], like_rate=metric["like_rate"],
            comment_rate=metric["comment_rate"], performance_band=observation["performance_band"],
            topic_family=observation["topic_family"], published_at=fact["published_at"],
            age_days=metric["age_days"], transcript_status=fact["transcript_status"],
            thumbnail_url=urls.get(fact["video_id"]), thumbnail_local_path=None,
        ))
    inspectable = sum(row["inspectable"] for row in thumbnails)
    return {
        "schema_version": "packaging-intelligence-pilot-1",
        "channel": channel,
        "evidence_snapshot": {
            "evidence_state": "CANONICAL_FACT",
            "metric_cutoff": topic["evidence_snapshot"]["metric_cutoff"],
            "canonical_item_count": len(canonical_items),
            "titles_accounted_for": sum(bool(row["title"]) for row in title_items),
            "transcripts_available": topic["evidence_snapshot"]["transcripts_available"],
            "formats": topic["evidence_snapshot"]["formats"],
            "thumbnail_urls_registered": len(urls),
            "locally_preserved_thumbnails": inspectable,
            "inspectable_thumbnails": inspectable,
            "missing_thumbnail_references": len(canonical_items) - len(urls),
            "packaging_screenshot_evidence": 0,
        },
        "title_feature_method": {
            "evidence_state": "DERIVED_METRIC",
            "method": "Deterministic regex and token features over all canonical titles.",
            "causal_claim": False,
        },
        "title_feature_summary": summarize_title_features(title_items),
        "title_features": title_items,
        "title_archetypes": aggregate_title_archetypes(title_items),
        "thumbnail_features": thumbnails,
        "thumbnail_archetypes": [],
        "pair_patterns": [],
        "limitations": LIMITATIONS,
        "guardrails": {
            "evidence_states": ["CANONICAL_FACT", "DERIVED_METRIC", "OBSERVATION", "HYPOTHESIS"],
            "private_metrics_not_inferred": [
                "CTR", "impressions", "retention", "watch time", "traffic source",
                "subscriber conversion", "unique viewers", "audience overlap",
            ],
            "prohibited_outputs": ["CTR_SCORE", "ALGORITHM_PACKAGE_SCORE", "GUARANTEED_WINNER", "PREDICTED_CTR"],
            "format_transfer_assumed": False,
            "classification_mutation": False,
        },
        "provenance": {
            "topic_artifact": str(topic_path),
            "topic_artifact_schema": topic["schema_version"],
            "dataset_id": channel["dataset_id"],
            "thumbnail_reference_source": "thumbnail_evidence table; registered Apify URLs",
            "visual_observation_basis": "No local thumbnail files; no visual observations made.",
        },
    }


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic-artifact", required=True)
    parser.add_argument("--db")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    with connect(args.db) as conn:
        payload = build_historical_report(conn, args.topic_artifact)
    rendered = render_json(payload)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
