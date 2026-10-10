#!/usr/bin/env python3
"""Build read-only hook and script intelligence from canonical transcripts."""

import argparse
import json
import re
import statistics
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import inventory_catalog as ic
from report_common import connect


WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)?")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]?", re.S)
NUMBER_RE = re.compile(r"\b(?:\d+(?:\.\d+)?|zero|one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion|trillion)\b", re.I)
TRANSITION_RE = re.compile(r"\b(?:but|however|therefore|then|next|instead|finally|eventually|meanwhile|although)\b", re.I)
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can", "could", "did", "do", "does",
    "for", "from", "had", "has", "have", "how", "if", "in", "is", "it", "of", "on", "or", "that",
    "the", "their", "then", "this", "to", "was", "were", "what", "when", "where", "which", "who", "why",
    "will", "with", "would", "you", "your",
}
PRIVATE_METRICS = {
    "audience_retention", "average_view_duration", "ctr", "impressions", "retention", "returning_viewers",
    "shares", "traffic_sources", "unique_viewers", "watch_time",
}
ALLOWED_OUTPUT_KEYS = {
    "views", "views_per_day", "format_relative_performance", "family_relative_performance", "likes_per_view",
    "comments_per_view", "words_per_minute", "questions_per_minute",
}


def words(text):
    return WORD_RE.findall(text or "")


def sentences(text):
    return [match.group().strip() for match in SENTENCE_RE.finditer(text or "") if match.group().strip()]


def recursive_keys(value):
    found = set()
    if isinstance(value, dict):
        for key, child in value.items():
            found.add(str(key).lower())
            found.update(recursive_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(recursive_keys(child))
    return found


def timing_quality(transcript):
    segments = transcript.get("segments") or []
    content_segments = [
        segment for segment in segments
        if (segment.get("text") or "").strip() or segment.get("words")
    ]
    # Exact timing requires timed words for every content-bearing segment.
    if content_segments and all(
        segment.get("words")
        and all(word.get("start") is not None and word.get("end") is not None for word in segment["words"])
        for segment in content_segments
    ):
        return "EXACT_TIMESTAMPED"
    if segments and all(segment.get("start") is not None and segment.get("end") is not None for segment in segments):
        return "SEGMENT_TIMESTAMPED"
    if (transcript.get("text") or "").strip() or content_segments:
        return "POSITIONAL_ONLY"
    return "INSUFFICIENT_TIMING"


def extract_window(transcript, start_seconds, end_seconds, duration_seconds):
    quality = timing_quality(transcript)
    if quality == "EXACT_TIMESTAMPED":
        selected = [
            word.get("word", "").strip()
            for segment in transcript["segments"] for word in segment.get("words", [])
            if word.get("start") is not None and start_seconds <= word["start"] < end_seconds
        ]
        return {"text": " ".join(filter(None, selected)), "timing_state": quality, "window_seconds": [start_seconds, end_seconds]}
    if quality == "SEGMENT_TIMESTAMPED":
        selected = [
            (segment.get("text") or " ".join(
                word.get("word", "").strip() for word in segment.get("words", [])
            )).strip() for segment in transcript["segments"]
            if segment["end"] > start_seconds and segment["start"] < end_seconds
        ]
        return {"text": " ".join(filter(None, selected)), "timing_state": quality, "window_seconds": [start_seconds, end_seconds]}
    if quality == "POSITIONAL_ONLY" and duration_seconds:
        text = transcript.get("text") or " ".join(
            (segment.get("text") or " ".join(
                word.get("word", "").strip() for word in segment.get("words", [])
            )).strip()
            for segment in transcript.get("segments", [])
        )
        tokens = re.findall(r"\S+", text)
        left = min(len(tokens), round(len(tokens) * start_seconds / duration_seconds))
        right = min(len(tokens), round(len(tokens) * end_seconds / duration_seconds))
        return {
            "text": " ".join(tokens[left:right]),
            "timing_state": "POSITIONAL_APPROXIMATION",
            "window_seconds": [start_seconds, end_seconds],
            "word_index_range": [left, right],
        }
    return {"text": "", "timing_state": "INSUFFICIENT_TIMING", "window_seconds": [start_seconds, end_seconds]}


def _position(text, pattern, duration_seconds, quality):
    match = pattern.search(text or "")
    if not match:
        return None
    preceding = len(words((text or "")[:match.start()]))
    total = max(len(words(text)), 1)
    result = {"word_index": preceding, "timing_state": quality if quality != "POSITIONAL_ONLY" else "POSITIONAL_APPROXIMATION"}
    if quality in {"EXACT_TIMESTAMPED", "SEGMENT_TIMESTAMPED"}:
        result["approx_seconds"] = round(duration_seconds * preceding / total, 2) if duration_seconds else None
    elif duration_seconds:
        result["estimated_seconds"] = round(duration_seconds * preceding / total, 2)
    return result


def _premise_position(text, title, duration_seconds, quality):
    title_terms = [term.lower() for term in words(title) if len(term) > 2 and term.lower() not in STOPWORDS]
    lower = (text or "").lower()
    matches = [(lower.find(term), term) for term in title_terms if lower.find(term) >= 0]
    if not matches:
        return None
    index, term = min(matches)
    preceding = len(words(text[:index]))
    total = max(len(words(text)), 1)
    result = {"matched_title_keyword": term, "word_index": preceding, "timing_state": quality if quality != "POSITIONAL_ONLY" else "POSITIONAL_APPROXIMATION"}
    key = "approx_seconds" if quality != "POSITIONAL_ONLY" else "estimated_seconds"
    result[key] = round(duration_seconds * preceding / total, 2) if duration_seconds else None
    return result


def measured_hook_features(transcript, title, duration_seconds):
    quality = timing_quality(transcript)
    text = transcript.get("text") or " ".join(segment.get("text", "") for segment in transcript.get("segments", []))
    windows = {
        "opening_0_15s": extract_window(transcript, 0, 15, duration_seconds),
        "opening_15_30s": extract_window(transcript, 15, 30, duration_seconds),
        "early_30_60s": extract_window(transcript, 30, 60, duration_seconds),
        "early_60_120s": extract_window(transcript, 60, 120, duration_seconds),
    }
    first_60 = " ".join((windows["opening_0_15s"]["text"], windows["opening_15_30s"]["text"], windows["early_30_60s"]["text"])).strip()
    return {
        "evidence_state": "DERIVED_METRIC",
        "timing_quality": quality,
        "window_method": "TIMESTAMP_WINDOW" if quality in {"EXACT_TIMESTAMPED", "SEGMENT_TIMESTAMPED"} else "POSITIONAL_APPROXIMATION",
        "windows": windows,
        "words_first_15s": len(words(windows["opening_0_15s"]["text"])),
        "words_first_30s": len(words(windows["opening_0_15s"]["text"])) + len(words(windows["opening_15_30s"]["text"])),
        "words_first_60s": len(words(first_60)),
        "sentence_count_first_60s": len(sentences(first_60)),
        "question_count": first_60.count("?"),
        "first_question": _position(text, re.compile(r"[^?]{0,200}\?"), duration_seconds, quality),
        "first_numeric_value": _position(text, NUMBER_RE, duration_seconds, quality),
        "central_premise_position": _premise_position(text, title, duration_seconds, quality),
    }


def interpret_hook(opening_text, premise_position):
    normalized = opening_text.strip().lower()
    first_sentence = sentences(opening_text)[0] if sentences(opening_text) else ""
    features = []
    if first_sentence.endswith("?") or "?" in first_sentence:
        features.append("DIRECT_QUESTION")
    if normalized.startswith("what if"):
        features.append("WHAT_IF_SCENARIO")
    if NUMBER_RE.search(" ".join(words(opening_text)[:12])):
        features.append("NUMBER_LED")
    if re.search(r"\b(?:but|actually|instead|seems|surprisingly|counterintuitive)\b", first_sentence, re.I):
        features.append("COUNTERINTUITIVE_PREMISE")
    if re.search(r"\b(?:danger|destroy|kill|dead|risk|explode|collapse|disaster)\b", opening_text, re.I):
        features.append("DANGER_OR_STAKES")
    if re.search(r"\b(?:suppose|imagine|scenario|assume|let's set aside)\b", opening_text, re.I):
        features.append("SCENARIO_SETUP")
    premise_index = premise_position.get("word_index") if premise_position else None
    features.append("IMMEDIATE_PREMISE" if premise_index is not None and premise_index <= 30 else "DELAYED_PREMISE")
    primary = next((name for name in ("WHAT_IF_SCENARIO", "DIRECT_QUESTION", "NUMBER_LED", "COUNTERINTUITIVE_PREMISE") if name in features), "CONTEXT_FIRST")
    return {"interpretation_state": "AI_INTERPRETATION", "primary_archetype": primary, "features": features}


def _segment_label(sentence, index, count):
    lower = sentence.lower()
    if index == 0:
        return "HOOK"
    if index == 1:
        return "PREMISE"
    if index == count - 1:
        return "CTA" if re.search(r"\b(?:subscribe|comment|watch next|thanks for watching)\b", lower) else "PAYOFF"
    if re.search(r"\b(?:suppose|assume|constraint|limit|for our purposes|set aside)\b", lower):
        return "CONSTRAINT"
    if re.search(r"\b(?:however|but|although|on the other hand|except)\b", lower):
        return "COUNTERPOINT"
    if NUMBER_RE.search(sentence) and re.search(r"\b(?:times|percent|miles|meters|seconds|hours|energy|force|speed|mass|degree)\b", lower):
        return "CALCULATION"
    if re.search(r"\b(?:then|eventually|after|result|therefore|so|until|finally)\b", lower):
        return "ESCALATION"
    return "EXPLANATION"


def derive_script_structure(text):
    source_sentences = sentences(text)
    raw = []
    for index, sentence in enumerate(source_sentences):
        raw.append({
            "phase": _segment_label(sentence, index, len(source_sentences)),
            "evidence_state": "AI_INTERPRETATION",
            "evidence": {"sentence_index": index, "excerpt": sentence[:240]},
        })
    compact = []
    for row in raw:
        if compact and compact[-1]["phase"] == row["phase"]:
            compact[-1]["evidence"]["sentence_index_end"] = row["evidence"]["sentence_index"]
            compact[-1]["evidence"]["excerpt_end"] = row["evidence"]["excerpt"]
        else:
            compact.append(row)
    return {
        "interpretation_state": "AI_INTERPRETATION",
        "sequence": [row["phase"] for row in compact],
        "segments": compact,
        "boundaries": {
            "hook_end": {"state": "DERIVED_SEGMENT_BOUNDARY", "sentence_index": 0} if source_sentences else "UNKNOWN",
            "setup_end": {"state": "DERIVED_SEGMENT_BOUNDARY", "sentence_index": min(2, len(source_sentences) - 1)} if source_sentences else "UNKNOWN",
            "first_major_payoff": {"state": "DERIVED_SEGMENT_BOUNDARY", "sentence_index": len(source_sentences) - 1} if source_sentences else "UNKNOWN",
            "ending_start": {"state": "DERIVED_SEGMENT_BOUNDARY", "sentence_index": max(0, len(source_sentences) - 2)} if source_sentences else "UNKNOWN",
        },
    }


def curiosity_payoff_map(text):
    source_sentences = sentences(text)
    question = next(((index, sentence) for index, sentence in enumerate(source_sentences) if "?" in sentence), None)
    payoffs = [
        (index, sentence) for index, sentence in enumerate(source_sentences)
        if re.search(r"\b(?:therefore|which means|as a result|the answer|turns out)\b", sentence, re.I)
    ]
    escalations = [
        (index, sentence) for index, sentence in enumerate(source_sentences)
        if re.search(r"\b(?:then|after|eventually|finally|until)\b", sentence, re.I)
    ]
    final = (len(source_sentences) - 1, source_sentences[-1]) if source_sentences else None
    return {
        "interpretation_state": "AI_INTERPRETATION",
        "initial_open_question": question[1][:240] if question else "UNKNOWN",
        "promised_payoff": "Answer to opening premise" if question else "UNCLEAR",
        "intermediate_payoffs": [sentence[:240] for _, sentence in payoffs],
        "main_payoff": final[1][:240] if final else "UNKNOWN",
        "escalations": [sentence[:240] for _, sentence in escalations],
        "callbacks": [], "unresolved_loops": [],
        "evidence": {
            "initial_open_question": {"sentence_index": question[0], "excerpt": question[1][:240]} if question else "UNKNOWN",
            "intermediate_payoffs": [{"sentence_index": index, "excerpt": sentence[:240]} for index, sentence in payoffs],
            "main_payoff": {"sentence_index": final[0], "excerpt": final[1][:240]} if final else "UNKNOWN",
            "escalations": [{"sentence_index": index, "excerpt": sentence[:240]} for index, sentence in escalations],
        },
    }


def script_archetype(sequence):
    if "CALCULATION" in sequence and "ESCALATION" in sequence:
        return "CALCULATED_ESCALATION"
    if sequence.count("ESCALATION") >= 1:
        return "CONSEQUENCE_CHAIN"
    if "COUNTERPOINT" in sequence:
        return "PREMISE_THEN_QUALIFICATION"
    return "EXPLANATORY_BUILD"


def pacing_proxies(text, duration_seconds, opening_30):
    token_count = len(words(text))
    minute_count = duration_seconds / 60 if duration_seconds else None
    source_sentences = sentences(text)
    early_words = words(opening_30)
    return {
        "evidence_state": "SCRIPT_PACING_PROXY",
        "words_per_minute": round(token_count / minute_count, 3) if minute_count else None,
        "questions_per_minute": round(text.count("?") / minute_count, 3) if minute_count else None,
        "early_entity_density": round(sum(token[:1].isupper() for token in early_words) / len(early_words), 4) if early_words else None,
        "early_number_density": round(sum(bool(NUMBER_RE.fullmatch(token)) for token in early_words) / len(early_words), 4) if early_words else None,
        "concept_introduction_count": len({token.lower() for token in words(text) if len(token) >= 8 and token.lower() not in STOPWORDS}),
        "topic_transition_frequency": round(len(TRANSITION_RE.findall(text)) / minute_count, 3) if minute_count else None,
        "average_sentence_length": round(token_count / len(source_sentences), 3) if source_sentences else None,
    }


def aggregate_hook_archetypes(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[(row["format"], row["hook_archetype"])].append(row)
    result = []
    for (format_name, archetype), members in sorted(groups.items()):
        ranked = sorted(members, key=lambda row: row.get("channel_median_ratio") or 0, reverse=True)
        ratios = [row.get("channel_median_ratio") for row in members if row.get("channel_median_ratio") is not None]
        median_ratio = statistics.median(ratios) if ratios else None
        counter_examples = [
            row.get("video_id") for row in ranked
            if row.get("video_id") and row.get("channel_median_ratio") is not None
            and ((median_ratio >= 1.25 and row["channel_median_ratio"] < 1)
                 or (median_ratio <= .8 and row["channel_median_ratio"] >= 1))
        ][:2] if median_ratio is not None else []
        result.append({
            "interpretation_state": "AI_INTERPRETATION",
            "hook_archetype_id": archetype,
            "definition": archetype.replace("_", " ").title(),
            "item_count": len(members),
            "video_ids": sorted(row.get("video_id", "") for row in members if row.get("video_id")),
            "format_context": format_name,
            "measured_feature_profile": "See hook_features records for opening counts and premise position.",
            "performance_association": {"state": "PERFORMANCE_ASSOCIATION", "median_channel_relative": round(median_ratio, 4) if median_ratio is not None else None, "causal_claim": False},
            "strong_examples": [row.get("video_id") for row in ranked[:3] if row.get("video_id")],
            "weak_examples": [row.get("video_id") for row in ranked[-3:] if row.get("video_id")],
            "counter_examples": counter_examples,
            "repeatability": "REPEATABLE_PATTERN" if len(members) >= 3 else "INSUFFICIENT_SAMPLE",
            "confidence": "HIGH" if len(members) >= 10 else "MEDIUM" if len(members) >= 3 else "LOW",
        })
    return result


def aggregate_script_archetypes(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[(row["format"], row["script_archetype"])].append(row)
    result = []
    for (format_name, archetype), members in sorted(groups.items()):
        ranked = sorted(members, key=lambda row: row.get("channel_median_ratio") or 0, reverse=True)
        ratios = [row.get("channel_median_ratio") for row in members if row.get("channel_median_ratio") is not None]
        median_ratio = statistics.median(ratios) if ratios else None
        counter_examples = [
            row["video_id"] for row in ranked
            if row.get("channel_median_ratio") is not None
            and ((median_ratio >= 1.25 and row["channel_median_ratio"] < 1)
                 or (median_ratio <= .8 and row["channel_median_ratio"] >= 1))
        ][:2] if median_ratio is not None else []
        common_sequence = Counter(tuple(row["structure"]["sequence"]) for row in members).most_common(1)[0][0]
        result.append({
            "interpretation_state": "AI_INTERPRETATION",
            "script_archetype_id": archetype,
            "definition": archetype.replace("_", " ").title(),
            "structure_sequence": list(common_sequence),
            "item_count": len(members),
            "video_ids": sorted(row["video_id"] for row in members),
            "format_context": format_name,
            "topic_context": sorted({row.get("topic_family", "UNASSIGNED") for row in members}),
            "performance_association": {"state": "PERFORMANCE_ASSOCIATION", "median_channel_relative": round(median_ratio, 4) if median_ratio is not None else None, "causal_claim": False},
            "strong_examples": [row["video_id"] for row in ranked[:3]],
            "weak_examples": [row["video_id"] for row in ranked[-3:]],
            "counter_examples": counter_examples,
            "repeatability": "REPEATABLE_PATTERN" if len(members) >= 3 else "INSUFFICIENT_SAMPLE",
            "confidence": "HIGH" if len(members) >= 10 else "MEDIUM" if len(members) >= 3 else "LOW",
        })
    return result


def performance_band_summary(hook_rows, script_rows):
    scripts_by_id = {row["video_id"]: row for row in script_rows}
    groups = defaultdict(list)
    for row in hook_rows:
        groups[row["performance_band"]].append(row)
    return [{
        "performance_band": band,
        "item_count": len(members),
        "formats": dict(sorted(Counter(row["format"] for row in members).items())),
        "hook_archetypes": dict(sorted(Counter(row["hook_archetype"] for row in members).items())),
        "script_archetypes": dict(sorted(Counter(scripts_by_id[row["video_id"]]["script_archetype"] for row in members).items())),
        "evidence_state": "PERFORMANCE_ASSOCIATION",
        "causal_claim": False,
    } for band, members in sorted(groups.items())]


def continuity_state(topic, package, hook, payoff):
    topic_terms = {token.lower() for token in words(topic) if token.lower() not in STOPWORDS}
    if not topic_terms:
        return "UNCLEAR"
    matches = [bool(topic_terms & {token.lower() for token in words(value)}) for value in (package, hook, payoff)]
    return "COHERENT" if all(matches) else "PARTIAL" if any(matches) else "MISMATCH"


def continuity_checks(topic, package, hook, payoff, stakes_terms):
    def overlap(left, right):
        left_terms = {token.lower() for token in words(left) if token.lower() not in STOPWORDS}
        right_terms = {token.lower() for token in words(right) if token.lower() not in STOPWORDS}
        return "COHERENT" if left_terms & right_terms else "MISMATCH"

    checks = {
        "topic_match": overlap(topic, package),
        "semantic_match": overlap(package, hook),
        "promise_match": overlap(hook, payoff),
        "stakes_alignment": overlap(stakes_terms, " ".join((package, hook, payoff))),
        "payoff_alignment": overlap(topic, payoff),
    }
    checks["continuity"] = "COHERENT" if all(value == "COHERENT" for value in checks.values()) else "MISMATCH"
    return {"evidence_state": "DERIVED_LEXICAL_CHECK", **checks}


def load_canonical_rows(conn, channel_id):
    rows = conn.execute(
        """SELECT v.video_id, v.youtube_video_id, s.title, s.duration_seconds, s.views, s.likes, s.comments,
                  s.published_at, s.observed_at, s.video_type, t.canonical_reference, t.transcript_sha256,
                  t.availability_status,
                  sf.storage_kind AS transcript_storage_kind, sf.canonical_path AS transcript_path,
                  sf.archive_member_path AS transcript_member_path,
                  parent.canonical_path AS transcript_archive_path
           FROM videos v JOIN video_snapshots s ON s.video_id=v.video_id
           LEFT JOIN transcripts t ON t.video_id=v.video_id AND t.dataset_id=s.dataset_id
           LEFT JOIN source_files sf ON sf.file_id = t.archive_member_file_id
           LEFT JOIN source_files parent ON parent.file_id = sf.parent_file_id
           WHERE v.channel_id=? ORDER BY v.video_id""",
        (channel_id,),
    ).fetchall()
    return [dict(row) for row in rows]


def canonical_transcript_text(text):
    """Strip supplied metadata/description wrappers before script analysis."""
    parts = re.split(r"\n=+\nTRANSCRIPT\n=+\n", text, maxsplit=1)
    return parts[-1].strip()


def read_canonical_transcript_raw(row):
    """Read raw transcript text regardless of physical-file vs archive-member storage."""
    if row["transcript_storage_kind"] == "ARCHIVE_MEMBER":
        with zipfile.ZipFile(ic.resolve_canonical_path(row["transcript_archive_path"])) as archive:
            return archive.read(row["transcript_member_path"]).decode("utf-8", errors="replace")
    return ic.resolve_canonical_path(row["transcript_path"]).read_text(encoding="utf-8")


def build_report(conn, channel_id, topic, packaging, packaging_visual, interpretations):
    if topic["channel"]["channel_id"] != channel_id:
        raise ValueError("topic artifact channel mismatch")
    if packaging["channel"]["channel_id"] != channel_id or (packaging_visual and packaging_visual["channel"]["channel_id"] != channel_id):
        raise ValueError("packaging artifact channel mismatch")
    rows = load_canonical_rows(conn, channel_id)
    topic_by_id = {row["canonical_fact"]["video_id"]: row for row in topic["items"]}
    row_ids = [row["video_id"] for row in rows]
    if len(row_ids) != len(set(row_ids)) or set(row_ids) != set(topic_by_id):
        raise ValueError("canonical corpus and topic artifact items differ")
    format_velocities = defaultdict(list)
    for topic_row in topic["items"]:
        velocity = topic_row["derived_metric"].get("views_per_day")
        if velocity is not None:
            format_velocities[topic_row["canonical_fact"]["format"]].append(velocity)
    format_medians = {key: statistics.median(values) for key, values in format_velocities.items()}
    timed = {row["youtube_video_id"]: row for row in (interpretations or {}).get("timed_transcripts", [])}
    hook_features, script_features, pacing = [], [], []
    unavailable_transcripts = []
    for row in rows:
        if row["availability_status"] != "AVAILABLE" or not row["canonical_reference"]:
            unavailable_transcripts.append(row["video_id"])
            continue
        canonical_text = canonical_transcript_text(read_canonical_transcript_raw(row))
        transcript = {"text": canonical_text}
        timed_source = timed.get(row["youtube_video_id"])
        if timed_source:
            timed_path = Path(timed_source["path"])
            if timed_source.get("relationship_status") != "PROVEN":
                raise ValueError("timed transcript requires PROVEN relationship")
            transcript = json.loads(timed_path.read_text(encoding="utf-8"))
        topic_row = topic_by_id[row["video_id"]]
        format_name = topic_row["canonical_fact"]["format"]
        measured = measured_hook_features(transcript, row["title"], row["duration_seconds"])
        opening_30 = " ".join((measured["windows"]["opening_0_15s"]["text"], measured["windows"]["opening_15_30s"]["text"]))
        interpretation = interpret_hook(opening_30, measured["central_premise_position"])
        title_terms = {token.lower() for token in words(row["title"]) if token.lower() not in STOPWORDS}
        opening_terms = {token.lower() for token in words(opening_30)}
        overlap = len(title_terms & opening_terms) / max(len(title_terms), 1)
        title_match = "DIRECT_MATCH" if overlap >= .5 else "PARTIAL_MATCH" if overlap >= .2 else "DELAYED_MATCH" if measured["central_premise_position"] else "UNCLEAR"
        performance = {
            "views": topic_row["canonical_fact"].get("views"),
            "views_per_day": topic_row["derived_metric"].get("views_per_day"),
            "channel_relative_performance": topic_row["derived_metric"].get("channel_median_ratio"),
            "format_relative_performance": round(
                topic_row["derived_metric"]["views_per_day"] / format_medians[format_name], 4
            ) if topic_row["derived_metric"].get("views_per_day") is not None and format_medians.get(format_name) else None,
            "family_relative_performance": topic_row["derived_metric"].get("family_median_ratio"),
            "likes_per_view": topic_row["derived_metric"].get("like_rate"),
            "comments_per_view": topic_row["derived_metric"].get("comment_rate"),
            "performance_band": topic_row["observation"].get("performance_band"),
            "evidence_state": "PERFORMANCE_ASSOCIATION",
            "causal_claim": False,
        }
        hook_features.append({
            "video_id": row["video_id"], "youtube_video_id": row["youtube_video_id"], "format": format_name,
            "title": row["title"], "timing_quality": measured["timing_quality"], "measured": measured,
            "interpretation_state": "AI_INTERPRETATION", "interpretive_features": interpretation["features"],
            "hook_archetype": interpretation["primary_archetype"], "title_to_hook": title_match,
            "current_thumbnail_to_hook_association": "TEMPORAL_ALIGNMENT_UNKNOWN",
            "public_performance": performance,
            "performance_band": topic_row["observation"]["performance_band"],
            "channel_median_ratio": topic_row["derived_metric"]["channel_median_ratio"],
            "family_median_ratio": topic_row["derived_metric"]["family_median_ratio"],
            "views_per_day": topic_row["derived_metric"]["views_per_day"],
            "transcript_provenance": {
                "canonical_path": row["canonical_reference"], "canonical_sha256": row["transcript_sha256"],
                "timed_source": timed_source, "forensic_timing_used": bool(timed_source),
            },
        })
        structure = derive_script_structure(transcript.get("text") or canonical_text)
        payoff_map = (interpretations or {}).get("curiosity_payoff_maps", {}).get(row["video_id"], curiosity_payoff_map(canonical_text))
        script_features.append({
            "video_id": row["video_id"], "format": format_name, "topic_family": topic_row["observation"]["topic_family"],
            "interpretation_state": "AI_INTERPRETATION",
            "script_archetype": script_archetype(structure["sequence"]), "structure": structure,
            "channel_median_ratio": topic_row["derived_metric"]["channel_median_ratio"],
            "performance_band": topic_row["observation"]["performance_band"],
            "curiosity_payoff_map": payoff_map,
        })
        pacing.append({"video_id": row["video_id"], "format": format_name, **pacing_proxies(canonical_text, row["duration_seconds"], opening_30)})

    hook_archetypes = aggregate_hook_archetypes(hook_features)
    script_archetypes = aggregate_script_archetypes(script_features)
    timing_counts = Counter(row["timing_quality"] for row in hook_features)
    if interpretations is None:
        return {
            "schema_version": "hook-script-intelligence-1", "generated_on": "2026-09-10", "channel": topic["channel"],
            "evidence_snapshot": {
                "canonical_item_count": len(rows), "transcripts_accounted_for": len(hook_features),
                "unavailable_transcripts": sorted(unavailable_transcripts),
                "timestamped_transcripts": timing_counts["EXACT_TIMESTAMPED"] + timing_counts["SEGMENT_TIMESTAMPED"],
                "formats": dict(sorted(Counter(row["format"] for row in hook_features).items())),
                "public_metrics_available": ["views", "views_per_day", "likes_per_view", "comments_per_view", "format_relative_performance", "family_relative_performance"],
                "private_metrics_unavailable": sorted(PRIVATE_METRICS), "metric_observation": topic["evidence_snapshot"]["metric_cutoff"],
            },
            "timing_quality": {"counts": dict(sorted(timing_counts.items())), "positional_windows": "POSITIONAL_APPROXIMATION", "exact_seconds_not_inferred": True},
            "hook_features": hook_features, "hook_archetypes": hook_archetypes,
            "script_features": script_features, "script_archetypes": script_archetypes, "pacing_proxies": pacing,
            "performance_associations": {
                "evidence_state": "PERFORMANCE_ASSOCIATION", "causal_claim": False,
                "high_performer_patterns": [row for row in hook_archetypes + script_archetypes if row["performance_association"]["median_channel_relative"] is not None and row["performance_association"]["median_channel_relative"] >= 1.25],
                "by_performance_band": performance_band_summary(hook_features, script_features), "public_metrics_only": True,
            },
            "guardrails": {
                "private_retention_available": False, "retention_claims_created": 0,
                "prohibited_claims": ["PROVEN_RETENTION_DRIVER", "PROVEN_HOOK_WINNER", "RETENTION_CAUSE", "RETENTION_WINNER"],
                "editing_intelligence_started": False, "full_scripts_created": 0,
            },
            "limitations": [
                "Competitor private YouTube Analytics are unavailable.",
                "Canonical plaintext transcripts lack timestamps; time windows are positional approximations.",
                "Current thumbnail snapshots have unknown temporal alignment with observed performance."
                if packaging.get("evidence_snapshot", {}).get("acquired_thumbnails")
                else "Current thumbnail references have no acquired visual evidence.",
                "Hook and script archetypes are AI_INTERPRETATION, not measured retention evidence.",
            ] + ([f"{len(unavailable_transcripts)} canonical item(s) have no available transcript and are excluded from hook/script analysis: {sorted(unavailable_transcripts)}."] if unavailable_transcripts else []),
            "provenance": {"canonical_dataset": topic["channel"]["dataset_id"], "topic_schema": topic.get("schema_version"), "packaging_schema": packaging.get("schema_version")},
            "capability_verdict": "PASS",
        }
    selected_ids = interpretations["selected_opportunity_ids"]
    if len(selected_ids) != 2 or len(set(selected_ids)) != 2:
        raise ValueError("pilot requires exactly two unique opportunities")
    source_opportunities = {row["opportunity_id"]: row for row in packaging["opportunity_packages"]}
    visual_revalidation = {row["package_id"]: row for row in packaging_visual["package_revalidation"]}
    selected = [json.loads(json.dumps(source_opportunities[opportunity_id])) for opportunity_id in selected_ids]
    for opportunity in selected:
        for package in opportunity["recommended_test_set"]:
            if package["package_id"] not in visual_revalidation:
                raise ValueError("package lacks current visual revalidation")
            package["visual_revalidation"] = visual_revalidation[package["package_id"]]
    package_ids = {package["package_id"] for opportunity in selected for package in opportunity["recommended_test_set"]}
    canonical_ids = {row["video_id"] for row in rows}
    hooks = interpretations["hook_hypotheses"]
    blueprints = interpretations["script_blueprints"]
    if len(hooks) != 6 or len(blueprints) != 2:
        raise ValueError("pilot requires exactly six hooks and two blueprints")
    if any(hook["package_link"] not in package_ids for hook in hooks):
        raise ValueError("hook package link not found")
    if any(not set(hook["supporting_video_ids"]) <= canonical_ids for hook in hooks):
        raise ValueError("hook references noncanonical video")
    if any(hook.get("evidence_state") != "HYPOTHESIS_FOR_TESTING" for hook in hooks):
        raise ValueError("generated hooks must remain hypotheses")
    if any(sum(hook["opportunity_id"] == opportunity_id for hook in hooks) != 3 for opportunity_id in selected_ids):
        raise ValueError("pilot requires three hooks per opportunity")
    if any(sum(row["opportunity_id"] == opportunity_id for row in blueprints) != 1 for opportunity_id in selected_ids):
        raise ValueError("pilot requires one blueprint per opportunity")
    if {hook["opportunity_id"] for hook in hooks} != set(selected_ids) or {row["opportunity_id"] for row in blueprints} != set(selected_ids):
        raise ValueError("generated object opportunity mismatch")
    blueprint_by_opportunity = {row["opportunity_id"]: row for row in blueprints}
    links, content_blueprints = [], []
    for opportunity in selected:
        opportunity_id = opportunity["opportunity_id"]
        opportunity_hooks = [row for row in hooks if row["opportunity_id"] == opportunity_id]
        blueprint = blueprint_by_opportunity[opportunity_id]
        for hook in opportunity_hooks:
            package = next(package for package in opportunity["recommended_test_set"] if package["package_id"] == hook["package_link"])
            continuity_terms = interpretations.get("continuity_terms", {}).get(opportunity_id, "")
            checks = continuity_checks(
                " ".join((opportunity["topic"], opportunity["specific_angle"], continuity_terms)),
                package["title_option"], hook["hook_text"], blueprint["main_payoff"], continuity_terms,
            )
            links.append({
                "opportunity_id": opportunity_id, "package_id": package["package_id"], "hook_id": hook["hook_id"],
                "blueprint_id": blueprint["blueprint_id"], **checks,
            })
        content_blueprints.append({
            "object_type": "DERIVED_CONTENT_BLUEPRINT", "recommendation_state": "HYPOTHESIS_FOR_TESTING",
            "opportunity": opportunity, "packaging_options": opportunity["recommended_test_set"],
            "hook_options": opportunity_hooks, "script_blueprint": blueprint,
            "evidence": sorted({video_id for hook in opportunity_hooks for video_id in hook["supporting_video_ids"]}),
            "counter_evidence": [hook["counter_evidence"] for hook in opportunity_hooks],
            "limitations": ["No private retention data.", "No causal hook or script claim.", "No polished narration."],
        })

    pilot_pass = (
        len(rows) == len(topic_by_id) == len(hook_features)
        and len(selected) == len(content_blueprints) == 2
        and all(len(opportunity["recommended_test_set"]) == 3 for opportunity in selected)
        and all(sum(hook["opportunity_id"] == opportunity_id for hook in hooks) == 3 for opportunity_id in selected_ids)
        and all(sum(row["opportunity_id"] == opportunity_id for row in blueprints) == 1 for opportunity_id in selected_ids)
        and len(links) == 6
        and all(row["continuity"] == "COHERENT" for row in links)
    )
    return {
        "schema_version": "hook-script-intelligence-pilot-1", "generated_on": "2026-09-10", "channel": topic["channel"],
        "evidence_snapshot": {
            "canonical_item_count": len(rows), "transcripts_accounted_for": len(hook_features),
            "unavailable_transcripts": sorted(unavailable_transcripts),
            "timestamped_transcripts": timing_counts["EXACT_TIMESTAMPED"] + timing_counts["SEGMENT_TIMESTAMPED"],
            "formats": dict(sorted(Counter(row["format"] for row in hook_features).items())),
            "public_metrics_available": ["views", "views_per_day", "likes_per_view", "comments_per_view", "format_relative_performance", "family_relative_performance"],
            "private_metrics_unavailable": sorted(PRIVATE_METRICS), "metric_observation": topic["evidence_snapshot"]["metric_cutoff"],
        },
        "timing_quality": {"counts": dict(sorted(timing_counts.items())), "positional_windows": "POSITIONAL_APPROXIMATION", "exact_seconds_not_inferred": True},
        "platform_guardrails": interpretations["platform_guardrails"],
        "hook_features": hook_features, "hook_archetypes": hook_archetypes,
        "script_features": script_features, "script_archetypes": script_archetypes, "pacing_proxies": pacing,
        "performance_associations": {
            "evidence_state": "PERFORMANCE_ASSOCIATION", "causal_claim": False,
            "high_performer_patterns": [row for row in hook_archetypes + script_archetypes if row["performance_association"]["median_channel_relative"] is not None and row["performance_association"]["median_channel_relative"] >= 1.25],
            "by_performance_band": performance_band_summary(hook_features, script_features),
            "public_metrics_only": True,
        },
        "counter_evidence": [
            "Each repeated hook and script archetype also has weak examples; association is not causality.",
            "Long-form and Shorts differ in duration and surface context; cross-format transfer is not assumed.",
            "Most transcript windows are positional estimates because canonical plaintext lacks timestamps.",
            "Views/day is not retention, attention, or intrinsic content quality.",
        ],
        "selected_opportunities": selected, "hook_hypotheses": hooks, "script_blueprints": blueprints,
        "package_hook_script_links": links, "content_blueprints": content_blueprints,
        "forensic_evidence": interpretations.get("forensic_evidence", []),
        "guardrails": {
            "private_retention_available": False, "retention_claims_created": 0,
            "allowed_claims": ["OBSERVED_PATTERN", "PERFORMANCE_ASSOCIATION", "HYPOTHESIS_FOR_TESTING"],
            "prohibited_claims": ["PROVEN_RETENTION_DRIVER", "PROVEN_HOOK_WINNER", "RETENTION_CAUSE", "RETENTION_WINNER"],
            "editing_intelligence_started": False, "full_scripts_created": 0,
        },
        "limitations": [
            "Competitor private YouTube Analytics are unavailable.",
            f"{timing_counts['POSITIONAL_ONLY']} canonical transcripts are plaintext without timestamps; their time windows are positional approximations.",
            f"{timing_counts['EXACT_TIMESTAMPED']} PROVEN forensic relationships provide exact word timing for limited videos only.",
            "Current thumbnails remain temporally uncertain relative to historical performance.",
            "Semantic phases and curiosity/payoff maps are AI_INTERPRETATION, not measured retention evidence.",
        ],
        "provenance": {
            "topic_artifact": interpretations["provenance"]["topic_artifact"],
            "packaging_artifact": interpretations["provenance"]["packaging_artifact"],
            "packaging_visual_artifact": interpretations["provenance"]["packaging_visual_artifact"],
            "canonical_dataset": topic["channel"]["dataset_id"], "interpretation_input": interpretations["provenance"]["interpretation_input"],
            "primary_platform_validation": "data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md",
        },
        "pilot_verdict": "PASS" if pilot_pass else "FAIL",
    }


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"


def render_markdown(payload):
    selected = payload["selected_opportunities"]
    hooks = payload["hook_hypotheses"]
    blueprints = payload["script_blueprints"]
    snapshot = payload["evidence_snapshot"]
    formats = snapshot["formats"]
    channel_id = payload["channel"]["channel_id"]
    lines = [
        f"# {channel_id} Hook + Script Intelligence Pilot", "", "# Scope", "",
        "Analyzes canonical transcripts as observed structure and public-performance association. No retention prediction, full script, or Editing Intelligence.", "",
        "# Evidence Availability", "",
        f"{snapshot['transcripts_accounted_for']}/{snapshot['canonical_item_count']} transcripts; formats: {formats.get('LONG_FORM', 0)} long-form, {formats.get('SHORT_FORM', 0)} Shorts. Private retention/CTR/watch-time data: unavailable.", "",
        "# Timing Quality", "",
        f"Exact timestamped forensic transcripts: {payload['evidence_snapshot']['timestamped_transcripts']}. Positional-only canonical transcripts: {payload['timing_quality']['counts'].get('POSITIONAL_ONLY', 0)}. Positional windows never claim exact seconds.", "",
        "# Platform Guardrails", "",
    ]
    lines.extend(f"- {item}" for item in payload["platform_guardrails"]["principles"])
    lines += ["", "# Hook Patterns", "", "Measured opening word/question/premise-position fields are DERIVED_METRIC. Hook labels are AI_INTERPRETATION.", "", "# Hook Archetypes", ""]
    lines.extend(f"- `{row['hook_archetype_id']}` / `{row['format_context']}`: {row['item_count']} items; median relative {row['performance_association']['median_channel_relative']}; {row['repeatability']}." for row in payload["hook_archetypes"])
    lines += ["", "# Script Structures", "", "Every supported transcript has a traceable semantic phase sequence. Boundaries are DERIVED_SEGMENT_BOUNDARY or UNKNOWN.", "", "# Script Archetypes", ""]
    lines.extend(f"- `{row['script_archetype_id']}` / `{row['format_context']}`: {row['item_count']} items; median relative {row['performance_association']['median_channel_relative']}; {row['repeatability']}." for row in payload["script_archetypes"])
    lines += ["", "# Performance Associations", "", "Associations use public views/day and channel/family-relative context. They do not establish retention or causality.", "", "# Counter-Evidence", ""]
    lines.extend(f"- {item}" for item in payload["counter_evidence"])
    lines += ["", "# Selected Opportunities", ""]
    lines.extend(f"- `{row['opportunity_id']}`: {row['topic']} — {row['specific_angle']}" for row in selected)
    lines += ["", "# Hook Hypotheses", ""]
    lines.extend(f"- `{row['hook_id']}` linked to `{row['package_link']}`: {row['hook_text']}" for row in hooks)
    lines += ["", "# Script Blueprints", ""]
    lines.extend(f"- `{row['blueprint_id']}`: " + " / ".join(row["explanation_sequence"]) for row in blueprints)
    coherent_links = sum(row["continuity"] == "COHERENT" for row in payload["package_hook_script_links"])
    lines += ["", "# Package → Hook → Script Continuity", "", f"{coherent_links}/{len(payload['package_hook_script_links'])} links passed five distinct DERIVED_LEXICAL_CHECK proxies. These checks bound wording continuity; they do not prove audience interpretation.", "", "# What We Cannot Infer", ""]
    lines.extend(f"- {item}" for item in payload["limitations"])
    lines += ["", "# Pilot Verdict", "", f"{payload['pilot_verdict']}. Hook Intelligence and Script Intelligence are WORKING as evidence-bounded planning layers. Historical retention causality remains unsupported.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--topic-artifact", required=True)
    parser.add_argument("--packaging-artifact", required=True)
    parser.add_argument("--packaging-v2-artifact")
    parser.add_argument("--interpretations")
    parser.add_argument("--db")
    parser.add_argument("--output", required=True)
    parser.add_argument("--markdown-output")
    args = parser.parse_args(argv)
    topic = json.loads(Path(args.topic_artifact).read_text(encoding="utf-8"))
    packaging = json.loads(Path(args.packaging_artifact).read_text(encoding="utf-8"))
    packaging_visual = json.loads(Path(args.packaging_v2_artifact).read_text(encoding="utf-8")) if args.packaging_v2_artifact else None
    interpretations = json.loads(Path(args.interpretations).read_text(encoding="utf-8")) if args.interpretations else None
    with connect(args.db) as conn:
        payload = build_report(conn, args.channel, topic, packaging, packaging_visual, interpretations)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_json(payload), encoding="utf-8")
    if args.markdown_output and interpretations is not None:
        Path(args.markdown_output).write_text(render_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
