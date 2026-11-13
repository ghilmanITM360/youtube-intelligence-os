# Complete Research Executive Report: finance and economics YouTube channels (2026-11-14)

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention and traffic-source data were never available and are UNKNOWN throughout. This report summarises the other 14 PDFs; it adds no new measurement except the rubric scorecard compile.

## 1. What was studied
Nine channels: Econ in a Nutshell, Casual Finance, Primate Economics, Crayon Capital, MonkeyExplains, Economics Explained, Capital Case, PENNY, Paper Billions TV. Seven are in the read-only channel database (181 long videos with transcripts for the opening test); PENNY and Paper Billions are not (Apify and Chrome only, and only 1 to 4 weeks old, so their numbers are early). Coverage differs: Capital Case, PENNY and Paper Billions are whole channels; the other six are samples.

## 2. What the data supports
1. **Format alone does not decide views.** The same template produced very different views inside the same channel (Capital Case 33k to 380k, Crayon 40k to 4.2M, PENNY 3.3k to 1.15M). Confidence MEDIUM.
2. **Strong videos are mostly a real, named, dated event tied to the viewer's money; weak ones are abstract questions, institutions and full company histories.** Seen in 5 of 9 channels, with exceptions. Selection by views, so MEDIUM-LOW.
3. **Stake-first openings (a number, date or stake in the first 30 words) went with higher views in 4 of 7 channels** (permutation test, pooled +0.64 log units, p < 0.001; per channel p between 0.001 and 0.06), and not in Economics Explained. Labels are rule-based, not blind; topic and channel-age confounds remain. Association only. INFERRED, MEDIUM-LOW.
4. **Thumbnails:** strong ones had a real name or event more often (17 vs 12 of 35); a big number alone did not separate strong from weak. The blind test was leaked, so it is not evidence.
5. **Endings and CTAs did not separate strong from weak** (CTA in 17% of strong vs 25% of weak endings; regex flags).
6. **vidIQ engagement percentage did not separate strong from weak** in 6 channels.
7. **Hits are concentrated:** two videos gave 90.7% of Econ in a Nutshell's views, one gave about 74% of PENNY's. A channel "model" built on one hit is not a repeatable system.

## 3. Playbook rubric (22 rules, page-numbered)
Scorecard below (compiled from each channel report's section 16; PENNY and Paper Billions not scored). Most common gaps: stakes in 5 to 15 s (P13), an open loop before 30 s (P14), direct address (P17). Counts of F/P/N per channel are in the scorecard; they describe rule match, not channel quality.

## 4. Topic discovery result
16 candidates screened (C1 to C3, D1 to D4, E1 to E5, F1 to F4) with Trends, autocomplete, 5 YouTube searches each and closest-video checks; **0 strict PASS**. After the owner allowed a depth tier, one candidate (C1 reframed: two NY Fed and TransUnion releases read side by side) reached **PASS-DEPTH (conditional, not approved)**; its gap check used two transcripts and two primary documents, and two more transcripts are still unread. Reasons: events lose search interest in days; terms with durable demand are covered by large channels; a small-channel pipeline covers news within days. Limits: titles not transcripts for most rejects; Trends read by eye. Full table in PDF 13, detail in PDF 12.

## 5. Decision for the owner
- **Approved first-10 list: empty by design** (PDF 13). Nothing was force-filled.
- **Depth tier (owner allowed 2026-11-14):** a document-depth angle on a covered topic is a conditional second tier, tested as a HYPOTHESIS with a kill rule (PDF 14). It is not tested on audience performance.
- **Launch model** (PDF 14) is a HYPOTHESIS: real dated event with a viewer-money link, stake-first opening, one source chart on screen, 11 to 14 minutes, no Shorts or sponsors in the first 10; judged after 10 videos against the channel's own median with Studio CTR and 30 s retention.

## 6. What is not done (honest list)
| item | status |
|---|---|
| Studio CTR, retention, traffic source | UNKNOWN, needs the owner's first-party export |
| PENNY and Paper Billions 14 and 28 day re-pull | due 2026-11-20 and 2026-12-04; Apify runs above about $0.50 need approval (about $4.7 of $10 used) |
| Blind relabel of 181 openings and thumbnails | needs a fresh labeler |
| Per-video watch log | only samples were watched, the rest NOT WATCHED |
| Winning-technique table with video link and timestamp | not built; PDF 11 has patterns without timestamps |
| Rubric for PENNY and Paper Billions | not scored (no transcripts) |
| Transcripts of Second Start Money (M81o4LQUa_M) and Mike the Credit Guy (SZ7AkgUGVuw) | NOT READ (HTTP 429 on retries); Daily Dollar Doodles and Stank Finance were read |
| Withdrawal of Planet Fitness, Dollar General, Costco drafts (archive, not delete) | not checked in the finance folder |
| Frames for opening and payoff | one video only (Capital Case) |

## 7. How to read the 15 PDFs
01 to 09 one per channel (database report plus live check). 10 cross-channel comparison. 11 techniques and failure patterns. 12 topic discovery (the full pilot). 13 first-10 result. 14 launch blueprint. 15 this report and the rubric scorecard. SHA-256 of every PDF is in `06_PDF_REPORTS/SHA256SUMS.txt`.
