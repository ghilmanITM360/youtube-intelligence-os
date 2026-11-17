# PROMPT — Senior Health: 18 naye channels (Apify extraction + Registry add)

Is poore prompt ko doosre Claude account/session mein paste karein. Token (`APIFY_TOKEN`) us session ke terminal environment mein pehle se export hona chahiye (`export APIFY_TOKEN=...` phir `claude` chalayein). Token chat mein kabhi paste na karein.

---

## ROLE AUR AUTONOMY

Tum is repo ke liye executor ho. Mujhe (owner) bar bar mat poochna. Jo kaam neeche likha hai wo poora khud karo: access check, pilot, full run, validation, registry add, commit, draft PR. Sirf in surton mein ruk kar poochna:
1. `APIFY_TOKEN` environment mein nahi hai (token mujhse chat mein mat maangna, bas bata do ke export karna hai).
2. Projected cost Apify ke bache hue balance se zyada hai (neeche "Cost rule").
3. Koi step AGENTS.md ke rule todta hai.

Jawab Roman Urdu mein do. Tokens/credentials kabhi print, log, commit ya file mein mat likhna.

## REPO

- Path: `/Users/ghilmanislam360/Documents/youtube-intelligence-os` (private repo, Python 3.12, SQLite + files)
- Pehle padho: `AGENTS.md` (core rules: raw evidence modify nahi, provenance rakho, facts/AI-inference alag, duplicates detect karo).
- Apify adapter (already maujood, naya mat likho): `scripts/apify_youtube_ingest.py` — actor `streamers/youtube-scraper`, stdlib-only, `APIFY_TOKEN` sirf process env se padhta hai, `DEFAULT_COST_CAP = 0.50` USD, SAFE_INPUT_KEYS allowlist.
- Registry script: `scripts/register_supplied_channel.py` (pehle `--help` aur code padho; naya registrar mat banao). Registry DB: `data/catalog/youtube_channel_registry.db` (Git LFS, 75 channels / 2,303 videos, un mein 8 Senior Health).
- Reference pattern (is ko follow karo, copy nahi): branch `research/monkey-explains-1999-metadata`, draft PR #38 — seven-sheet workbook, CSV/JSONL master, validation report, public vs members-only handling, run report.
- Naya branch: `research/senior-health-metadata`, base = latest `origin/main` (`git fetch` phir `git worktree` ya clean checkout; mere uncommitted audit changes `research/finance-economics-intelligence` par hain, unhein mat chhoona).

## 18 CHANNELS (Dr. Elias Senior Health SKIP — registry mein pehle se hai)

| # | Channel | URL |
|---|---|---|
| 1 | DR HENRY JASON | https://www.youtube.com/@drhenryjason |
| 2 | Dr Nimra – Health After 60 | https://www.youtube.com/@DrNimraHealth |
| 3 | Neal K. Shah | https://www.youtube.com/@nealkshah |
| 4 | Dr. Dinnes Senior | https://www.youtube.com/@DrDinnes-YT |
| 5 | Doctor Laura | https://www.youtube.com/@DoctorLaura-e1w1o |
| 6 | Dr. Wade Collins | https://www.youtube.com/@Dr.WadeCollins |
| 7 | Senior Health Board | https://www.youtube.com/@SeniorHealthBoard-t |
| 8 | Longevity Harbor | https://www.youtube.com/@LongevityHarbor-tv |
| 9 | Dr. Cale Smith | https://www.youtube.com/@Dr.CaleSmith |
| 10 | Dr. Maki Bennett | https://www.youtube.com/@Dr.MakiBennett |
| 11 | Dr. Vitalis | https://www.youtube.com/@DrVitalisHealth |
| 12 | Ansel Senior Health | https://www.youtube.com/@AnselSeniorHealth |
| 13 | Metabolic Insights | https://www.youtube.com/@MetabolicInsights-H1B |
| 14 | Dr. William Parker Senior Health | https://www.youtube.com/@Dr.WilliamSeniorHealth |
| 15 | Dr Sami Senior Health | https://www.youtube.com/@DrSamiSeniorHealth |
| 16 | Clinical Senior Health | https://www.youtube.com/@ClinicalSeniorHealth |
| 17 | Healing & Health | https://www.youtube.com/@HealingHealth-l4c |
| 18 | DR, Alan A.M | **URL maujood nahi** — registry/repo (`data/`, `docs/`) mein khoj lo; na mile to is channel ko `PENDING_URL` likho, baqi channels rokay bina aage barho |

Skip: **Dr. Elias Senior Health** (`@Dr.EliasYT`) — registry mein pehle se, dobara scrape mat karo.

Har URL ko run se pehle verify karo (channel resolve hota hai, naam match karta hai). Jo resolve na ho use `UNRESOLVED` mark karo, chup chaap bhoolo mat.

## KAAM KA ORDER

### Step 0 — Access check (non-destructive)
- `APIFY_TOKEN` env mein hai ya nahi (value print mat karna). Nahi hai → ruk kar mujhe batao.
- Apify account ka bacha hua credit/limit API se dekho (token header mein, URL mein nahi) aur run report mein likho.
- `git status`, `gh auth status`, Python 3.12 check.

### Step 1 — Duplicate / registry check
- Har channel ko registry mein handle/URL/naam se dhoondo. Jo pehle se hai usay skip karke batao.
- Registry ka SHA-256 pehle aur baad mein record karo.

### Step 2 — Pilot (sirf 1 channel)
- Ek chhota channel chuno, `scripts/apify_youtube_ingest.py` se chalao (maxResults chhota, shorts/streams policy MonkeyExplains report ke mutabiq).
- Asal cost naapo. Per-video cost × total videos se poore 17 channels ka projection nikalo.

### Cost rule
- Pilot ke baad projected total cost vs Apify balance compare karo.
- Total ≤ balance → seedha full run.
- Total > balance → metadata-only (subtitles/transcripts band) pehle chalao; transcripts ko `PENDING_PURCHASE` likho. Phir bhi balance se zyada ho to ruk kar mujhe numbers ke sath poochna.
- Adapter ka `DEFAULT_COST_CAP` per-run guard hai; usay chupke se mat barhao, flag se explicit barhao aur report mein likho.

### Step 3 — Full extraction (har channel ke liye)
Jo kuch actor deta hai sab save karo: channel info (id, handle, subscribers, description, joined, country, links), saare videos (id, title, URL, publish date, duration, views, likes, comments, description, thumbnail URL, tags), shorts/streams alag, subtitles/transcripts (jahan afford ho), public vs members-only/unavailable ko alag flag karo. Raw Apify JSON jyon ka tyon alag save karo (kabhi edit nahi); derived tables alag.

### Step 4 — Output location (repo ke ANDAR, `YIOS-local-audits` mein NAHI)
`research/senior-health-metadata/` mein:
- `raw/` — har channel ki raw actor JSON + input config (token ke baghair) + SHA-256 manifest
- `SENIOR_HEALTH_VIDEO_MASTER.csv` aur `.jsonl`
- `SENIOR_HEALTH_CHANNELS.csv`
- `TRANSCRIPTS_ALL.jsonl` (jo mile)
- `SENIOR_HEALTH_METADATA.xlsx` — seven-sheet workbook (MonkeyExplains wala layout)
- `RUN_REPORT.md` — Roman Urdu mein: kitne channels/videos/transcripts, gaps, cost, balance, UNRESOLVED/PENDING items
- `VALIDATION_REPORT.md`

### Step 5 — Registry mein add karna (8 purane Senior Health channels ke sath)
- `scripts/register_supplied_channel.py` se har naya channel registry DB mein daalo, niche = Senior Health, source = Apify run (provenance/run id/hash ke sath), taake baad mein in par research ho sake. Purane 8 channels ko haath mat lagana.
- Provenance rule: har field ka source batao; AI inference ko fact mat banao.
- Registry DB LFS hai — `git lfs` sahi se chalna chahiye. Add ke baad registry validators chalao (repo ke existing validator scripts; `scripts/` aur `tests/` dekho) aur channels/videos ke counts (pehle/baad) report mein likho. Expected: 75 → 75 + (resolved naye channels).

### Step 6 — Validation
- `python3.12 -m pytest -q` (existing 462+ tests pass rehne chahiye), `ruff check`.
- Registry integrity (`PRAGMA integrity_check`, foreign keys).
- Cross-check: CSV rows = JSONL rows = registry videos; duplicate video IDs; empty fields ki ginti.
- Secret scan: koi token/key koi file mein na ho.

### Step 7 — Git
- Naye branch par commit (chhote, saaf messages), phir push (force push NAHI), phir **draft PR** kholo (MonkeyExplains PR #38 jaisa). `main` mein merge mat karna. Doosre branches/PRs ko mat chhoona.
- PR description mein: kya add hua, cost, gaps, UNRESOLVED/PENDING list.

## AAKHRI JAWAB (Roman Urdu, mukhtasar)
Table: channel | videos | transcripts | status (OK / SKIPPED / UNRESOLVED / PENDING_URL) + total cost + Apify balance + PR link + registry counts pehle/baad. Jo kaam nahi hua wo saaf likho.
