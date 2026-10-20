# Finance expansion from the 12-channel metadata snapshot

This directory is a derived classification layer over commit `967ea707a0d7198754d132a978962baa96073f49` on `research/youtube-12-channel-metadata` (draft PR #39). The source acquisition was not repeated, merged, or mutated.

## Reconciled population

- Acquisition: 445 unique public-video metadata records across 12 channels.
- Finance-eligible acquisition records: 225.
- Exact overlap with the frozen 966-video baseline: 28, all Primate Economics records with matching `Channel_ID`.
- Unique Finance expansion: 197.
- Combined unique research population: 966 + 197 = 1,163.
- Expansion deep audits complete: 0. Metadata presence is not counted as deep analysis.

`FINANCE_INCLUSION_CROSSWALK.csv` contains one decision for every acquired video. `FINANCE_EXPANSION_MASTER.csv` contains only unique eligible additions. `DUPLICATE_OVERLAP_WITH_BASELINE.csv` records exact overlap and owner checks. `SOURCE_PROVENANCE.json`, `EXPANSION_VALIDATION.json`, and `FILE_CHECKSUMS_SHA256.json` preserve provenance and reproducibility.

## Classification boundary

Logical Money, Mark Invests, Primate Economics, Uncle Frank Retirement, and Uncle John Financial are included video-by-video because each captured title/description is directly within Finance and Economics scope. Primitive Education contributes 13 capitalism/mortgage videos. Chronofold contributes two national-history videos whose descriptions explicitly foreground wealth, trade/resources, banking, or economic development; these are marked medium uncertainty pending full-text audit.

All captured monke and Unknown Frequencies videos are out of scope. Timepiece History, What if 4k, and Serious History were reviewed at the individual-video title/description level and conservatively excluded because their stated subjects are general, military, biographical, or ancient history; incidental money, pay, wealth, corruption, or cryptocurrency references were not enough for Finance inclusion.

## Limitations and continuation

The source reports remote thumbnail URLs and generally unavailable transcripts; it contains no private analytics. The next expansion work is evidence registration and the first deep audit, starting with the unique new Primate Economics record `HjlVexL2Lxk` if transcript and thumbnail evidence can be registered without a new scrape. Medium-uncertainty Chronofold decisions should be revisited after full text is available.

Rebuild from the source worktree without network acquisition:

```bash
python3 research/finance-economics-intelligence/build_finance_expansion.py --source-root /private/tmp/yios-youtube-12-channel-metadata/research/youtube-12-channel-metadata
```
