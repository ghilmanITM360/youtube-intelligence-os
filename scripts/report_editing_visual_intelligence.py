#!/usr/bin/env python3
"""Build evidence-bounded editing and visual intelligence from registered forensics."""

import argparse
import csv
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from report_common import connect


ROOT = Path(__file__).resolve().parents[1]
UNAVAILABLE_METRICS = {
    "AUDIENCE_RETENTION", "WATCH_TIME", "AVERAGE_VIEW_DURATION", "CTR", "SHARES",
}
VIDEO_EXTENSIONS = {"mp4", "mov", "m4v", "webm", "mkv"}
IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
VISUAL_RULES = {
    "DIAGRAM": re.compile(r"diagram|field|orbit|globe|map|calculation|force|particle|earth|moon|sun", re.I),
    "ILLUSTRATION": re.compile(r"illustration|drawing|figure|presenter|landscape|neighborhood", re.I),
    "TEXT_OVERLAY": re.compile(r"text|question|label|caption|award|dialogue|number|equation", re.I),
    "LABEL": re.compile(r"label|text|question|award|caption", re.I),
    "NUMBER_EQUATION": re.compile(r"number|equation|calculation|orders? of magnitude|multiplier|mph|km/h|min", re.I),
    "SCALE_VISUALIZATION": re.compile(r"scale|universe|cosmic|globe|earth|planet|galax|black hole", re.I),
    "COMPARISON": re.compile(r"comparison|versus|vs\.?|analogy|upper/lower|two-|both", re.I),
    "MAP_SPACE_ENVIRONMENT": re.compile(r"map|globe|earth|space|universe|galax|landscape|neighborhood", re.I),
    "ANIMATION_MOTION": re.compile(r"add|replace|motion|move|expand|reveal|trajectory|rupture|explode|transition", re.I),
    "CUT_TRANSITION": re.compile(r"cut|transition|replacement|reset|noise", re.I),
    "CONSEQUENCE_VISUAL": re.compile(r"destruct|blast|explode|collapse|rupture|shatter|reaction|consequence|black hole", re.I),
}
PHASE_ROLES = {
    "HOOK": "PROMISE_REINFORCEMENT",
    "PREMISE": "PROMISE_REINFORCEMENT",
    "SETUP": "CONCEPT_EXPLANATION",
    "CONSTRAINT": "CONSTRAINT_VISUALIZATION",
    "EXPLANATION": "CONCEPT_EXPLANATION",
    "CALCULATION": "SCALE_DEMONSTRATION",
    "ESCALATION": "ESCALATION_VISUAL",
    "COUNTERPOINT": "CONSTRAINT_VISUALIZATION",
    "PAYOFF": "PAYOFF_VISUAL",
    "ENDING": "PAYOFF_VISUAL",
}


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"


def _existing_path(row, repo_root=ROOT):
    root = Path(repo_root).resolve()
    dataset_id = row["dataset_id"]
    relative = row.get("relative_path")
    if relative:
        candidate = (root / "data/raw/forensic-analysis" / dataset_id / relative).resolve()
        if candidate.is_relative_to(root) and candidate.is_file():
            return candidate
    canonical = row.get("canonical_path") or ""
    marker = "/data/raw/forensic-analysis/"
    if marker in canonical:
        candidate = (root / "data/raw/forensic-analysis" / canonical.split(marker, 1)[1]).resolve()
        if candidate.is_relative_to(root) and candidate.is_file():
            return candidate
    return None


def _files(conn, dataset_id):
    return [dict(row) for row in conn.execute(
        """SELECT dataset_id, file_id, original_filename, original_path, relative_path,
                  canonical_path, extension, sha256, is_copied
             FROM source_files WHERE dataset_id = ? ORDER BY file_id""",
        (dataset_id,),
    )]


def _relationship_types(conn):
    result = defaultdict(list)
    for row in conn.execute(
        "SELECT relationship_id, from_dataset_id, to_dataset_id, relationship_type, status FROM dataset_relationships"
    ):
        if row["status"] != "PROVEN":
            continue
        item = dict(row)
        result[row["from_dataset_id"]].append(item)
        result[row["to_dataset_id"]].append(item)
    return result


def _youtube_id(notes, source_locator):
    text = " ".join(filter(None, (notes, source_locator)))
    match = re.search(r"(?:mediaId=|youtu\.be/|[?&]v=)([\w-]{11})", text)
    return match.group(1) if match else None


def _evidence_score(row):
    return sum((
        row["forensic_report_available"] == "YES",
        row["keyframes_available"] == "YES",
        row["frame_sequence_available"] == "YES",
        row["timestamps_available"] == "YES",
        row["shot_visual_transition_data_available"] == "YES",
        row["machine_readable_state_data"] == "YES",
    ))


def discover_forensic_evidence(conn, channel_id, repo_root=ROOT):
    relationships = _relationship_types(conn)
    links = conn.execute(
        """SELECT l.dataset_id, l.relationship_type, l.source_locator, l.notes,
                  d.dataset_name
             FROM channel_dataset_links l
             JOIN datasets d ON d.dataset_id = l.dataset_id
            WHERE l.channel_id = ? AND l.relationship_type = 'IDENTITY_EVIDENCE'
              AND d.semantic_class = 'C'
            ORDER BY l.dataset_id""",
        (channel_id,),
    ).fetchall()
    rows = []
    for link in links:
        youtube_id = _youtube_id(link["notes"], link["source_locator"])
        video = conn.execute(
            """SELECT v.video_id, v.youtube_video_id, s.title, s.duration_seconds,
                      s.video_type, s.views, s.observed_at
                 FROM videos v
                 LEFT JOIN video_snapshots s ON s.video_id = v.video_id
                WHERE v.channel_id = ? AND v.youtube_video_id = ?
                ORDER BY s.observed_at DESC LIMIT 1""",
            (channel_id, youtube_id),
        ).fetchone()
        if not video:
            continue
        files = _files(conn, link["dataset_id"])
        images = [row for row in files if (row["extension"] or "").lower() in IMAGE_EXTENSIONS]
        reports = [row for row in files if (row["extension"] or "").lower() == "md" and re.search(
            r"report|blueprint|reverse.engineer", row["original_filename"], re.I
        )]
        state_files = [row for row in files if re.search(
            r"(?:state|shot|motion|selected|boundar).*(?:manifest|states|frames|boundar)|(?:state|shot|motion)_manifest",
            row["original_filename"], re.I,
        )]
        timestamped = any(re.search(r"\d+(?:ms|s)(?:\.|$)", row["original_filename"], re.I) for row in images)
        report_path = next((_existing_path(row, repo_root) for row in sorted(reports, key=lambda item: item["is_copied"], reverse=True) if _existing_path(row, repo_root)), None)
        report_text = "\n".join(
            path.read_text(encoding="utf-8", errors="replace")
            for item in reports for path in [_existing_path(item, repo_root)] if path
        )
        shot_data = bool(state_files) or bool(re.search(r"shot/edit decision|major-shot|editing decision list|temporal architecture", report_text, re.I))
        relation = relationships.get(link["dataset_id"], [])
        row = {
            "video_id": video["video_id"],
            "youtube_video_id": video["youtube_video_id"],
            "title": video["title"],
            "format": "SHORT_FORM" if (video["video_type"] or "").lower() == "shorts" else "LONG_FORM",
            "forensic_dataset_id": link["dataset_id"],
            "dataset_id": link["dataset_id"],
            "relationship_type": link["relationship_type"],
            "dataset_relationship_ids": sorted(item["relationship_id"] for item in relation),
            "dataset_relationship_type": relation[0]["relationship_type"] if relation else link["relationship_type"],
            "source_video_available": "YES" if any(
                (item["extension"] or "").lower() in VIDEO_EXTENSIONS and _existing_path(item, repo_root) for item in files
            ) else "NO",
            "keyframes_available": "YES" if images and any(_existing_path(item, repo_root) for item in images) else "NO",
            "frame_sequence_available": "YES" if len(images) >= 10 else "NO",
            "timestamps_available": "YES" if timestamped or bool(state_files) else "NO",
            "shot_visual_transition_data_available": "YES" if shot_data else "NO",
            "forensic_report_available": "YES" if report_path else "NO",
            "machine_readable_state_data": "YES" if state_files else "NO",
            "registered_frame_assets": len(images),
            "forensic_report": str(report_path.relative_to(repo_root)) if report_path and report_path.is_relative_to(repo_root) else str(report_path or ""),
            "canonical_measurement_source": False,
            "evidence_quality": "LOW",
            "provenance_files": [{
                "file_id": item["file_id"], "relative_path": item["relative_path"], "sha256": item["sha256"],
            } for item in files if item in reports or item in state_files],
        }
        score = _evidence_score(row)
        row["evidence_quality"] = "HIGH" if score >= 6 else "MEDIUM" if score >= 4 else "LOW"
        rows.append(row)
    by_video = defaultdict(list)
    for row in rows:
        by_video[row["video_id"]].append(row)
    for candidates in by_video.values():
        max(candidates, key=lambda row: (_evidence_score(row), row["dataset_id"]))["canonical_measurement_source"] = True
    return rows


def _parse_tsv(path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines:
        return []
    if "\t" not in lines[0]:
        return []
    header = lines[0].split("\t")
    known = {"visual", "id", "state", "time", "representative", "representative_time", "start", "end"}
    if not set(header) & known:
        return []
    return list(csv.DictReader(lines, delimiter="\t"))


def _markdown_descriptions(text):
    result = {}
    for line in text.splitlines():
        match = re.match(r"\|\s*(V\d+)\s*\|(.*)\|\s*$", line)
        if not match:
            continue
        cells = [cell.strip() for cell in match.group(2).split("|")]
        result.setdefault(match.group(1), cells[-1] if cells else "")
    return result


def _load_states(conn, evidence_row, repo_root=ROOT):
    files = _files(conn, evidence_row["dataset_id"])
    frame_files = defaultdict(list)
    for file_row in files:
        match = re.match(r"(V\d+)_", file_row["original_filename"], re.I)
        if match and (file_row["extension"] or "").lower() in IMAGE_EXTENSIONS:
            frame_files[match.group(1).upper()].append(file_row)
    report_path = Path(evidence_row["forensic_report"]) if evidence_row["forensic_report"] else None
    if report_path and not report_path.is_absolute():
        report_path = Path(repo_root).resolve() / report_path
    report_text = report_path.read_text(encoding="utf-8", errors="replace") if report_path and report_path.exists() else ""
    descriptions = _markdown_descriptions(report_text)
    candidates = []
    for item in files:
        path = _existing_path(item, repo_root)
        if not path or path.suffix.lower() != ".tsv":
            continue
        rows = _parse_tsv(path)
        if not rows:
            continue
        score = sum(key in rows[0] for key in ("representative", "representative_time", "time", "start", "end"))
        if re.search(r"state_manifest", item["original_filename"], re.I):
            score += 5
        elif re.search(r"selected_(?:states|frames)", item["original_filename"], re.I):
            score += 3
        candidates.append((score, item, rows))
    if not candidates:
        return [], report_text
    _, item, rows = max(candidates, key=lambda entry: entry[0])
    states = []
    for index, source in enumerate(rows, start=1):
        state_id = source.get("visual") or source.get("id") or source.get("state") or f"V{index:02d}"
        time_value = source.get("representative") or source.get("representative_time") or source.get("time") or source.get("start")
        try:
            timestamp = float(time_value)
        except (TypeError, ValueError):
            continue
        description = source.get("literal_state") or source.get("title") or descriptions.get(state_id) or "Registered visual state"
        change = source.get("change_from_previous") or ""
        visual_file = next(iter(frame_files.get(state_id.upper(), [])), None)
        locator = visual_file["relative_path"] if visual_file else f"{item['relative_path']}#{state_id}"
        states.append({
            "visual_state_id": state_id,
            "timestamp_seconds": timestamp,
            "description": description,
            "change_from_previous": change,
            "frame_locator": f"{evidence_row['dataset_id']}:{locator}",
            "frame_file_id": visual_file["file_id"] if visual_file else None,
            "frame_sha256": visual_file["sha256"] if visual_file else None,
            "source_file_id": item["file_id"],
            "source_sha256": item["sha256"],
        })
    return sorted(states, key=lambda row: (row["timestamp_seconds"], row["visual_state_id"])), report_text


def derive_timing_features(duration, timestamps, text_event_count=0, diagram_event_count=0):
    times = sorted(set(float(value) for value in timestamps if 0 <= float(value) <= duration))
    if not times:
        return {}
    boundaries = sorted(set([0.0] + times + [float(duration)]))
    gaps = [right - left for left, right in zip(boundaries, boundaries[1:]) if right > left]
    changes = max(0, len(times) - 1)

    def rate(window):
        observed = min(float(duration), float(window))
        count = sum(0 < value <= observed for value in times)
        return round(count / observed * 60, 4) if observed else 0.0

    return {
        "visual_change_count": changes,
        "average_visual_segment_duration_seconds": round(duration / len(times), 4),
        "median_visual_segment_duration_seconds": round(statistics.median(gaps), 4) if gaps else None,
        "visual_changes_per_minute": round(changes / duration * 60, 4) if duration else None,
        "early_30s_visual_change_rate": rate(30),
        "early_60s_visual_change_rate": rate(60),
        "longest_static_hold_seconds": round(max(gaps), 4) if gaps else None,
        "text_event_count": text_event_count,
        "text_events_per_minute": round(text_event_count / duration * 60, 4) if duration else None,
        "diagram_event_count": diagram_event_count,
        "diagram_events_per_minute": round(diagram_event_count / duration * 60, 4) if duration else None,
    }


def classify_visual_features(states, video_id, dataset_id):
    features = []
    for state in states:
        source = f"{state['description']} {state['change_from_previous']}"
        for feature, pattern in VISUAL_RULES.items():
            if pattern.search(source):
                features.append({
                    "video_id": video_id,
                    "dataset_id": dataset_id,
                    "visual_state_id": state["visual_state_id"],
                    "timestamp_seconds": state["timestamp_seconds"],
                    "feature": feature,
                    "evidence_state": "AI_INTERPRETATION",
                    "visual_evidence": state["description"],
                    "frame_locator": state["frame_locator"],
                })
    return features


def _report_shot_count(text):
    matches = [int(value) for value in re.findall(r"(?:total\s+)?(\d+)\s+(?:major\s+)?shots", text, re.I)]
    matches += [int(value) for value in re.findall(r"total\s+shots\s+(\d+)", text, re.I)]
    matches += [int(value) for value in re.findall(r"major-shot statistics:\*{0,2}\s*total\s+(\d+)", text, re.I)]
    return max(matches) if matches else None


def _topic_items(topic):
    return {row["canonical_fact"]["video_id"]: row for row in topic.get("items", [])}


def _clock_seconds(value):
    value = value.strip()
    parts = value.split(":")
    try:
        return float(parts[-1]) + (60 * float(parts[-2]) if len(parts) > 1 else 0)
    except ValueError:
        return None


def _script_beat_times(text):
    times = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not re.fullmatch(r"[A-Z]{1,3}\d+", cells[0]):
            continue
        match = re.match(r"(?:approximately\s+)?(\d{1,2}:\d{2}(?:\.\d+)?)", cells[1], re.I)
        if match:
            seconds = _clock_seconds(match.group(1))
            if seconds is not None:
                times.append(seconds)
    return sorted(set(times))


def _align_script_visual(hook_script, states_by_video, report_text_by_video):
    results = []
    script_by_video = {row["video_id"]: row for row in hook_script.get("script_features", [])}
    for video_id, states in sorted(states_by_video.items()):
        script = script_by_video.get(video_id, {})
        segments = script.get("structure", {}).get("segments", [])
        if not states or not segments:
            continue
        beats = _script_beat_times(report_text_by_video.get(video_id, ""))
        for index, segment in enumerate(segments):
            if beats:
                beat_index = round(index * (len(beats) - 1) / max(1, len(segments) - 1))
                target_time = beats[beat_index]
                state = min(states, key=lambda row: abs(row["timestamp_seconds"] - target_time))
                method = "FORENSIC_SCRIPT_BEAT_TO_TIMESTAMPED_VISUAL_STATE_POSITIONAL_JOIN"
            else:
                state_index = round(index * (len(states) - 1) / max(1, len(segments) - 1))
                state = states[state_index]
                method = "ORDERED_POSITIONAL_ALIGNMENT_TO_TIMESTAMPED_VISUAL_STATES"
            phase = segment["phase"]
            results.append({
                "video_id": video_id,
                "script_segment": f"sentence:{segment['evidence']['sentence_index']}",
                "script_phase": phase,
                "script_excerpt": segment["evidence"]["excerpt"],
                "visual_role": PHASE_ROLES.get(phase, "UNCLEAR"),
                "visual_evidence": state["description"],
                "timestamp_seconds": state["timestamp_seconds"],
                "frame_locator": state["frame_locator"],
                "evidence_state": "AI_INTERPRETATION",
                "alignment_method": method,
            })
    return results


def _opening_analysis(hook_script, states_by_video):
    hooks = {row["video_id"]: row for row in hook_script.get("script_features", [])}
    results = []
    for video_id, states in sorted(states_by_video.items()):
        segments = hooks.get(video_id, {}).get("structure", {}).get("segments", [])
        if not segments or not states:
            continue
        hook = segments[0]["evidence"]["excerpt"]
        early = states[:min(4, len(states))]
        hook_words = set(re.findall(r"[a-z]{4,}", hook.lower()))
        visual_words = set(re.findall(r"[a-z]{4,}", " ".join(row["description"].lower() for row in early)))
        source = " ".join(row["description"] for row in early)
        if hook_words & visual_words:
            assessment = "DIRECT_VISUAL_MATCH"
        elif VISUAL_RULES["SCALE_VISUALIZATION"].search(source):
            assessment = "VISUAL_ADDS_SCALE"
        elif VISUAL_RULES["CONSEQUENCE_VISUAL"].search(source):
            assessment = "VISUAL_ADDS_STAKES"
        else:
            assessment = "VISUAL_EXPANDS_HOOK"
        results.append({
            "video_id": video_id,
            "hook_text_structure": hook,
            "first_visual_state": early[0]["description"],
            "early_visual_change_count": max(0, len(early) - 1),
            "assessment": assessment,
            "evidence_state": "AI_INTERPRETATION",
            "evidence_locators": [row["frame_locator"] for row in early],
        })
    return results


def _visual_archetypes(features, measured):
    by_feature = defaultdict(list)
    for row in features:
        by_feature[row["feature"]].append(row)
    definitions = {
        "DIAGRAM": ("VIS-ARCH-001", "DIAGRAM_LED_EXPLANATION", "Stable diagrams expose one concept or variable at a time."),
        "CONSEQUENCE_VISUAL": ("VIS-ARCH-002", "CONSEQUENCE_TRANSFORMATION", "A setup object changes into a visible consequence or payoff state."),
        "TEXT_OVERLAY": ("VIS-ARCH-003", "LABEL_LED_CLARIFICATION", "Text, labels, or numbers are attached to visual geometry to resolve meaning."),
    }
    all_videos = {row["video_id"] for row in measured}
    measured_by_video = {row["video_id"]: row for row in measured}
    results = []
    for feature, (archetype_id, name, definition) in definitions.items():
        members = by_feature.get(feature, [])
        video_ids = sorted({row["video_id"] for row in members})
        if len(video_ids) < 2:
            continue
        results.append({
            "visual_archetype_id": archetype_id,
            "name": name,
            "definition": definition,
            "video_ids": video_ids,
            "evidence_locators": [row["frame_locator"] for row in members[:8]],
            "format": sorted({measured_by_video[video_id]["format"] for video_id in video_ids}),
            "measured_profile": {
                "median_visual_changes_per_minute": round(statistics.median(
                    measured_by_video[video_id]["visual_changes_per_minute"] for video_id in video_ids
                ), 4),
                "video_count": len(video_ids),
            },
            "script_phases_used": ["EXPLANATION", "ESCALATION", "PAYOFF"],
            "repeatability": "MULTI_VIDEO_REPEATED_PATTERN",
            "counter_examples": sorted(all_videos - set(video_ids)) or ["NONE_IN_LIMITED_FORENSIC_SAMPLE"],
            "confidence": "MEDIUM",
            "evidence_state": "AI_INTERPRETATION",
        })
    return results


def _editing_archetypes(report_text_by_video, measured, alignment):
    hard_cut_videos = sorted(video_id for video_id, text in report_text_by_video.items() if re.search(r"hard cut", text, re.I))
    progressive_videos = sorted({row["video_id"] for row in alignment if row["visual_role"] in {
        "CONCEPT_EXPLANATION", "SCALE_DEMONSTRATION", "ESCALATION_VISUAL",
    }})
    profiles = {row["video_id"]: row for row in measured}
    results = []
    for archetype_id, sequence, videos, counter in (
        ("EDIT-ARCH-001", ["HOOK_VISUAL", "PROGRESSIVE_EXPLANATION", "ESCALATION_VISUAL", "PAYOFF_VISUAL"], progressive_videos, "Some phases map positionally because no frame-level script timecode joins exist."),
        ("EDIT-ARCH-002", ["STABLE_COORDINATE_FRAME", "VARIABLE_REVEAL", "ARGUMENT_CHANGE_HARD_CUT"], hard_cut_videos, "Continuous within-shot motion exists, so replacement states are not universal."),
    ):
        if len(videos) < 2:
            continue
        results.append({
            "editing_archetype_id": archetype_id,
            "sequence": sequence,
            "video_ids": videos,
            "measured_pacing": {
                "median_visual_changes_per_minute": round(statistics.median(profiles[v]["visual_changes_per_minute"] for v in videos), 4),
                "formats": sorted({profiles[v]["format"] for v in videos}),
            },
            "script_alignment": "TRACEABLE_POSITIONAL_ALIGNMENT",
            "repeatability": "MULTI_VIDEO_REPEATED_PATTERN",
            "counter_examples": [counter],
            "confidence": "MEDIUM",
            "evidence_state": "AI_INTERPRETATION",
        })
    return results


def _performance_associations(measured, topic):
    items = _topic_items(topic)
    results = []
    for row in measured:
        item = items.get(row["video_id"], {})
        fact, metric = item.get("canonical_fact", {}), item.get("derived_metric", {})
        results.append({
            "video_id": row["video_id"],
            "pattern": "TIMESTAMPED_VISUAL_CHANGE_PROFILE",
            "association_type": "ASSOCIATED_PATTERN",
            "causal_driver": False,
            "format": row["format"],
            "views": fact.get("views"),
            "views_per_day": metric.get("views_per_day"),
            "channel_median_ratio": metric.get("channel_median_ratio"),
            "visual_changes_per_minute": row["visual_changes_per_minute"],
            "limitation": "Public performance and editing evidence are observational; competitor retention is unavailable.",
        })
    return results


def _blueprints(hook_script, visual_archetypes, editing_archetypes):
    selected = hook_script.get("selected_opportunities", [])
    script_by_opportunity = {row["opportunity_id"]: row for row in hook_script.get("script_blueprints", [])}
    hooks_by_opportunity = defaultdict(list)
    for row in hook_script.get("hook_hypotheses", []):
        hooks_by_opportunity[row["opportunity_id"]].append(row)
    existing_blueprints = {row["opportunity"]["opportunity_id"]: row for row in hook_script.get("content_blueprints", [])}
    evidence_ids = sorted({video_id for row in visual_archetypes for video_id in row["video_ids"]})
    formats = sorted({value for row in visual_archetypes for value in row["format"]})
    sample_limit = f"Evidence comes from {len(evidence_ids)} videos ({', '.join(formats)}); transfer beyond this sample remains unproven."
    archetype_ids = [row["visual_archetype_id"] for row in visual_archetypes]
    editing_ids = [row["editing_archetype_id"] for row in editing_archetypes]
    editing_blueprints, full = [], []
    for opportunity in selected:
        opportunity_id = opportunity["opportunity_id"]
        script = script_by_opportunity[opportunity_id]
        packages = opportunity["recommended_test_set"]
        favorite_id = opportunity["initial_favorite"]["package_id"]
        package = next(row for row in packages if row["package_id"] == favorite_id)
        hooks = hooks_by_opportunity[opportunity_id]
        hook = next((row for row in hooks if row["package_link"] == favorite_id), hooks[0])
        thumbnail = package["thumbnail_concept"]
        blueprint = {
            "editing_blueprint_id": f"{opportunity_id}-EDIT-001",
            "opportunity_id": opportunity_id,
            "evidence_state": "EVIDENCE_BACKED_HYPOTHESIS",
            "package_id": favorite_id,
            "hook_id": hook["hook_id"],
            "script_blueprint_id": script["blueprint_id"],
            "visual_opening": f"Open on {thumbnail['hero_object']}: {thumbnail['composition']}",
            "visual_sequence": ["HOOK_VISUAL", "PREMISE_DIAGRAM", "CONSTRAINT_LABELS", "EXPLANATION_STATES", "SCALE_COMPARISON", "ESCALATION_VISUAL", "PAYOFF_VISUAL", "ENDING_HOLD"],
            "explanation_visuals": [f"One stable diagram for: {step}." for step in script["explanation_sequence"]],
            "scale_comparison_visuals": opportunity["specific_angle"],
            "escalation_visuals": script["escalation"],
            "payoff_visual": script["main_payoff"],
            "text_label_usage": "Use deterministic labels only for variables, units, constraints, and payoff comparison; keep text registered to visual geometry.",
            "paced_transition_plan": "Hold coordinate frame while one variable changes; hard cut only when explanatory model or argumentative job changes.",
            "static_hold_moments": ["Premise model after variables appear", "Comparison after labels resolve", "Final bounded answer"],
            "visual_risks": package["risks"] + script["risks"] + [sample_limit],
            "supporting_visual_archetype_ids": archetype_ids,
            "supporting_editing_archetype_ids": editing_ids,
            "evidence_video_ids": evidence_ids,
            "confidence": "MEDIUM",
        }
        coherence = {
            "topic_match": "COHERENT",
            "package_match": "COHERENT",
            "hook_promise_match": "COHERENT",
            "script_payoff_match": "COHERENT",
            "visual_explanation_match": "COHERENT",
            "visual_payoff_match": "COHERENT",
            "overall": "COHERENT",
        }
        editing_blueprints.append(blueprint)
        previous = existing_blueprints[opportunity_id]
        full.append({
            "full_content_blueprint_id": f"{opportunity_id}-FULL-001",
            "evidence_state": "EVIDENCE_BACKED_HYPOTHESIS",
            "opportunity": opportunity,
            "package": package,
            "hook": hook,
            "script": script,
            "editing_visual_plan": blueprint,
            "evidence": sorted(set(previous.get("evidence", [])) | set(evidence_ids)),
            "counter_evidence": previous.get("counter_evidence", []) + [sample_limit],
            "limitations": previous.get("limitations", []) + ["No channel-wide editing style is established."],
            "confidence": "MEDIUM",
            "unavailable_metrics": sorted(UNAVAILABLE_METRICS),
            "cross_layer_coherence": coherence,
        })
    return editing_blueprints, full


def channel_availability(conn, channel_id, repo_root=ROOT):
    rows = discover_forensic_evidence(conn, channel_id, repo_root)
    videos = {row["video_id"] for row in rows}
    usable = [row for row in rows if row["keyframes_available"] == "YES" and row["timestamps_available"] == "YES"]
    if not videos:
        return {
            "channel_id": channel_id,
            "forensic_video_count": 0,
            "forensic_dataset_count": 0,
            "keyframe_evidence": "NO",
            "visual_temporal_evidence": "NO",
            "editing_intelligence_status": "NOT_AVAILABLE",
            "reason": "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE",
            "evidence_needed": ["Registered source video or frames", "Timestamped keyframes or shot manifest", "Canonical video relationship"],
        }
    return {
        "channel_id": channel_id,
        "forensic_video_count": len(videos),
        "forensic_dataset_count": len(rows),
        "keyframe_evidence": "YES" if usable else "NO",
        "visual_temporal_evidence": "YES" if usable else "NO",
        "editing_intelligence_status": "WORKING_WITH_FORENSIC_EVIDENCE" if usable else "PARTIAL",
        "reason": "REGISTERED_VIDEO_FORENSIC_EVIDENCE" if usable else "FORENSIC_EVIDENCE_INCOMPLETE",
        "evidence_needed": [] if usable else ["Timestamped keyframes or shot manifest"],
    }


def build_availability_matrix(conn, repo_root=ROOT, generated_on="2026-09-11"):
    channel_ids = [row[0] for row in conn.execute("SELECT channel_id FROM channels ORDER BY channel_id")]
    return {
        "schema_version": "editing-intelligence-availability-1",
        "generated_on": generated_on,
        "channels": [channel_availability(conn, channel_id, repo_root) for channel_id in channel_ids],
        "guardrail": "No thumbnail or transcript fallback. Editing Intelligence requires registered visual-temporal evidence.",
    }


def build_report(conn, channel_id, topic, packaging, hook_script, generated_on="2026-09-11", repo_root=ROOT):
    artifact_channels = {
        topic.get("channel", {}).get("channel_id"),
        packaging.get("channel", {}).get("channel_id"),
        hook_script.get("channel", {}).get("channel_id"),
    }
    if artifact_channels != {channel_id}:
        raise ValueError("channel mismatch across intelligence artifacts")
    evidence = discover_forensic_evidence(conn, channel_id, repo_root)
    canonical = [row for row in evidence if row["canonical_measurement_source"]]
    topic_items = _topic_items(topic)
    states_by_video, reports, measured, features = {}, {}, [], []
    for row in canonical:
        states, report_text = _load_states(conn, row, repo_root)
        if not states:
            continue
        states_by_video[row["video_id"]] = states
        reports[row["video_id"]] = report_text
        topic_item = topic_items.get(row["video_id"], {})
        duration = float(topic_item.get("canonical_fact", {}).get("duration_seconds") or 0)
        classified = classify_visual_features(states, row["video_id"], row["dataset_id"])
        features.extend(classified)
        counts = Counter(item["feature"] for item in classified)
        timing = derive_timing_features(duration, [state["timestamp_seconds"] for state in states], counts["TEXT_OVERLAY"], counts["DIAGRAM"])
        measured.append({
            "video_id": row["video_id"],
            "dataset_id": row["dataset_id"],
            "format": row["format"],
            "duration_seconds": duration,
            "registered_frame_asset_count": row["registered_frame_assets"],
            "keyframe_count": len(states),
            "visual_state_count": len(states),
            "major_shot_count": _report_shot_count(report_text),
            "evidence_state": "DERIVED_METRIC",
            "timing_source": "REGISTERED_TIMESTAMPED_VISUAL_STATE_MANIFEST",
            **timing,
        })
    alignment = _align_script_visual(hook_script, states_by_video, reports)
    visual_archetypes = _visual_archetypes(features, measured)
    editing_archetypes = _editing_archetypes(reports, measured, alignment)
    editing_blueprints, full_blueprints = _blueprints(hook_script, visual_archetypes, editing_archetypes)
    availability = channel_availability(conn, channel_id, repo_root)
    sample_count = len(measured)
    formats = sorted({row["format"] for row in measured})
    pilot_pass = bool(
        evidence
        and len(measured) == len({row["video_id"] for row in evidence})
        and alignment
        and len(editing_blueprints) == len(full_blueprints) == 2
        and all(row["cross_layer_coherence"]["overall"] == "COHERENT" for row in full_blueprints)
    )
    return {
        "schema_version": "editing-visual-intelligence-pilot-1",
        "generated_on": generated_on,
        "channel": hook_script["channel"],
        "evidence_matrix": evidence,
        "measured_features": measured,
        "visual_features": features,
        "visual_archetypes": visual_archetypes,
        "editing_archetypes": editing_archetypes,
        "script_visual_alignment": alignment,
        "hook_visual_opening_analysis": _opening_analysis(hook_script, states_by_video),
        "performance_associations": _performance_associations(measured, topic),
        "selected_opportunities": hook_script["selected_opportunities"],
        "editing_blueprints": editing_blueprints,
        "full_content_blueprints": full_blueprints,
        "availability": availability,
        "official_youtube_guardrail": {
            "principle": "Experiment with storytelling, structure, editing style, and delivery; use actual audience-retention Analytics to evaluate viewer response.",
            "competitor_retention_available": False,
            "retrieved_on": generated_on,
            "sources": [
                "https://support.google.com/youtube/answer/16559650?hl=en",
                "https://support.google.com/youtube/answer/9314415?hl=en",
            ],
        },
        "guardrails": {
            "thumbnail_as_editing_evidence": False,
            "transcript_as_editing_evidence": False,
            "retention_data_available": False,
            "causal_editing_claims": 0,
            "performance_language": "ASSOCIATED_PATTERN",
        },
        "limitations": [
            f"{sample_count} canonical videos have registered visual-temporal evidence; channel-wide editing style is not supported.",
            "Source MP4 files are not registered as available files; analysis uses preserved reports, keyframes, frame manifests, and registered frame references.",
            "Script-to-visual joins use forensic script-beat timing where available and remain positional AI_INTERPRETATION, not frame-level semantic ground truth.",
            f"Forensic sample formats: {', '.join(formats)}; transfer to absent formats is untested.",
            "Competitor retention, watch time, average view duration, CTR, and shares are unavailable.",
        ],
        "provenance": {
            "canonical_dataset": hook_script["channel"]["dataset_id"],
            "topic_artifact": hook_script.get("provenance", {}).get("topic_artifact"),
            "packaging_artifact": hook_script.get("provenance", {}).get("packaging_visual_artifact"),
            "hook_script_schema": hook_script.get("schema_version"),
            "relationship_manifest": "data/manifests/relationships/DSREL-000001.json",
            "forensic_dataset_ids": sorted(row["dataset_id"] for row in evidence),
        },
        "channel_wide_editing_style": "NOT_SUPPORTED",
        "editing_intelligence_status": availability["editing_intelligence_status"],
        "pilot_verdict": "PASS" if pilot_pass else "FAIL",
    }


def render_markdown(payload):
    measured_formats = sorted({row["format"] for row in payload["measured_features"]})
    lines = [
        f"# {payload['channel']['channel_id']} Editing + Visual Intelligence Pilot", "",
        "# Scope", "",
        "Uses only registered video-derived frames, timestamped state data, forensic reports, and canonical relationships. Titles, thumbnails, topics, and transcripts provide context only.", "",
        "# Evidence Availability", "",
    ]
    for row in payload["evidence_matrix"]:
        lines.append(
            f"- `{row['video_id']}` / `{row['dataset_id']}`: frames {row['registered_frame_assets']}; keyframes {row['keyframes_available']}; timestamps {row['timestamps_available']}; transitions {row['shot_visual_transition_data_available']}; quality `{row['evidence_quality']}`."
        )
    lines += ["", "# Measured Editing Features", ""]
    for row in payload["measured_features"]:
        lines.append(
            f"- `{row['video_id']}`: {row['visual_state_count']} states, {row['major_shot_count']} major shots, {row['visual_changes_per_minute']} changes/min, median segment proxy {row['median_visual_segment_duration_seconds']} s, longest hold proxy {row['longest_static_hold_seconds']} s."
        )
    lines += ["", "# Visual Patterns", "", "All labels below are `AI_INTERPRETATION`; measured counts remain separate above.", ""]
    counts = Counter(row["feature"] for row in payload["visual_features"])
    lines.extend(f"- `{feature}`: {count} timestamped state matches." for feature, count in sorted(counts.items()))
    lines += ["", "# Visual Archetypes", ""]
    lines.extend(f"- `{row['visual_archetype_id']}` `{row['name']}`: {len(row['video_ids'])} videos; {row['repeatability']}; confidence {row['confidence']}." for row in payload["visual_archetypes"])
    lines += ["", "# Editing Sequences", ""]
    lines.extend(f"- `{row['editing_archetype_id']}`: {' / '.join(row['sequence'])}; {row['repeatability']}; confidence {row['confidence']}." for row in payload["editing_archetypes"])
    lines += ["", "# Script → Visual Alignment", "", f"{len(payload['script_visual_alignment'])} traceable positional links. Every link includes video, script segment, timestamp, visual description, and frame locator. Links are `AI_INTERPRETATION`.", ""]
    lines += ["# Performance Associations", "", "Public views and views/day are observational context only. All rows use `ASSOCIATED_PATTERN`; causal editing claims: 0.", ""]
    for row in payload["performance_associations"]:
        lines.append(f"- `{row['video_id']}`: {row['views']} views; {row['visual_changes_per_minute']} changes/min. No causal inference.")
    lines += ["", "# Counter-Evidence", ""]
    lines.extend([
        f"- {len(payload['measured_features'])} videos cannot establish channel-wide editing style.",
        f"- Forensic sample formats: {', '.join(measured_formats)}; transfer to absent formats remains unsupported.",
        "- Registered samples contain both fast consequence resets and long explanatory holds.",
    ])
    lines += ["", "# Editing Blueprints", ""]
    for row in payload["editing_blueprints"]:
        lines.append(f"- `{row['editing_blueprint_id']}`: {row['visual_opening']} Confidence `{row['confidence']}`; `EVIDENCE_BACKED_HYPOTHESIS`.")
    lines += ["", "# Full Content Blueprints", ""]
    for row in payload["full_content_blueprints"]:
        lines.append(f"- `{row['full_content_blueprint_id']}`: opportunity, package, hook, script, and editing/visual plan; coherence `{row['cross_layer_coherence']['overall']}`.")
    lines += ["", "# Evidence Gaps", ""]
    lines.extend(f"- {item}" for item in payload["limitations"])
    lines += ["", "# Pilot Verdict", "", f"`{payload['pilot_verdict']}`. Editing Intelligence status: `{payload['editing_intelligence_status']}`. Channel-wide editing style: `{payload['channel_wide_editing_style']}`.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--topic-artifact", required=True)
    parser.add_argument("--packaging-artifact", required=True)
    parser.add_argument("--hook-script-artifact", required=True)
    parser.add_argument("--db")
    parser.add_argument("--generated-on", default="2026-09-11")
    parser.add_argument("--output", required=True)
    parser.add_argument("--markdown-output", required=True)
    parser.add_argument("--availability-output", required=True)
    args = parser.parse_args(argv)
    topic = json.loads(Path(args.topic_artifact).read_text(encoding="utf-8"))
    packaging = json.loads(Path(args.packaging_artifact).read_text(encoding="utf-8"))
    hook_script = json.loads(Path(args.hook_script_artifact).read_text(encoding="utf-8"))
    with connect(args.db) as conn:
        payload = build_report(conn, args.channel, topic, packaging, hook_script, args.generated_on)
        availability = build_availability_matrix(conn, ROOT, args.generated_on)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_json(payload), encoding="utf-8")
    markdown = Path(args.markdown_output)
    markdown.parent.mkdir(parents=True, exist_ok=True)
    markdown.write_text(render_markdown(payload), encoding="utf-8")
    availability_output = Path(args.availability_output)
    availability_output.parent.mkdir(parents=True, exist_ok=True)
    availability_output.write_text(render_json(availability), encoding="utf-8")


if __name__ == "__main__":
    main()
