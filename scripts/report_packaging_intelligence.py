#!/usr/bin/env python3
"""Build channel-scoped packaging intelligence from canonical topic evidence."""

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from report_common import connect


WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)?")
NUMBER_RE = re.compile(
    r"\d|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|"
    r"hundred|thousand|million|billion|trillion)\b",
    re.I,
)
COMPARISON_RE = re.compile(r"\b(?:versus|vs\.?|than|compared|instead|or)\b|%", re.I)
WARNING_RE = re.compile(
    r"\b(?:warning|risks?|danger|dangerous|mistakes?|worst|never|avoid|regret|"
    r"fail|broke|wrong|backfire|silent|quiet signs?|do not|don['’]t)\b",
    re.I,
)
CONSEQUENCE_RE = re.compile(
    r"\b(?:what happens?|what would|result|after|before|leads? to|"
    r"changes?|ends?|costs?|affects?|predicts?)\b",
    re.I,
)
EXTREME_RE = re.compile(
    r"\b(?:all|every|entire|largest|fastest|highest|lowest|billion|trillion|"
    r"never|worst|best|perfect|zero|million|literally|most|least)\b",
    re.I,
)
AUDIENCE_RE = re.compile(
    r"\b(?:age[sd]?|after|before|over|under)\s*\d+\b|\b(?:senior|retiree|"
    r"parent|couple|people|person|beginner|owner|adult|child|teen)\w*\b",
    re.I,
)
FIRST_PERSON_RE = re.compile(r"\b(?:i|me|my|mine|we|us|our|ours)\b", re.I)
SECOND_PERSON_RE = re.compile(r"\b(?:you|your|yours)\b", re.I)

BOOLEAN_FEATURES = (
    "question_form", "statement_form", "has_number", "has_entity_candidate",
    "extreme_condition", "comparison", "warning_or_risk",
    "consequence_framing", "audience_or_life_stage", "curiosity_framing",
    "parenthetical", "first_person", "second_person",
)

ARCHETYPE_DEFINITIONS = {
    "QUESTION": "Title directly asks a question.",
    "NUMBERED_SPECIFICITY": "Title uses a number or quantified promise.",
    "WARNING_OR_RISK": "Title foregrounds risk, error, warning, or avoidance.",
    "COMPARISON_OR_CHOICE": "Title contrasts options or asks a choice.",
    "EXPLANATORY": "Title begins with why, how, or what and promises explanation.",
    "DIRECT_STATEMENT": "Declarative title without another dominant structural pattern.",
}

LIMITATIONS = [
    "Public performance associations are observational and do not establish causality.",
    "No impressions, CTR, watch time, retention, traffic source, subscriber conversion, unique viewers, or audience overlap.",
    "Current thumbnails are not historical package evidence unless independently proven.",
    "Long-form and Shorts remain separate; format transfer is not assumed.",
]


def extract_title_features(title):
    title = title or ""
    words = WORD_RE.findall(title)
    question = "?" in title
    entities = [
        word for index, word in enumerate(words)
        if index > 0 and word[:1].isupper() and word.lower() not in
        {"a", "an", "and", "are", "at", "but", "for", "if", "in", "is", "of", "on", "or", "the", "to", "what", "when", "which", "why"}
    ]
    return {
        "character_length": len(title),
        "word_count": len(words),
        "question_form": question,
        "statement_form": bool(title) and not question,
        "has_number": bool(NUMBER_RE.search(title)),
        "capitalized_entity_candidates": entities,
        "has_entity_candidate": bool(entities),
        "extreme_condition": bool(EXTREME_RE.search(title)),
        "comparison": bool(COMPARISON_RE.search(title)),
        "warning_or_risk": bool(WARNING_RE.search(title)),
        "consequence_framing": bool(CONSEQUENCE_RE.search(title)),
        "audience_or_life_stage": bool(AUDIENCE_RE.search(title)),
        "curiosity_framing": question or bool(re.match(r"^(?:why|how|what|when|which)\b", title, re.I)),
        "specificity": "HIGH" if NUMBER_RE.search(title) or entities else "MEDIUM" if len(words) >= 6 else "LOW",
        "question_marks": title.count("?"),
        "exclamation_marks": title.count("!"),
        "colon_count": title.count(":"),
        "dash_count": len(re.findall(r"[-–—]", title)),
        "parenthetical": bool(re.search(r"\([^)]*\)", title)),
        "first_person": bool(FIRST_PERSON_RE.search(title)),
        "second_person": bool(SECOND_PERSON_RE.search(title)),
    }


def title_archetype(title):
    features = extract_title_features(title)
    if features["warning_or_risk"]:
        return "WARNING_OR_RISK"
    if features["comparison"]:
        return "COMPARISON_OR_CHOICE"
    if features["has_number"]:
        return "NUMBERED_SPECIFICITY"
    if re.match(r"^(?:why|how|what|when|which)\b", title or "", re.I):
        return "EXPLANATORY"
    if features["question_form"]:
        return "QUESTION"
    return "DIRECT_STATEMENT"


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
        "performance_band": metrics.get("performance_band"),
        "topic_family": metrics.get("topic_family"),
        "published_at": metrics.get("published_at"),
        "age_days": metrics.get("age_days"),
        "transcript_status": metrics.get("transcript_status"),
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
    if high >= 2 and high / len(measured) >= 0.5:
        return "REPEATABLE_PATTERN"
    if low >= 2 and low / len(measured) >= 0.5:
        return "LOW_ASSOCIATION"
    return "MIXED_PATTERN"


def aggregate_title_archetypes(items):
    groups = defaultdict(list)
    for item in items:
        groups[item["title_archetype"]].append(item)
    rows = []
    for archetype_id, members in sorted(groups.items()):
        ranked = sorted(
            members,
            key=lambda row: row["channel_median_ratio"] if row["channel_median_ratio"] is not None else float("-inf"),
            reverse=True,
        )
        rows.append({
            "archetype_id": archetype_id,
            "definition": ARCHETYPE_DEFINITIONS[archetype_id],
            "evidence_state": "OBSERVATION",
            "item_count": len(members),
            "supporting_video_ids": sorted(row["video_id"] for row in members),
            "format_mix": dict(sorted(Counter(row["format"] for row in members).items())),
            "median_normalized_performance": _median(row["views_per_day"] for row in members),
            "median_channel_relative_performance": _median(row["channel_median_ratio"] for row in members),
            "strong_examples": [row["video_id"] for row in ranked[:3]],
            "counter_examples": [row["video_id"] for row in ranked[-3:]],
            "repeatability": _repeatability(members),
            "confidence": "HIGH" if len(members) >= 10 else "MEDIUM" if len(members) >= 3 else "LOW",
        })
    return rows


def summarize_title_features(items):
    return [{
        "feature": feature,
        "evidence_state": "DERIVED_METRIC",
        "item_count": len(members),
        "frequency": round(len(members) / len(items), 4) if items else None,
        "median_normalized_performance": _median(row["views_per_day"] for row in members),
        "median_channel_relative_performance": _median(row["channel_median_ratio"] for row in members),
        "format_mix": dict(sorted(Counter(row["format"] for row in members).items())),
    } for feature in BOOLEAN_FEATURES for members in [[row for row in items if row["features"][feature]]]]


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


def validate_visual_annotations(rows, canonical_video_ids):
    for row in rows:
        if row.get("video_id") not in canonical_video_ids:
            raise ValueError("unknown canonical video")
        if row.get("interpretation_state") != "AI_INTERPRETATION":
            raise ValueError("visual judgment must be AI_INTERPRETATION")
        if row.get("temporal_alignment_state") != "TEMPORAL_ALIGNMENT_UNKNOWN":
            raise ValueError("unsupported historical temporal state")
        if row.get("format") not in {"LONG_FORM", "SHORTS", "UNCLASSIFIED"}:
            raise ValueError("invalid format")
    return rows


def normalize_candidate(candidate):
    angle = re.sub(
        r"^Source-derived concept represented by VID-[^:]+:\s*", "",
        candidate["specific_angle"], flags=re.I,
    )
    return {
        "candidate_id": candidate.get("candidate_id") or candidate.get("opportunity_id"),
        "topic": candidate["topic"],
        "specific_angle": angle,
        "supporting_video_ids": candidate["supporting_video_ids"],
        "performance_signal": candidate.get("performance_signal") or candidate.get("internal_performance"),
        "counter_evidence": candidate.get("counter_evidence") or "; ".join(candidate.get("risks", [])),
        "initial_confidence": candidate.get("initial_confidence") or candidate.get("confidence", "LOW"),
    }


def select_candidates(topic):
    rows = topic.get("internal_candidates") or topic.get("final_opportunities") or topic.get("candidate_opportunities") or []
    return [normalize_candidate(row) for row in rows[:2]]


def generate_package_hypotheses(channel_id, candidate, canonical_video_ids, visual_video_ids=(), format_name="LONG_FORM"):
    support = sorted(set(candidate["supporting_video_ids"]) & set(canonical_video_ids))
    visual_support = sorted(set(support) & set(visual_video_ids))
    if not support:
        raise ValueError("candidate lacks canonical video support")
    topic = candidate["topic"].strip()
    angle = candidate["specific_angle"].strip().rstrip(".")
    candidate_id = candidate["candidate_id"]
    base_id = candidate_id if candidate_id.startswith(channel_id + "-") else f"{channel_id}-{candidate_id}"
    variants = [
        ("A", "QUESTION", f"What Should You Know About {topic}?", "One concrete subject with a single unresolved question.", "SINGLE_HERO", "QUESTION_PLUS_VISUAL_SETUP"),
        ("B", "EXPLANATORY", angle[:1].upper() + angle[1:], "Two concrete states showing the decision or contrast.", "COMPARISON_LAYOUT", "TITLE_ADDS_CONTEXT"),
        ("C", "WARNING_OR_RISK", f"What Changes the Outcome for {topic}?", "One consequence scene showing stakes without claiming certainty.", "CONSEQUENCE_SCENE", "TITLE_ADDS_STAKES"),
    ]
    return [{
        "package_id": f"{base_id}-PKG-{suffix}",
        "evidence_state": "HYPOTHESIS_FOR_TESTING",
        "title": title,
        "title_archetype": title_type,
        "thumbnail_concept": thumbnail,
        "thumbnail_archetype": thumbnail_type,
        "pair_relationship": relationship,
        "format_context": format_name,
        "native_ab_eligible": "NO" if format_name == "SHORTS" else "YES",
        "historical_support": {
            "video_ids": support,
            "performance_signal": candidate["performance_signal"],
        },
        "visual_support": {
            "state": "CHANNEL_VISUAL_PRECEDENT" if visual_support else "THUMBNAIL_REFERENCE_GAP",
            "video_ids": visual_support,
            "causal_claim": False,
        },
        "risks": ["Generated direction requires factual review before production.", "No causal performance claim."],
        "counter_evidence": candidate["counter_evidence"],
        "confidence": candidate["initial_confidence"],
    } for suffix, title_type, title, thumbnail, thumbnail_type, relationship in variants]


def derive_thumbnail_archetypes(visual_rows):
    patterns = [
        ("TEXT_LED", "Text is a dominant visual element.", lambda row: row.get("approx_text_amount") == "HIGH"),
        ("PERSON_LED", "Person or face is a primary visual element.", lambda row: row.get("human_face_present") or row.get("human_figure_present")),
        ("SINGLE_HERO", "One dominant visual subject.", lambda row: row.get("single_hero")),
        ("COMPARISON_LAYOUT", "Two states or objects are compared.", lambda row: row.get("comparison_layout") or row.get("split_layout")),
        ("CONSEQUENCE_SCENE", "Visual depicts a result, risk, or aftermath.", lambda row: row.get("consequence_scene")),
        ("DIAGRAM_OR_ILLUSTRATION", "Diagram or illustration carries the concept.", lambda row: row.get("diagram_style") or row.get("illustration_style")),
        ("PHOTO_SCENE", "Photographic scene carries the concept.", lambda row: row.get("photo_style")),
    ]
    rows = []
    for archetype_id, definition, predicate in patterns:
        members = [row for row in visual_rows if predicate(row)]
        if len(members) < 2:
            continue
        rows.append({
            "archetype_id": archetype_id,
            "definition": definition,
            "item_count": len(members),
            "video_ids": sorted(row["video_id"] for row in members),
            "format_distribution": dict(sorted(Counter(row["format"] for row in members).items())),
            "evidence_state": "AI_INTERPRETATION",
            "temporal_alignment": "TEMPORAL_ALIGNMENT_UNKNOWN",
            "performance_association": {
                "state": "ASSOCIATED_PATTERN",
                "median_channel_relative_performance": _median(row.get("channel_median_ratio") for row in members),
                "causal_claim": False,
            },
            "counter_examples": sorted(
                row["video_id"] for row in visual_rows if not predicate(row)
            )[:3],
            "repeatability": "REPEATABLE_PATTERN" if len(members) >= 3 else "INSUFFICIENT_SAMPLE",
            "confidence": "HIGH" if len(members) >= 10 else "MEDIUM",
        })
    return sorted(rows, key=lambda row: (-row["item_count"], row["archetype_id"]))[:5]


def derive_pair_archetypes(visual_rows):
    groups = defaultdict(list)
    for row in visual_rows:
        groups[row.get("pair_relationship", "OTHER")].append(row)
    rows = []
    for index, (relationship, members) in enumerate(sorted(groups.items()), 1):
        ranked = sorted(
            members,
            key=lambda row: row.get("channel_median_ratio") if row.get("channel_median_ratio") is not None else float("-inf"),
            reverse=True,
        )
        title_patterns = Counter(row.get("title_archetype", "UNKNOWN") for row in members)
        thumbnail_patterns = Counter(
            "TEXT_LED" if row.get("approx_text_amount") == "HIGH"
            else "SINGLE_HERO" if row.get("single_hero")
            else "MULTI_OBJECT"
            for row in members
        )
        rows.append({
        "archetype_id": f"PAIR-{index:03d}",
        "title_pattern": title_patterns.most_common(1)[0][0],
        "thumbnail_pattern": thumbnail_patterns.most_common(1)[0][0],
        "pair_relationship": relationship,
        "item_count": len(members),
        "video_ids": sorted(row["video_id"] for row in members),
        "format": dict(sorted(Counter(row["format"] for row in members).items())),
        "performance_association": {
            "state": "ASSOCIATED_PATTERN",
            "median_normalized_performance": _median(row.get("views_per_day") for row in members),
            "median_channel_relative_performance": _median(row.get("channel_median_ratio") for row in members),
            "causal_claim": False,
        },
        "temporal_alignment": "TEMPORAL_ALIGNMENT_UNKNOWN",
        "counter_examples": [row["video_id"] for row in ranked[-3:]],
        "repeatability": "REPEATABLE_PATTERN" if len(members) >= 3 else "INSUFFICIENT_SAMPLE",
        "confidence": "HIGH" if len(members) >= 10 else "MEDIUM" if len(members) >= 3 else "LOW",
        })
    return rows


def build_report(topic, acquisition=None, visual_annotations=None, registered_thumbnail_urls=None):
    items = topic.get("items", [])
    title_items = [
        title_item(
            row["canonical_fact"]["video_id"], row["canonical_fact"]["title"],
            row["canonical_fact"].get("format", "UNCLASSIFIED"),
            row["derived_metric"].get("channel_median_ratio"),
            views=row["canonical_fact"].get("views"),
            views_per_day=row["derived_metric"].get("views_per_day"),
            family_median_ratio=row["derived_metric"].get("family_median_ratio"),
            performance_band=row["observation"].get("performance_band"),
            topic_family=row["observation"].get("topic_family"),
            published_at=row["canonical_fact"].get("published_at"),
            age_days=row["derived_metric"].get("age_days"),
            transcript_status=row["canonical_fact"].get("transcript_status"),
        ) for row in items
    ]
    canonical_ids = {row["video_id"] for row in title_items}
    if acquisition and acquisition.get("channel_id") != topic["channel"]["channel_id"]:
        raise ValueError("acquisition manifest channel does not match topic artifact")
    if acquisition:
        unknown_snapshots = {
            row.get("video_id") for row in acquisition.get("snapshots", [])
        } - canonical_ids
        if unknown_snapshots:
            raise ValueError("acquisition manifest contains unknown canonical video")
    visual_rows = validate_visual_annotations(visual_annotations or [], canonical_ids)
    visual_video_ids = {row["video_id"] for row in visual_rows}
    title_by_id = {row["video_id"]: row for row in title_items}
    for row in visual_rows:
        title = title_by_id[row["video_id"]]
        row.update({
            "title_archetype": title["title_archetype"],
            "views_per_day": title["views_per_day"],
            "channel_median_ratio": title["channel_median_ratio"],
            "performance_association_state": "ASSOCIATED_PATTERN",
        })
    candidates = select_candidates(topic)
    formats = topic["evidence_snapshot"].get("formats", {"UNCLASSIFIED": 0})
    default_format = max(formats, key=formats.get)
    packages = [{
        "candidate": candidate,
        "recommended_test_set": generate_package_hypotheses(
            topic["channel"]["channel_id"], candidate, canonical_ids, visual_video_ids, default_format
        ),
    } for candidate in candidates]
    acquired = acquisition or {}
    registered_urls = acquired.get("registered_urls", 0) if registered_thumbnail_urls is None else registered_thumbnail_urls
    thumbnail_state = (
        "CURRENT_REMOTE_SNAPSHOT" if acquired.get("successful_images")
        else "REGISTERED_REFERENCE_ONLY" if registered_urls
        else "THUMBNAIL_REFERENCE_GAP"
    )
    return {
        "schema_version": "packaging-intelligence-1",
        "generated_on": "2026-09-10",
        "channel": topic["channel"],
        "evidence_snapshot": {
            "metric_cutoff": topic["evidence_snapshot"].get("metric_cutoff"),
            "canonical_item_count": len(items),
            "titles_accounted_for": sum(bool(row["title"]) for row in title_items),
            "transcripts_available": topic["evidence_snapshot"].get("transcripts_available"),
            "formats": topic["evidence_snapshot"].get("formats"),
            "registered_thumbnail_urls": registered_urls,
            "acquired_thumbnails": acquired.get("successful_images", 0),
            "thumbnail_evidence_state": thumbnail_state,
        },
        "title_features": title_items,
        "title_feature_summary": summarize_title_features(title_items),
        "title_archetypes": aggregate_title_archetypes(title_items),
        "archetype_scope": "PACKAGE_ARCHETYPE" if visual_rows else "TITLE_ONLY_ARCHETYPE",
        "thumbnail_snapshots": [{
            key: row.get(key) for key in (
                "video_id", "format", "original_registered_url", "url_recorded_at",
                "retrieval_timestamp", "final_url", "redirect_chain", "mime_type",
                "byte_size", "width", "height", "aspect_ratio", "sha256",
                "evidence_state", "temporal_alignment_state",
            )
        } for row in acquired.get("snapshots", [])],
        "visual_features": visual_rows,
        "thumbnail_archetypes": derive_thumbnail_archetypes(visual_rows),
        "package_archetypes": derive_pair_archetypes(visual_rows),
        "opportunity_packages": packages,
        "temporal_alignment": {
            "verified_historical_pairs": 0,
            "current_snapshot_pairs": len(visual_rows),
            "state": "TEMPORAL_ALIGNMENT_UNKNOWN" if visual_rows else "NO_THUMBNAIL_EVIDENCE",
        },
        "guardrails": {
            "packaging_model": "PACKAGE -> VIEWER_RESPONSE -> POSSIBLE_PERFORMANCE_CHANGE",
            "direct_algorithm_bonus_claimed": False,
            "causal_claims_created": 0,
            "historical_causal_package_analysis": "NOT_SUPPORTED",
            "all_recommendations": "HYPOTHESIS_FOR_TESTING",
            "prohibited_outputs": ["CTR_SCORE", "PACKAGE_SUCCESS_SCORE", "PREDICTED_CTR", "PREDICTED_WINNER"],
        },
        "limitations": LIMITATIONS,
        "provenance": {
            "topic_artifact_schema": topic.get("schema_version"),
            "acquisition_manifest_present": bool(acquisition),
            "visual_review_state": "AI_INTERPRETATION" if visual_rows else "NOT_AVAILABLE",
        },
    }


def build_items_from_db(conn, topic):
    cutoff = topic["evidence_snapshot"]["metric_cutoff"]
    cutoff_dt = datetime.fromisoformat(cutoff.replace("Z", "+00:00"))
    channel_id = topic["channel"]["channel_id"]
    rows = conn.execute(
        """WITH latest AS (
               SELECT vs.*, ROW_NUMBER() OVER (
                 PARTITION BY vs.video_id ORDER BY vs.observed_at DESC, vs.video_snapshot_id DESC
               ) rank
               FROM video_snapshots vs JOIN videos v ON v.video_id=vs.video_id
               WHERE v.channel_id=?
           )
           SELECT * FROM latest WHERE rank=1 ORDER BY video_id""",
        (channel_id,),
    ).fetchall()
    velocities = []
    prepared = []
    for row in rows:
        published = datetime.fromisoformat(row["published_at"].replace("Z", "+00:00"))
        if published.tzinfo is None and cutoff_dt.tzinfo is not None:
            published = published.replace(tzinfo=cutoff_dt.tzinfo)
        age_days = max((cutoff_dt - published).total_seconds() / 86400, 1)
        velocity = row["views"] / age_days if row["views"] is not None else None
        velocities.append(velocity)
        prepared.append((row, age_days, velocity))
    median_velocity = statistics.median(value for value in velocities if value is not None)
    return [{
        "canonical_fact": {
            "video_id": row["video_id"], "title": row["title"],
            "format": "SHORTS" if (row["video_type"] or "").lower() == "shorts" else "LONG_FORM",
            "views": row["views"], "published_at": row["published_at"],
            "transcript_status": "AVAILABLE" if row["transcript_word_count"] else "MISSING",
        },
        "derived_metric": {
            "views_per_day": round(velocity, 4) if velocity is not None else None,
            "channel_median_ratio": round(velocity / median_velocity, 4) if velocity is not None and median_velocity else None,
            "family_median_ratio": None, "age_days": round(age_days, 4),
        },
        "observation": {
            "performance_band": "HIGH_RELATIVE_PERFORMER" if velocity >= median_velocity * 1.25 else "LOW_RELATIVE_PERFORMER" if velocity < median_velocity * 0.75 else "NORMAL_RANGE",
            "topic_family": "UNASSIGNED",
        },
    } for row, age_days, velocity in prepared]


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--topic-artifact", required=True)
    parser.add_argument("--acquisition-manifest")
    parser.add_argument("--visual-annotations")
    parser.add_argument("--db")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    topic_path = Path(args.topic_artifact)
    topic = json.loads(topic_path.read_text(encoding="utf-8"))
    if topic["channel"]["channel_id"] != args.channel:
        raise ValueError("topic artifact channel does not match --channel")
    if not topic.get("items"):
        with connect(args.db) as conn:
            topic["items"] = build_items_from_db(conn, topic)
    acquisition = json.loads(Path(args.acquisition_manifest).read_text()) if args.acquisition_manifest else None
    annotations = json.loads(Path(args.visual_annotations).read_text()) if args.visual_annotations else None
    with connect(args.db) as conn:
        registered_thumbnail_urls = conn.execute(
            "SELECT COUNT(DISTINCT vs.video_id) FROM video_snapshots vs "
            "JOIN videos v ON v.video_id=vs.video_id "
            "WHERE v.channel_id=? AND vs.thumbnail_url IS NOT NULL",
            (args.channel,),
        ).fetchone()[0]
    payload = build_report(topic, acquisition, annotations, registered_thumbnail_urls)
    payload["provenance"]["topic_artifact"] = str(topic_path)
    if args.acquisition_manifest:
        payload["provenance"]["acquisition_manifest"] = args.acquisition_manifest
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_json(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
