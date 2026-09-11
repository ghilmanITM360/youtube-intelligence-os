"""Unified YouTube Intelligence OS orchestrator.

Composes existing Topic / Packaging / Hook / Script / Editing intelligence
artifacts for one (channel, opportunity) pair into one evidence-traceable
content intelligence plan (JSON + Markdown).

This is a COMPOSER / VALIDATOR only:
- read-only against the catalog DB
- never calls YouTube/Apify/the web
- never mutates the DB or regenerates intelligence artifacts
- degrades gracefully (e.g. EDITING -> NOT_AVAILABLE) instead of failing
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from report_common import connect  # noqa: E402

CHANNELS_DIR = REPO_ROOT / "data" / "intelligence" / "channels"
CROSS_CHANNEL_DIR = REPO_ROOT / "data" / "intelligence" / "cross-channel"
PLANS_DIR = REPO_ROOT / "data" / "intelligence" / "plans"
SYSTEM_DIR = REPO_ROOT / "data" / "intelligence" / "system"
EDITING_AVAILABILITY_ARTIFACT = CROSS_CHANNEL_DIR / "editing-intelligence-availability-2026-09-11.json"

SCHEMA_VERSION = "youtube-intelligence-os-content-plan-1"

# Never fabricated: always reported as NOT_AVAILABLE unless a canonical source
# artifact explicitly carries a measured value for one of these.
PRIVATE_METRICS = [
    "CTR", "IMPRESSIONS", "RETENTION", "AVERAGE_VIEW_DURATION", "WATCH_TIME",
    "UNIQUE_VIEWERS", "TRAFFIC_SOURCES", "SUBSCRIBER_CONVERSION",
]

MEDICAL_CHANNELS = {"CH-000003", "CH-000005"}

OFFICIAL_YOUTUBE_GUARDRAILS = {
    "appeal": "Topic/package gets viewer interest and communicates value.",
    "engagement": "Viewer response after choosing to watch.",
    "satisfaction": "Whether viewers enjoyed/found value in the content.",
    "no_proprietary_algorithm_score": True,
    "recommendation_surfaces_differ": True,
    "personalization_matters": True,
    "no_universal_ideal_video_length": True,
    "no_fixed_ctr_target": True,
    "no_fixed_retention_target": True,
    "no_hidden_ranking_weights": True,
    "no_direct_metadata_change_algorithm_boost": True,
}


class OrchestrationError(ValueError):
    """Raised for an unresolvable or malformed (channel, opportunity) request."""


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _pick_current(paths):
    """Deterministic artifact selection: prefer non-pilot files, else the
    lexicographically-last match (dated filenames sort chronologically)."""
    if not paths:
        return None
    non_pilot = sorted(p for p in paths if "pilot" not in p.name)
    return (non_pilot or sorted(paths))[-1]


def channel_dir(channel_id):
    cdir = CHANNELS_DIR / channel_id
    if not cdir.is_dir():
        raise OrchestrationError(f"unknown channel: {channel_id}")
    return cdir


def find_topic_artifact(cdir):
    path = _pick_current(list(cdir.glob("topic-opportunity-intelligence*.json")))
    if path is None:
        raise OrchestrationError(f"no Topic Intelligence artifact for {cdir.name}")
    return path


def find_packaging_artifact(cdir):
    path = _pick_current(list(cdir.glob("packaging-intelligence*.json")))
    if path is None:
        raise OrchestrationError(f"no Packaging Intelligence artifact for {cdir.name}")
    return path


def find_hook_script_artifact(cdir):
    path = _pick_current(list(cdir.glob("hook-script-intelligence*.json")))
    if path is None:
        raise OrchestrationError(f"no Hook/Script Intelligence artifact for {cdir.name}")
    return path


def find_editing_artifact(cdir):
    return _pick_current(list(cdir.glob("editing-visual-intelligence*.json")))


def load_editing_availability():
    if not EDITING_AVAILABILITY_ARTIFACT.exists():
        return {}
    data = load_json(EDITING_AVAILABILITY_ARTIFACT)
    return {row["channel_id"]: row for row in data.get("channels", [])}


def find_candidate(topic_json, opportunity_id):
    for c in topic_json.get("internal_candidates", []):
        if c["candidate_id"] == opportunity_id:
            return c
    return None


def find_composed_blueprint(editing_json, opportunity_id):
    if not editing_json:
        return None
    for fb in editing_json.get("full_content_blueprints", []):
        if fb.get("full_content_blueprint_id", "").startswith(f"{opportunity_id}-FULL") \
                or fb.get("opportunity", {}).get("opportunity_id") == opportunity_id:
            return fb
    return None


def find_opportunity_package(packaging_json, opportunity_id):
    for op in packaging_json.get("opportunity_packages", []):
        candidate = op.get("candidate", {})
        if candidate.get("candidate_id") == opportunity_id:
            return op
    return None


def best_archetype_by_evidence_overlap(archetypes, evidence_ids, id_field):
    """Deterministic join: pick the archetype whose evidence overlaps most
    with the opportunity's supporting video ids. No new interpretation is
    generated -- this only links archetypes already derived by the generic
    reporters."""
    evidence_set = set(evidence_ids)
    scored = []
    for archetype in archetypes:
        pool = set(archetype.get("video_ids") or archetype.get("strong_examples") or [])
        overlap = evidence_set & pool
        if overlap:
            scored.append((len(overlap), archetype[id_field], archetype, sorted(overlap)))
    if not scored:
        return None, []
    scored.sort(key=lambda t: (-t[0], t[1]))
    _, _, archetype, overlap_ids = scored[0]
    return archetype, overlap_ids


def _native_ab_eligibility(formats):
    formats = {f for f in formats if f}
    if formats == {"SHORT_FORM"}:
        return "NO"
    if formats and "SHORT_FORM" not in formats:
        return "POTENTIALLY_ELIGIBLE"
    return "NOT_APPLICABLE"


def _external_validation_for(channel_id, cdir):
    web_validation = list(cdir.glob("*web-validation*.md")) + list(cdir.glob("*web-validation*.json"))
    if web_validation:
        return {
            "state": "EXTERNAL_VALIDATION",
            "source": str(_pick_current(web_validation).relative_to(REPO_ROOT)),
        }
    return "NOT_AVAILABLE"


def _from_composed_blueprint(channel_id, opportunity_id, blueprint, availability, cdir):
    opp = blueprint["opportunity"]
    package = blueprint["package"]
    hook = blueprint["hook"]
    script = blueprint["script"]
    editing_plan = blueprint.get("editing_visual_plan")

    opportunity = {
        "opportunity_id": opportunity_id,
        "topic": opp.get("topic"),
        "angle": opp.get("specific_angle"),
        "confidence": blueprint.get("confidence"),
        "evidence_state": blueprint.get("evidence_state"),
        "internal_evidence": blueprint.get("evidence", []),
        "external_validation": _external_validation_for(channel_id, cdir),
        "risks": [item for r in opp.get("recommended_test_set", []) for item in r.get("risks", [])],
        "falsification_condition": (opp.get("recommended_test_set") or [{}])[0].get("what_not_to_overclaim"),
        "counter_evidence": blueprint.get("counter_evidence", []),
    }

    packaging = {
        "title_hypotheses": [r.get("title_option") for r in opp.get("recommended_test_set", [])],
        "thumbnail_concepts": [r.get("thumbnail_concept") for r in opp.get("recommended_test_set", [])],
        "package_archetypes": package.get("historical_support", {}).get("package_archetype_ids", []),
        "temporal_evidence_state": package.get("evidence_state"),
        "native_ab_eligibility": _native_ab_eligibility(
            {r.get("format_context") for r in opp.get("recommended_test_set", [])} | {opp.get("format_decision")}
        ),
        "confidence": package.get("confidence"),
        "selected_package": package,
    }

    hook_out = {
        "hook_hypotheses": [hook.get("hook_text")],
        "hook_archetypes": [hook.get("hook_archetype")],
        "package_linkage": hook.get("package_link"),
        "evidence": hook.get("supporting_video_ids", []),
        "counter_evidence": [hook.get("counter_evidence")] if hook.get("counter_evidence") else [],
        "selected_hook": hook,
    }

    script_out = {
        "script_blueprint": script.get("blueprint_id"),
        "script_archetype": script.get("script_archetype"),
        "payoff_structure": {
            "explanation_sequence": script.get("explanation_sequence", []),
            "escalation": script.get("escalation"),
            "ending": script.get("ending"),
            "intermediate_payoffs": script.get("intermediate_payoffs", []),
        },
        "evidence": script.get("supporting_video_ids", []),
        "limitations": blueprint.get("limitations", []),
        "selected_script": script,
    }

    editing_out = {
        "status": "AVAILABLE" if editing_plan else "NOT_AVAILABLE",
        "reason": None if editing_plan else availability.get("reason", "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE"),
        "blueprint": editing_plan,
        "channel_wide_editing_style": "NOT_SUPPORTED",
    }

    return {
        "opportunity": opportunity,
        "packaging": packaging,
        "hook": hook_out,
        "script": script_out,
        "editing": editing_out,
        "generation_state": "COMPOSED_FROM_EXISTING_BLUEPRINT",
    }


def _from_assembled_layers(channel_id, opportunity_id, candidate, opp_package, hook_script_json, availability, cdir):
    evidence_ids = candidate.get("supporting_video_ids", [])

    hook_archetype, hook_overlap = best_archetype_by_evidence_overlap(
        hook_script_json.get("hook_archetypes", []), evidence_ids, "hook_archetype_id"
    )
    script_archetype, script_overlap = best_archetype_by_evidence_overlap(
        hook_script_json.get("script_archetypes", []), evidence_ids, "script_archetype_id"
    )

    test_set = opp_package.get("recommended_test_set", []) if opp_package else []

    opportunity = {
        "opportunity_id": opportunity_id,
        "topic": candidate.get("topic"),
        "angle": candidate.get("specific_angle"),
        "confidence": candidate.get("initial_confidence"),
        "evidence_state": candidate.get("evidence_state"),
        "internal_evidence": evidence_ids,
        "external_validation": _external_validation_for(channel_id, cdir),
        "risks": [item for r in test_set for item in r.get("risks", [])],
        "falsification_condition": candidate.get("counter_evidence"),
        "counter_evidence": [candidate.get("counter_evidence")] if candidate.get("counter_evidence") else [],
    }

    packaging = {
        "title_hypotheses": [r.get("title") for r in test_set],
        "thumbnail_concepts": [r.get("thumbnail_concept") for r in test_set],
        "package_archetypes": sorted({r.get("thumbnail_archetype") for r in test_set if r.get("thumbnail_archetype")}),
        "temporal_evidence_state": "HYPOTHESIS_FOR_TESTING" if test_set else "NOT_AVAILABLE",
        "native_ab_eligibility": _native_ab_eligibility({r.get("format_context") for r in test_set}),
        "confidence": candidate.get("initial_confidence"),
        "selected_package": opp_package,
    }

    hook_out = {
        "hook_hypotheses": [hook_archetype["definition"]] if hook_archetype else [],
        "hook_archetypes": [hook_archetype["hook_archetype_id"]] if hook_archetype else [],
        "package_linkage": "EVIDENCE_OVERLAP_JOIN" if hook_archetype else None,
        "evidence": hook_overlap,
        "counter_evidence": (hook_archetype or {}).get("counter_examples", []),
        "selected_hook": hook_archetype,
    }

    script_out = {
        "script_blueprint": (script_archetype or {}).get("definition"),
        "script_archetype": (script_archetype or {}).get("structure_sequence"),
        "payoff_structure": {"structure_sequence": (script_archetype or {}).get("structure_sequence", [])},
        "evidence": script_overlap,
        "limitations": [
            "Hook/script linkage derived by evidence-video overlap, not an authored per-opportunity blueprint."
        ],
        "selected_script": script_archetype,
    }

    editing_out = {
        "status": "NOT_AVAILABLE",
        "reason": availability.get("reason", "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE"),
        "blueprint": None,
        "channel_wide_editing_style": "NOT_SUPPORTED",
    }

    return {
        "opportunity": opportunity,
        "packaging": packaging,
        "hook": hook_out,
        "script": script_out,
        "editing": editing_out,
        "generation_state": "ASSEMBLED_FROM_LAYERS",
    }


def _video_ids_exist(conn, video_ids):
    if not video_ids:
        return True
    placeholders = ",".join("?" for _ in video_ids)
    rows = conn.execute(
        f"SELECT video_id FROM videos WHERE video_id IN ({placeholders})", list(video_ids)
    ).fetchall()
    return {r["video_id"] for r in rows} == set(video_ids)


def validate_coherence(channel_id, opportunity_id, plan, conn):
    dims = {}

    ids_with_prefix = [
        plan["hook"].get("package_linkage"),
        *(plan["hook"].get("hook_archetypes") or []),
    ]
    dims["CHANNEL_MATCH"] = "PASS" if plan["opportunity"]["opportunity_id"].startswith(channel_id) else "FAIL"
    dims["OPPORTUNITY_MATCH"] = "PASS" if plan["opportunity"]["opportunity_id"] == opportunity_id else "FAIL"
    dims["TOPIC_MATCH"] = "PASS" if plan["opportunity"].get("topic") else "FAIL"

    if plan["generation_state"] == "COMPOSED_FROM_EXISTING_BLUEPRINT":
        selected_hook = plan["hook"]["selected_hook"] or {}
        selected_script = plan["script"]["selected_script"] or {}
        selected_package = plan["packaging"]["selected_package"] or {}
        editing_bp = plan["editing"]["blueprint"]

        dims["PACKAGE_PROMISE_MATCH"] = (
            "PASS" if selected_hook.get("package_link") == selected_package.get("package_id") else "PARTIAL"
        )
        dims["HOOK_PROMISE_MATCH"] = (
            "PASS" if selected_hook.get("hook_id") in (selected_script.get("hook_links") or []) else "PARTIAL"
        )
        dims["SCRIPT_PAYOFF_MATCH"] = "PASS" if selected_script.get("ending") else "FAIL"
        if editing_bp:
            dims["EDITING_VISUAL_MATCH"] = (
                "PASS" if editing_bp.get("hook_id") == selected_hook.get("hook_id")
                and editing_bp.get("package_id") == selected_package.get("package_id") else "PARTIAL"
            )
        else:
            dims["EDITING_VISUAL_MATCH"] = "NOT_APPLICABLE"
        dims["FORMAT_MATCH"] = "PARTIAL" if plan["packaging"]["native_ab_eligibility"] == "NOT_APPLICABLE" else "PASS"
    else:
        dims["PACKAGE_PROMISE_MATCH"] = "PASS" if plan["packaging"]["selected_package"] else "FAIL"
        dims["HOOK_PROMISE_MATCH"] = "PARTIAL" if plan["hook"]["selected_hook"] else "FAIL"
        dims["SCRIPT_PAYOFF_MATCH"] = "PARTIAL" if plan["script"]["selected_script"] else "FAIL"
        dims["EDITING_VISUAL_MATCH"] = "NOT_APPLICABLE"
        dims["FORMAT_MATCH"] = "PARTIAL" if plan["packaging"]["native_ab_eligibility"] == "NOT_APPLICABLE" else "PASS"

    all_video_ids = set(plan["opportunity"].get("internal_evidence") or [])
    all_video_ids |= set(plan["hook"].get("evidence") or [])
    all_video_ids |= set(plan["script"].get("evidence") or [])
    dims["EVIDENCE_TRACEABILITY"] = "PASS" if _video_ids_exist(conn, all_video_ids) else "FAIL"

    dims["UNAVAILABLE_METRICS_DISCLOSED"] = "PASS"
    dims["TEMPORAL_LIMITATIONS_PRESERVED"] = (
        "PASS" if (plan["opportunity"].get("counter_evidence") or plan["script"].get("limitations")) else "FAIL"
    )

    values = set(dims.values())
    if "FAIL" in values:
        overall = "INCOHERENT"
    elif "PARTIAL" in values:
        overall = "PARTIAL"
    else:
        overall = "COHERENT"

    return {"dimensions": dims, "overall": overall}


def build_plan(channel_id, opportunity_id, generated_on=None):
    cdir = channel_dir(channel_id)
    topic_path = find_topic_artifact(cdir)
    packaging_path = find_packaging_artifact(cdir)
    hook_script_path = find_hook_script_artifact(cdir)
    editing_path = find_editing_artifact(cdir)

    topic_json = load_json(topic_path)
    packaging_json = load_json(packaging_path)
    hook_script_json = load_json(hook_script_path)
    editing_json = load_json(editing_path) if editing_path else None

    channel_fact = topic_json.get("channel", {})
    if channel_fact.get("channel_id") != channel_id:
        raise OrchestrationError("channel mismatch between request and topic artifact")

    availability = load_editing_availability().get(channel_id, {
        "editing_intelligence_status": "NOT_AVAILABLE",
        "reason": "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE",
    })

    composed = find_composed_blueprint(editing_json, opportunity_id)
    if composed is not None:
        layers = _from_composed_blueprint(channel_id, opportunity_id, composed, availability, cdir)
    else:
        candidate = find_candidate(topic_json, opportunity_id)
        if candidate is None:
            raise OrchestrationError(
                f"opportunity {opportunity_id!r} not found in Topic Intelligence for {channel_id}"
            )
        opp_package = find_opportunity_package(packaging_json, opportunity_id)
        layers = _from_assembled_layers(
            channel_id, opportunity_id, candidate, opp_package, hook_script_json, availability, cdir
        )

    plan = {
        "schema_version": SCHEMA_VERSION,
        "generated_on": generated_on or "2026-09-11",
        "channel_id": channel_id,
        "opportunity_id": opportunity_id,
        "channel": channel_fact,
        "generation_state": layers["generation_state"],
        "opportunity": layers["opportunity"],
        "packaging": layers["packaging"],
        "hook": layers["hook"],
        "script": layers["script"],
        "editing": layers["editing"],
        "global": {
            "provenance": {
                "topic_artifact": str(topic_path.relative_to(REPO_ROOT)),
                "packaging_artifact": str(packaging_path.relative_to(REPO_ROOT)),
                "hook_script_artifact": str(hook_script_path.relative_to(REPO_ROOT)),
                "editing_artifact": str(editing_path.relative_to(REPO_ROOT)) if editing_path else None,
                "canonical_dataset": channel_fact.get("dataset_id"),
            },
            "unavailable_metrics": {metric: "NOT_AVAILABLE" for metric in PRIVATE_METRICS},
            "platform_guardrails": OFFICIAL_YOUTUBE_GUARDRAILS,
            "evidence_quality_summary": layers["opportunity"].get("evidence_state"),
            "warnings": (
                [] if layers["editing"]["status"] == "AVAILABLE"
                else [f"EDITING NOT_AVAILABLE: {layers['editing']['reason']}"]
            ),
            "generation_state": layers["generation_state"],
            "medical_validation_required": (
                channel_id in MEDICAL_CHANNELS
                and layers["opportunity"].get("external_validation") == "NOT_AVAILABLE"
            ),
        },
    }

    with connect() as conn:
        plan["coherence"] = validate_coherence(channel_id, opportunity_id, plan, conn)

    return plan


def render_markdown(plan):
    opp = plan["opportunity"]
    pkg = plan["packaging"]
    hook = plan["hook"]
    script = plan["script"]
    editing = plan["editing"]
    coherence = plan["coherence"]

    lines = [
        "# Content Intelligence Plan",
        "",
        "## Channel",
        f"- {plan['channel_id']} ({plan['channel'].get('display_name', 'unknown')})",
        "",
        "## Opportunity",
        f"- ID: {opp['opportunity_id']}",
        f"- Topic: {opp.get('topic')}",
        f"- Angle: {opp.get('angle')}",
        f"- Confidence: {opp.get('confidence')} ({opp.get('evidence_state')})",
        "",
        "## Why This Opportunity",
        f"- {opp.get('angle') or 'See topic intelligence.'}",
        "",
        "## Evidence",
        f"- Internal video evidence: {', '.join(opp.get('internal_evidence') or []) or 'NOT_AVAILABLE'}",
        f"- External validation: {opp.get('external_validation')}",
        "",
        "## Packaging Options",
    ]
    for title in pkg.get("title_hypotheses") or []:
        lines.append(f"- {title}")
    lines += [
        f"- Native A/B eligibility: {pkg.get('native_ab_eligibility')}",
        "",
        "## Hook Options",
    ]
    for h in hook.get("hook_hypotheses") or []:
        lines.append(f"- {h}")
    lines += [
        "",
        "## Script Blueprint",
        f"- {script.get('script_blueprint')}",
        "",
        "## Editing / Visual Plan",
        f"- Status: {editing['status']}" + (f" ({editing['reason']})" if editing["reason"] else ""),
        "",
        "## Cross-Layer Coherence",
        f"- Overall: {coherence['overall']}",
    ]
    for dim, verdict in coherence["dimensions"].items():
        lines.append(f"  - {dim}: {verdict}")
    lines += [
        "",
        "## Risks",
    ]
    for risk in opp.get("risks") or []:
        lines.append(f"- {risk}")
    lines += [
        "",
        "## What Is Unknown",
    ]
    for metric, state in plan["global"]["unavailable_metrics"].items():
        lines.append(f"- {metric}: {state}")
    lines += [
        "",
        "## Validation Needed",
        f"- Medical validation required: {plan['global']['medical_validation_required']}",
        "",
        "## Provenance",
    ]
    for key, value in plan["global"]["provenance"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    return "\n".join(lines)


def write_outputs(plan, output_dir=None):
    output_dir = Path(output_dir) if output_dir else PLANS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{plan['opportunity_id']}-content-intelligence-v1"
    json_path = output_dir / f"{stem}.json"
    md_path = output_dir / f"{stem}.md"
    json_path.write_text(json.dumps(plan, indent=2, sort_keys=True), encoding="utf-8")
    md_path.write_text(render_markdown(plan), encoding="utf-8")
    return json_path, md_path


def build_capability_registry(generated_on=None):
    availability = load_editing_availability()
    channels = []
    for cdir in sorted(CHANNELS_DIR.iterdir()):
        if not cdir.is_dir():
            continue
        channel_id = cdir.name
        has_topic = bool(list(cdir.glob("topic-opportunity-intelligence*.json")))
        has_packaging = bool(list(cdir.glob("packaging-intelligence*.json")))
        has_hook_script = bool(list(cdir.glob("hook-script-intelligence*.json")))
        editing_row = availability.get(channel_id, {})
        editing_status = editing_row.get("editing_intelligence_status", "NOT_AVAILABLE")
        if editing_status == "WORKING_WITH_FORENSIC_EVIDENCE":
            editing_status = "WORKING_WITH_LIMITATIONS"

        def _layer(present, reason_if_missing="NO_ARTIFACT_REGISTERED"):
            return {"status": "WORKING" if present else "NOT_AVAILABLE",
                     "reason": None if present else reason_if_missing}

        channels.append({
            "channel_id": channel_id,
            "TOPIC": _layer(has_topic),
            "PACKAGING": _layer(has_packaging),
            "HOOK": _layer(has_hook_script),
            "SCRIPT": _layer(has_hook_script),
            "EDITING": {
                "status": editing_status,
                "reason": editing_row.get("reason", "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE"),
            },
        })

    return {
        "schema_version": "youtube-intelligence-os-v1-capabilities-1",
        "generated_on": generated_on or "2026-09-11",
        "channels": channels,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel")
    parser.add_argument("--opportunity")
    parser.add_argument("--output-dir")
    parser.add_argument("--generated-on")
    parser.add_argument("--json-only", action="store_true")
    parser.add_argument("--capability-registry", action="store_true",
                         help="Emit the global capability registry instead of a single plan.")
    args = parser.parse_args(argv)

    if args.capability_registry:
        registry = build_capability_registry(generated_on=args.generated_on)
        SYSTEM_DIR.mkdir(parents=True, exist_ok=True)
        out_path = SYSTEM_DIR / "youtube-intelligence-os-v1-capabilities-2026-09-11.json"
        out_path.write_text(json.dumps(registry, indent=2, sort_keys=True), encoding="utf-8")
        print(out_path)
        return 0

    if not args.channel or not args.opportunity:
        parser.error("--channel and --opportunity are required unless --capability-registry is set")

    plan = build_plan(args.channel, args.opportunity, generated_on=args.generated_on)
    json_path, md_path = write_outputs(plan, args.output_dir)
    print(json_path)
    if not args.json_only:
        print(md_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
