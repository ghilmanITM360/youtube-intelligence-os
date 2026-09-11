"""Channel Strategy Intelligence -- Phase 4 pilot (Step 22A).

Composes ALREADY-COMPUTED Topic/Packaging/Hook/Script Intelligence artifacts
(never re-reads the catalog DB for performance data) into:

- a channel strategic diagnosis (what works, what doesn't, why)
- a peer benchmark between two or more channels
- CONTINUE/DOUBLE_DOWN/FIX/REDUCE/STOP/TEST/WATCH actions, each evidence-backed
- a new-channel strategy blueprint for a niche

Also carries a compact, provenance-tagged training-knowledge registry built
from DS-000011 (17-document creative/creator corpus) and DS-000018 (33
already-validated 2026 algorithm claims) -- no re-derivation of validation
that already exists.

This module is a COMPOSER/DIAGNOSER only:
- read-only against already-written JSON artifacts (no DB writes)
- never calls YouTube/Apify/the web
- never invents private analytics (CTR/impressions/retention/... stay NOT_AVAILABLE)
- never promotes association into causation (CAUSALITY_STATUS is always ASSOCIATION_ONLY)
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from run_youtube_intelligence import (  # noqa: E402
    channel_dir, find_topic_artifact, find_packaging_artifact,
    find_hook_script_artifact, load_json, OrchestrationError,
)

SYSTEM_DIR = REPO_ROOT / "data" / "intelligence" / "system"
CHANNELS_DIR = REPO_ROOT / "data" / "intelligence" / "channels"
CROSS_CHANNEL_DIR = REPO_ROOT / "data" / "intelligence" / "cross-channel"
BLUEPRINTS_DIR = REPO_ROOT / "data" / "intelligence" / "blueprints"

TRAINING_REGISTRY_SCHEMA = "youtube-strategy-training-knowledge-1"
DIAGNOSIS_SCHEMA = "channel-strategy-diagnosis-1"
BENCHMARK_SCHEMA = "channel-strategy-benchmark-1"
BLUEPRINT_SCHEMA = "channel-strategy-blueprint-1"

VIDEO_PERFORMANCE_STATES = [
    "BREAKOUT", "REPEATABLE_WINNER_EXAMPLE", "STRONG_RELATIVE_PERFORMER",
    "BASELINE", "WEAK_RELATIVE_PERFORMER", "FAILED_EXPERIMENT",
    "ONE_OFF_OUTLIER", "INSUFFICIENT_EVIDENCE",
]
FAMILY_HEALTH_STATES = [
    "REPEATABLE_WINNER_FAMILY", "EMERGING_FAMILY", "MIXED_FAMILY",
    "ONE_OFF_DEPENDENT", "WEAK_FAMILY", "VOLATILE_FAMILY", "INSUFFICIENT_SAMPLE",
]
ACTION_TYPES = [
    "CONTINUE", "DOUBLE_DOWN", "FIX", "REDUCE", "STOP", "TEST", "WATCH",
    "INSUFFICIENT_EVIDENCE",
]
ROOT_CAUSE_LAYERS = [
    "TOPIC_SELECTION", "AUDIENCE_FIT", "SATURATION", "PACKAGING",
    "HOOK_PROMISE_MATCH", "SCRIPT_STRUCTURE", "VISUAL_EDITING", "FORMAT",
    "TIMING_MARKET_CONTEXT", "INSUFFICIENT_EVIDENCE",
]
PRIVATE_METRICS = [
    "CTR", "IMPRESSIONS", "RETENTION", "AVD", "WATCH_TIME",
    "TRAFFIC_SOURCES", "NEW_CASUAL_REGULAR_VIEWERS", "AUDIENCE_OVERLAP",
]

CHANNEL_DISPLAY_NAMES = {
    "CH-000001": "Matty Invests",
    "CH-000002": "Mr. Finance",
    "CH-000003": "Dr. Aliza Wright | Advice",
    "CH-000004": "xkcd's What If?",
    "CH-000005": "Dr. Elias Senior Health",
}

# ---------------------------------------------------------------------------
# Training-knowledge registry
#
# DS-000011 rows: one compact rule per characterized document (see
# data/manifests/DS-000011.md / document_records table). DOC-000002 and
# DOC-000003 are a proven byte-identical pair (see document_records notes),
# so they share one rule with both source locators.
#
# DS-000018 rows: one rule per already-validated claim/interpretation/
# recommendation. PRIMARY_VALIDATION_STATUS is copied verbatim from the
# Final DS-000018 Validation Synthesis (Step 15C-R) -- not re-derived here.
# ---------------------------------------------------------------------------

TRAINING_RULES = [
    # --- DS-000011: creative frameworks / creator heuristics / diagnostics ---
    dict(RULE_ID="TR-011-001", DOMAIN="CREATIVE_VISUAL", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="Six AI engines can be assigned cinematic 'filmmaker persona' lenses (strengths/weaknesses/psychological mode) for collaborative script and story analysis.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000001 Engine-by-Engine Personality & Lens",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="AI-collaboration workflow meta-framework only.",
         PROHIBITED_USE="Do not treat engine 'personalities' as a platform ranking mechanism.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-002", DOMAIN="HOOK", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="The 3-Step Hook Formula: Context Lean (establish a relatable frame) -> Scroll-Stop word/beat (pattern interrupt) -> Contrarian Snapback (reveal the real, counter-expectation payoff).",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000002/DOC-000003 Hook (1).pdf / Hook guide.pdf (proven byte-identical pair)",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="CORPUS_PARTIALLY_SUPPORTED",
         SAFE_DOWNSTREAM_USE="Diagnostic lens for reviewing an existing hook's structure (maps to the CONTEXT_FIRST measured hook archetype).",
         PROHIBITED_USE="Do not claim this guarantees retention -- retention itself is NOT_AVAILABLE in this corpus.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-003", DOMAIN="HOOK", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="Intro Analyzer: judge a video's first 0-30 seconds for hook clarity, curiosity, emotional tone, and algorithmic fit.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000004 Intro Analyzer Prompts",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Qualitative checklist for reviewing a hook/intro draft.",
         PROHIBITED_USE="Do not convert 'algorithmic fit' language into a measured ranking signal.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-004", DOMAIN="PACKAGING", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Packaging SOP: know the target audience first; thumbnails should use bright/natural colors, bold/big fonts with fewer words, and sell one big idea; titles should be short (one sentence) and matched to broad-vs-narrow targeting.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000005 Packaging (Thumbnail/Title) - SOP",
         SOURCE_QUALITY="HUMAN_AUTHORED_DIRECT", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="CORPUS_PARTIALLY_SUPPORTED",
         SAFE_DOWNSTREAM_USE="Packaging design checklist; genuineness ('no fake attention') aligns with official satisfaction guardrail.",
         PROHIBITED_USE="Do not treat the stated '10%+ CTR' figure as a universal target -- no fixed CTR target exists.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-005", DOMAIN="RETENTION_HEURISTIC", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="The same SOP claims a video's first ~10 seconds function as 'the new packaging' because YouTube autoplays, so early-video CTR-like effects matter as much as thumbnail/title.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000005 Packaging (Thumbnail/Title) - SOP",
         SOURCE_QUALITY="HUMAN_AUTHORED_DIRECT", PRIMARY_VALIDATION_STATUS="NOT_CURRENTLY_VERIFIABLE",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Treat as an unverified creator hypothesis about autoplay behavior.",
         PROHIBITED_USE="Do not present as an official platform mechanism; first-30-second retention data is NOT_AVAILABLE here.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-006", DOMAIN="STORYTELLING", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="Renae Creative Engine v2.5: a 7-engine architecture fusing cinematic storytelling, emotional psychology, and the 16 Commandments of Storytelling into one authoring system.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000006 Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Meta-framework for script review; individual commandments (see TR-011-014) are the calibratable unit.",
         PROHIBITED_USE="Do not treat as a validated retention mechanism.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-007", DOMAIN="SCRIPT", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="Script Analyzer: judge a full script's hook, narrative spine, cinematic imagination, retention mechanics, CTA/monetization, and title/thumbnail alignment.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000007 Script Analyzer",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="CORPUS_PARTIALLY_SUPPORTED",
         SAFE_DOWNSTREAM_USE="Maps to the measured CALCULATED_ESCALATION/CONSEQUENCE_CHAIN script archetypes as a diagnostic lens.",
         PROHIBITED_USE="Do not infer retention from this checklist alone -- retention stays NOT_AVAILABLE.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-008", DOMAIN="CREATIVE_VISUAL", RULE_TYPE="PROMPTING_TECHNIQUE",
         RULE_TEXT="'Nano-Banana' prompt structure guide for AI image generation/editing: prompt structure, editing verbs, camera/lighting glossary, master prompt template.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000008 The Ultimate Nano-Banana Prompt Guide",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Thumbnail/creative asset prompting reference only.",
         PROHIBITED_USE="Not a channel-strategy or algorithm rule.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-009", DOMAIN="CREATIVE_VISUAL", RULE_TYPE="PROMPTING_TECHNIQUE",
         RULE_TEXT="Google VEO 3 prompting playbook: capabilities, prompt formulas, dialogue/audio, camera language, and JSON prompting for AI video generation.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000009 Ultimate Google VEO 3 Prompt Guide for VIRAL Videos",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="AI-video prompting reference only.",
         PROHIBITED_USE="Not a channel-strategy or algorithm rule; the phrase 'for VIRAL videos' is marketing framing, not a validated outcome.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-010", DOMAIN="HOOK", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="Viral Checklist item -- Audience Pain Point: name a specific pain/desire/challenge the audience already has.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000010 Viral Checklist (Codie Sanchez), item 1",
         SOURCE_QUALITY="CREATOR_ATTRIBUTED", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Hook/title drafting checklist item.",
         PROHIBITED_USE="Not independently measurable from title/hook archetype fields alone.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-011", DOMAIN="TITLE", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="Viral Checklist item -- Specificity & Numbers: stats, details, or concrete numbers make a hook/title more actionable.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000010 Viral Checklist (Codie Sanchez), item 5",
         SOURCE_QUALITY="CREATOR_ATTRIBUTED", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="MIXED",
         SAFE_DOWNSTREAM_USE="Directly calibratable against the measured NUMBERED_SPECIFICITY title archetype and NUMBER_LED hook archetype.",
         PROHIBITED_USE="Do not generalize a single channel's positive result to all channels -- see cross-channel evidence.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-012", DOMAIN="HOOK", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="Viral Checklist item -- Contrarian Thinking: an idea that challenges conventional wisdom.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000010 Viral Checklist (Codie Sanchez), item 4",
         SOURCE_QUALITY="CREATOR_ATTRIBUTED", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="INSUFFICIENT_EVIDENCE",
         SAFE_DOWNSTREAM_USE="Maps to the measured COUNTERINTUITIVE_PREMISE hook archetype, which is corpus-wide too sparse (1-2 items/channel) to calibrate -- see the CH-000001 single-item 281x ratio counter-example.",
         PROHIBITED_USE="Do not promote the single extreme CH-000001 counterintuitive-premise ratio into a general rule -- one item is not a repeatable pattern.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-013", DOMAIN="TITLE", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="Title Analyzer: opens with creator notes on title psychology and 7 viral title formulas, framed against YouTube's 'Viewer Satisfaction' signal language, before AI-persona title-rewrite prompts.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000011 YouTube Title Analyzer",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_CURRENTLY_VERIFIABLE",
         EMPIRICAL_CALIBRATION_STATUS="MIXED",
         SAFE_DOWNSTREAM_USE="Title-drafting checklist; the 7 formulas map loosely onto measured title archetypes (QUESTION, NUMBERED_SPECIFICITY, WARNING_OR_RISK, ...).",
         PROHIBITED_USE="Do not treat 'Viewer Satisfaction' language here as equivalent to the official Appeal/Engagement/Satisfaction framework without independent confirmation.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-014", DOMAIN="STORYTELLING", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="16 Commandments of Storytelling: script quality judged across story arc, promise alignment, narrative spine, retention engineering, and cinematic energy.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000017 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated)",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="CORPUS_PARTIALLY_SUPPORTED",
         SAFE_DOWNSTREAM_USE="'Promise alignment' commandment maps directly to the HOOK_PROMISE_MATCH root-cause layer already used in unified plan coherence checks.",
         PROHIBITED_USE="Do not treat commandment adherence as a guaranteed retention driver -- retention is NOT_AVAILABLE.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-015", DOMAIN="STORYTELLING", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="'BUT/THEREFORE' causal storytelling: chain scenes and script beats with 'but' (complication) and 'therefore' (consequence) instead of flat 'and then' sequencing.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000015 The Magic of 'BUT' and 'THEREFORE' in Storytelling",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="CORPUS_PARTIALLY_SUPPORTED",
         SAFE_DOWNSTREAM_USE="Maps to the measured CONSEQUENCE_CHAIN script archetype (causal escalation) as a diagnostic lens.",
         PROHIBITED_USE="Do not claim causal-chain scripting causes higher retention -- retention is NOT_AVAILABLE; only views-per-day association is measured.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-011-016", DOMAIN="SEO", RULE_TYPE="DIAGNOSTIC_HEURISTIC",
         RULE_TEXT="YouTube Video SEO checklist: phase-by-phase keyword research, script/video-quality optimization, title/description/tag optimization, and thumbnail SEO.",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000016 YouTube Video SEO - COMPLETE CHECKLIST DOCUMENT",
         SOURCE_QUALITY="HUMAN_AUTHORED_DIRECT", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Publishing/metadata checklist.",
         PROHIBITED_USE="Do not treat keyword-density claims as a confirmed ranking mechanism.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-011-017", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CREATIVE_FRAMEWORK",
         RULE_TEXT="'YouTube Intelligence Brain v1' operating system: unifies research, ideation, packaging, scripting, retention engineering, SEO, and publishing for a senior-health/doctor-led channel around an explicit truth-hierarchy and evidence-labeling discipline (this repository's own evidence-layer vocabulary traces to this document).",
         SOURCE_ID="DS-000011", SOURCE_LOCATOR="DOC-000013 YouTube Intelligence Brain v1.0 - Verified Creator Operating System",
         SOURCE_QUALITY="AI_GENERATED_SYNTHESIS", PRIMARY_VALIDATION_STATUS="NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM",
         EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Directly relevant meta-framework for the CH-000003/CH-000005 senior-health/health niche diagnosis and blueprint.",
         PROHIBITED_USE="Do not treat as validated platform mechanism; it is a creator operating-system template.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),

    # --- DS-000018: 33 already-validated 2026 Algorithm Update claims ---
    dict(RULE_ID="TR-018-CLM-001", DOMAIN="AUDIENCE", RULE_TYPE="PLATFORM_FACT",
         RULE_TEXT="Recommendations are selected per-viewer at surface load time, using viewer history and current context to rank candidates for that viewer.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-001", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="General personalization framing.", PROHIBITED_USE="Do not infer a specific ranking formula from this.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-CLM-002", DOMAIN="AUDIENCE", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Early subscriber response is not one global verdict; the system can learn different responses for subscribers, non-subscribers, and new viewers.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-002", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Bounded hypothesis only.", PROHIBITED_USE="Do not assume an exact three-cohort training architecture.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-003", DOMAIN="PUBLISHING", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Initial performance is not the sole basis for later recommendations; evergreen videos may receive most views well after publication.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-003", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Supports LONGITUDINAL_TREND=NOT_AVAILABLE discipline (later discovery is possible but not measured here).",
         PROHIBITED_USE="Do not claim a majority-of-lifetime-views outcome as measured.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-004", DOMAIN="RETENTION_HEURISTIC", RULE_TYPE="PLATFORM_FACT",
         RULE_TEXT="Long-term viewer value is the broad ranking objective; ranking uses multiple context-dependent signals rather than one universal metric or fixed weight.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-004", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Grounds the 'no single success score' system rule.", PROHIBITED_USE="Do not collapse into one score.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-CLM-005", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Channels should align with audiences; recommendations may still distinguish topic, length, Shorts/long-form/podcast/live-stream preferences within one channel.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-005", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Bounded hypothesis; conflicts with CLM-018.", PROHIBITED_USE="Do not treat mixing formats on one channel as risk-free.",
         CONFLICTS=["TR-018-CLM-018"], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-006", DOMAIN="AUDIENCE", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A suggested video need not share the current video's topic; personalization can connect cross-topic videos through a viewer's broader interests.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-006", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="General framing only.", PROHIBITED_USE="No exact cross-topic matcher mechanism is established.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-007", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="New channels/fresh videos can be matched to viewers without prior channel-viewer history, using topical preferences and subject understanding.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-007", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Supports new-channel blueprint cold-start framing.", PROHIBITED_USE="No exact first-upload audience-assignment mechanism is established.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-008", DOMAIN="AUDIENCE", RULE_TYPE="PLATFORM_FACT",
         RULE_TEXT="A subscription does not imply interest in every upload; the system seeks the interested subset rather than relying on aggregate subscriber click behavior.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-008", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Subscribers are not a guaranteed audience.", PROHIBITED_USE="No numerical subscriber-CTR gate is validated.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-CLM-009", DOMAIN="FORMAT", RULE_TYPE="PLATFORM_FACT",
         RULE_TEXT="Literal near-identical templated repetition may be treated as spam, while a reusable format with genuinely differing episodes can remain acceptable.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-009", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Supports 'repeatable format' vs 'templated spam' distinction in family health labeling.",
         PROHIBITED_USE="Do not infer a specific ranking penalty.", CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-CLM-010", DOMAIN="PUBLISHING", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A subscription-feed recommendation shelf can select from subscribed channels using recent interests while a chronological feed remains available below it.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-010", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Bounded context only.", PROHIBITED_USE="Do not assume universal rollout.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-011", DOMAIN="AUDIENCE", RULE_TYPE="PLATFORM_FACT",
         RULE_TEXT="Watch history is an important recommendation input because it indicates viewer interests.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-011", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="General framing.", PROHIBITED_USE="No universal cross-surface weight is asserted.", CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-CLM-012", DOMAIN="TOPIC", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A translated creator transcript claims YouTube uses a large recommender model and semantic IDs derived from metadata, frames, audio, pacing, and format.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-012", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Only the audiovisual-embedding portion has primary support.", PROHIBITED_USE="Do not assert the full metadata/pacing/format bundle as confirmed.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-013", DOMAIN="TOPIC", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="The same transcript claims semantic IDs connect to watch-history clusters representing recent formats, styles, interests, and mood.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-013", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_CURRENTLY_VERIFIABLE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption.", PROHIBITED_USE="Private mood-cluster linkage is not publicly verifiable.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-014", DOMAIN="FORMAT", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A strategist reports TV viewing rising from ~23-24% to over 50% of selected clients' viewing.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-014", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption.", PROHIBITED_USE="Self-reported client sample lacks underlying data.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-015", DOMAIN="FORMAT", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A strategist reports mean/median long-form duration increased 51% since 2020 across a 100-billion-view analysis.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-015", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption.", PROHIBITED_USE="No universal ideal-length rule follows even if true.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-016", DOMAIN="THUMBNAIL", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Experiments with larger, fewer homepage thumbnails allegedly improved selection/long-form viewing while smaller/new-channel recommendations stayed near the top.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-016", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption.", PROHIBITED_USE="No direct official record for the claimed outcome.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-017", DOMAIN="THUMBNAIL", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Shorts thumbnails do not appear in the swipe feed but can matter in search, browse, and Shorts-shelf contexts.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-017", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Bounded context only.", PROHIBITED_USE="Do not generalize beyond search/browse/shelf contexts.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-CLM-018", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="A creator claims Shorts and long-form use separate algorithms/audiences and should not share a channel.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-CLM-018", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="CONTRADICTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Preserve the conflict with CLM-005; do not resolve by assertion.", PROHIBITED_USE="Do not present as settled platform fact -- it is contradicted.",
         CONFLICTS=["TR-018-CLM-005"], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-INT-001", DOMAIN="TOPIC", RULE_TYPE="SOURCE_INTERPRETATION",
         RULE_TEXT="A speaker frames YouTube discovery history as keyword -> attention -> interest -> 'semantic' eras.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-INT-001", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Historical narrative framing only.", PROHIBITED_USE="Do not present as an official platform timeline.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-INT-002", DOMAIN="TOPIC", RULE_TYPE="SOURCE_INTERPRETATION",
         RULE_TEXT="Semantic matching is interpreted as reducing the value of generic content/subscriber totals relative to specific content for a clearly understood viewer.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-INT-002", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Strategic hypothesis for niche specificity.", PROHIBITED_USE="Not a measured platform rule.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-INT-003", DOMAIN="FORMAT", RULE_TYPE="SOURCE_INTERPRETATION",
         RULE_TEXT="TV friction/lean-back viewing is interpreted as favoring recognizable, show-like, bingeable, sometimes longer videos.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-INT-003", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Not a working assumption; participants describe divergent personal behavior.", PROHIBITED_USE="Do not treat as universal.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-INT-004", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="SOURCE_INTERPRETATION",
         RULE_TEXT="Personality/personal connection is argued to become a stronger differentiator as high-production spectacle becomes easier to imitate.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-INT-004", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Creator-strategy interpretation only.", PROHIBITED_USE="Not a measured platform rule.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-INT-005", DOMAIN="FORMAT", RULE_TYPE="SOURCE_INTERPRETATION",
         RULE_TEXT="A strategist speculates the mature long-form recommender is more sophisticated than the newer Shorts recommender.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-INT-005", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_CURRENTLY_VERIFIABLE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Personal judgment, explicitly framed as such by the speaker.", PROHIBITED_USE="Do not present as fact.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-REC-001", DOMAIN="RETENTION_HEURISTIC", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Compare analytics against similar videos, inspect retention-drop points and like rates, and combine metrics with direct audience feedback.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-001", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Sound practice; retention-drop data itself is NOT_AVAILABLE in this corpus.", PROHIBITED_USE="Do not fabricate retention-drop values to follow this recommendation.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-REC-002", DOMAIN="AUDIENCE", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Do not disable subscriber notifications merely to game recommendations; inspect subscriber-source behavior separately.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-002", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Operational guidance.", PROHIBITED_USE="Not applicable outside notification settings.", CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-REC-003", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Align channels with audiences and brand promises; choose same-channel vs separate-channel formats by audience overlap and creator goals, not a universal rule.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-003", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Channel-architecture guidance; explicitly rejects a universal answer.", PROHIBITED_USE="Do not force a single answer for every channel.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-REC-004", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Find differentiated value and make a consistent promise to a defined audience rather than becoming the Nth interchangeable treatment of a topic.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-004", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Directly usable for the new-channel blueprint differentiation section.", PROHIBITED_USE="Strategic advice, not a guaranteed outcome.",
         CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-REC-005", DOMAIN="PUBLISHING", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Launch with several linked videos so a viewer can continue through a coherent journey and build multiple watch-history interactions.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-005", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Usable for a new-channel launch-cohort experiment category.", PROHIBITED_USE="Not an experimentally verified rule in this repository.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-REC-006", DOMAIN="FORMAT", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Develop repeatable formats into recognizable 'shows' supporting multiple episodes, binge paths, and returning-viewer relationships.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-006", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Maps to REPEATABLE_WINNER_FAMILY family-health thinking.", PROHIBITED_USE="Do not maximize every isolated view at the expense of format identity.", CONFLICTS=[], CONFIDENCE="MEDIUM"),
    dict(RULE_ID="TR-018-REC-007", DOMAIN="SEO", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Structure scripts with an early direct answer and specific names/dates/places to make passages citation-friendly for AI answers (AEO).",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-007", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption for ranking.", PROHIBITED_USE="Claimed AEO ranking/citation mechanism is not independently supported.",
         CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-REC-008", DOMAIN="CHANNEL_STRATEGY", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Build linked off-platform profiles so a faceless channel reads as a consistent brand rather than an anonymous content farm.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-008", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="NOT_SUPPORTED_BY_PRIMARY_EVIDENCE", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Do not use as a working assumption for ranking.", PROHIBITED_USE="Claimed platform trust signal is not established.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-REC-009", DOMAIN="TOPIC", RULE_TYPE="CREATOR_HEURISTIC",
         RULE_TEXT="Seek specific questions/subjects not already covered well and contribute net-new information rather than generic duplication.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-009", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Usable as a content-gap research hypothesis for the new-channel blueprint.", PROHIBITED_USE="Not established for ranking effects specifically.", CONFLICTS=[], CONFIDENCE="LOW"),
    dict(RULE_ID="TR-018-REC-010", DOMAIN="PUBLISHING", RULE_TYPE="CLAIM_REQUIRING_VALIDATION",
         RULE_TEXT="Prefer unlisting to deleting an underperforming video, since deletion may remove useful audience-learning data.",
         SOURCE_ID="DS-000018", SOURCE_LOCATOR="ALG26-REC-010", SOURCE_QUALITY="CREATOR_SELF_REPORTED",
         PRIMARY_VALIDATION_STATUS="PARTIALLY_SUPPORTED", EMPIRICAL_CALIBRATION_STATUS="NOT_OBSERVABLE",
         SAFE_DOWNSTREAM_USE="Operational hedge.", PROHIBITED_USE="Platform behavior asserted without primary support.", CONFLICTS=[], CONFIDENCE="LOW"),
]

# archetype_id (as it appears in title/hook/script archetype arrays) -> the
# training rule it lets us calibrate, plus the archetype family it lives in.
CALIBRATION_TARGETS = [
    dict(rule_id="TR-011-011", archetype_kind="title", archetype_id="NUMBERED_SPECIFICITY",
         claim="Numbers/specificity in titles increase relative performance."),
    dict(rule_id="TR-011-013", archetype_kind="title", archetype_id="QUESTION",
         claim="Question-form titles increase relative performance."),
    dict(rule_id="TR-011-002", archetype_kind="hook", archetype_id="CONTEXT_FIRST",
         claim="Opening with context before the twist ('Context Lean') increases relative performance."),
    dict(rule_id="TR-011-011", archetype_kind="hook", archetype_id="NUMBER_LED",
         claim="Leading a hook with a concrete number increases relative performance."),
    dict(rule_id="TR-011-012", archetype_kind="hook", archetype_id="COUNTERINTUITIVE_PREMISE",
         claim="A counterintuitive/contrarian premise hook increases relative performance."),
    dict(rule_id="TR-011-007", archetype_kind="script", archetype_id="CALCULATED_ESCALATION",
         claim="Calculated-escalation script structure increases relative performance."),
    dict(rule_id="TR-011-015", archetype_kind="script", archetype_id="CONSEQUENCE_CHAIN",
         claim="Causal consequence-chain ('but/therefore') script structure increases relative performance."),
]

MEASURED_ONLY_CHANNELS = ["CH-000001", "CH-000002", "CH-000003", "CH-000005"]


# ---------------------------------------------------------------------------
# Artifact loading
# ---------------------------------------------------------------------------

def load_channel_artifacts(channel_id):
    cdir = channel_dir(channel_id)
    topic = load_json(find_topic_artifact(cdir))
    try:
        packaging = load_json(find_packaging_artifact(cdir))
    except OrchestrationError:
        packaging = None
    try:
        hook_script = load_json(find_hook_script_artifact(cdir))
    except OrchestrationError:
        hook_script = None
    return {"topic": topic, "packaging": packaging, "hook_script": hook_script}


def family_by_key(topic_artifact):
    return {f["family_key"]: f for f in topic_artifact.get("topic_families", [])}


# ---------------------------------------------------------------------------
# Video / family success-failure classification (deterministic mapping over
# already-computed Topic Intelligence fields -- no re-derivation of stats)
# ---------------------------------------------------------------------------

def classify_video_performance(band, family_repeatability):
    if band == "NEGATIVE_OUTLIER":
        return "FAILED_EXPERIMENT"
    if band == "POSITIVE_OUTLIER":
        return "REPEATABLE_WINNER_EXAMPLE" if family_repeatability == "REPEATABLE_WINNER" else "BREAKOUT"
    if band == "HIGH_RELATIVE_PERFORMER":
        if family_repeatability == "REPEATABLE_WINNER":
            return "REPEATABLE_WINNER_EXAMPLE"
        if family_repeatability in ("INSUFFICIENT_SAMPLE", "ONE_OFF_OUTLIER"):
            return "ONE_OFF_OUTLIER"
        return "STRONG_RELATIVE_PERFORMER"
    if band == "LOW_RELATIVE_PERFORMER":
        return "WEAK_RELATIVE_PERFORMER"
    if band == "NORMAL_RANGE":
        return "BASELINE"
    return "INSUFFICIENT_EVIDENCE"


def classify_family_health(family):
    rep = family.get("repeatability")
    n = family.get("item_count", 0)
    ratio = family.get("channel_median_ratio", 1.0)
    if rep == "INSUFFICIENT_SAMPLE":
        return "INSUFFICIENT_SAMPLE"
    if rep == "ONE_OFF_OUTLIER":
        return "ONE_OFF_DEPENDENT"
    if rep == "REPEATABLE_WINNER":
        return "REPEATABLE_WINNER_FAMILY" if n >= 3 else "EMERGING_FAMILY"
    if rep == "MIXED_FAMILY":
        strong = family.get("strongest_examples") or []
        weak = family.get("weakest_examples") or []
        if strong and weak:
            top = strong[0].get("views_per_day")
            bottom = weak[-1].get("views_per_day")
            if top and bottom:
                spread = top / bottom if bottom > 0 else None
                if spread is not None:
                    if ratio < 0.85 and spread < 3:
                        return "WEAK_FAMILY"
                    if spread >= 5:
                        return "VOLATILE_FAMILY"
        return "MIXED_FAMILY"
    return "INSUFFICIENT_SAMPLE"


def label_all_videos(topic_artifact):
    families = family_by_key(topic_artifact)
    labeled = []
    for item in topic_artifact["items"]:
        obs = item["observation"]
        family = families.get(obs["topic_family"])
        band = obs["performance_band"]
        family_rep = family["repeatability"] if family else "INSUFFICIENT_SAMPLE"
        label = classify_video_performance(band, family_rep)
        labeled.append({
            "video_id": item["canonical_fact"]["video_id"],
            "title": item["canonical_fact"]["title"],
            "topic_family": obs["topic_family"],
            "performance_band": band,
            "channel_median_ratio": item["derived_metric"]["channel_median_ratio"],
            "performance_class": label,
        })
    return labeled


def label_all_families(topic_artifact):
    labeled = []
    for family in topic_artifact.get("topic_families", []):
        labeled.append({
            "family_key": family["family_key"],
            "item_count": family["item_count"],
            "repeatability_input": family["repeatability"],
            "channel_median_ratio": family.get("channel_median_ratio"),
            "family_health": classify_family_health(family),
            "strongest_examples": family.get("strongest_examples", []),
            "weakest_examples": family.get("weakest_examples", []),
            "video_ids": family.get("video_ids", []),
        })
    return labeled


# ---------------------------------------------------------------------------
# Root-cause layering + WHY objects
# ---------------------------------------------------------------------------

def _archetype_lookup(hook_script, packaging):
    """video_id -> list of (layer, archetype_id, repeatability, median_channel_relative, role)."""
    signals = {}

    def add(video_id, layer, archetype_id, repeatability, ratio, role):
        signals.setdefault(video_id, []).append({
            "layer": layer, "archetype_id": archetype_id,
            "repeatability": repeatability, "median_channel_relative": ratio, "role": role,
        })

    if packaging:
        for a in packaging.get("title_archetypes", []):
            ratio = a.get("median_channel_relative_performance")
            for vid in a.get("strong_examples", []):
                add(vid, "PACKAGING", a["archetype_id"], a["repeatability"], ratio, "STRONG_EXAMPLE")
            for vid in a.get("supporting_video_ids", []):
                if vid not in a.get("strong_examples", []):
                    add(vid, "PACKAGING", a["archetype_id"], a["repeatability"], ratio, "SUPPORTING")
    if hook_script:
        for a in hook_script.get("hook_archetypes", []):
            ratio = a["performance_association"]["median_channel_relative"]
            for vid in a.get("strong_examples", []):
                add(vid, "HOOK_PROMISE_MATCH", a["hook_archetype_id"], a["repeatability"], ratio, "STRONG_EXAMPLE")
            for vid in a.get("weak_examples", []):
                add(vid, "HOOK_PROMISE_MATCH", a["hook_archetype_id"], a["repeatability"], ratio, "WEAK_EXAMPLE")
        for a in hook_script.get("script_archetypes", []):
            ratio = a["performance_association"]["median_channel_relative"]
            for vid in a.get("strong_examples", []):
                add(vid, "SCRIPT_STRUCTURE", a["script_archetype_id"], a["repeatability"], ratio, "STRONG_EXAMPLE")
            for vid in a.get("weak_examples", []):
                add(vid, "SCRIPT_STRUCTURE", a["script_archetype_id"], a["repeatability"], ratio, "WEAK_EXAMPLE")
    return signals


def root_cause_layers(video_id, video_label, family_label, archetype_signals):
    """Layers contributing to a video's performance class, each with evidence.
    Never blames PACKAGING purely because views are weak -- only when a
    packaging/hook/script archetype signal for this specific video is itself weak."""
    layers = []
    if family_label["family_health"] in ("WEAK_FAMILY", "ONE_OFF_DEPENDENT", "VOLATILE_FAMILY"):
        layers.append({
            "layer": "TOPIC_SELECTION" if family_label["family_health"] != "VOLATILE_FAMILY" else "SATURATION",
            "evidence": f"topic family {family_label['family_key']} is {family_label['family_health']}",
        })
    for sig in archetype_signals.get(video_id, []):
        if sig["role"] == "WEAK_EXAMPLE" and sig["repeatability"] not in ("INSUFFICIENT_SAMPLE",):
            layers.append({
                "layer": sig["layer"],
                "evidence": f"{sig['archetype_id']} archetype ({sig['repeatability']}, median_channel_relative={sig['median_channel_relative']})",
            })
    if not layers:
        layers.append({"layer": "INSUFFICIENT_EVIDENCE", "evidence": "no weak packaging/hook/script archetype signal found for this video"})
    return layers


def build_why_object(video_id, video_label, family_label, archetype_signals, training_rules_by_archetype):
    signals = archetype_signals.get(video_id, [])
    strong_signals = [s for s in signals if s["role"] in ("STRONG_EXAMPLE",)]
    weak_signals = [s for s in signals if s["role"] in ("WEAK_EXAMPLE",)]
    matched_rules = sorted({training_rules_by_archetype[s["archetype_id"]]
                             for s in signals if s["archetype_id"] in training_rules_by_archetype})
    counter_examples = [s["archetype_id"] for s in signals if s["repeatability"] == "INSUFFICIENT_SAMPLE"]
    return {
        "VIDEO_ID": video_id,
        "PERFORMANCE_CLASS": video_label["performance_class"],
        "WHAT_WORKED": [f"{s['layer']}:{s['archetype_id']} (median_channel_relative={s['median_channel_relative']})" for s in strong_signals] or ["INSUFFICIENT_EVIDENCE"],
        "WHAT_DID_NOT_WORK": [f"{s['layer']}:{s['archetype_id']} (median_channel_relative={s['median_channel_relative']})" for s in weak_signals] or ["NONE_IDENTIFIED"],
        "TOPIC_SIGNAL": f"{video_label['topic_family']} family is {family_label['family_health']}",
        "PACKAGING_SIGNAL": next((f"{s['archetype_id']} ({s['repeatability']})" for s in signals if s["layer"] == "PACKAGING"), "INSUFFICIENT_EVIDENCE"),
        "HOOK_SIGNAL": next((f"{s['archetype_id']} ({s['repeatability']})" for s in signals if s["layer"] == "HOOK_PROMISE_MATCH"), "INSUFFICIENT_EVIDENCE"),
        "SCRIPT_SIGNAL": next((f"{s['archetype_id']} ({s['repeatability']})" for s in signals if s["layer"] == "SCRIPT_STRUCTURE"), "INSUFFICIENT_EVIDENCE"),
        "EDITING_SIGNAL": "NOT_AVAILABLE",
        "TRAINING_HEURISTICS_MATCHED": matched_rules,
        "COUNTER_EVIDENCE": counter_examples or ["NONE_IDENTIFIED"],
        "CAUSALITY_STATUS": "ASSOCIATION_ONLY",
        "CONFIDENCE": "HIGH" if strong_signals and any(s["repeatability"] in ("REPEATABLE_PATTERN", "REPEATABLE_WINNER") for s in strong_signals) else "MEDIUM",
    }


# ---------------------------------------------------------------------------
# Empirical calibration (deterministic thresholds over already-measured
# archetype fields; never a single-item ratio is treated as calibrating)
# ---------------------------------------------------------------------------

def _archetype_observations(archetype_kind, archetype_id, channel_artifacts_by_id):
    observations = []
    for channel_id, artifacts in channel_artifacts_by_id.items():
        source = None
        if archetype_kind == "title" and artifacts["packaging"]:
            source = artifacts["packaging"].get("title_archetypes", [])
            key, ratio_key = "archetype_id", "median_channel_relative_performance"
        elif archetype_kind == "hook" and artifacts["hook_script"]:
            source = artifacts["hook_script"].get("hook_archetypes", [])
            key, ratio_key = "hook_archetype_id", None
        elif archetype_kind == "script" and artifacts["hook_script"]:
            source = artifacts["hook_script"].get("script_archetypes", [])
            key, ratio_key = "script_archetype_id", None
        else:
            continue
        for a in source or []:
            if a[key] != archetype_id:
                continue
            ratio = a[ratio_key] if ratio_key else a["performance_association"]["median_channel_relative"]
            observations.append({
                "channel_id": channel_id, "repeatability": a["repeatability"],
                "median_channel_relative": ratio, "item_count": a["item_count"],
            })
    return observations


def empirical_calibration_verdict(observations, min_items=3, band=0.15):
    usable = [o for o in observations if o["item_count"] >= min_items]
    if not usable:
        return "INSUFFICIENT_EVIDENCE"
    positive = [o for o in usable if o["median_channel_relative"] >= 1 + band]
    negative = [o for o in usable if o["median_channel_relative"] <= 1 - band]
    neutral = [o for o in usable if o not in positive and o not in negative]
    if positive and negative:
        return "MIXED"
    if len(positive) == len(usable):
        return "CORPUS_SUPPORTED"
    if len(negative) == len(usable):
        return "CORPUS_NOT_SUPPORTED"
    if positive or neutral:
        return "CORPUS_PARTIALLY_SUPPORTED"
    return "INSUFFICIENT_EVIDENCE"


def cross_channel_robustness(observations, min_items=3, band=0.15):
    usable = [o for o in observations if o["item_count"] >= min_items]
    if len(usable) == 0:
        return "INSUFFICIENT_EVIDENCE"
    if len(usable) == 1:
        return "CHANNEL_SPECIFIC_PATTERN"
    directions = {("POSITIVE" if o["median_channel_relative"] >= 1 + band else
                    "NEGATIVE" if o["median_channel_relative"] <= 1 - band else "NEUTRAL")
                  for o in usable}
    if "POSITIVE" in directions and "NEGATIVE" in directions:
        return "CONFLICTING_PATTERN"
    if len(directions - {"NEUTRAL"}) >= 1 and len(usable) >= 2:
        return "ROBUST_CROSS_CHANNEL_PATTERN"
    return "CHANNEL_SPECIFIC_PATTERN"


def calibrate_all(channel_ids=None):
    channel_ids = channel_ids or MEASURED_ONLY_CHANNELS
    channel_artifacts_by_id = {cid: load_channel_artifacts(cid) for cid in channel_ids}
    results = []
    for target in CALIBRATION_TARGETS:
        observations = _archetype_observations(target["archetype_kind"], target["archetype_id"], channel_artifacts_by_id)
        results.append({
            "rule_id": target["rule_id"], "archetype_kind": target["archetype_kind"],
            "archetype_id": target["archetype_id"], "claim": target["claim"],
            "channels_evaluated": channel_ids,
            "observations": observations,
            "empirical_calibration_status": empirical_calibration_verdict(observations),
            "cross_channel_robustness": cross_channel_robustness(observations),
        })
    return results


# ---------------------------------------------------------------------------
# Training-knowledge registry artifact
# ---------------------------------------------------------------------------

def build_training_registry(source_inventory=None):
    calibration = calibrate_all()
    by_rule_id = {}
    for c in calibration:
        by_rule_id.setdefault(c["rule_id"], []).append(c)

    rules = []
    for rule in TRAINING_RULES:
        rule = dict(rule)
        matches = by_rule_id.get(rule["RULE_ID"])
        if matches:
            # a rule may map to more than one archetype (title AND hook); keep the
            # strongest observed verdict rather than silently picking the first.
            order = ["CORPUS_SUPPORTED", "CORPUS_PARTIALLY_SUPPORTED", "MIXED",
                      "CORPUS_NOT_SUPPORTED", "INSUFFICIENT_EVIDENCE"]
            best = min(matches, key=lambda m: order.index(m["empirical_calibration_status"]))
            rule["EMPIRICAL_CALIBRATION_STATUS"] = best["empirical_calibration_status"]
        rules.append(rule)

    return {
        "schema_version": TRAINING_REGISTRY_SCHEMA,
        "generated_on": "2026-09-11",
        "source_inventory": source_inventory or {},
        "rules": rules,
        "empirical_calibration_evidence": calibration,
        "guardrails": {
            "prohibited_scores": ["CHANNEL_SUCCESS_SCORE", "VIRALITY_SCORE", "ALGORITHM_SCORE", "CHANNEL_HEALTH_PERCENTAGE"],
            "causality_status": "ASSOCIATION_ONLY_EVERYWHERE",
            "private_metrics_not_inferred": PRIVATE_METRICS,
        },
    }


# ---------------------------------------------------------------------------
# Channel diagnosis
# ---------------------------------------------------------------------------

def _top_families(labeled_families, health_states, limit=3):
    matches = [f for f in labeled_families if f["family_health"] in health_states]
    return sorted(matches, key=lambda f: -(f.get("channel_median_ratio") or 0))[:limit]


def _archetype_summaries(hook_script, packaging):
    summaries = {"title": [], "hook": [], "script": []}
    if packaging:
        for a in packaging.get("title_archetypes", []):
            summaries["title"].append({
                "archetype_id": a["archetype_id"], "repeatability": a["repeatability"],
                "median_channel_relative": a["median_channel_relative_performance"], "item_count": a["item_count"],
            })
    if hook_script:
        for a in hook_script.get("hook_archetypes", []):
            summaries["hook"].append({
                "archetype_id": a["hook_archetype_id"], "repeatability": a["repeatability"],
                "median_channel_relative": a["performance_association"]["median_channel_relative"], "item_count": a["item_count"],
            })
        for a in hook_script.get("script_archetypes", []):
            summaries["script"].append({
                "archetype_id": a["script_archetype_id"], "repeatability": a["repeatability"],
                "median_channel_relative": a["performance_association"]["median_channel_relative"], "item_count": a["item_count"],
            })
    return summaries


def generate_actions(target_id, labeled_videos, labeled_families, archetype_summaries, benchmark_summaries=None):
    actions = []
    action_seq = 1

    def next_id():
        nonlocal action_seq
        aid = f"ACT-{target_id}-{action_seq:03d}"
        action_seq += 1
        return aid

    for kind in ("title", "hook", "script"):
        for a in archetype_summaries.get(kind, []):
            evidence = f"{kind}_archetype={a['archetype_id']}, repeatability={a['repeatability']}, median_channel_relative={a['median_channel_relative']}, item_count={a['item_count']}"
            counter = "none within this channel" if a["item_count"] >= 3 else "sample too small to rule out chance"
            if a["item_count"] < 3:
                action_type, why = "TEST", "sample too small to act on yet"
            elif a["repeatability"] in ("REPEATABLE_PATTERN", "REPEATABLE_WINNER") and a["median_channel_relative"] >= 1.15:
                action_type, why = "DOUBLE_DOWN", "repeatable pattern with above-median relative performance"
            elif a["repeatability"] in ("REPEATABLE_PATTERN", "REPEATABLE_WINNER") and 0.85 <= a["median_channel_relative"] < 1.15:
                action_type, why = "CONTINUE", "repeatable, at-baseline pattern -- no evidence to change it"
            elif a["median_channel_relative"] < 0.85:
                action_type, why = "FIX" if kind != "title" else "REDUCE", "below-median relative performance for a recurring pattern"
            else:
                action_type, why = "WATCH", "mixed/uncertain signal"
            actions.append({
                "ACTION_ID": next_id(), "ACTION_TYPE": action_type,
                "TARGET": f"{kind}:{a['archetype_id']}",
                "WHY": why,
                "INTERNAL_EVIDENCE": evidence,
                "BENCHMARK_EVIDENCE": (benchmark_summaries or {}).get(kind, "no benchmark evidence used for this action"),
                "TRAINING_RULES_USED": [t["rule_id"] for t in CALIBRATION_TARGETS if t["archetype_kind"] == kind and t["archetype_id"] == a["archetype_id"]],
                "COUNTER_EVIDENCE": counter,
                "CONFIDENCE": "MEDIUM" if a["item_count"] >= 5 else "LOW",
                "WHAT_WOULD_FALSIFY_IT": f"item_count for {a['archetype_id']} growing while median_channel_relative moves to the opposite side of 1.0",
            })

    for family in labeled_families:
        if family["family_health"] == "REPEATABLE_WINNER_FAMILY":
            action_type, why = "DOUBLE_DOWN", "repeatable winner family with 3+ items"
        elif family["family_health"] == "WEAK_FAMILY":
            action_type, why = "REDUCE", "consistently below-median family"
        elif family["family_health"] == "ONE_OFF_DEPENDENT":
            action_type, why = "WATCH", "family success depends on a single outlier item"
        elif family["family_health"] == "VOLATILE_FAMILY":
            action_type, why = "TEST", "high spread between strongest and weakest items in this family"
        elif family["family_health"] == "EMERGING_FAMILY":
            action_type, why = "TEST", "winning signal present but too few items to call repeatable yet"
        elif family["family_health"] == "MIXED_FAMILY":
            action_type, why = "WATCH", "mixed within-family signal"
        else:
            action_type, why = "INSUFFICIENT_EVIDENCE", "too few items in this family to classify"
        actions.append({
            "ACTION_ID": next_id(), "ACTION_TYPE": action_type,
            "TARGET": f"topic_family:{family['family_key']}",
            "WHY": why,
            "INTERNAL_EVIDENCE": f"item_count={family['item_count']}, channel_median_ratio={family.get('channel_median_ratio')}, family_health={family['family_health']}",
            "BENCHMARK_EVIDENCE": (benchmark_summaries or {}).get("topic", "no benchmark evidence used for this action"),
            "TRAINING_RULES_USED": [],
            "COUNTER_EVIDENCE": ", ".join(v["video_id"] for v in family.get("weakest_examples", [])) or "none identified",
            "CONFIDENCE": "MEDIUM" if family["item_count"] >= 3 else "LOW",
            "WHAT_WOULD_FALSIFY_IT": "family_health reclassifying on the next diagnosis run as new items publish",
        })
    return actions


def diagnose_channel(target_id, benchmark_ids):
    target_artifacts = load_channel_artifacts(target_id)
    benchmark_artifacts = {bid: load_channel_artifacts(bid) for bid in benchmark_ids}

    labeled_videos = label_all_videos(target_artifacts["topic"])
    labeled_families = label_all_families(target_artifacts["topic"])
    archetype_signals = _archetype_lookup(target_artifacts["hook_script"], target_artifacts["packaging"])
    archetype_summaries = _archetype_summaries(target_artifacts["hook_script"], target_artifacts["packaging"])

    training_rules_by_archetype = {}
    for t in CALIBRATION_TARGETS:
        training_rules_by_archetype[t["archetype_id"]] = t["rule_id"]

    videos_by_id = {v["video_id"]: v for v in labeled_videos}
    families_by_key = {f["family_key"]: f for f in labeled_families}

    def why_for(video_id):
        vlabel = videos_by_id[video_id]
        flabel = families_by_key.get(vlabel["topic_family"], {"family_key": vlabel["topic_family"], "family_health": "INSUFFICIENT_SAMPLE"})
        return build_why_object(video_id, vlabel, flabel, archetype_signals, training_rules_by_archetype)

    strong_candidates = sorted(
        [v for v in labeled_videos if v["performance_class"] in ("REPEATABLE_WINNER_EXAMPLE", "STRONG_RELATIVE_PERFORMER", "BREAKOUT")],
        key=lambda v: -v["channel_median_ratio"])[:3]
    weak_candidates = sorted(
        [v for v in labeled_videos if v["performance_class"] in ("WEAK_RELATIVE_PERFORMER", "FAILED_EXPERIMENT")],
        key=lambda v: v["channel_median_ratio"])[:3]

    why_objects = [why_for(v["video_id"]) for v in strong_candidates] + [why_for(v["video_id"]) for v in weak_candidates]
    root_causes = {
        v["video_id"]: root_cause_layers(v["video_id"], v, families_by_key.get(v["topic_family"], {"family_key": v["topic_family"], "family_health": "INSUFFICIENT_SAMPLE"}), archetype_signals)
        for v in weak_candidates
    }

    benchmark_summaries = {}
    for kind in ("title", "hook", "script", "topic"):
        parts = []
        for bid, artifacts in benchmark_artifacts.items():
            if kind == "topic":
                bench_families = label_all_families(artifacts["topic"])
                winners = [f["family_key"] for f in bench_families if f["family_health"] == "REPEATABLE_WINNER_FAMILY"]
                parts.append(f"{bid} repeatable-winner families: {winners or 'none'}")
            else:
                bench_summary = _archetype_summaries(artifacts["hook_script"], artifacts["packaging"]).get(kind, [])
                strong = [a["archetype_id"] for a in bench_summary if a["repeatability"] in ("REPEATABLE_PATTERN",) and a["median_channel_relative"] >= 1.15]
                parts.append(f"{bid} strong {kind} archetypes: {strong or 'none'}")
        benchmark_summaries[kind] = "; ".join(parts)

    actions = generate_actions(target_id, labeled_videos, labeled_families, archetype_summaries, benchmark_summaries)

    calibration = calibrate_all([target_id] + list(benchmark_ids))
    holds = [c for c in calibration if c["empirical_calibration_status"] in ("CORPUS_SUPPORTED", "CORPUS_PARTIALLY_SUPPORTED")]
    does_not_hold = [c for c in calibration if c["empirical_calibration_status"] in ("CORPUS_NOT_SUPPORTED", "MIXED")]
    # a rule_id can map to more than one archetype (e.g. TR-011-011 covers both a
    # title archetype and a hook archetype); qualify each entry by archetype so a
    # rule holding in one context and not another never reads as a contradiction.
    holds_detail = [{"rule_id": c["rule_id"], "archetype": f"{c['archetype_kind']}:{c['archetype_id']}"} for c in holds]
    does_not_hold_detail = [{"rule_id": c["rule_id"], "archetype": f"{c['archetype_kind']}:{c['archetype_id']}"} for c in does_not_hold]

    canonical_topics = target_artifacts["topic"]["evidence_snapshot"].get("canonical_topics", {})

    return {
        "schema_version": DIAGNOSIS_SCHEMA,
        "generated_on": "2026-09-11",
        "target_channel": {"channel_id": target_id, "display_name": CHANNEL_DISPLAY_NAMES.get(target_id, target_id)},
        "benchmark_channels": [{"channel_id": bid, "display_name": CHANNEL_DISPLAY_NAMES.get(bid, bid)} for bid in benchmark_ids],
        "positioning": {
            "content_pillars": sorted(canonical_topics, key=lambda k: -canonical_topics[k]),
            "topic_distribution": canonical_topics,
        },
        "trajectory_discipline": {
            "cross_sectional_performance": "AVAILABLE",
            "publish_cohort_pattern": "NOT_COMPUTED_THIS_PILOT",
            "longitudinal_trend": "NOT_AVAILABLE",
        },
        "video_labels": labeled_videos,
        "family_labels": labeled_families,
        "archetype_summaries": archetype_summaries,
        "repeatable_winners": _top_families(labeled_families, {"REPEATABLE_WINNER_FAMILY"}),
        "emerging": _top_families(labeled_families, {"EMERGING_FAMILY"}),
        "one_off_or_weak": _top_families(labeled_families, {"ONE_OFF_DEPENDENT", "WEAK_FAMILY", "VOLATILE_FAMILY"}),
        "why_objects": why_objects,
        "root_cause_layers": root_causes,
        "benchmark_summaries": benchmark_summaries,
        "training_heuristics_hold": holds_detail,
        "training_heuristics_do_not_hold": does_not_hold_detail,
        "calibration_detail": calibration,
        "actions": actions,
        "medical_note": "Competitor/creator transcript claims are never treated as medical facts; MEDICAL_VALIDATION_STATUS is tracked separately per the unified orchestrator (VALIDATION_REQUIRED for this channel unless an EXTERNAL_VALIDATION source is supplied).",
        "unavailable_private_metrics": PRIVATE_METRICS,
    }


# ---------------------------------------------------------------------------
# Cross-channel benchmark
# ---------------------------------------------------------------------------

def benchmark_channels(channel_ids):
    per_channel = {}
    for cid in channel_ids:
        artifacts = load_channel_artifacts(cid)
        per_channel[cid] = {
            "families": label_all_families(artifacts["topic"]),
            "archetypes": _archetype_summaries(artifacts["hook_script"], artifacts["packaging"]),
        }

    pattern_rows = []
    for target in CALIBRATION_TARGETS:
        observations = _archetype_observations(
            target["archetype_kind"], target["archetype_id"],
            {cid: load_channel_artifacts(cid) for cid in channel_ids})
        pattern_rows.append({
            "archetype_kind": target["archetype_kind"], "archetype_id": target["archetype_id"],
            "claim": target["claim"], "observations": observations,
            "classification": cross_channel_robustness(observations),
            "empirical_calibration_status": empirical_calibration_verdict(observations),
        })

    return {
        "schema_version": BENCHMARK_SCHEMA,
        "generated_on": "2026-09-11",
        "channels": [{"channel_id": cid, "display_name": CHANNEL_DISPLAY_NAMES.get(cid, cid)} for cid in channel_ids],
        "per_channel_summary": per_channel,
        "cross_channel_patterns": pattern_rows,
        "raw_view_comparison_prohibited": "Absolute raw views are not compared across channels as strategic truth; only within-channel normalized ratios and structural pattern recurrence are compared.",
        "unavailable_private_metrics": PRIVATE_METRICS,
    }


# ---------------------------------------------------------------------------
# New-channel blueprint
# ---------------------------------------------------------------------------

def assemble_blueprint(niche_label, benchmark, diagnosis_by_channel):
    robust = [p for p in benchmark["cross_channel_patterns"] if p["classification"] == "ROBUST_CROSS_CHANNEL_PATTERN"]
    channel_specific = [p for p in benchmark["cross_channel_patterns"] if p["classification"] == "CHANNEL_SPECIFIC_PATTERN"]
    conflicting = [p for p in benchmark["cross_channel_patterns"] if p["classification"] == "CONFLICTING_PATTERN"]

    all_pillars = {}
    for cid, diag in diagnosis_by_channel.items():
        for topic, count in diag["positioning"]["topic_distribution"].items():
            all_pillars[topic] = all_pillars.get(topic, 0) + count

    experiments = []
    exp_id = 1
    for p in robust:
        experiments.append({
            "EXPERIMENT_CATEGORY_ID": f"EXP-{exp_id:02d}", "CATEGORY": f"{p['archetype_kind'].upper()}_{p['archetype_id']}",
            "SOURCE": "BENCHMARK_PATTERN", "RATIONALE": p["claim"], "CONFIDENCE": "MEDIUM",
        })
        exp_id += 1
    for topic in sorted(all_pillars, key=lambda k: -all_pillars[k])[:3]:
        experiments.append({
            "EXPERIMENT_CATEGORY_ID": f"EXP-{exp_id:02d}", "CATEGORY": f"TOPIC_PILLAR_{topic}",
            "SOURCE": "CORPUS_EVIDENCE", "RATIONALE": f"observed across benchmark channels ({all_pillars[topic]} canonical items combined)",
            "CONFIDENCE": "MEDIUM",
        })
        exp_id += 1
    for rule in TRAINING_RULES:
        if rule["DOMAIN"] in ("CHANNEL_STRATEGY", "AUDIENCE") and rule["RULE_TYPE"] == "CREATOR_HEURISTIC" and rule["PRIMARY_VALIDATION_STATUS"] == "SUPPORTED":
            experiments.append({
                "EXPERIMENT_CATEGORY_ID": f"EXP-{exp_id:02d}", "CATEGORY": rule["RULE_ID"],
                "SOURCE": "TRAINING_HEURISTIC", "RATIONALE": rule["RULE_TEXT"], "CONFIDENCE": "LOW",
            })
            exp_id += 1
        if exp_id > 10:
            break

    return {
        "schema_version": BLUEPRINT_SCHEMA,
        "generated_on": "2026-09-11",
        "niche": niche_label,
        "benchmark_channels": [c["channel_id"] for c in benchmark["channels"]],
        "target_audience": {
            "value": "Adults managing their own or a family member's senior/aging-related health concerns, seeking clear, non-alarmist explanation before a doctor visit.",
            "source": "CORPUS_EVIDENCE", "confidence": "MEDIUM",
            "evidence": "Derived from combined canonical topic distribution across CH-000003/CH-000005 (HEALTHY_AGING, CARDIOVASCULAR_HEALTH, METABOLIC_HEALTH families).",
        },
        "positioning": {
            "value": "A doctor-led, evidence-labeled explainer channel -- distinct from both benchmark channels' individual presentation style, not a copy of either.",
            "source": "TRAINING_HEURISTIC", "confidence": "MEDIUM", "evidence": "TR-018-REC-004 (differentiated promise) + TR-011-017 (truth-hierarchy operating system).",
        },
        "niche_boundaries": {
            "value": "Senior/aging-adult health explanation and risk-awareness content; explicitly not diagnosis, treatment, or medication guidance.",
            "source": "OFFICIAL_PLATFORM_KNOWLEDGE", "confidence": "HIGH",
            "evidence": "Medical content requires MEDICAL_VALIDATION_STATUS; this repository never treats competitor transcript claims as medical fact.",
        },
        "core_content_pillars": [
            {"pillar": topic, "combined_item_count": count, "source": "CORPUS_EVIDENCE"}
            for topic, count in sorted(all_pillars.items(), key=lambda kv: -kv[1])
        ],
        "robust_cross_channel_patterns": [
            {"pattern": f"{p['archetype_kind']}:{p['archetype_id']}", "claim": p["claim"], "source": "BENCHMARK_PATTERN", "confidence": "MEDIUM"}
            for p in robust
        ],
        "channel_specific_patterns_to_avoid_copying": [
            {"pattern": f"{p['archetype_kind']}:{p['archetype_id']}", "claim": p["claim"], "source": "BENCHMARK_PATTERN",
             "note": "significant in only one benchmark channel -- do not generalize"}
            for p in channel_specific
        ],
        "weak_or_conflicting_patterns": [
            {"pattern": f"{p['archetype_kind']}:{p['archetype_id']}", "classification": p["classification"], "source": "BENCHMARK_PATTERN"}
            for p in conflicting
        ],
        "underexploited_opportunities": [
            {"opportunity": f["family_key"], "source": "CORPUS_EVIDENCE", "confidence": "LOW",
             "evidence": f"EMERGING_FAMILY in {cid}: item_count={f['item_count']}"}
            for cid, diag in diagnosis_by_channel.items() for f in diag["emerging"]
        ],
        "title_language": {"value": "Prefer WARNING_OR_RISK and NUMBERED_SPECIFICITY structures where a channel's own evidence supports them; do not assume either transfers to a new channel with zero data.",
                            "source": "BENCHMARK_PATTERN", "confidence": "LOW"},
        "thumbnail_language": {"value": "NOT_AVAILABLE for CH-000001/CH-000002-style gap; where thumbnail evidence exists (CH-000003/CH-000005), favor bright/natural colors, bold fonts, one big idea per the Packaging SOP.",
                                "source": "TRAINING_HEURISTIC", "confidence": "LOW", "rule_id": "TR-011-004"},
        "hook_principles": {"value": "Use the Context Lean -> Scroll-Stop -> Snapback structure as a diagnostic lens for drafts; do not assume a fixed hook archetype outperforms until the new channel has >=3 items in that archetype.",
                             "source": "TRAINING_HEURISTIC", "confidence": "LOW", "rule_id": "TR-011-002"},
        "script_structures": {"value": "Favor calculated-escalation / causal consequence-chain structuring as a baseline discipline; treat it as structurally common rather than a differentiator per current corpus calibration.",
                               "source": "CORPUS_EVIDENCE", "confidence": "MEDIUM", "rule_id": "TR-011-015"},
        "format_strategy": {"value": "Start long-form only (matches both benchmark channels' canonical evidence); do not add Shorts on the same channel without an explicit test, per the unresolved CLM-005/CLM-018 conflict.",
                             "source": "OFFICIAL_PLATFORM_KNOWLEDGE", "confidence": "LOW", "rule_id": "TR-018-CLM-018"},
        "differentiation": {"value": "Make one explicit, consistently-kept audience promise per TR-018-REC-004 rather than replicating either benchmark channel's topic mix wholesale.",
                             "source": "TRAINING_HEURISTIC", "confidence": "MEDIUM"},
        "first_10_experiment_categories": experiments[:10],
        "metrics_to_monitor": {
            "available_now": ["views_per_day (within-channel normalized)", "channel_median_ratio", "family repeatability", "archetype repeatability"],
            "not_available_until_first_party_analytics": PRIVATE_METRICS,
        },
        "falsification_criteria": [
            "A ROBUST_CROSS_CHANNEL_PATTERN used here fails to reach REPEATABLE_PATTERN status (>=3 items, consistent direction) within the new channel's first 10-15 uploads.",
            "A TOPIC_PILLAR experiment category produces a WEAK_FAMILY or ONE_OFF_DEPENDENT classification instead of REPEATABLE_WINNER_FAMILY after 5+ items.",
        ],
        "guardrails": {
            "no_copying_one_competitor": True,
            "no_causal_claims_from_public_correlation": True,
            "private_analytics_not_available": PRIVATE_METRICS,
        },
    }


# ---------------------------------------------------------------------------
# Markdown rendering (Dr. Elias-style diagnosis)
# ---------------------------------------------------------------------------

def render_diagnosis_markdown(diagnosis, benchmark_channel_id):
    target = diagnosis["target_channel"]
    lines = [f"# {target['display_name']} ({target['channel_id']}) -- Channel Strategy Diagnosis", ""]
    lines += ["# Executive Diagnosis", "",
              f"Target: {target['display_name']} ({target['channel_id']}). Benchmark: "
              + ", ".join(f"{b['display_name']} ({b['channel_id']})" for b in diagnosis["benchmark_channels"]) + ".",
              f"Content pillars observed: {', '.join(diagnosis['positioning']['content_pillars'])}.", ""]

    lines += ["# What Is Working", ""]
    for f in diagnosis["repeatable_winners"]:
        lines.append(f"- `{f['family_key']}` -- REPEATABLE_WINNER_FAMILY, {f['item_count']} items, channel_median_ratio={f['channel_median_ratio']}.")
    if not diagnosis["repeatable_winners"]:
        lines.append("- No family reached REPEATABLE_WINNER_FAMILY (>=3 items) yet in this corpus.")
    lines.append("")

    lines += ["# What Is Not Working", ""]
    for f in diagnosis["one_off_or_weak"]:
        lines.append(f"- `{f['family_key']}` -- {f['family_health']}, {f['item_count']} items, channel_median_ratio={f['channel_median_ratio']}.")
    if not diagnosis["one_off_or_weak"]:
        lines.append("- No family classified WEAK_FAMILY/ONE_OFF_DEPENDENT/VOLATILE_FAMILY in this corpus.")
    lines.append("")

    lines += ["# Repeatable Winners", ""]
    for why in diagnosis["why_objects"]:
        if why["PERFORMANCE_CLASS"] == "REPEATABLE_WINNER_EXAMPLE":
            lines.append(f"- `{why['VIDEO_ID']}`: {', '.join(why['WHAT_WORKED'])}.")
    lines.append("")

    lines += ["# One-Off Successes", ""]
    for why in diagnosis["why_objects"]:
        if why["PERFORMANCE_CLASS"] in ("BREAKOUT", "ONE_OFF_OUTLIER"):
            lines.append(f"- `{why['VIDEO_ID']}` ({why['PERFORMANCE_CLASS']}): counter-evidence={why['COUNTER_EVIDENCE']}; causality={why['CAUSALITY_STATUS']}.")
    if not any(w["PERFORMANCE_CLASS"] in ("BREAKOUT", "ONE_OFF_OUTLIER") for w in diagnosis["why_objects"]):
        lines.append("- None identified among the sampled representative videos.")
    lines.append("")

    lines += ["# Weak / Failed Experiments", ""]
    for why in diagnosis["why_objects"]:
        if why["PERFORMANCE_CLASS"] in ("WEAK_RELATIVE_PERFORMER", "FAILED_EXPERIMENT"):
            causes = diagnosis["root_cause_layers"].get(why["VIDEO_ID"], [])
            layer_text = "; ".join(f"{c['layer']} ({c['evidence']})" for c in causes)
            lines.append(f"- `{why['VIDEO_ID']}` ({why['PERFORMANCE_CLASS']}): root-cause layers -- {layer_text}.")
    lines.append("")

    lines += [f"# {target['display_name'].split()[0]} {target['display_name'].split()[1] if len(target['display_name'].split())>1 else ''} vs {CHANNEL_DISPLAY_NAMES.get(benchmark_channel_id, benchmark_channel_id)}".replace("  ", " "), ""]
    lines.append(diagnosis["benchmark_summaries"].get("topic", ""))
    lines.append(diagnosis["benchmark_summaries"].get("title", ""))
    lines.append(diagnosis["benchmark_summaries"].get("hook", ""))
    lines.append(diagnosis["benchmark_summaries"].get("script", ""))
    lines.append("")

    lines += ["# Training Heuristics That Hold", ""]
    for entry in diagnosis["training_heuristics_hold"]:
        rule = next(r for r in TRAINING_RULES if r["RULE_ID"] == entry["rule_id"])
        lines.append(f"- `{entry['rule_id']}` (via {entry['archetype']}): {rule['RULE_TEXT']}")
    lines.append("")

    lines += ["# Training Heuristics That Do Not Hold", ""]
    for entry in diagnosis["training_heuristics_do_not_hold"]:
        rule = next(r for r in TRAINING_RULES if r["RULE_ID"] == entry["rule_id"])
        lines.append(f"- `{entry['rule_id']}` (via {entry['archetype']}): {rule['RULE_TEXT']}")
    lines.append("")

    for heading, action_type in [("Continue", "CONTINUE"), ("Double Down", "DOUBLE_DOWN"), ("Fix", "FIX"),
                                  ("Reduce / Stop", None), ("Test", "TEST"), ("Watch", "WATCH")]:
        lines += [f"# {heading}", ""]
        if action_type:
            matches = [a for a in diagnosis["actions"] if a["ACTION_TYPE"] == action_type]
        else:
            matches = [a for a in diagnosis["actions"] if a["ACTION_TYPE"] in ("REDUCE", "STOP")]
        for a in matches:
            lines.append(f"- `{a['ACTION_ID']}` {a['TARGET']}: {a['WHY']} (confidence={a['CONFIDENCE']}).")
        if not matches:
            lines.append("- None classified this pilot run.")
        lines.append("")

    lines += ["# Evidence Limitations", "",
              "- Private YouTube Analytics (CTR, impressions, retention, AVD, watch time, traffic sources, subscriber conversion, audience overlap) are NOT_AVAILABLE for this channel.",
              "- LONGITUDINAL_TREND is NOT_AVAILABLE; only cross-sectional, publish-cohort-aware normalized performance is used.",
              "- Every archetype/family association is CAUSALITY_STATUS=ASSOCIATION_ONLY, never a causal claim.",
              f"- {diagnosis['medical_note']}",
              ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Source inventory (ZIP/XLSX dedup) -- used only to populate the training
# registry's provenance section; never mutates raw evidence.
# ---------------------------------------------------------------------------

def build_source_inventory_summary():
    return {
        "supplied_zip": {
            "filename": "all training data of youtube 2.zip",
            "sha256": "3567072fa8081b414a4c897cfdbf343d371fddf7fe3c1dcdef4b70b43eaa65b8",
            "byte_size": 5192483,
            "substantive_file_count": 15,
            "dedup_verdict": "EXACT_DUPLICATE",
            "dedup_target": "DS-000011",
            "note": "All 15 substantive members are byte-identical (SHA-256) to 15 of the 17 files already registered under DS-000011. No new evidence; no new dataset registered.",
        },
        "supplied_xlsx": {
            "filename": "Youtube Algorithm Explained (2026) .xlsx",
            "sha256": "10290b46f6894f09e7039394b09da3ea5fa3cdbd93aca82c34a02a0d0ce9494a",
            "byte_size": 506708,
            "row_count": 63,
            "unique_source_count": 62,
            "duplicate_groups": [{"rows": ["51.0", "52.0"], "reason": "identical content_hash within the workbook"}],
            "dedup_verdict": "VARIANT",
            "dedup_target": "DS-000018",
            "note": ("Row-for-row content matches (difflib quick_ratio >=0.92, mostly >=0.98 after stripping "
                     "hyperlinks/URLs) the 63-tab '2026 Algorithm Update' Google Docs snapshot already registered "
                     "as DS-000018. DS-000018 additionally contains one video (tab-47) absent from this workbook. "
                     "No new dataset registered; this is a reformatted re-export of already-captured evidence."),
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    diag = sub.add_parser("diagnose", help="Diagnose a target channel against one or more benchmark channels.")
    diag.add_argument("--target", required=True)
    diag.add_argument("--benchmarks", required=True, help="comma-separated channel IDs")

    bench = sub.add_parser("benchmark", help="Cross-channel pattern benchmark.")
    bench.add_argument("--channels", required=True, help="comma-separated channel IDs")

    registry = sub.add_parser("training-registry", help="Emit the training-knowledge registry.")

    blueprint = sub.add_parser("blueprint", help="Assemble a new-channel strategy blueprint.")
    blueprint.add_argument("--niche", required=True)
    blueprint.add_argument("--benchmarks", required=True, help="comma-separated channel IDs")

    args = parser.parse_args(argv)

    if args.command == "diagnose":
        benchmarks = args.benchmarks.split(",")
        result = diagnose_channel(args.target, benchmarks)
        print(json.dumps(result, indent=2, default=str))
    elif args.command == "benchmark":
        channels = args.channels.split(",")
        result = benchmark_channels(channels)
        print(json.dumps(result, indent=2, default=str))
    elif args.command == "training-registry":
        result = build_training_registry(build_source_inventory_summary())
        print(json.dumps(result, indent=2, default=str))
    elif args.command == "blueprint":
        benchmarks = args.benchmarks.split(",")
        bench_result = benchmark_channels(benchmarks)
        diagnosis_by_channel = {cid: diagnose_channel(cid, [b for b in benchmarks if b != cid]) for cid in benchmarks}
        result = assemble_blueprint(args.niche, bench_result, diagnosis_by_channel)
        print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
