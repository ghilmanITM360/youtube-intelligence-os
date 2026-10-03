# YouTube Thumbnail Forensic Intelligence — Compact V1

**Inventory and inspection batch 001 · 2 October 2026 · IN PROGRESS**

This is a traceable first installment, not the requested exhaustive final report. Only six individual thumbnails have been visually inspected. Findings below must not be generalized to the unopened assets. The remaining work is itemized in `completion-ledger.csv`.

## 1. Executive summary

**DATA:** The repository inventory contains 7,031 file/member occurrences, including 1,452 image files, all decodable. There are 50 ZIP occurrences, zero nested ZIPs, zero image files inside the scanned ZIP/Office containers, and no identical image-byte hashes. This does **not** mean there are no visually repeated thumbnails: screenshots can contain the same image at different sizes or alongside different interface elements.

**DATA:** Three acquisition manifests identify 144 individual thumbnail snapshots: 32 Dr. Aliza Wright long-form; 29 Dr. Elias Senior Health long-form; 43 xkcd long-form and 40 xkcd Shorts. All 144 local image hashes match their manifests. Six long-form extremes were opened at source resolution and reviewed again at 160 × 90 pixels.

**INFERENCE:** The first batch demonstrates why visual quality, public popularity and causal thumbnail effectiveness must stay separate. The highest-viewed Elias example scores only 65/100 because its thumbnail escalates the title into an unverified overnight-repair promise. The lowest-viewed xkcd example scores 83/100, but was only approximately three days old when its views were captured. Neither observation validates the rubric as a performance predictor.

**DATA:** No production first-party analytics export was identified in the inventory. The repository capability status explicitly records `REAL_FIRST_PARTY_DATA_INGESTED=false` as of 11 September. That historical status supports, but does not replace, the present inventory. Unopened screenshots/documents have not yet been cleared of potentially relevant metrics. Registered-image cohorts currently have public views, publication timestamps and snapshot dates, but no verified impressions, registered-impression CTR, watch time, retention, AVD, traffic-source breakdown or experiment outcomes. Blank fields mean unavailable/unverified, never zero.

## 2. Inventory and research method

Scope: `data/`, existing `docs/research/`, and `channels/` in the canonical repository. No new attachments were present in the request; no claim is made about folders elsewhere on the computer. Output files from this study are excluded from its source inventory. Raw evidence and databases were read only.

| Inventory category | Occurrences | Current disposition |
|---|---:|---|
| Registered individual thumbnail snapshots | 144 | 6 inspected; 138 pending |
| Screenshots requiring thumbnail identification/cropping | 120 | Pending visual opening and per-thumbnail mapping |
| Forensic support images | 1,186 | Pending relevance triage; not automatically treated as thumbnails |
| Acquisition/preflight screenshots | 2 | Pending review; not silently excluded |
| All image occurrences | 1,452 | 6 inspected, 1,446 pending, 0 excluded |
| ZIP archives | 50 | Member enumeration/read completed; contents not all semantically reviewed |

The inventory recursively opened ZIP and Office containers, hashed member bytes and recorded complete `outer.zip!/member` provenance paths. No recursion, size, read or decode exception occurred. PDFs were inventoried as files; embedded pages/images remain a distinct pending work item. Successful image decoding is not visual inspection. SHA-256 deduplication detects exact bytes only; perceptual near-duplicate review remains pending.

Persistent image identities are `THB-` plus the full SHA-256 for registered thumbnails. `AS-` identifies other file/member bytes. These IDs survive file moves and reruns; a changed image gets a new ID. Aliases B001-01 through B001-06 below are convenience labels, with full IDs in the audit CSV. Screenshot-derived thumbnails will require source image ID and crop coordinates; none has yet been assigned a falsely certain video match.

Mapping uses acquisition manifests plus the read-only `youtube_inventory.db` videos, channels and video_snapshots tables. Each registered row records image capture date, title, canonical and YouTube video IDs, format, source manifest, local path, metric snapshot and metric observation date. Niche labels are analyst classifications. Prefer same-dataset metrics; source snapshot IDs make any fallback auditable. Date-only metric captures have approximately one-day uncertainty; decimal ages in the machine dataset are calculation outputs, not extra measurement precision.

### Evidence labels and scoring

- **DATA:** Visible marks, text, source metadata and supplied public metrics.
- **SOURCE:** Claims verified in external publications or official documentation.
- **INFERENCE:** Analyst interpretation, diagnoses, eye-path heuristics and scores.
- **HYPOTHESIS:** Proposed explanations or changes requiring testing.

Visual score: story 15; psychological hook 15; title partnership 15; hierarchy 10; mobile readability 10; composition 10; emotion/subject alignment 10; credibility 10; distinctiveness 5. Each component is an ordinal expert judgment: roughly zero for absent/misleading communication, half credit for mixed execution, full credit for unusually clear execution. Credibility evaluates whether the package establishes its promise, not whether the author or presenter is trustworthy. No inter-rater reliability or predictive calibration has been established. Scores are not measured click likelihoods.

## 3. Individual thumbnail audit dataset

`individual-audit-batch-001.csv` and `.json` contain six individualized A–J audits, nine component scores, evidence labels, confidence, source paths and corrective actions. `thumbnail-ledger.csv` contains all 144 registered images, including explicitly unscored pending rows. No score is imputed to an unopened image.

The 160 × 90 contact sheet is a small-display readability check, not a user study or calibrated model of all phone interfaces. Full-size observations were recorded separately. Authenticity and AI generation cannot be established from smooth rendering alone; no image here is labeled definitively AI-generated.

## 4. Actual performance comparisons

**PROVISIONAL public-view extremes within the registered long-form image subset.** These are cumulative view ranks, not matched exposure experiments, verified CTR winners, or complete-channel success/failure labels. Each channel has one common metrics snapshot date; publication ages and distribution contexts differ. Shorts are kept separate and are not in this six-case sample.

| Alias / canonical video | Channel | Niche | Public views | Age at capture | Selected within | Visual score |
|---|---|---|---:|---:|---|---:|
| B001-01 / VID-000169 | Dr. Aliza Wright | Senior health | 31 | ~69 days | Lowest of 32 long-form | 53 |
| B001-02 / VID-000162 | Dr. Aliza Wright | Senior health | 219,009 | ~63 days | Highest of 32 long-form | 67 |
| B001-03 / VID-000231 | xkcd's What If? | Science explanations | 584,173 | ~3 days | Lowest of 43 long-form | 83 |
| B001-04 / VID-000263 | xkcd's What If? | Science explanations | 9,534,650 | ~822 days | Highest of 43 long-form | 87 |
| B001-05 / VID-000301 | Dr. Elias Senior Health | Senior health | 1,186 | ~30 days | Lowest of 29 long-form | 61 |
| B001-06 / VID-000296 | Dr. Elias Senior Health | Senior health | 568,520 | ~24 days | Highest of 29 long-form | 65 |

Aliza and xkcd views were captured on 28 August; their images were acquired 10 and 9 September respectively. Elias metrics are dated 10 September, with images also acquired that day, but historical creative exposure remains unknown. All images may differ from those responsible for accumulated views.

**INFERENCE:** The Aliza and Elias pairs are closer in age than the xkcd pair, but still differ in topic, audience need, release timing, recommendation exposure and possibly creative history. The xkcd low cumulative total is an age-confounded counterexample to a naive “loser” label. Views/day would not solve non-linear distribution or unknown impressions and is not used to declare effectiveness. Formal matched-age/traffic comparisons are unavailable here.

## 5. Instructive cases: strengths, failures and confounders

### B001-01 — Taking Amlodipine for Blood Pressure | Here is What Your Doctors Won't Tell You This!

**DATA:** 31 views; yellow/white text, pointing woman in green scrubs, heart graphic, four bottom benefit icons. Mechanism: **INFERENCE**, hidden information combined with an authority cue. The medicine name is prominent; at 160 × 90 the footer claims and badge cannot be read. Multiple text blocks compete.

**INFERENCE:** The communication failure is density and competing propositions, not an established reason for low views. **HYPOTHESIS:** Retain the medicine name and one accurate question; remove the icon footer and unsubstantiated “99%” framing. Verify badge identity. Confidence: high for visible layout; low for performance explanation. Confounders: topic demand, exposure, image timing, content and audience differences.

### B001-02 — One SIMPLE Change to How You Walk That Could Save Your Life | After 70

**DATA:** 219,009 views; “UNSTABLE WALK” and age text beside a pointing, slightly smiling woman. **INFERENCE:** A recognizable problem and withheld solution create a coherent package; the actual movement is absent. **HYPOTHESIS:** Test an authentic demonstration of the content's first movement instead of the long age block. The high observed views do not establish that the pointing portrait caused them. Same confounders as B001-01.

The two Aliza images use different badge names from the channel label. This is an observed identity inconsistency requiring source verification, not proof of deception, an invented person or an AI portrait.

### B001-03 — What if Earth’s Water Suddenly Disappeared?

**DATA:** 584,173 views at approximately three days; boat, figure and sea creatures falling in white space. **INFERENCE:** The title states the premise while the image supplies a consequence. Thin linework and small fish weaken mobile detail; the story still has a clear hero object. **HYPOTHESIS:** Enlarge one falling marine subject and strengthen line weight. Do not call this a failed thumbnail: age alone makes the raw rank a poor judgment. Confidence: high for observation, very low for a negative performance diagnosis.

### B001-04 — If all humans died, when would the last light go out?

**DATA:** 9,534,650 views at approximately 822 days; bright hut doorway, generator, grave and dark island. **INFERENCE:** A surviving light embodies the unanswered duration question; the grave reinforces human absence. Dark small supporting objects are difficult at mobile scale. **HYPOTHESIS:** Increase their edge visibility without competing with the doorway. The image demonstrates that large human faces and large topical text are not necessary features of every high-viewed package; it does not prove they reduce performance. Confounders include enormous age difference and channel/topic demand.

### B001-05 — What a Stroke Looks Like the Day Before It Hits – Early Warnings You Should Never Ignore!

**DATA:** 1,186 views; large stroke text, arrow toward a distressed older illustrated face, hand on chest. **INFERENCE:** The image loses the title's “day before” distinction and uses a nonspecific distress gesture. This is a communication diagnosis, not a clinical interpretation. **HYPOTHESIS:** Depict one medically reviewed sign actually discussed in the video, with accurate timing, and remove the arrow unless it locates that sign. Confidence: high for marks and text; low for causal popularity attribution.

### B001-06 — Doctor Reveals: The #1 Best Fruit to Eat for Healthy Eyesight!

**DATA:** 568,520 views; face beside “THE FRUIT / REPAIRS EYES / OVERNIGHT / CATARACTS”; no fruit pictured. **INFERENCE:** Hidden identity plus rapid transformation is a strong curiosity mechanism, but the thumbnail materially escalates the title's healthy-eyesight promise. It supplies no evidence for overnight repair. This report does not endorse the health claim or infer that the full video substantiates it. **HYPOTHESIS:** Remove the unsupported speed/treatment promise and align the package with the verified content. High views cannot compensate for an unestablished promise. Confidence: high for title/image mismatch; low for effect on viewer behavior.

## 6. Visual pattern library — first-batch candidates only

| Candidate | Classification | Supporting IDs | Contradiction / boundary | Appropriate interpretation |
|---|---|---|---|---|
| Title supplies premise; picture supplies consequence | Cross-niche candidate | B001-03, B001-04; partial B001-05 | B001-02 succeeds in raw views with no movement illustration | Transfer information division; no measured lift |
| Yellow/white type plus right-side older/person portrait | Niche-specific candidate | B001-01,02,05,06 | Appears in both high and low public-view examples | Style alone does not explain outcome |
| One unsolved question | Cross-niche candidate | B001-02,03,04,06 | B001-01 has curiosity rhetoric but low raw views | Coherence hypothesis, not a causal rule |
| Large face is necessary | Unproven; counterexamples present | Face in B001-02,06 | B001-03,04 have no large human face | Avoid treating faces as universal requirement |
| Arrows establish effectiveness | Unproven | B001-05 contains arrow | B001-06 has higher views without arrow, different topic | Arrow presence cannot be ranked causally |
| Extreme promise establishes quality | Unproven; reject as scoring shortcut | B001-06 has high views | Low credibility score and unverified promise | Popularity and credibility remain separate |

Exact hero-area fractions, palette proportions, text occupancy, background-complexity measurements and full-dataset associations have not been computed. No fabricated effect sizes, significance tests, cross-niche robustness claims or aesthetic universals are reported. Six deliberately selected extremes are unsuitable for prevalence estimates or correlation mining.

## 7. Title–thumbnail partnership

**INFERENCE:** Separate four jobs: title identifies premise/audience; image makes a concrete situation visible; the unresolved question motivates investigation; content must fulfill that question. B001-03 and B001-04 provide the cleanest examples in this batch. B001-01 largely repeats the title and adds competing claims. B001-06 changes the promise rather than merely illustrating it. Full transcript/content verification remains pending for all six.

## 8. Cross-niche storytelling framework

**HYPOTHESIS, not validated design law:** Audience-relevant premise → one visible subject/action → a meaningful missing answer → a truthful payoff. Science may use an impossible physical consequence; senior-health education may use a recognizable problem and a responsibly bounded explanation. Transfer the relationship between premise and visual evidence, not the portrait, colors, medical claims or illustrations. Use a face when its expression/action communicates needed information; use an object when it carries the story better.

## 9. Failure taxonomy

- **Competing propositions:** B001-01 splits attention among secrecy, medicine, age and four benefits.
- **Missing action:** B001-02 promises movement but pictures only a pointing presenter.
- **Mobile detail loss:** B001-03's small animals and B001-04's dark contextual objects.
- **Temporal promise loss:** B001-05 drops “day before” from its visual claim.
- **Promise escalation:** B001-06 adds overnight repair and cataracts.
- **Analytical mislabeling:** Treating B001-03's low cumulative rank as failure despite its young age.

These are communication or analysis failure modes. None is a demonstrated cause of low CTR in this dataset.

## 10. Evidence-backed operating rules and research

**SOURCE:** Registered-impression CTR covers views following counted thumbnail impressions; it is not all views divided by impressions. Traffic-source mix changes CTR, and small differences without sufficient data should not drive conclusions. The often-cited 2–10% range is descriptive across many videos/channels, not a target or universal quality threshold. [YouTube CTR FAQ](https://support.google.com/youtube/answer/7628154?hl=en).

**SOURCE:** Impressions require eligible YouTube surfaces; the help page specifies visibility for more than one second with at least 50% of the thumbnail visible. External websites/apps, notifications and some other exposures are excluded. Follow the registered-impressions-to-views-to-watch-time funnel rather than mixing denominators. [YouTube impressions and watch time](https://support.google.com/youtube/answer/9314486?hl=en).

**SOURCE:** Analytics separates videos, Shorts and live content and distinguishes discovery sources including Browse, Suggested and Search. Compare like formats and source contexts where the export supports them. [YouTube content performance](https://support.google.com/youtube/answer/12220281?hl=en).

**SOURCE:** YouTube advises readable typography, limited complexity and accurate titles. It recommends examining Home/Suggested CTR during the first 24 hours for videos with above-average impressions, and Subscriptions-feed CTR for subscriber response. Treat these as audience-specific checks rather than pooling everything. [Thumbnail and title tips](https://support.google.com/youtube/answer/12340300?hl=en-GB).

**SOURCE:** Intro retention describes who remains after the first 30 seconds; YouTube notes a strong intro may reflect a match to title/thumbnail expectations. Spikes can reflect interest or confusion, so they are not automatically positive. Retention is a video-level report. [Audience retention](https://support.google.com/youtube/answer/9314415?hl=en).

**SOURCE:** Scene-viewing research found that semantic meaning helps explain gaze allocation beyond low-level image salience in its experiments. This does not establish YouTube CTR effects or a fixed eye path for these thumbnails. **INFERENCE:** Prioritize a meaningful subject and legible relationship, not contrast alone. [Henderson & Hayes, 2017](https://www.nature.com/articles/s41562-017-0208-0).

**INFERENCE:** Readability corrections in this report are supported by direct 160 × 90 inspection; proposed CTR or watch-time gains remain hypotheses. A clinical assertion would require separate appropriate medical evidence and content review; no such assertion is being validated here.

## 11. Genuine A/B/C test recommendations

**SOURCE, checked 2 October 2026:** Current official guidance supports up to three titles, thumbnails or paired title/thumbnail variants, tested concurrently. Native results use watch time share; current result labels include Winner, Performed Same and Inconclusive. Tests may take up to two weeks; Shorts are ineligible. The older thumbnail-only help URL now redirects to this expanded guidance. [YouTube A/B testing](https://support.google.com/youtube/answer/16391400?hl=en).

**HYPOTHESIS:** On an eligible owned video, keep its title and content constant when isolating a thumbnail mechanism. Save variant files/hashes, start/end timestamps and native outcome. Do not treat sequential thumbnail replacements as randomized tests. Do not stop merely because an early result looks favorable; retain an inconclusive result as inconclusive. A paired title/thumbnail test tests the package, not the independent effect of either component.

| Test | A | B | C | Learning question |
|---|---|---|---|---|
| Walking explanation | Accurate short condition line + verified presenter | Same copy + actual movement demonstration | Same copy + clear two-stage movement depiction | Which visual communicates the promised action? |
| Last-light science explanation | Existing eligible original/control | Same scene with brighter generator outline | Same scene with larger grave silhouette | Does contextual legibility improve qualified engagement? |
| Eye-health nutrition explanation | Truthful nutrition wording + face | Identical wording + actual discussed fruit | Identical wording + fruit and smaller face | Is identity concealment needed when the premise is accurate? |

These are test briefs, not generated assets or launched experiments. Do not retain an unsupported treatment claim as a control. Record native watch-time outcome first; inspect available source-specific CTR, AVD and retention as diagnostic context without inventing variant-level metrics the interface does not supply. Repetition across videos/channels is needed before declaring transferability.

## 12. Limitations, sources and next steps

The inventory is complete for the stated directories and supported container formats; semantic analysis is not. All 120 screenshots, 138 remaining registered thumbnails, 1,186 forensic support images and two preflight images remain pending. PDF page review, embedded-image extraction, near-duplicate checks, full source-content promise checks, all-channel title/metric reconciliation and formal cohort assembly also remain pending. No asset is silently excluded. Finance and other niches in screenshots are not represented by this first visual batch.

Continue in traceable batches, update the ledger only after actual opening, then rebuild the final report from all completed observations. Review middling performers and counterexamples before estimating associations. A final all-channel winner/loser ranking and cross-niche rule set would be premature now. Collect genuine Studio exports and native experiment results where available; public views alone cannot close that gap.

External sources were checked on 2 October 2026 and are linked beside the supported claims. Local source provenance is preserved in the CSV/JSON rows. This installment is delivered in Markdown and structured CSV; a final PDF has not been produced while the report remains incomplete.
