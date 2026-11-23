# V1 Rent: research dossier and audio reconciliation (2026-11-21)

Status: DRAFT v1. Written by Claude. Not a script: it contains no new narration.
Branch: visual-audit/casual-finance (base d9f544dd). Nothing pushed.

## 1. Audio (recorded by owner)

| Item | Value |
|---|---|
| Original | `~/Downloads/Generated Audio November 21, 2026 - 9_38AM.wav` |
| Working copy | `audio/v1_rent_voiceover_master.wav` |
| SHA-256 | `63c7ccf458a4356129749a7bba329d731290a3a9e06d1094ae234eaaa1613737` (copy verified equal) |
| Format | PCM s16le, 24,000 Hz, mono, 369.24 s (6:09), 17,723,564 bytes |
| Timing data | `audio/analysis/v1_words_merged.json` (1,096 word tokens), `v1_sentences_timed.tsv` (92 sentences, S001-S092), `pauses_raw.txt` |
| ASR | whisper-cli large-v3-turbo-q5_0, English. Timings are ASR estimates (about +/-0.1 s). Not a forced alignment. |

### 1.1 CRITICAL: the recording does NOT match the approved script

The approved extract is about 802 words. The recording is about 1,100 spoken words. It is a different, spliced take:

| Audio block | What it is | Problem |
|---|---|---|
| S001-S026 (0:00-1:52) | Matches approved script | none |
| **S027-S049 (1:52-3:33)** | NOT in the approved script. A full alternate section ending in a conclusion ("In the end, your own rent depends on your own lease", "This has been a general educational explanation") | A conclusion appears at 3:28, with 2.5 minutes of video still to come. Contains unverified figures (see C-21, C-22). |
| S050-S051 (3:33-3:44) | Vacancy and age adjustments. In the script these follow the panel/sixth-root paragraph | Out of order (they are now after the fake ending) |
| S052-S079, S081-S092 | Matches approved script (minor wording changes) | none |
| S080 | "So the honest answer is narrower than a headline." (extra line) | duplicate of S042 |

Duplicates inside the audio: "We went looking for a clean story" (S036 and S069), "the honest answer is narrower than a headline" (S042, S080), "ask yourself these three things" (S043 and S084), "general educational explanation" disclaimer (S049) and "This is not financial advice" (S090).

Recommendation (owner decision, not applied): re-record, or cut the audio. S027-S049 (112.4-213.3 s) can be removed cleanly in an edit, and S050-S051 (213.6-223.2 s) then sit right after S026, which restores the script order. Cutting leaves about 4:30 of audio. This does NOT change any recorded sentence. Owner must approve the cut before it is used as the master.

## 2. Verified claims

Status key: V = verified against a primary source I read this session. D = derived (arithmetic from verified figures). X = not verified or contradicted. B = Zillow page blocked for me (HTTP 403), value known only from search snippet or from the page text I did read.

| ID | Audio | Narration | Verified value | Source (publisher, date, location) | Status |
|---|---|---|---|---|---|
| C-01 | S002 | Official US rent index rose 2.8% in the year to September | Rent of primary residence, 12-month change Sep 2025-Sep 2026: 2.8% (index 450.402) | BLS CPI release 2026-10-14, Table 1. https://www.bls.gov/news.release/archives/cpi_10142026.htm | V |
| C-02 | S003 | Zillow typical market rent rose 2.7% over the same 12 months | Typical asking rent $1,932, +2.7% y/y, +0.1% m/m (Sep 2026 report) | Zillow Research, September Rent Report. https://www.zillow.com/research/september-2026-rent-report/ | B (page 403; figures from search snippet; capture by hand needed) |
| C-03 | S011 | Rent of primary residence = 7.7% of CPI (Aug 2026 weights) | 7.728 | BLS 2026-10-14 Table 1 "Relative importance Aug. 2026" | V |
| C-04 | S012 | Owners' equivalent rent 25.9% | 25.902 | same | V |
| C-05 | S013 | Shelter 35.3% | 35.323 | same | V |
| C-06 | n/a | (context) Sep 2026 weights differ | Shelter 35.238, rent 7.707, OER 25.853 (Sep 2026 weights) | BLS 2026-11-10 release | V. Label every weight with its month. |
| C-07 | S020 | Each unit priced every six months | "collects rent data from each sampled unit every 6 months" | BLS factsheet https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm | V |
| C-08 | S021-S023 | Six panels; panel 1 in Jan and Jul, next in Feb and Aug | "divides each area's rent sample into six subsamples called panels"; "panel 1 are collected in January and July; panel 2, in February and August" | same | V |
| C-09 | S025-S026 | Monthly change is the sixth root of the six-month ratio | "The sixth root of this relative is the 1-month change" | same | V |
| C-10 | S050 | Vacant unit estimated from newly rented units | "estimated current rent of a vacant unit is its previous rent times the average rent change of newly occupied units" | same | V |
| C-11 | S051 | Age adjustment | "each time the CPI observes the rent of a sample unit, it is 6 months older"; "age-bias factor is applied" | same | V |
| C-12 | S057 | Zillow Oct 2026 index = $1,913 | "typical asking rent is $1,913 in October, flat month-over-month" | Zillow October Rent Report, written 2026-11-12. https://www.zillow.com/research/october-2026-rent-report/ | V (read in browser) |
| C-13 | S058 | A year earlier it was $1,859 | Not printed on the page. 1,913 / 1.029 = 1,859.0 | derived | D. Must be labelled "implied". Check the Zillow data download (ZORI csv) before showing it as a published figure. |
| C-14 | S059 | Rise of 2.9% | "Rents are now 2.9% up from last year" | Zillow Oct Rent Report | V |
| C-15 | S060 | In September it was 2.7% | see C-02 | Zillow Sep Rent Report | B |
| C-16 | S076 | October BLS rent index rose 0.2% for the month | "the index for rent increased 0.2 percent" (Table 1, Sep-Oct 2026, seasonally adjusted) | BLS CPI release 2026-11-10 | V |
| C-17 | S077 | Zillow almost flat in October | "flat month-over-month" | Zillow Oct Rent Report | V |
| C-18 | S078-S079 | BLS printed no 12-month rent change for October | "BLS did not collect survey data for October 2025 because of a lapse in appropriations ... cannot publish 12-month percent changes for October 2026 for indexes where October 2025 data are unavailable" | BLS 2026-11-10 release; notice https://www.bls.gov/cpi/notices/2026/12m-changes-202610.htm | V. The gap is caused by missing October 2025 data, not an omission. A better narration reason exists; the recorded one is accurate but incomplete. |
| C-19 | S082 | The two measures "match within a fraction of a point" today | BLS 2.8% (Sep) vs Zillow 2.7% (Sep): 0.1 pt. Oct 2.9% has no BLS pair | derived | D, true for September only |
| C-20 | S003 | Zillow figure is "typical market rent" | Zillow calls it "typical asking rent"; ZORI is a repeat-rent index of listings, smoothed (3-month moving average), not seasonally adjusted for the headline series | Zillow methodology (search snippet; page 403 to me). https://www.zillow.com/research/methodology-zori-repeat-rent-27092/ | B. Use "asking rent" on screen. |
| C-21 | S031 | "In August 2026 the BLS says the average rent was $1,497" | I found no such BLS figure. The CPI publishes index levels and percent changes, not dollar average rents. | none | **X. Do not show.** |
| C-22 | S032 | Zillow "says $2,131" | Not found. Zillow Sep $1,932, Oct $1,913. Single-family $2,243-$2,266. Zillow's own rental-manager page shows $2,000 (different method). | Zillow Oct Rent Report | **X. Do not show.** |
| C-23 | S029 | "published numbers are seasonally adjusted" | The BLS Oct release table shows the 0.2% as seasonally adjusted. The 12-month 2.8% is a not-seasonally-adjusted change. Not checked further. | BLS 2026-11-10 Table 1 | partly V; needs care |

## 3. Data-vintage problem: Zillow $1,932 (September report) vs $1,913 (October report)

- September report: $1,932, +0.1% m/m. October report: $1,913, "flat" m/m. A $19 drop cannot be "flat" or +0.1% for one month.
- Most likely cause: ZORI history is revised each month (smoothed 3-month index, and the repeat-rent regression re-estimates). This is my inference, not confirmed. I could not open the methodology page to see a revision note (403).
- Rule for the video: never plot Sep $1,932 and Oct $1,913 on one line. Label each figure "as published in the [Month] report ([date])". Prefer percent changes (2.7%, 2.9%) for the comparison, and use $1,913 only as a single labelled level.
- To close this: download the ZORI csv from https://www.zillow.com/research/data/ by hand and read the Sep and Oct values in one vintage.

## 4. Correction report (recorded audio vs facts). Recorded text is preserved; nothing was edited.

1. S027-S049 insert: contains C-21 and C-22, and a premature conclusion. Needs a cut or re-record.
2. S038 "The short answer is not that rent rose 2.8%": confusing. 2.8% is the verified rise.
3. S003 "typical market rent": Zillow's term is "asking rent". Low risk, fix with the on-screen label.
4. S058 "$1,859": implied, not published. Label "implied".
5. S017 "BLS's own explanation" fix is already in the audio. Good.
6. Script header target said 8-10 min. Real audio is 6:09 as recorded (about 4:30 if the insert is cut).
7. Next CPI release is 2026-12-10. Refresh figures if publishing after that.

## 5. Evidence collection status

- BLS pages: readable by tool. Screenshots NOT yet captured.
- Zillow pages: the Oct rent report loaded in the in-app browser. The Sep rent report and methodology page returned "Access to this page has been denied" (403). I did not try to get around it. Needs a manual capture by the owner, or the owner's permission to try another route.
- No screenshots, logos or photos have been saved yet. No licence register yet.

## 6. Take 2 (2026-11-21 10:03) adopted as the narration of record, by owner decision
Script file: V1_RENT_TAKE2_RECORDED_SCRIPT.md. Timeline: audio/take2/t2_words_merged.json (1,124 words). 416.88 s.
Block 122.7-255.1 s claims, all UNVERIFIED (status X) until sourced; do not show a number or a "source" tag for them on screen:
| ID | Audio claim | Status |
|---|---|---|
| C-24 | "In July 2024, a new rule started adjusting the mix ..." (BLS) | X not found in BLS pages I read |
| C-25 | "new construction and old buildings ... half a percent or less" | X |
| C-26 | Zillow rent "September 2024 $2,157", "twelve months before $2,101", +2.7% | X. Different year and level from the $1,932/$1,913 figures; 2,157/2,101 = +2.67%, arithmetic only |
| C-27 | "rent data is checked by independent academic teams" | X |
| C-28 | "Zillow matches the BLS trends very closely over many years" | X no source |
| C-29 | "BLS explicitly accounts for short-term lease renewals" | X |
Visual rule: those sentences get a neutral visual (character, plain text card, no numbers/source tags), or the owner cuts 122.72-255.14 s. Risk: finance claims without sources (gate C5).

## 7. Evidence status update
Headless Chrome capture of BLS returned an Access Denied bot page (no bypass attempted, bad file deleted). All 7 screenshots need manual capture: evidence/CAPTURE_REQUEST.md. Storyboard v1: STORYBOARD.md. Take 2 timeline: audio/take2/.

## 8. Zillow September 2026 figure verified (2026-11-21, owner lead, checked by Claude)
C-02 / C-15 upgraded from B to V. Primary source: Zillow Group investor-relations press release, dateline "SEATTLE, Oct. 6, 2026 /PRNewswire/", https://investors.zillowgroup.com/news-and-events/news/news-details/2026/Zillows-September-Market-Report-shows-an-early-winter-in-the-housing-market-as-newly-pending-sales-fall-8-5/default.aspx . Text read by Claude (WebFetch): "The typical U.S. rent rose 2.7% from a year earlier to $1,932", series named Zillow Observed Rent Index; "biggest annual gain since April 2025". The owner reports a second release dated Oct 15, 2026 with the same figures; Claude did not open it. The release does not explain the method, so "asking rent / smoothed repeat-rent index" (C-20) still rests on the methodology page (403) and should not be stated on screen; the video label is "typical rent".
Still open: the $1,932 (Sep report) vs $1,913 (Oct report) vintage question (section 3), the $1,859 implied figure (C-13), and C-24..C-29.
