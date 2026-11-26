# AI-slop risk rules (pre-delivery gate)

- **Source:** Mathur, Liu, Tan, Liu (Google), *Scalable Detection of Adversarial Synthetic Slop and Coordinated Media Abuse: A LoRA-Enabled Multimodal Defense System* (4 pp., no venue or dataset sizes stated). PDF copy (supplied by the user, added 2026-11-17): [`reference/scalable-detection-adversarial-synthetic-slop-mathur-2026.pdf`](reference/scalable-detection-adversarial-synthetic-slop-mathur-2026.pdf).
- **Gate:** `scripts/check_slop_risk.py`. It runs automatically on production scripts (`productions/<project>/**/*SCRIPT*.md|txt`) through the Claude Code hooks (SessionStart banner, UserPromptSubmit guard, PostToolUse check with a user alert), `.githooks/pre-commit`, CI (`validate.yml`) and `production_pipeline.py validate`. See AGENTS.md, "Pre-delivery AI-slop risk gate".
- **Labels:** `PAPER_FACT` means the paper states it. `OUR_INFERENCE` means a rule we derived; it is not shown by the paper.

## What the paper says (PAPER_FACT)

| # | Fact | Paper section |
|---|---|---|
| F1 | Enforcement targets **clusters** of accounts, not single uploads. A cluster is actioned when a coordination detector (Ψ_A) and a synthetic-content classifier (Ψ_C) both fire, and when "a certain percentage of channels" show synthetic patterns. | I, III, Fig. 1 |
| F2 | Ψ_A uses infrastructure signals: API usage patterns, event time series, GenAI-specific metadata. These form "Generation Clusters", meaning accounts likely using the same generative API or script. | II-A, III-A |
| F3 | Ψ_C features: video text embeddings, title/description salient terms ("repetitive, templated narratives"), upload pacing (`avg_log_upload_pace`, `time_to_first_upload_secs`), and visual embeddings. | IV-A |
| F4 | Target verticals: synthetic impersonation, procedural gore, AI-generated scams. Reported results cover TTS narratives, generative NSFW, and procedural shock/gore. | I, Table I |
| F5 | The cluster requirement is a safeguard so that individual creators using AI tools are not penalised ("Creative AI Use" vs "Adversarial Slop"). The system is set for precision over recall. | V-A, VI-A |
| F6 | LoRA + prompt optimisation are meant to adapt fast to new generators (Sora, Kling). The authors call this an "architectural hypothesis" because data is limited. | IV-B, V-C |

## Rules the gate checks automatically (OUR_INFERENCE, derived from F1–F4)

| Rule | Check | Level | Why |
|---|---|---|---|
| R1 | Script 5-gram overlap with any single existing transcript (registry + extracted competitor transcripts) is ≥15%. A score of ≥5% gives WARN. | FAIL | Copying or lightly re-spinning a competitor script is the "templated narrative" signal (F3). |
| R2 | Title is identical to an existing video or one of our other projects. Word-set Jaccard ≥0.8 gives WARN. | FAIL | Title/description salient terms (F3); Senior Health Report 2 found a 12-channel network sharing titles word for word. |
| R3 | ≥3 stock AI/clickbait phrases in the script. | WARN | Generic machine phrasing is what anyone can produce from a prompt. |
| R4 | Script ≥15% overlap with a script in one of **our own other projects** (`productions/<other>/`); ≥5% gives WARN. | FAIL | Reusing one script across our channels makes us look like a Generation Cluster (F1, F2). |
| R5 | No `Sources` section with at least one item (own data, study, document, URL). | FAIL | Substance and accuracy; YMYL niches (health, finance) need it. |
| R6 | Script claims an expert persona ("as a doctor…") and `--verified-presenter` is not set. | FAIL | Synthetic impersonation is a named target vertical (F4). |
| R7 | Provided images/frames have dHash distance ≤5 to a competitor thumbnail in the repo. Distance ≤10 gives WARN. Images come from the script header `images:` or `--images`. | FAIL | Visual embeddings are a named feature (F3); cloned visual templates across channels are a coordination signal. |

## Manual checklist (a script cannot show these; a human confirms each one)

- C1 Upload cadence looks human; no bulk-scheduled bursts (F3 upload-pacing features).
- C2 Our channels do not share accounts, devices, API keys, templates or upload automation in a way that makes them one cluster (F2).
- C3 Realistic synthetic or altered visuals/voice are disclosed with YouTube's altered/synthetic content setting.
- C4 No realistic AI likeness or voice clone of a real person; no invented expert persona (F4).
- C5 A human has checked health/finance claims against the listed sources.

## Hard limits of this gate

1. **It is a proxy.** The paper's strongest signals (F2: account infrastructure, API usage, upload timing) do not appear in a script. PASS means "no risk signal found", never "will not be detected".
2. **Triggers have gaps.** The Claude hook only sees Write/Edit tool calls, and the pre-commit hook must be installed per clone. CI is the backstop for anything merged.
3. **The overlap checks are lexical.** A paraphrased copy can pass R1/R4. Semantic similarity would need a new dependency, which is not approved.
4. **Evasion is out of scope and is itself a violation.** Do not paraphrase, spin or reorder a competitor script, or add noise to images, to push R1/R4/R7 below threshold. The fix for a FAIL is original work, not disguise.
5. **Exceptions:** `--exception R5="reason"` turns that rule's FAIL into an `EXCEPTION` entry, recorded in the report and shown to the user. It is never silent.
   **Reviewed register (2026-11-25).** The CLI flag cannot reach the git hook or CI, which only receive file paths. So `productions/.slop-gate-exceptions.txt` holds per-file waivers (`script | RULE | counterpart | reason`) that the gate itself reads, which makes the hook, CI, Claude hook and pipeline agree. Only R2, R4 and R5 can be waived; R1 (competitor copy), R3, R6 and R7 never can. For R2/R4 the line names the one of our own scripts that the file revises or preserves, and the waiver holds only while no other match fails the rule: an identical title on a competitor video, or a copy of a different project, still blocks. Each waiver prints as `EXCEPTION` with its reason. Valid uses: a documented revision of the same video (identical title), a byte-identical preserved copy of an approved script, and a navigation index that only matched because its file name contains "script". Add a line only with the owner's written approval; never to hide a new script. `productions/.slop-gate-legacy.txt` stays a closed list. Change authorized by the owner's V3 publication directive (chat, 2026-11-25); tests in `tests/test_check_slop_risk.py`.
6. Thresholds are starting values, not calibrated against platform outcomes. Recalibrate them only with evidence, and record the change here.
