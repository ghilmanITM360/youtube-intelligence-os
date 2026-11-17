# REPORT 1 — Data Inventory & Research Readiness (Senior Health)

Date: 2026-11-11 · Scope: inventory only, koi strategic recommendation nahi.
Reproduce: `python3 -I docs/research/senior-health-2026-11-11/build_inventory.py` (sources read-only).
Outputs: `01-unified-video-table.csv` (778 rows), `01-channel-coverage.csv` (23 rows).

Labels: **OBSERVED** = files se seedha gina gaya · **INFERRED** = data se nikala gaya nateeja · **NOT VERIFIED** = data maujood nahi.

## 1. Headline numbers (OBSERVED)

| Item | Count |
|---|---|
| Competitor channels with usable data | **22** (26 nahi) |
| Competitor videos | **712** (691 long-form, 21 Shorts) |
| Competitor videos with real transcript | **710 / 712** |
| Dr Rehan videos (alag dataset, OWN) | **66** (29 long-form + 37 Shorts per Apify type) |
| Dr Rehan transcripts | 66 / 66 (56 plaintext, 10 timestamped SRT) |
| Duplicate video IDs across sources | **0** |
| Dr Rehan competitor set mein shamil? | **Nahi** — double-counting nahi hai |

## 2. 26 vs 22 — gap ka hisaab

| Status | Channels |
|---|---|
| Data complete (Batch A, Nov 2026 Apify) | 15 |
| Data complete (Batch B, registry, Sept 2026) | 7 |
| Probe only, acquire nahi hui | DoctorLaura-e1w1o (67 videos reported; ~$0.28 approval pending) |
| Acquisition prompt mein thi, koi data nahi | nealkshah |
| Baqi 2 | **NOT VERIFIED** — repo mein koi naam ya record nahi mila |

## 3. Per-channel coverage (OBSERVED)

Snapshot = jab view counts liye gaye. Subs = subscribers at snapshot.

| Channel | Snapshot | Subs | Videos | First → last upload | Total views | Median views | Transcripts | Thumb URLs |
|---|---|---|---|---|---|---|---|---|
| Ansel Senior Health | Nov | 2,200 | 31 | 2026-10-16 → 11-10 | 1,297 | 34 | 31 | 31 |
| Clinical Senior Health | Nov | 706 | 25 | 2026-09-29 → 11-10 | 57,931 | 65 | 25 | 25 |
| DR HENRY JASON | Nov | 14,400 | 6 | 2026-09-30 → 10-23 | 1,757,773 | 3,200 | 6 | 6 |
| Dr Nimra \| Health After 60 | Nov | 1,160 | 21 | 2026-09-29 → 11-07 | 150,215 | 248 | 21 | 21 |
| Dr Sami Senior Health | Nov | 1,040 | 14 | 2026-09-18 → 11-09 | 151,665 | 166 | 14 | 14 |
| Dr. Cale Smith | Nov | 24,000 | 17 | 2026-09-03 → 11-07 | 3,268,948 | 34,123 | 17 | 17 |
| Dr. Dinnes Senior | Nov | 6,590 | 23 | 2026-09-28 → 11-09 | 1,079,311 | 381 | 23 | 23 |
| Dr. Maki Bennett | Nov | 1,960 | 21 | 2026-09-24 → 11-10 | 406,749 | 193 | 21 | 21 |
| Dr. Vitalis | Nov | 34,200 | 27 | 2026-09-10 → 10-19 | 1,125,095 | 12,004 | 26 | 27 |
| Dr. Wade Collins | Nov | 16,100 | 10 | 2026-10-05 → 11-07 | 665,558 | 3,650 | 10 | 10 |
| Dr. William Parker Senior Health | Nov | 94,700 | 26 | 2026-06-21 → 07-28 | 9,608,953 | 125,994 | 26 | 26 |
| Healing & Health | Nov | 4,960 | 20 | 2026-10-21 → 11-10 | 764,880 | 1,440 | 20 | 20 |
| Longevity Harbor | Nov | 762 | 28 | 2026-10-14 → 11-10 | 117,754 | 142 | 28 | 28 |
| Metabolic Insights | Nov | 3,750 | 20 | 2026-10-09 → 11-10 | 241,042 | 1,214 | 20 | 20 |
| Senior Health Board | Nov | 4,690 | 19 | 2026-10-08 → 11-10 | 672,033 | 962 | 19 | 19 |
| Better Health While Aging | Sept | — | 98 | 2021-11-04 → 2026-09-18 | 13,865,335 | 19,346 | 98 | 98 |
| Doctor Thomas | Sept | — | 22 | 2026-06-04 → 07-27 | 2,162,421 | 8,234 | 21 (+1 placeholder) | 22 |
| Dr. Aliza Wright \| Advice | Sept | — | 32 | 2026-06-05 → 07-25 | 295,264 | 217 | 32 | 0 |
| Dr. Ares Senior | Sept | — | 35 | 2026-08-06 → 09-19 | 5,993,457 | 45,512 | 35 | 35 |
| Dr. Elias Senior Health | Sept | — | 29 | 2026-08-06 → 09-09 | 4,322,033 | 87,120 | 29 | 29 |
| Dr. Okoro | Sept | — | 66 | 2026-03-20 → 07-20 | 630,221 | 199 | 66 | 66 |
| Senior Health Hub | Sept | — | 122 | 2025-09-15 → 2026-09-20 | 10,258,640 | 9,539 | 122 | 0 |
| **Decode Your Heart – Dr. Rehan (OWN)** | Nov | **55** | 66 | 2026-02-03 → 11-02 | **14,782** | **114** | 66 | 66 |

Metadata completeness: title, date, duration, views, likes har 778 row mein maujood. Description sirf 3 videos mein khali (Doctor Thomas 1, Senior Health Hub 2).

## 4. Knowledge resources

| Resource | Status |
|---|---|
| Master Playbook PDF (`~/Downloads/YouTube_Automation_Complete_Master_Playbook.pdf`, sha256 `c630c24bc189ac39…`) | OBSERVED: 556 pages, text-extractable, ~92,000 words. 14 pages near-empty (image/divider). Abhi tak sirf pages 1–6 **parhe** gaye hain. Repo ke bahar hai (Downloads), registered dataset nahi. |
| `global-youtube-knowledge/DS-000011` | 17 files. 13 PDFs text-extractable (~78,000 words; sab se bari "YouTube algorithm guide" 47,420 words). `Hook (1).pdf` aur `Hook guide.pdf` same content (58 pages, 10,002 words dono) — ek hi baar gina jaye. 2 `.docx` (Nano-Banana, VEO 3) image/video prompt guides hain, is project ke liye low relevance. |
| `DS-000018` | "2026 Algorithm Update" Google Docs snapshot zip — abhi unzip/parha nahi. |
| `DS-000031` | Creator strategy corpus `.txt`, 70 KB. Pichle audit (memory note, 2026-10-26) ke mutabiq yeh zyada tar AI paraphrase hai → claims HYPOTHESIS class. |
| `data/knowledge/reference_knowledge.db` | Maujood (`ref_rule`, `ref_section`, FTS). AGENTS.md ke mutabiq analysis mein retrieve + cite karna lazmi. |

Knowledge files abhi sirf **inventoried** hain, **analyze nahi** hue.

## 5. Data-quality issues

| # | Issue | Class | Asar |
|---|---|---|---|
| Q1 | Do alag snapshots: 15 channels + Rehan = Nov 2026; 7 channels = Sept 2026 (~7 hafte purane views). | OBSERVED | Cross-batch raw view comparison biased. Outliers sirf **within-channel** baseline par nikalne chahiye. |
| Q2 | Subscribers 7 Sept-batch channels ke liye missing. | OBSERVED | Views-to-subscriber ratio sirf 15 channels + Rehan par possible. |
| Q3 | Sirf ek snapshot per channel (Rehan ke ilawa) — view velocity/time-series nahi. | OBSERVED | Evergreen vs spike ka farq sirf video age se INFER ho sakta hai. |
| Q4 | Video age bohat mukhtalif: 14 channels ki pehli captured upload Sept–Nov 2026 mein hai (kuch videos 1 din purani); Better Health While Aging 2021 se. | OBSERVED | Age-adjustment (views/day, age cohorts) lazmi. |
| Q5 | 30 titles **word-for-word** ek se zyada channels par (misal: "Cardiologist warns: these 4 morning habits…" 3 channels par; "Stool stuck in the rectum…" 4 channels par). 7 cross-channel transcript pairs mein >30% text overlap. | OBSERVED | Yeh channels independent evidence nahi (AGENTS rule 9). INFERRED: template/network cluster. Report 2 mein cluster ko ek evidence unit treat karna hoga. |
| Q6 | 2 videos bina usable transcript: Dr. Vitalis `pZ_TXPAngLA` (missing), Doctor Thomas `fj4TaPrLl8U` (placeholder). | OBSERVED | Negligible (0.3%). |
| Q7 | Dr. Okoro ke 3 transcripts implausible lambe (360–1,718 words/min: `E8agElb1PCo`, `6V_H293FSko`, `9I5eoxexiGk`). | OBSERVED; cause INFERRED (repeated caption lines) | Script-length/density analysis se exclude ya clean karne honge. |
| Q8 | Tamam competitor transcripts plaintext hain, timestamps nahi. 628/712 (88%) auto-generated captions, 78 creator-uploaded, 6 type-unrecorded. | OBSERVED | "First 15–30 seconds" sirf word-count se approximate hoga (~first 40–80 words), exact timing nahi. |
| Q9 | Thumbnails: sirf URLs (images download nahi). Senior Health Hub (122) aur Aliza Wright (32) ke URLs bhi nahi; Aliza ke liye DS-000006 screenshots hain. | OBSERVED | Thumbnail review ke liye images fetch karni hongi; warna NOT VERIFIED. |
| Q10 | Inactive channels: Dr. William Parker (last upload 2026-07-28), Doctor Thomas, Aliza Wright, Dr. Okoro (July), Dr. Vitalis (Oct 19). | OBSERVED; wajah NOT VERIFIED | Channel deletion/strike/abandon — pata nahi. Risk signal ke taur par note. |
| Q11 | Rehan: Shorts count 37 (Apify type) vs 38 (≤60s rule) — ek long-form video ≤60s. | OBSERVED | Report 3 mein Apify `type` field use hoga. |
| Q12 | Rehan ke 56 purane transcripts plaintext; sirf 10 naye timestamped. | OBSERVED | Hook timing limited; $0.224 mein 56 re-fetch ho sakte hain (approval chahiye). |
| Q13 | Koi first-party data nahi: impressions, CTR, AVD, retention, traffic sources, demographics. | NOT VERIFIED (sab) | Yeh metrics kabhi estimate/invent nahi honge. |
| Q14 | 15 Nov-batch channels registry DB mein registered nahi (sirf extracted CSV/JSONL). | OBSERVED | Analysis par asar nahi; provenance housekeeping baqi. |

## 6. Dr Rehan — pehli OBSERVED jhalak (diagnosis nahi)

- Channel: `UCQIzqH7QZ9viBYpOFqgSXMg`, joined 2026-02-03, 55 subscribers, 14,782 total views, 66 uploads 9 mahine mein.
- 56 common videos ke views Sept → Nov: 8,315 → 9,970.
- Mix: 37 Shorts + 29 long-form. Competitor set mein Shorts sirf 21/712 (3%).
- Median views 114; competitor channel medians 34 se 125,994 tak.

Interpretation Report 3 tak defer hai.

## 7. Research readiness

| Analysis | Ready? |
|---|---|
| Within-channel outlier detection, topic/title/format clustering (712 videos) | ✅ |
| Transcript structure/hook analysis (710 transcripts) | ✅ (timing approximate) |
| Views-to-subscriber ratio | ⚠️ 15/22 channels |
| Thumbnail analysis | ⚠️ images fetch karni hongi |
| CTR / retention / traffic diagnosis | ❌ Studio export chahiye |
| 26-channel claim | ❌ 22 confirmed |
