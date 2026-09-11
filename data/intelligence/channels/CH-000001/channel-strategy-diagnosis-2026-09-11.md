# Matty Invests (CH-000001) -- Channel Strategy Diagnosis

# Executive Diagnosis

Target: Matty Invests (CH-000001). Benchmark: Mr. Finance (CH-000002).
Content pillars observed: RETIREMENT_PLANNING, PERSONAL_FINANCE, UNCLASSIFIED.

# What Is Working

- `RETIREES` -- REPEATABLE_WINNER_FAMILY, 15 items, channel_median_ratio=11.1762.
- `RETIREMENT` -- REPEATABLE_WINNER_FAMILY, 24 items, channel_median_ratio=2.0997.

# What Is Not Working

- `RETIREMENT_WEALTH` -- ONE_OFF_DEPENDENT, 3 items, channel_median_ratio=0.9683.
- `SMART_RETIREES` -- ONE_OFF_DEPENDENT, 6 items, channel_median_ratio=0.9505.
- `RICH_RETIREES` -- ONE_OFF_DEPENDENT, 3 items, channel_median_ratio=0.7325.

# Repeatable Winners

- `VID-000042`: PACKAGING:DIRECT_STATEMENT (median_channel_relative=2.519), HOOK_PROMISE_MATCH:CONTEXT_FIRST (median_channel_relative=3.0821), SCRIPT_STRUCTURE:CALCULATED_ESCALATION (median_channel_relative=0.9683).
- `VID-000005`: PACKAGING:EXPLANATORY (median_channel_relative=4.6983), HOOK_PROMISE_MATCH:NUMBER_LED (median_channel_relative=0.6938).

# One-Off Successes

- `VID-000107` (BREAKOUT): counter-evidence=['COUNTERINTUITIVE_PREMISE', 'COUNTERINTUITIVE_PREMISE']; causality=ASSOCIATION_ONLY.

# Weak / Failed Experiments

- `VID-000156` (WEAK_RELATIVE_PERFORMER): root-cause layers -- HOOK_PROMISE_MATCH (CONTEXT_FIRST archetype (REPEATABLE_PATTERN, median_channel_relative=3.0821)); SCRIPT_STRUCTURE (CALCULATED_ESCALATION archetype (REPEATABLE_PATTERN, median_channel_relative=0.9683)).
- `VID-000158` (WEAK_RELATIVE_PERFORMER): root-cause layers -- HOOK_PROMISE_MATCH (NUMBER_LED archetype (REPEATABLE_PATTERN, median_channel_relative=0.6938)); SCRIPT_STRUCTURE (CALCULATED_ESCALATION archetype (REPEATABLE_PATTERN, median_channel_relative=0.9683)).
- `VID-000157` (WEAK_RELATIVE_PERFORMER): root-cause layers -- HOOK_PROMISE_MATCH (NUMBER_LED archetype (REPEATABLE_PATTERN, median_channel_relative=0.6938)).

# Matty Invests vs Mr. Finance

CH-000002 repeatable-winner families: ['BUSINESS_ECONOMICS']
CH-000002 strong title archetypes: none
CH-000002 strong hook archetypes: ['NUMBER_LED']
CH-000002 strong script archetypes: none

# Training Heuristics That Hold

- `TR-011-002` (via hook:CONTEXT_FIRST): The 3-Step Hook Formula: Context Lean (establish a relatable frame) -> Scroll-Stop word/beat (pattern interrupt) -> Contrarian Snapback (reveal the real, counter-expectation payoff).
- `TR-011-015` (via script:CONSEQUENCE_CHAIN): 'BUT/THEREFORE' causal storytelling: chain scenes and script beats with 'but' (complication) and 'therefore' (consequence) instead of flat 'and then' sequencing.

# Training Heuristics That Do Not Hold

- `TR-011-011` (via title:NUMBERED_SPECIFICITY): Viral Checklist item -- Specificity & Numbers: stats, details, or concrete numbers make a hook/title more actionable.
- `TR-011-011` (via hook:NUMBER_LED): Viral Checklist item -- Specificity & Numbers: stats, details, or concrete numbers make a hook/title more actionable.
- `TR-011-007` (via script:CALCULATED_ESCALATION): Script Analyzer: judge a full script's hook, narrative spine, cinematic imagination, retention mechanics, CTA/monetization, and title/thumbnail alignment.

# Continue

- `ACT-CH-000001-010` hook:WHAT_IF_SCENARIO: repeatable, at-baseline pattern -- no evidence to change it (confidence=LOW).
- `ACT-CH-000001-011` script:CALCULATED_ESCALATION: repeatable, at-baseline pattern -- no evidence to change it (confidence=MEDIUM).

# Double Down

- `ACT-CH-000001-002` title:DIRECT_STATEMENT: repeatable pattern with above-median relative performance (confidence=MEDIUM).
- `ACT-CH-000001-003` title:EXPLANATORY: repeatable pattern with above-median relative performance (confidence=MEDIUM).
- `ACT-CH-000001-006` hook:CONTEXT_FIRST: repeatable pattern with above-median relative performance (confidence=MEDIUM).
- `ACT-CH-000001-012` script:CONSEQUENCE_CHAIN: repeatable pattern with above-median relative performance (confidence=MEDIUM).
- `ACT-CH-000001-013` topic_family:RETIREMENT: repeatable winner family with 3+ items (confidence=MEDIUM).
- `ACT-CH-000001-014` topic_family:RETIREES: repeatable winner family with 3+ items (confidence=MEDIUM).

# Fix

- `ACT-CH-000001-008` hook:DIRECT_QUESTION: below-median relative performance for a recurring pattern (confidence=MEDIUM).
- `ACT-CH-000001-009` hook:NUMBER_LED: below-median relative performance for a recurring pattern (confidence=MEDIUM).

# Reduce / Stop

- `ACT-CH-000001-001` title:COMPARISON_OR_CHOICE: below-median relative performance for a recurring pattern (confidence=MEDIUM).
- `ACT-CH-000001-005` title:WARNING_OR_RISK: below-median relative performance for a recurring pattern (confidence=MEDIUM).

# Test

- `ACT-CH-000001-007` hook:COUNTERINTUITIVE_PREMISE: sample too small to act on yet (confidence=LOW).

# Watch

- `ACT-CH-000001-004` title:NUMBERED_SPECIFICITY: mixed/uncertain signal (confidence=MEDIUM).
- `ACT-CH-000001-016` topic_family:SMART_RETIREES: family success depends on a single outlier item (confidence=MEDIUM).
- `ACT-CH-000001-017` topic_family:RETIREMENT_SAVINGS: family success depends on a single outlier item (confidence=MEDIUM).
- `ACT-CH-000001-018` topic_family:RETIREMENT_WEALTH: family success depends on a single outlier item (confidence=MEDIUM).
- `ACT-CH-000001-019` topic_family:RICH_RETIREES: family success depends on a single outlier item (confidence=MEDIUM).

# Evidence Limitations

- Private YouTube Analytics (CTR, impressions, retention, AVD, watch time, traffic sources, subscriber conversion, audience overlap) are NOT_AVAILABLE for this channel.
- LONGITUDINAL_TREND is NOT_AVAILABLE; only cross-sectional, publish-cohort-aware normalized performance is used.
- Every archetype/family association is CAUSALITY_STATUS=ASSOCIATION_ONLY, never a causal claim.
- Competitor/creator transcript claims are never treated as verified domain fact (medical, financial, or otherwise); high-stakes domain claims require EXTERNAL_VALIDATION per the unified orchestrator before being treated as authoritative.
