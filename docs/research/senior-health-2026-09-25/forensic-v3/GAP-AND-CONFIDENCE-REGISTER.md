# Gap & Confidence Register — Senior Health Forensic V3

**Date:** 2026-09-25
**Purpose:** Per the master research brief's Section 17/26 acceptance criteria — an explicit accounting of what is missing, what conclusion it limits, whether it's reducible with existing repository/browser evidence, and what stays permanently unknowable. This register also records the statistical sensitivity/robustness checks the Stage 2 audit already performed, so they aren't silently lost in the underlying agent transcripts.

---

## 1. Internal channel and video coverage

**Status:** Strong. 73 canonical channels, 2,149 videos, 2,137 real transcripts corpus-wide; the 6-channel/306-video Senior Health cohort is exactly accounted for (independently re-verified in Stage 2). 44 channels have full video-metadata coverage; 29 remain identity-only (outside the Senior Health cohort, not a current blocker).

**Gap — CLOSED (2026-09-25, second audit pass):** The 6-channel cohort was originally hand-selected (`00-cohort-readiness.json`), not derived from a systematic niche-classification pass over all 73 canonical channels. A full content-based reclassification of all 73 channels has now been run — see `CHANNEL-REGISTRY-CLASSIFICATION.md`. Result: **zero additional Senior-Health-relevant channels found**; the hand-picked 6 remain the complete verified population (58 channels are genuinely unrelated niches — finance, history, general fitness, parenting, science-explainer — and 9 remain identity-only/unresolved pending acquisition, so this could still change). Two new caveats surfaced by that same pass, not previously documented anywhere in V2 or V3: (1) 3 verbatim-identical video titles were found shared between two "independent" cohort channels (`Dr. Ares Senior` / `Dr. Elias Senior Health`), plus heavily templated scripts across all 6 — meaning some of the cohort's apparent independence is illusory (shared content-mill source); (2) all 6 channels' "Dr."/"Cardiologist"/"Surgeon" branding is unverified — a sampled transcript reads as generic scripted narration, not a credentialed individual. See `STAGE2-CORRECTION-LEDGER.md`'s second-pass section for full detail.

**What this limits:** The "6-channel internal cohort" may not be exhaustive of the repository's actual Senior-Health-relevant holdings. Conclusions about "internal competitor coverage" are scoped to the 6 hand-picked channels, not validated as the complete internal set.

**Reducible?** Yes — with existing data (no new acquisition needed): a title/description keyword pass over all 73 channels' video corpora could surface additional relevant channels already sitting in the registry under a different `target_group` label.

---

## 2. Historical performance snapshots

**Status:** Weak, and permanently limited. All view counts (internal and external) are single point-in-time captures — the registry has no historical snapshot table, and none of the external YouTube research includes repeated observations over time.

**Gap:** No case in this investigation can show *when* views accumulated — whether a breakout's views arrived in the first 48 hours (organic/subscriber-driven) or accumulated over months (recommendation-driven, long-tail). The master brief explicitly warns against inventing this.

**What this limits:** Every "breakout" in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` is described by its *current* view count relative to surrounding videos' *current* view counts — a defensible relative-outlier measure, but not proof of *when* the multiple was achieved, or whether early velocity vs. slow-burn accumulation explains the difference between e.g. SeniorHood's 1.05M video and its neighboring 1.3K-view siblings.

**Reducible?** Partially, going forward only — this repository could start capturing daily/weekly snapshots for the cohort channels from today. Cannot be reduced retroactively; this is a genuine, disclosed permanent gap for all data already collected.

---

## 3. Transcript precision

**Status:** Strong for coverage (305/306 real transcripts), weak for exact timing. `TRANSCRIPT-FORENSICS.json` timestamps (hook position, payoff position, etc.) are `APPROXIMATED_FROM_WORD_POSITION`, not verified against actual video playback — this is explicitly disclosed in the V2 status file and holds up under audit.

**What this limits:** Any claim like "the payoff arrives at 8 minutes" should be read as "the payoff arrives after roughly this fraction of the script's word count," not a verified timestamp. For most narrative-structure claims (does a hook exist, is there an open loop, is the promise fulfilled) this doesn't matter; for claims sensitive to exact seconds (e.g., comparing two videos' hook length to the second) it does.

**Reducible?** Yes, but expensive — would require actually watching/scrubbing each video rather than parsing transcript text, which is a large time investment not undertaken in V2 or V3.

---

## 4. Thumbnail evidence

**Status:** Mixed. 149/149 sampled thumbnails were LIVE_WEB_VISUAL-inspected (not just labeled from a URL) per V2, and the Stage 2 audit found the "answer-withholding thumbnails outperform" claim survives a genuine per-channel confound check (WITHHELD > REVEALED in 5/5 channels tested) — this is one of the strongest, most-scrutinized claims in the whole corpus.

**Gap:** Only 149 of 306 videos have thumbnail observations (the other 157 were never sampled); the REVEALED category has only 14 videos corpus-wide, a thin base for the specific magnitude of its effect (though not for its direction). Several cohort channels have no `thumbnail_url` in the registry DB at all (confirmed under DQ-19) — coverage relies on raw Apify exports and repository snapshots, not a uniform DB field.

**What this limits:** The withheld/revealed finding's *direction* is well-supported; its exact *magnitude* (the specific multiples reported) should be treated as indicative, not precise, given n=14 on one side.

**Reducible?** Yes — the remaining 157 un-sampled videos' thumbnails could be pulled from the same raw Apify/live-web sources already used for the 149.

---

## 5. External competitor coverage

**Status:** Substantially expanded in V3. Original external sample: 172 videos across 13 clusters, 5 channel pages (not 6, per NC-04), 4 watch pages. V3 added: 16 more external channels opened in full for the small-channel breakout investigation (2 new successes, 4 documented failures, 10 screened/excluded), surfacing a previously-undocumented "content-mill ecosystem" of 10+ near-identical small channels sharing one script template.

**Gap:** This remains a disclosed *sample*, not a census — one flagged lead (`Imperial Fitness Hub`, 128K views on what may be a small channel) was found but not opened due to research-time budget. The 13 topic clusters from V2 were not re-audited for completeness against the master brief's full topic taxonomy in Section 5 (e.g., no dedicated cluster for "Longevity/Healthspan" or "Chronic Conditions" as distinct from the exercise/nutrition clusters already covered).

**What this limits:** Cross-niche or adjacent-cluster conclusions (anything outside exercise/nutrition/cardiovascular framing) rest on thinner external evidence than the core clusters.

**Reducible?** Yes, with more live browser research time — no acquisition blocker, just effort.

---

## 6. Google Trends coverage

**Status:** REFINED as of Stage 2 audit, now under active remediation. All 32 entries have complete query/geo/property/time-window/capture-date metadata (unusually rigorous for this kind of research). However: (a) one entry (GT-20) was directly falsified by live re-verification — its causal claim about post-upload search-interest lift does not hold; (b) no raw exported artifact (CSV/screenshot/full time series) existed behind any of the 32 entries prior to this V3 pass — only a duplicated hand-typed summary in two files.

**Remediation in progress:** A dedicated re-capture pass is running as of this writing to pull and save the actual full time-series data for all 32 queries (not just summary stats), and to give GT-20 a corrected, re-verified write-up. See `TRENDS-RECAPTURE-SUMMARY.md` (produced separately) for the outcome.

**What this limits, until remediation completes:** Any conclusion resting specifically on GT-20 (the "shower frequency" search-interest story) should not be cited. All other 31 entries' *numbers* checked out in the 5-entry audit spot-check (4/5 exact), but the *evidence-preservation* gap (no raw artifact) was real regardless of whether the numbers were accurate.

---

## 7. Historical competition evidence

**Status:** Reasonably strong. 10 historical-context events, all with real checkable sources (2 independently live-verified in Stage 2, both matched exactly). Confidence labeling is honest — 1 explicitly rejected, 4 more marked LOW — no case of a weak source being silently upgraded to support a conclusion.

**Gap:** This is a sample of 10 hand-selected events tied to specific case studies, not a systematic scan of the health-news landscape across the full 306-video corpus's upload window (Sep 2025–Sep 2026).

**Reducible?** Partially — more events could be researched for additional case studies as they're built, but a fully systematic scan is a large undertaking not attempted in V2 or V3.

---

## 8. First-party analytics

**Status:** Absent, and this is the single largest limitation on the entire investigation's causal claims. File-based ingestion is schema-ready (`first_party_analytics_status: SCHEMA_READY_NO_DATA` for the cohort channels), but no real YouTube Studio export (impressions, CTR, average view duration, traffic source, audience retention curve) has been ingested for any channel, internal or external.

**What this limits:** Every performance claim in this entire research program — internal and external, V1/V2/V3 alike — is a statement about *outcome* (view count) correlated with *packaging* (title/thumbnail/hook), never a statement about *mechanism* (why the recommendation system chose to surface it). The Stage 2 audit and the small-channel breakout report both state this explicitly rather than implying causation. This is not fixable with more browser research — it requires the channel owner's own first-party data, which this project does not have for any competitor and does not yet have for the user's own (not-yet-launched) channel.

**Reducible?** Only for the user's own channel, once launched, via the already-built ingestion pipeline. Not reducible for any competitor channel — this is a hard, permanent limit on competitive intelligence in general, not specific to this project.

---

## 9. Medical verification

**Status:** Strong. 24 claims reviewed, exact 10/2/9/3 breakdown independently reproduced, 4 spot-checked entries all cite real, checkable sources with logically consistent verdicts — including one case (MV-19) where the review itself caught and rejected a likely-fabricated "Stanford study" citation, which is a meaningful positive signal about the review's rigor.

**Gap:** 24 claims is a sample tied to the specific videos already investigated in depth, not a claim-by-claim review of all 306 videos' medical content. New content surfaced in V3 (e.g., the 12 additional Senior Health Hub clove breakouts, the external SeniorHood/Amos Boone videos) has not been medically fact-checked.

**Reducible?** Yes, incrementally, as more videos get deep case-study treatment.

---

## 10. Reproducibility of prior research

**Status:** Now well-established as a general property, not just an assertion. The Stage 2 audit independently recomputed 18 distinct claims from raw SQL/Apify sources with zero fabrications found, several reproducing to the exact decimal. This is strong evidence that the underlying pipeline (SQL → JSON artifact) is trustworthy, even though 4 specific errors were caught along the way (NC-01–NC-04).

**Gap:** Reproducibility was checked by re-deriving numbers from the same underlying sources (the registry DB, raw Apify JSON) — it was not checked by re-running the original Python analysis scripts themselves (`forensic-v2/scripts/`) to confirm they produce byte-identical output. A script bug that happens to be undetectable from the final JSON's face value (e.g., a systematic off-by-one that both the script and every downstream check happened to miss) cannot be ruled out by this audit method alone.

**Reducible?** Yes — re-running the original scripts end-to-end against the current DB and diffing output would close this specific residual gap.

---

## Statistical robustness checks already performed (per Section 17's explicit requirement)

The master brief requires checking whether findings survive excluding the largest outlier/channel. The Stage 2 audit performed several such checks organically while verifying claims — recorded here so they aren't lost:

| Finding | Sensitivity check performed | Result |
|---|---|---|
| Answer-withholding thumbnails outperform | Excluded Senior Health Hub (the single most extreme-outlier channel) entirely | WITHHELD median drops from 1.904 to 1.249 but still clearly exceeds REVEALED (0.467) — finding survives |
| Answer-withholding thumbnails outperform | Per-channel disaggregation (5 channels with both categories) | WITHHELD &gt; REVEALED in all 5 individually — not a pooled/confounded artifact |
| Direct-command &gt; warning-style hooks | Per-channel disaggregation (5 channels with both categories) | Holds in 4/5; reverses in 1 (Dr. Elias, but n=1 vs n=3 — too thin to weigh) |
| Title features (curiosity gap, named food, doctor specialty) — Pass-1 claim | Within-channel median vs. raw pooled comparison | **Reversed/collapsed** — this was V2's own DQ-12 correction; raw pooled 3.5x/3.1x/3.5x collapsed to 1.22x/1.49x/0.99x within-channel. Cited here as the cautionary precedent that motivated the other sensitivity checks above |
| 29 matched pairs CLEAN/TIME_CONFOUNDED split | Independent re-derivation from upload-date and upload-index gap, not reused from the file's own labels | Reproduced exactly (14/14/1), though the audit noted the two signals are highly collinear in this dataset given near-daily posting cadence — a caveat on independence, not a reversal |
| Duplication network "first-mover advantage" | Directional win/loss count across all 37 cross-channel same-title pairs, not just cherry-picked examples | 22 second-movers won vs. 15 lost — near coin-flip, actively undercuts a naive first-mover thesis |
| Senior Health Hub "no durable lift" from clove hits | Full 13-breakout inventory (not V2's original 4-hit sample) before/after median comparison | Confirmed at full-inventory scale: ~9,539 before vs. ~9,418 after — still no lift with more than 3x the original sample of hits |

No finding in this table was accepted without an attempt to break it. The title-feature reversal (DQ-12) is the one case where a pooled/raw finding did not survive scrutiny — it is kept in this table as the standing reminder of why every other finding above was re-tested the same way.
