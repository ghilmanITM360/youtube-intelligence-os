#!/usr/bin/env python3
"""Build reproducible transcript-structure evidence for all DS-000033 videos.

This output is automated structural analysis, not manual deep investigation.
Plaintext captions have no cue timestamps, so time windows and positions are
estimated from word position and registered duration.
"""

from __future__ import annotations

import json
import re
import sqlite3
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data/catalog/youtube_channel_registry.db"
OUTPUT = ROOT / "docs/research/senior-health-2026-09-25/forensic-v3/BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json"
CHANNEL_ID = "UCFpxvukIqCAUA7YizI-q9Dw"
TIME_LABEL = "ESTIMATED_FROM_WORD_POSITION_PLAINTEXT_CAPTIONS"
ORIGINAL_NINE = {
    "MpohFGvHZHI", "JUCiIDVTshA", "16n80OQCVSM", "XX5Kw2OotL0",
    "k-3BY-naQ0M", "Ev-i_E_MlTo", "8_depH-gT4o", "R7uXQBjnTjk",
    "OCWvaUcSPOU",
}

PATTERNS = {
    "authority": re.compile(r"\b(board[- ]certified|geriatrician|doctor|physician|study|research|evidence|guideline|criteria)\b", re.I),
    "curiosity": re.compile(r"\b(surpris|what if|why|secret|most people|don't realize|in a moment|later|but first)\w*\b", re.I),
    "recommendation": re.compile(r"\b(recommend|should|ask your|talk to|speak with|try|avoid|consider|check|review)\w*\b", re.I),
    "cta": re.compile(r"\b(subscribe|comment|join button|member|watch next|like this video|share)\b", re.I),
    "evidence": re.compile(r"\b(study|studies|research|data|evidence|trial|journal|society|association|criteria|guideline)\b", re.I),
    "revelation": re.compile(r"\b(key|important|surprising|problem|risk|cause|reason|means|bottom line|good news)\b", re.I),
}


def words(text: str) -> list[str]:
    return re.findall(r"\S+", text)


def excerpt(items: list[str], start: int, count: int = 55) -> str:
    return " ".join(items[start : start + count]).strip()


def timed_excerpt(items: list[str], duration: int | None, seconds: int) -> str:
    if not items:
        return ""
    count = round(len(items) * seconds / duration) if duration else round(seconds * 2.2)
    return " ".join(items[: max(1, min(len(items), count))])


def first_match(pattern: re.Pattern[str], text: str, items: list[str], duration: int | None) -> dict | None:
    match = pattern.search(text)
    if not match:
        return None
    index = len(text[: match.start()].split())
    seconds = round(index * duration / len(items)) if duration and items else None
    return {
        "matched_text": match.group(0),
        "word_index": index,
        "estimated_seconds": seconds,
        "time_label": TIME_LABEL,
    }


def structure(items: list[str]) -> list[dict]:
    if not items:
        return []
    boundaries = [("opening", 0.0, 0.1), ("development_1", 0.1, 0.35),
                  ("development_2", 0.35, 0.65), ("payoff_and_application", 0.65, 0.9),
                  ("conclusion_and_cta", 0.9, 1.0)]
    result = []
    for label, start_share, end_share in boundaries:
        start = min(len(items) - 1, round(len(items) * start_share))
        end = max(start + 1, round(len(items) * end_share))
        result.append({
            "section": label,
            "start_word": start,
            "end_word": min(len(items), end),
            "opening_excerpt": excerpt(items, start),
        })
    return result


def classify_hook(opening: str) -> list[str]:
    labels = []
    if re.search(r"board[- ]certified|geriatrician|doctor", opening, re.I):
        labels.append("CREDENTIAL_FIRST")
    if "?" in opening:
        labels.append("QUESTION")
    if re.search(r"\b(today|in this episode|going to|you'll learn|show you|explain)\b", opening, re.I):
        labels.append("EXPLICIT_PROMISE")
    if re.search(r"\b(risk|warning|danger|harm|avoid|memory loss|dementia|alzheimer)\b", opening, re.I):
        labels.append("PROBLEM_OR_RISK")
    return labels or ["PLAIN_EXPLANATORY_OPENING"]


def main() -> None:
    connection = sqlite3.connect(DB)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT v.youtube_video_id,v.title,v.published_at,v.duration_seconds,
               v.video_type,v.views,v.thumbnail_url,t.transcript_text,
               t.word_count,t.caption_type,t.language,t.evidence_locator,
               t.transcript_sha256
        FROM videos v JOIN transcripts t USING(youtube_video_id)
        WHERE v.canonical_channel_id=? AND t.dataset_id='DS-000033'
        ORDER BY v.published_at,v.youtube_video_id
        """,
        (CHANNEL_ID,),
    ).fetchall()
    connection.close()
    if len(rows) != 98:
        raise RuntimeError(f"Expected 98 DS-000033 videos, found {len(rows)}")

    views = [int(row["views"] or 0) for row in rows]
    median_views = statistics.median(views)
    records = []
    for row in rows:
        text = row["transcript_text"] or ""
        item_words = words(text)
        if not item_words:
            raise RuntimeError(f"Missing real transcript: {row['youtube_video_id']}")
        duration = row["duration_seconds"] if row["duration_seconds"] and row["duration_seconds"] > 0 else None
        opening_60 = timed_excerpt(item_words, duration, 60)
        first_120 = excerpt(item_words, 0, 120)
        conclusion = " ".join(item_words[-120:])
        counts = {name: len(pattern.findall(text)) for name, pattern in PATTERNS.items()}
        records.append({
            "video_id": row["youtube_video_id"],
            "title": row["title"],
            "published_at": row["published_at"],
            "video_type": row["video_type"],
            "views": row["views"],
            "duration_seconds": duration,
            "caption_provenance": {
                "caption_type": row["caption_type"], "language": row["language"],
                "evidence_locator": row["evidence_locator"], "transcript_sha256": row["transcript_sha256"],
            },
            "timing_method": TIME_LABEL,
            "opening_first_15_seconds": timed_excerpt(item_words, duration, 15),
            "opening_first_30_seconds": timed_excerpt(item_words, duration, 30),
            "opening_first_60_seconds": opening_60,
            "actual_opening_and_audience_promise": first_120,
            "hook_and_audience_psychology": {
                "hook_labels": classify_hook(opening_60),
                "audience_address_present": bool(re.search(r"\b(older adults?|people over age 60|as we age|you|your)\b", opening_60, re.I)),
                "risk_language_count": len(re.findall(r"\b(risk|harm|danger|warning|avoid|problem)\w*\b", opening_60, re.I)),
                "promise_language_present": bool(re.search(r"\b(today|this episode|going to|show you|explain|learn)\b", opening_60, re.I)),
            },
            "script_structure": structure(item_words),
            "narrative_progression": [section["section"] for section in structure(item_words)],
            "information_density": {
                "word_count": len(item_words),
                "words_per_minute": round(len(item_words) / (duration / 60), 1) if duration else None,
                "numbers_per_1000_words": round(1000 * len(re.findall(r"\b\d+(?:\.\d+)?\b", text)) / len(item_words), 2),
                "enumeration_markers": len(re.findall(r"\b(first|second|third|fourth|fifth|number one|number two|\d+)\b", text, re.I)),
            },
            "authority_and_supporting_evidence": {
                "counts": {key: counts[key] for key in ("authority", "evidence")},
                "first_authority_cue": first_match(PATTERNS["authority"], text, item_words, duration),
                "first_evidence_cue": first_match(PATTERNS["evidence"], text, item_words, duration),
            },
            "curiosity_mechanisms": {
                "count": counts["curiosity"],
                "first": first_match(PATTERNS["curiosity"], text, item_words, duration),
            },
            "major_revelation_proxy": first_match(PATTERNS["revelation"], text, item_words, duration),
            "practical_recommendations": {
                "count": counts["recommendation"],
                "first": first_match(PATTERNS["recommendation"], text, item_words, duration),
            },
            "conclusion_and_cta": {
                "ending_excerpt": conclusion,
                "cta_count": counts["cta"],
                "first_cta": first_match(PATTERNS["cta"], text, item_words, duration),
            },
            "completion_state": "AUTOMATED_STRUCTURAL_ANALYSIS_COMPLETE",
            "deep_investigation_state": (
                "PREVIOUSLY_REPORTED_DEEP_REVIEW" if row["youtube_video_id"] in ORIGINAL_NINE
                else "NOT_YET_DEEPLY_INVESTIGATED"
            ),
            "limitations": [
                "Timing is estimated from word position because stored captions contain no cue timestamps.",
                "Lexical counts and section excerpts are machine-extracted observations, not causal interpretation.",
                "This record does not by itself satisfy manual deep-investigation criteria.",
            ],
        })

    breakout_rows = sorted(
        (row for row in records if row["views"] >= 5 * median_views),
        key=lambda row: row["views"], reverse=True,
    )
    breakouts = [{
        "rank": index,
        "video_id": row["video_id"],
        "title": row["title"],
        "views": row["views"],
        "multiple_vs_all_video_median": round(row["views"] / median_views, 2),
        "cohort": "ORIGINAL_NINE" if row["video_id"] in ORIGINAL_NINE else "REMAINING_SIXTEEN",
    } for index, row in enumerate(breakout_rows, start=1)]
    if len(breakouts) != 25:
        raise RuntimeError(f"Expected 25 breakout candidates, found {len(breakouts)}")

    payload = {
        "artifact_type": "AUTOMATED_TRANSCRIPT_STRUCTURAL_ANALYSIS",
        "generated_from": "data/catalog/youtube_channel_registry.db",
        "population": {
            "videos": len(records),
            "regular_videos": sum(row["video_type"] == "video" for row in records),
            "shorts": sum(row["video_type"] == "shorts" for row in records),
            "real_transcripts": len(records),
            "all_video_median_views": median_views,
            "regular_video_median_views": statistics.median(row["views"] for row in records if row["video_type"] == "video"),
            "shorts_median_views": statistics.median(row["views"] for row in records if row["video_type"] == "shorts"),
        },
        "breakout_definition": "views >= 5 times median across all 98 videos; descriptive candidate threshold",
        "breakout_inventory": breakouts,
        "videos": records,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(records)} records and {len(breakouts)} breakout candidates to {OUTPUT}")


if __name__ == "__main__":
    main()
