# Master prompt (A-N) vs jo repo mein hai: gap map, 2026-11-13

Labels: VERIFIED / INFERRED / UNKNOWN. Folder naam: master prompt `research/finance_economics_9_channel_forensics/` suggest karta hai, magar maujooda folder `research/finance-economics-channel-forensics/` hai aur usi mein 9 channels ke saath 60 aur channels hain. Naya folder nahi banaya (suggestion "existing conventions dekho" kehti hai).

| Part | Maang | Maujooda halat | Gap |
|---|---|---|---|
| Phase 0 | Playbook, global-youtube-knowledge, DB, remote | VERIFIED: Playbook `~/Downloads/YouTube_Automation_Complete_Master_Playbook.pdf` (556 pp), `data/raw/global-youtube-knowledge`, DB, git remote sab mil gaye | koi nahi |
| Phase 1 | Playbook rubric + knowledge map | `00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md`, `GLOBAL_KNOWLEDGE_MAP.md` maujood | Har channel ka **page-numbered rubric score** (Playbook page ke saath) 9 channels ke liye nahi bana |
| Phase 2 | Inventory (records vs unique, duplicates, transcripts, thumbnails) | `DATABASE_INVENTORY.md`, har channel mein `VIDEO_INVENTORY.csv` (7 DB channels) | PENNY, Paper Billions DB mein nahi (Apify raw se); view-snapshot dates alag record nahi |
| Phase 3 | 9 channel reports + **PDF** | 9 `CHANNEL_REPORT`/`LIVE_EVIDENCE_2026-11-13.md` (markdown) | **Koi PDF nahi.** Dated sections CHANNEL_REPORT.md mein baaqi. Har video ka watch log (play kiya / NOT WATCHED) sirf sample par |
| Phase 4 | Cross-channel + winning-technique table (video link + timestamp) | `NINE_CHANNEL_LIVE_COMPARISON...`, opening/thumbnail/ending tests | Technique table mein **timestamp aur source link** nahi |
| Phase 5-6 | Naye topics, Chrome YouTube competition check, Trends 6-window (YouTube Search) | **Kuch nahi hua** | Poora. Ye sabse bara kaam: har candidate ke liye 5 searches, closest video inspect, 6 windows |
| Phase 7 | First 10 videos (sirf PASS) | Launch model mein 10-video **plan** hai, par topics PASS nahi hue | Topics ke bina shortlist nahi ban sakti |
| Phase 8 | Blueprint (A-N) | Launch model HYPOTHESIS ek page | Niche pick, pillars, formats, workflow, scoring matrix, 30-day plan |
| Phase 9 | 15 PDFs, quality inspect | 0 | PDF tooling: pandoc/wkhtmltopdf/reportlab/matplotlib **nahi**; Google Chrome headless HTML->PDF possible (INFERRED, test baaqi) |
| Withdraw | Planet Fitness, Dollar General, Costco | Is repo (finance folder) mein grep karna baaqi | Archived/withdrawn status ke saath preserve karna, delete nahi |

## Hard blockers (UNKNOWN jo main khud nahi bhar sakta)
- Studio CTR/retention/traffic: owner ke first-party export ke bina UNKNOWN.
- Blind labels (opening 181 + thumbnails): taza labeler chahiye.
- PENNY/PB 14/28 din ka data: 2026-11-20 / 2026-12-04 se pehle nahi.
- Trends YouTube Search + har candidate ki Chrome searches: kaafi tool calls, Chrome session chahiye.

## Suggested order (sasta pehle)
1. Chrome headless se PDF pipeline test (1 channel, Capital Case) -> render check.
2. 9 channel PDFs existing evidence se (kuch naya claim nahi), phir synthesis PDFs 10-11.
3. Phase 5-7 alag session mein: candidate topics, searches, Trends. Ye PDFs 12-13-14 ka input hai.
