# Handoff prompt: 9-channel deep verification (written 2026-11-13)

Copy everything inside the block below and give it to the next AI.

```
ROLE
You are continuing a forensic research study for the YouTube Intelligence OS (YIOS) owner. The owner writes Hinglish/Roman Urdu. Answer the owner in simple Roman Urdu/Hinglish with real numbers, file pointers and evidence labels. No generic YouTube advice.

WHERE TO WORK (do not create a new project, folder, clone or worktree)
- Checkout: /Users/ghilmankhan/workprojects/yios-audit-fixes
- Branch: data/finance-economics-complete-2026-11-11 (verify with git status first; pull/fast-forward only)
- Study folder: research/finance-economics-channel-forensics/
- Read first, in this order:
  1. 04_FINAL_SYNTHESIS/NINE_CHANNEL_LIVE_COMPARISON_AND_LAUNCH_MODEL_2026-11-13.md
  2. 01_CHANNEL_REPORTS/<NNN>_<channel>/LIVE_EVIDENCE_2026-11-13.md for each of the 9 channels (037, 024, 039, 040, 055, 059, 066, 070, 071)
  3. 04_FINAL_SYNTHESIS/FINAL_RESEARCH_CONCLUSIONS.md (see "Live-pass amendments") and FINANCE_ECONOMICS_WINNING_MODELS.md (section D)
  4. 05_OWNER_QA/ (CHANNEL_QA_*.md, EXPLAINER_CLUSTER_PDF_REANALYSIS_2026-11-12.md, APIFY_SPOT_SCRAPES_README.md)
- Source DB (read-only, never modify): data/catalog/finance_economics_complete.db (69 channels; PENNY and Paper Billions are NOT in it). Judge: the "YouTube Automation - Complete Master Playbook" PDF (P05 formats, P13 stakes pp.283/320, P21 topic selection p.33) plus global-youtube-knowledge.

THE 9 CHANNELS (owner's list)
Econ in a Nutshell (066), Casual Finance (037), Primate Economics (055), Crayon Capital (039), MonkeyExplains (024), Economics Explained (040), Capital Case (059), PENNY @pennyexplainsfinance (070), Paper Billions @PaperBillionsTV (071).

OWNER'S GOAL
Verify each of the nine separately, analyze all their data, and find out exactly how each one works: what each channel promises, what repeats, why similar videos succeed or fail, and what a new channel should copy or test. Then update the comparison and the single launch model.

WHAT IS ALREADY DONE (do not redo; build on it)
- All nine have a LIVE_EVIDENCE_2026-11-13.md with Roman Urdu answers to 5 questions (promise, repeating model, why similar videos fail, first video for a new channel, PDF rule), a video table with vidIQ Engagement/Outlier/VPH, Trends, one web search, and limits.
- Coverage: Capital Case 13/13 (whole channel), PENNY 13 long + 5 Shorts (whole channel), Paper Billions 4/4 (whole channel); the other six are 15-video samples (5 strong / 5 typical / 5 weak) or similar.
- Primate and Casual Finance also have opening + middle + payoff frames. Others mostly have ONE mid-frame per video (ads/black frames hit several).
- Cross-channel synthesis + one launch model written, and reconciled with FINAL_RESEARCH_CONCLUSIONS.md and WINNING_MODELS.md (commit 4eddc126, pushed).
- Raw Apify data saved with SHA-256: 070_pennyexplainsfinance/raw/, 071_paperbillionstv/raw/.
- MASTER_TRACKER.csv live_chrome_pass column updated for channels done before PENNY/Paper Billions (not for 070/071, which are not among its 69 rows).

KEY FINDINGS SO FAR (all MEDIUM-LOW, confounded by age/size; re-test, do not trust)
- Same template gives very different views (Capital Case 33k-380k; PENNY 3.3k-1.15M; Crayon 40k-4.2M).
- Strong videos: big famous or in-the-news events tied to viewer money. Weak: abstract questions, institutions, company biographies, repeats.
- vidIQ engagement % does not separate strong from weak (6 channels). Opening style: only Casual Finance and Primate hint (joke/skit-first weaker); other channels no separation.
- Repeats shrink (Monkey Epstein 838k -> 137k; PENNY $40T 1.15M -> 13.6k/3.3k). Hit concentration: Nutshell 2 videos = 90.7%, PENNY 1 video ~74%.
- Primate's "Shorts-first" claim was wrong; its 2026 long median fell to ~162k from ~980k.

WHAT IS NOT DONE (this is your work, highest value first)
1. Studio-level data (CTR, impressions, retention, traffic sources) is UNKNOWN for all nine. Do not invent it. If the owner can export first-party analytics for ANY own channel, use scripts/ file-based ingestion; competitor Studio data does not exist.
2. Transcripts / opening lines: not read for PENNY, Paper Billions (Apify scraper returns no subtitles; yt-dlp is not installed). The DB has transcripts for the other seven (partial for some). Read the first 60 seconds of every strong and weak video and test the "claim-first vs joke/skit-first" hypothesis properly (count, label, show the table).
3. Opening + payoff frames for Capital Case, PENNY, Paper Billions, Crayon, Monkey, Economics Explained, Nutshell (only mid-frames exist). Capture at 0-15 s and the last 30 s, with ad/black-frame handling noted.
4. Thumbnails: only vidIQ cards and a few montages were inspected. Do a blinded per-video thumbnail review for the nine (thumbnails for DB channels are on disk under the study/audit folders; PENNY/Paper Billions thumbnails need downloading via the Apify dataset field thumbnailUrl).
5. Age/size confound: re-pull views for PENNY and Paper Billions after 14 and 28 days (their videos are 1-25 days old); re-pull Capital Case. Compare each video to the channel's own views-at-same-age where publish dates exist. Economics Explained DB has NO publish dates (30 of 457 videos only).
6. Unseen videos: Economics Explained (427 videos outside sample), MonkeyExplains (11 videos under 180 s and newest uploads), Crayon (5 newest not in DB), Primate (2 long videos not viewed: Stocks, Financial Terms), Casual Finance (MicroStrategy is now private), Nutshell (3 uploads after the DB snapshot).
7. Trends: PENNY and Paper Billions have none; Trends window starts Nov 2025 (older uploads not covered). Trends is topic interest only.
8. Per-channel CHANNEL_REPORT.md files are NOT updated with the live findings; only LIVE_EVIDENCE files exist. Update them carefully (do not overwrite originals; add a dated section).
9. Add PENNY and Paper Billions to the DB/tracker only if the owner approves; otherwise keep them as external-source channels.
10. Creator/team/production workflow: unknown for all nine (web search found nothing for Capital Case, PENNY, Paper Billions). Do not guess.
11. Paper Billions channel age is UNKNOWN (joined Sep 21 2022 per Apify, first video 2026-11-06): find out only from public sources.
12. 3 earlier overstated lines were amended (P21 count, Primate Shorts, length). CHANNEL_COMPARISON.md and REPEATED_WINNING_PATTERNS.md still say "46 channels FOLLOWED" and are unedited.

PIPELINE FOR EACH CHANNEL (one at a time, commit after each)
DB inventory (or Apify) -> Chrome + vidIQ pass -> opening transcript read -> frames -> Trends + web -> Roman Urdu verdict (5 questions) -> update LIVE_EVIDENCE (new dated file or dated section) -> tracker -> commit -> push -> verify with git ls-remote.

TOOLS / HOW (learned the hard way)
- Chrome (claude-in-chrome): read vidIQ via JS: document.body.innerText sliced from 'Engagement'. Wait ~9 s after navigate. browser_batch needs a tabId in every action. Ads can cover mid-frames.
- Apify (owner's account, Console in the browser, not the API token): actor YouTube Scraper id h7sDV53CddomktSi5. Input JSON: {"aiVideoDescription":false,"aiVideoSummary":false,"maxResultStreams":0,"maxResults":30,"maxResultsShorts":30,"startUrls":[{"url":"https://www.youtube.com/channel/<UC id>"}]}. Set it with monaco.editor.getEditors()[0].executeEdits after switching to JSON mode; the Save & start button position moves when an "unsaved changes" banner shows, so screenshot first. A small run costs about $0.02-0.07; the account showed about $4.7 of $10 used. Download the dataset JSON from the Export dialog; copy to raw/ and record SHA-256. Ask the owner before any run above about $0.50.
- Tracker CSV uses CRLF; edit with the csv module (live_chrome_pass is column index 18).
- Searching the repo: use `grep -r -i -l --include='*.md' pattern .` (an unquoted zsh glob once made a search fail silently and caused a wrong "not found" claim).

RULES (do not break)
- Never modify raw source evidence. Keep VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN separate; never turn an inference into a fact. Report "weak" only relative to the channel's own baseline and age.
- No new worktrees/clones; no hard reset, force push, or destructive clean; preserve stashes and untracked files. Do not merge or close PRs. Commit trailer: Co-Authored-By: <your model name> <noreply@anthropic.com>.
- Check usage first (5-hour, weekly, context). Near 90% five-hour or 95% weekly, start no expensive work and write a handoff. Spend no paid credits without the owner's approval.
- Never put the owner's name, email or project details into outside services (web search, Apify inputs beyond channel URLs).
- Do not touch or restart the claude-mem worker. claude-mem has been down since 2026-11-12T17:20Z ("Your organization has disabled Claude subscription access for Claude Code"); it is the owner's/admin's to fix. Nothing is being remembered, so keep everything in files and commits.
- Do not give personalized investment advice; this is channel research only.

DELIVERABLES
Per channel: a dated, evidence-labelled addition with the table(s) for the open items above, then an updated NINE_CHANNEL comparison and the single launch model (keep it a HYPOTHESIS with an explicit test and kill rule). End with a short Roman Urdu summary to the owner: kitna ho gaya, kitna reh gaya, aur agla qadam.
```

## Status at handoff
- Branch tip when written: 4eddc126511930150d105e77c6f860092f8f7ee6 (pushed and verified at origin before this file was added).
- Usage at the last check: 5-hour about 52%, weekly about 91%.
