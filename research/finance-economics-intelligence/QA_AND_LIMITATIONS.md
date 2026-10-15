# QA and limitations

**Phase status: RESOURCE_CHECKPOINT.** Reports and a pilot proposal exist, but the complete requested scope is not finished. Deliverable presence is not completion.

## Verified scope

- 13 canonical finance channels, 966 unique videos, 966 titles; 955 nonplaceholder transcripts with 955 distinct exact text hashes. Eleven videos lack available transcript text (ten Lucas Grant placeholders and one Matty Invests gap). Exact hashes do not detect paraphrase/template duplication.
- 794 source-classified long-form, 13 Shorts and 159 unknown formats. No duration-only inference. No new timed transcript segments; 3/10/30-second analysis unavailable in this baseline.
- 176 canonical historical comparisons; 790 insufficient. 34/176 labels change with five-peer sensitivity. No channel-growth-at-publication controls. Current canonical views not fetched.
- 30 transcript excerpt reviews, including nine full stored-text reads. These are AI analyst readings, **not human/audio verification**. Thirty contextual labels do not constitute 966 semantic topic audits.
- 807 registry thumbnail URLs, 159 missing registry fields. Thirty attempted sample videos; 27 downloaded and inspected at 320px width; three remain 404 at both saved maxres and fallback hq URLs. 939 canonical videos lack new mobile review; 936 of those were not in the attempted sample. The two CDN-derived fallback URLs do not repair canonical registry fields.
- 206 Casually Finance and 11 Casual Economics records reused through immutable sources, without new forensic work. Full Economics AV sign-off remains 0/11. These are separate from canonical channels.
- Six additional public channel pages, 180 distinct first-page video cards, rounded metrics and relative dates. They are partial Tier B, not full histories. Emerging-channel growth coverage remains incomplete.
- Distinct referenced Video_ID union is 1,363, with no overlap across canonical, overlays and new landscape. This is a locator/metadata universe, not the count of deep reviews.

## Source gaps and freshness

[Twenty-six original-path dispositions](SOURCE_GAP_DISPOSITIONS.csv) preserve the known missing-machine paths. DS-000001 directly affects this audit: its canonical registry/transcript records are available, while original location recovery and historical observation-time/format gaps remain unresolved. Other missing paths do not block the selected baseline. Existing general knowledge is reused from the indexed canonical copies.

Drive remains 128 discovered candidates with five previously content-reviewed. No Drive connector is available in this session; no new content review is claimed. Available branch reports provide finance reuse despite the cloud gap. No hidden assumption that discovery-only documents have been read.

Canonical dates are August/September-era stored records, not current public totals. Four dataset collection/packaging days support approximate observation dates; ingestion-only datasets are deliberately unranked. Branch snapshots span October 11–14. New channel/thumbnail fetches are October 16 local (UTC metadata can be October 15). A current thumbnail need not match the one that generated historical views.

## Interpretation boundaries

Lexical title/topic/script features are provisional proxies. Evidence-word counts do not verify sources. ASR punctuation distorts sentence statistics. Deep sample is purposive and channel-balanced, not random. Shorts have only one canonical sampled channel, so no cross-channel Shorts generalization is justified. Private metrics remain UNKNOWN. Source financial claims are not all fact-checked. No recommendation to copy scripts, illustrations or channel identities.

The new landscape adds mostly established channels; it does **not** fulfill the requested representative weak/average/emerging-channel study. No exhaustive finance-channel census. No evidence of causal virality or an optimal upload schedule. Backlog ratings are editorial 1–5 equal weights; higher affordability/headroom means easier production/less competition, both uncertain judgments. No probability of success is estimated.

## Validation contracts

`build_baseline.py` opens SQLite read-only and checks its before/after hash. The baseline unittest covers missing date/format/views, age eligibility, format/channel isolation, sparse/zero cohorts, threshold ties and malformed dates. `validate_research.py` checks table joins, counts, image hashes, source blobs, ranking reproducibility, score arithmetic and unchanged canonical evidence. Repository knowledge validation verifies all 2,732 indexed local hashes. Run the tracked secret scanner and whitespace check after staging. Exact-head CI must be rechecked after every push; a previous green head does not certify a new commit.

The initial baseline commit used CRLF CSV lines, caught by whitespace validation; the subsequent generator correction uses LF and regenerates all baseline tables. The public-page collector initially recognized an older renderer and returned identity-only results; corrected capture uses the observed lockup renderer. Initial identity captures are retained separately. Neither issue modified source evidence.

Legacy follow-up: [LEGACY_METADATA_PROBE.json](LEGACY_METADATA_PROBE.json) records the existing inventory catalog's candidate DS-000001 observation day, 2026-08-24, for all 159 records. The original date provenance still needs verification and all formats remain null; no tiers were promoted. Do not repeat this catalog lookup.

Resource checkpoint: live five-hour usage reached 93%, weekly 41%; context UNKNOWN. No new research unit started after this reading. Finish validation/push/CI only. The research remains incomplete; use the remaining matrix in RESUME_HERE.md.
