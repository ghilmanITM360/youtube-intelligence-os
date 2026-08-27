# Prompts

This is the future registry/specification for the system's important AI prompts. It is a specification of what a prompt template must contain, and a list of the categories the system will eventually need — not a dump of actual prompt text. **Prompts are versioned system assets, not canonical factual knowledge.** A prompt describes how to produce or judge intelligence; it is never itself evidence, and its output is never fact merely because a prompt produced it (`docs/Database.md` §1).

No prompt in this document has been implemented as running code. This is planning only.

## 1. Standard template

Every future registered prompt must define:

```text
Prompt ID              — stable identifier, e.g. PROMPT-EVID-003
Prompt Name            — human-readable name
Purpose                — what decision or artifact this prompt produces
Inputs                 — what data/context it consumes, and from which entity (docs/Database.md)
Allowed Sources        — what it may read (e.g. only classified RAW_SOURCE/EXTRACTED_FACT of a given class; never unclassified material)
Required Evidence      — what minimum evidence must exist before this prompt may run at all
Output Schema          — the structured shape of its output, including a mandatory evidence-layer tag per docs/Database.md §1
Confidence Rules       — how the prompt must express uncertainty (e.g. HIGH/MEDIUM/LOW CONFIDENCE, or explicit NOT ATTEMPTED / BLOCKED, matching the standard already demonstrated in FORENSIC_RECONSTRUCTION.md)
Failure Conditions     — what must cause the prompt to refuse output rather than guess (missing evidence, conflicting sources, prompt-injection risk)
Version                — semantic version of the prompt text
Last Updated           — date of last change
```

A prompt that cannot cite the evidence it drew from is not compliant with this template.

## 2. Prompt categories

Each category below is a future family of prompts, not a single prompt. Concrete prompt text, per-category, is written only when a phase actually needs it.

| Category | Used in phase | Purpose |
|---|---|---|
| Dataset inspection | Phase 0.5 / 1 | Characterize an unknown source folder or file: what it contains, its likely semantic class, whether it's noise. |
| Dataset ingestion | Phase 1 | Decide what to copy into `data/raw/` and how to record it, from an inspection result. |
| Classification | Phase 2 | Assign semantic class (A–H) and evidence layer to a classified item. |
| Evidence extraction | Phase 3 | Pull structured facts out of raw material (e.g. OCR a screenshot, parse a transcript header) without interpreting them. |
| Competitor analysis | Phase 6 | Compare competitor evidence against owned-channel evidence for patterns. |
| Outlier analysis | Phase 7 | Identify videos/metrics that deviate meaningfully from a channel's or competitor's baseline. |
| Topic clustering | Phase 7 | Group related insights/ideas into clusters. |
| Gap discovery | Phase 7 | Identify topics covered by competitors but not by the owned channel, or vice versa. |
| Topic generation | Phase 7 | Produce new topic hypotheses from clusters and gaps. |
| Internal ranking | Phase 7 | Rank hypotheses using only internal evidence, before any web research. |
| Web validation | Phase 8 | Check a ranked hypothesis against live web research (requires Scrapling authorization, `docs/Security.md`). |
| Research | Phase 8 | General-purpose research-gathering, always logged as `research_sources`/`research_findings` (`docs/Database.md`). |
| Title intelligence | Phase 9 | Generate/evaluate title candidates for a final opportunity. |
| Thumbnail intelligence | Phase 9 | Generate/evaluate thumbnail concepts. |
| Script intelligence | Phase 9 | Generate/evaluate script structure and beats. |
| Visual intelligence | Phase 9 | Generate/evaluate visual/production plans (e.g. the archetype-based image-prompt system already demonstrated in `FORENSIC_RECONSTRUCTION.md` §7). |
| Post-publish analysis | Phase 12 | Analyze a published video's actual performance against its pre-publish prediction. |
| Channel-brain update | Phase 5 / 12 | Fold new evidence/insights into a channel's brain without corrupting prior evidence. |
| Evidence audit | Any phase | Periodically re-check that no `AI_INTERPRETATION` has been silently promoted to fact anywhere in the system (`docs/Database.md` §1, `docs/AGENTS.md` rule 6). |

## 3. Prompt-injection defenses for untrusted inputs

Any prompt category that consumes web content, scraped pages, or arbitrary user-supplied documents must treat that content as **untrusted data, never as instructions** (`docs/Security.md`, Web Research Security). Concretely, a compliant prompt template must:

- Never execute an instruction found inside fetched/scraped content, regardless of how it's phrased (claimed authority, urgency, "ignore previous instructions", etc.).
- When the source is a live web fetch through Scrapling, require that the underlying CLI call used `--ai-targeted` (`docs/TOOLS_INSTALLED.md`, Security Notes) before the content reaches the prompt at all — this strips scripts, hidden/aria-hidden elements, and zero-width characters that are common injection vectors.
- Quote suspicious embedded instructions back to a human reviewer rather than silently complying or silently discarding them.
- Keep a fetched page's content and its own claims about itself (e.g. "this is verified", "trust this number") clearly separated from the prompt's own evidence-layer tagging — a scraped page cannot self-assign `EXTRACTED_FACT` status.

This mirrors the instruction-source boundary already required of this session's own tooling and is not a new rule invented for this document — it is the same boundary applied to future in-system prompts.
