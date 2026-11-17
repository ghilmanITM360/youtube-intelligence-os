# YIOS Growth Experiment Roadmap — original channels (2026-10-26)

**Premise from the evidence:**
- Public competitor data shows *what has happened* but cannot *predict* (prediction test failed; title effects did not transfer across channels).
- The signals YouTube documents (appeal among those shown, engagement, satisfaction, per-surface behaviour) are only observable on **our own channels**.
- So the highest-value next step is to create owned-channel evidence under controlled conditions.

Nothing here promises views, virality, revenue or rankings.

## Priority order (evidence quality × learning per cost)

| # | Experiment | Why (official + YIOS) | Design | Success / failure metric | Cost / effort | Must NOT claim |
|---|---|---|---|---|---|---|
| **E0** | **Instrument the channel before publishing** | 75/75 channels `SCHEMA_READY_NO_DATA`; the file-based first-party import contract already exists (`data/intelligence/system/first-party-analytics-import-contract.json`, `docs/FIRST_PARTY_ANALYTICS_WORKFLOW.md`) | Define a weekly Studio export (per video: impressions, impressions CTR, views by traffic source, AVD, APV, retention curve, stayed-to-watch for Shorts, new/returning, subs gained). Freeze each export with its date. Log the title/thumbnail actually live at each date | Exports land on schedule with no gaps | Low (≈1 h/week) | That any metric means "the algorithm likes us" |
| **E1** | **Title/thumbnail A/B via Studio "Test & compare"** on every eligible long-form upload | S9: up to 3 variants, winner by **watch-time share**. Title wording effects in competitors were channel-specific (H02/H03 failed replication), so we must learn **our** audience's response | Pre-register a hypothesis per test (e.g. concrete number vs no number; curiosity vs plain statement). Variants must differ meaningfully (S9 tip). Let tests run up to 2 weeks. Log `Winner / Performed same / Inconclusive` | Count of Winner results and their direction across ≥ 20 tests; per-family win rate | Low; time only | A CTR uplift alone (S9: watch time decides). One test is not a rule. "Inconclusive" is a valid result |
| **E2** | **Opening-structure test**: question-first vs answer/stake-first opening | YIOS H11a: question openings were 0.74× within channel (q=0.04) but unreplicated. S3: intro must deliver on the promise quickly | Alternate opening type across matched-topic uploads (or Shorts pairs). Pre-register. Compare first-30-s retention and stayed-to-watch | Relative retention at 30 s; Shorts stayed-to-watch; AVD | Medium (script discipline) | That questions are "bad" in general |
| **E3** | **Decision-math format pilot**: "X vs Y — the real math" with fully reconciled, sourced numbers | Cross-channel recurring winners (rent vs buy 350×/297×; compounding number 51×/67×). Competitor claim audits repeatedly find arithmetic or source errors, so credibility is our differentiation. S6: search ranks on relevance + engagement + quality (E-E-A-T-like) | 6–10 videos with published calculation sheets in the description. Compare against our own other formats | Search share of views over 90 days; AVD vs channel median; survey-like signals not available → comments asking for follow-ups (qualitative only) | Medium–High (research per video) | "This format goes viral". The cross-channel wins are n=4 concept pairs and topic demand is unmeasured |
| **E4** | **Audience-fit validation before production** | Channel identity explains 38–58% of variance. Identical concepts flip between channels (14.8× vs 0.14×) | For each idea, write the viewer, the problem and the payoff in one line. Check against the channel promise. Run a cheap Short or community post on the core claim and look at stayed-to-watch, comments and saves before committing long-form budget | Kill rate of ideas; long-form median of pre-validated vs non-validated ideas | Low | That a Short's result predicts long-form (format units differ) |
| **E5** | **Length test within a topic** | Duration association weak and inconsistent (median ρ 0.09) | For 3–4 topics, publish a tight cut vs a fuller cut on different but matched topics. Compare AVD, APV and total watch time | APV and watch time per impression | Medium | "Longer is better" or "shorter is better" |
| **E6** | **Shorts → long-form bridge test** | Official: format neutrality (S4). Prior validation: 2026 Shorts→long-form bridging reported (partially supported) | Shorts that preview a long-form video's core question vs stand-alone Shorts. Measure long-form views from Shorts-feed/related traffic | Traffic-source rows "Shorts feed" / related, long-form views attributable | Low–Medium | That Shorts views equal long-form value |
| **E7** | **Satisfaction proxies** | S1/S10: satisfaction (surveys) is a core objective but not exposed to creators. YIOS: like-rate is negatively associated with breakouts (9/9 channels), so it is a poor proxy | Track returning-viewer share, end-screen and playlist continuation, comment sentiment (blind-coded), "not interested" is not available | Returning viewers %, continuation rate | Low | That like-rate measures satisfaction |
| **E8** | **Blind re-coding of competitor packaging** (research, no channel needed) | Current analyst prose is outcome-aware (it quotes tiers) | A coder (human or model) sees only title + current thumbnail + first 60 words, never metrics. Code mismatch, specificity, emotion and visual elements. Re-run the tests with this audit's script | Effects that survive BH + LOCO + replication | Medium (≈450 items) | Causation; upload-era thumbnails are unknown |

## Measurement plan after each launch (owned channel)

| Window | Pull | Use |
|---|---|---|
| Day 0 | Title/thumbnail live versions (screenshot + text), upload time, duration | Version log for later attribution |
| Day 2, 7, 28, 90 | Impressions, CTR, views by traffic source, AVD, APV, retention curve, relative retention, stayed-to-watch (Shorts), new vs returning, subs gained | Surface-specific diagnosis: Browse vs Suggested vs Search vs Shorts feed |
| On A/B test completion | Result class + watch-time share | E1 ledger |
| Monthly | Channel medians per format; STRONG frequency with the project's peer rule on **our** videos | Judge strategy on distributions, not single hits |

Diagnosis grammar (official, S7):
- High CTR + low AVD + falling impressions → expectation mismatch (clickbait pattern).
- High CTR + high AVD + low impressions → narrow, loyal audience. Broaden the framing (S3 coffee example) rather than changing the content.

## How the existing YIOS modules should change (proposal only; nothing changed in this audit)

1. `scripts/run_youtube_intelligence.py` plans: attach an **evidence label** to every packaging or hook recommendation. Downgrade any claim that rests on a single channel's pattern to `CHANNEL_SPECIFIC_HYPOTHESIS`.
2. Remove or avoid any composite "virality" score. Replace it with a **research-confidence score** whose inputs are listed: number of supporting channels, replication status, whether owned-channel data exists, and whether the claim audit passed.
3. Add the **peer-ratio rule** (already in `build_baseline.compare`) as the single shared benchmark across niches, so every module uses the same outcome definition.
4. When first-party exports arrive, the first analyses should be: traffic-source share by format, the CTR–AVD quadrant by video, and A/B test outcomes by hypothesis family.

## Highest information-gain data additions (ranked)

1. **Our own Studio exports** (E0). Unlocks every surface-specific question.
2. **A/B test results** at volume (E1). The only causal packaging evidence available to us.
3. **Repeat snapshots of competitor public views** (e.g. weekly for 8 weeks on the existing 1,612). Turns lifetime averages into real velocity curves, so we can see plateaus and long-tail revival. No API use; collection follows the existing user-supplied workflow and needs separate cost approval.
4. **Blind packaging codes** (E8).
5. **Transcripts for the 646 expansion videos**. Enables hook replication (H11) on unseen channels.
6. **Upload-era thumbnails/titles** (if any archive exists). Removes the "current artwork ≠ historical artwork" caveat.
