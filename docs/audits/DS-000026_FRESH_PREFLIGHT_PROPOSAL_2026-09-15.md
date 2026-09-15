# DS-000026 Fresh Preflight Proposal

Audit date: 2026-09-15
Audit type: read-only, continuing from pushed checkpoint `bf74d4c` on `main`.
**No Apify Actor launched. No credits spent. No commit/push performed automatically (per instruction).**

Status: **Phases 1–3 and 5 (partial) complete. Phase 4 (authenticated Apify balance/pricing) is BLOCKED and unresolved as of this checkpoint.** A Chrome-extension/claude.ai account mismatch prevented authenticated browser access; the recovery attempt in this session did not resolve it (see "Phase 4 recovery attempt" below). Section 4/5 numbers below remain PENDING, not final.

**Checkpoint re-verification (2026-09-15, this session):** `mcp__claude-in-chrome__list_connected_browsers` was re-run at the start of this continuation. **Result: zero browsers connected**, identical to the prior checkpoint. Per the standing safety rule, this session stopped immediately without opening any authenticated Apify page, without running Apify, and without guessing pricing or balance. The blocker is unchanged and remains the user's to resolve (see Phase 7).

**Three arithmetic/bookkeeping corrections made this checkpoint (details below):** (1) the "4,206 total videos" figure was mis-summed — the correct sum of the 29 per-channel counts already in this document is **4,941**; (2) the Phase 5 allocation table had a duplicate rank ("4" used twice) and one row out of numeric order — both fixed; (3) the "8 original + 1 new" untracked-file count in Phase 1 did not reconcile with a direct `git status` count and has been corrected to **8 pre-existing + 2 new-today reports (10 total)**.

---

## Phase 1 — Repository state verification

```
$ git rev-parse HEAD
bf74d4cfea7f7d63c89e715ee299f531abff5d66
$ git rev-parse @{upstream}
bf74d4cfea7f7d63c89e715ee299f531abff5d66
$ git ls-remote origin refs/heads/main
bf74d4cfea7f7d63c89e715ee299f531abff5d66
```

- Local HEAD == upstream == remote `origin/main`: **identical** (`bf74d4c`).
- Branches: only `main` and `ui/v1` exist locally and on remote (plus `remotes/origin/HEAD -> origin/main`). No stray branches.
- No tracked-file diffs (`git diff --stat HEAD` empty).
- **Untracked-file count, corrected this checkpoint:** `git status --porcelain=v1 -b -uall | grep '^??' | wc -l` = **10 untracked paths** (verified by direct count, not eyeballed). Breakdown: **8 pre-existing (dated 2026-08-28 through 2026-09-14, none touched this session) + 2 new-today (2026-09-15) DS-000026-preflight reports** — not "8 original + 1 new" as an earlier pass at this document stated (that earlier count missed that this proposal file itself is also a new, uncommitted, 2026-09-15 path):
  - Pre-existing (8): `.codex/environments/` (dir, mtime 2026-08-28), `docs/YOUTUBE_INTELLIGENCE_OS_FULL_AUDIT_2026-08-31.md`, `docs/YOUTUBE_INTELLIGENCE_OS_REAUDIT_2026-09-01.md`, `docs/audits/CHANNEL_COVERAGE_LEDGER_FUNDED_2026-09-14.csv`, `docs/audits/INTELLIGENCE_CAPABILITY_AUDIT_2026-09-14.csv`, `docs/audits/REPOSITORY_AUDIT_2026-09-14.md`, `docs/audits/REPOSITORY_AUDIT_HANDOFF_2026-09-14.md`, `docs/audits/REPOSITORY_BRANCH_LEDGER_2026-09-14.csv`.
  - New-today (2): `docs/audits/FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md` (produced earlier today, 3:28–3:43 PM) and this document, `docs/audits/DS-000026_FRESH_PREFLIGHT_PROPOSAL_2026-09-15.md` (the active work product of this continuation).
  - None of the 8 pre-existing paths were modified, moved, or deleted this session. All are documentation/config artifacts, not raw or extracted channel data, and none affect DS-000026 safety guarantees.
- **DS-000026 status:** no `data/raw/channel-data/DS-000026*` directory exists anywhere in the repo. Most recent dataset on disk is `DS-000025` (`data/raw/channel-data/DS-000025`, mtime 2026-09-14). Confirmed DS-000026 has not started, prior to this session's evidence writes below.

## Phase 2 — Remaining-channel authority (29 channels)

Source: `data/manifests/YOUTUBE_CHANNEL_TARGETS.md` (header states "Identity verified, data not extracted: 29") cross-checked against `data/catalog/youtube_channel_registry.db` → `channels` table where `status = 'IDENTITY_VERIFIED_DATA_NOT_EXTRACTED'` (exact literal match, **29 rows**, no memory or prior-report figures used).

Per-channel name, canonical ID, original submitted URL(s), current handle, target group, and identity-evidence locator were pulled from the `channels`, `submissions`, and `identity_evidence` tables and written to:

`data/raw/channel-data/DS-000026/preflight/29_channel_registry_export.json`

All 29 rows currently have `existing dataset status = None` (no dataset assigned) and `evidence_source_type = OFFICIAL_YOUTUBE`, verified `2026-09-14`.

## Phase 3 — Fresh public channel-count lookup

**Method:** direct HTTPS fetch (`curl`, no auth, no API key, zero cost) of each channel's public `/about` page with `hl=en&gl=US` query params to force English locale. YouTube embeds an `aboutChannelViewModel` JSON block in the page's `ytInitialData` containing `channelId`, `videoCountText`, `subscriberCountText`, `viewCountText`, and `joinedDateText`. Each result was matched against the **exact canonical `channelId`** from Phase 2 (not just the first match in the page — the same page also embeds unrelated "recommended channel" shelf data that had to be excluded) to avoid false positives.

**Result: all 29 of 29 channels resolved with an exact channel-ID match** — no `UNKNOWN`s for the total-video metric. Raw evidence: `data/raw/channel-data/DS-000026/preflight/29_channel_public_counts.json`. Lookup timestamp: 2026-09-15 (UTC timestamps recorded per-row in the evidence file).

**Known limitation — explicitly marked UNKNOWN:** YouTube's public pages do not expose a regular-video / Shorts / livestream breakdown anywhere in the static or embedded page data (confirmed by inspecting the full `ytInitialData` tree; no `shortsCountText` or `liveCountText` equivalent exists). Only the **combined total upload count** is publicly available without either (a) the YouTube Data API (not configured in this repo — no API key found in env or config), or (b) a paid scraping call, which this preflight is explicitly barred from making. **Regular / Shorts / Livestream counts are marked UNKNOWN for all 29 channels for this reason**, not inferred or estimated.

### 29-channel table (sorted alphabetically; see Phase 5 for cost-sort ordering once pricing lands)

| # | Channel | Canonical ID | Original submitted URL | Handle | Target group | Total videos (verified) | Regular/Shorts/Live | Lookup evidence URL |
|---|---|---|---|---|---|---:|---|---|
| 1 | Alicia Invests | `UCFPfloFwa6X2UddqRH83rAA` | https://www.youtube.com/@AliciaInvestsUS | @AliciaInvestsUS | ADDED_TARGET | 229 | UNKNOWN (see limitation above) | https://www.youtube.com/@AliciaInvestsUS/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 2 | Bernard | `UC_FStSURaDad8-xo6jH1j4Q` | https://www.youtube.com/@BernardAnimationOfficial/videos | @BernardAnimationOfficial | ORIGINAL_TARGET | 82 | UNKNOWN | https://www.youtube.com/@BernardAnimationOfficial/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 3 | Brick Body | `UCq1V-pmuLDjjTrgFyzxYQ5g` | https://www.youtube.com/@bricklifts/videos | @bricklifts | ORIGINAL_TARGET | 189 | UNKNOWN | https://www.youtube.com/@bricklifts/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 4 | Brofessor Stein | `UCZqJKUTmgB-cffFSzL3ENJA` | https://www.youtube.com/@BrofessorStein/videos | @BrofessorStein | ORIGINAL_TARGET | 220 | UNKNOWN | https://www.youtube.com/@BrofessorStein/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 5 | Casual Finance | `UCrNfRFWnLC3tCy1TnyhVQ7g` | https://www.youtube.com/@CasuallyFinance | @CasuallyFinance | ADDED_TARGET | 191 | UNKNOWN | https://www.youtube.com/@CasuallyFinance/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 6 | Casually Explained | `UCr3cBLTYmIK9kY0F_OdFWFQ` | https://www.youtube.com/@CasuallyExplained/videos | @CasuallyExplained | ORIGINAL_TARGET | 123 | UNKNOWN | https://www.youtube.com/@CasuallyExplained/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 7 | Chat History | `UCicVSNyM7PMXEzdoAsTB02w` | https://www.youtube.com/@ChatHistory/videos | @ChatHistory | ORIGINAL_TARGET | 99 | UNKNOWN | https://www.youtube.com/@ChatHistory/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 8 | Chill Dude Explains | `UCYwOOHF1BZ_hqPVnLnrT_fw` | https://www.youtube.com/@ChillDudeExplains | @ChillDudeExplains | ADDED_TARGET | 826 | UNKNOWN | https://www.youtube.com/@ChillDudeExplains/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 9 | David Explains Money | `UC2ExrTzlNc8uNmNXodWOC-A` | https://www.youtube.com/@DavidExplainsMoney | @DavidExplainsMoney | ADDED_TARGET | 11 | UNKNOWN | https://www.youtube.com/@DavidExplainsMoney/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 10 | Fasted Fred | `UC91LLjU9cbyLBOjSxWR3cMg` | https://www.youtube.com/@ItsFastedFred/videos | @ItsFastedFred | ORIGINAL_TARGET | 87 | UNKNOWN | https://www.youtube.com/@ItsFastedFred/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 11 | Finance Simplified | `UCogYxvdGc8i7qfjPct1c-Bg` | https://www.youtube.com/@FinanceSimplified-USA1 | @FinanceSimplified-USA1 | ADDED_TARGET | 68 | UNKNOWN | https://www.youtube.com/@FinanceSimplified-USA1/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 12 | Ivan Invests | `UCDokTQePVxNZUqmzevDM7NQ` | https://www.youtube.com/@VanillaInvestor | @VanillaInvestor | ADDED_TARGET | 435 | UNKNOWN | https://www.youtube.com/@VanillaInvestor/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 13 | Mark - Retired at 55 | `UCegPlgZVNg0g1pAzZtGH4dw` | https://www.youtube.com/@MarkRetiredAt55 | @MarkRetiredAt55 | ADDED_TARGET | 328 | UNKNOWN | https://www.youtube.com/@MarkRetiredAt55/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 14 | Max Invests | `UCXSpMZ1S5In6aRCyWdM5CAw` | https://www.youtube.com/@MaxInvests-US/videos | @MaxInvests-US | ORIGINAL_TARGET | 118 | UNKNOWN | https://www.youtube.com/@MaxInvests-US/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 15 | Millionaire Problems | `UCQnC6FoEgp4VcmbPTsO9VRQ` | https://www.youtube.com/@millyproblems | @millyproblems | ADDED_TARGET | 9 | UNKNOWN | https://www.youtube.com/@millyproblems/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 16 | Neu | `UChS4VG1jXDcxDnUvwcMcxtg` | https://www.youtube.com/@neu-youtube | @neu-youtube | ADDED_TARGET | 42 | UNKNOWN | https://www.youtube.com/@neu-youtube/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 17 | Nostalgic Wheels | `UC3itSU41yG8jSOk8UudxoaQ` | https://www.youtube.com/@TheWealthCortexx | @TheWealthCortexx | ADDED_TARGET | 27 | UNKNOWN | https://www.youtube.com/@TheWealthCortexx/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 18 | Overhead | `UCmzMVqE2c-yPv7vmjThk4CA` | https://www.youtube.com/@OverheadCosts | @OverheadCosts | ADDED_TARGET | 10 | UNKNOWN | https://www.youtube.com/@OverheadCosts/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 19 | Parenting Hacks | `UC4eR2RUwoQrYEgbzReQV3HA` | https://www.youtube.com/@Parentinghacks-x6k | @Parentinghacks-x6k | ORIGINAL_TARGET | 352 | UNKNOWN | https://www.youtube.com/@Parentinghacks-x6k/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 20 | Parentitude | `UCJ8_5EeAN8fg0JIhxgHKndw` | https://www.youtube.com/@Parentitude | @Parentitude | ORIGINAL_TARGET | 135 | UNKNOWN | https://www.youtube.com/@Parentitude/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 21 | Rick Finance | `UCDLINT0o_8a0kObYN5bBqUw` | https://www.youtube.com/@RickFinance1 | @RickFinance1 | ADDED_TARGET | 112 | UNKNOWN | https://www.youtube.com/@RickFinance1/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 22 | The Career Machine | `UChGiil8Qsg7qdJ0tZsQo2VA` | https://www.youtube.com/channel/UChGiil8Qsg7qdJ0tZsQo2VA | @careermachine-u4f | ADDED_TARGET | 27 | UNKNOWN | https://www.youtube.com/@careermachine-u4f/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 23 | The Expensive Part | `UCe2TLO3VWaMP8EthzGjSG6Q` | https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q | UNKNOWN (no handle on record) | ADDED_TARGET | 26 | UNKNOWN | https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 24 | The Wise Future | `UC5OaD2jizn_ZFQrB6jzXo4g` | https://www.youtube.com/@TheWiseFuture | @TheWiseFuture | ADDED_TARGET | 204 | UNKNOWN | https://www.youtube.com/@TheWiseFuture/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 25 | Tom - Lazy Dividend Investor | `UCUhTFmf6v8Kk2-ofFD2udkg` | https://www.youtube.com/@Tom-Lazy-Dividend-Investor/videos | @Tom-Lazy-Dividend-Investor | ADDED_TARGET | 41 | UNKNOWN | https://www.youtube.com/@Tom-Lazy-Dividend-Investor/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 26 | Tom - Lazy Investor | `UCHKwo7_qXD8ixLZmpPlIb_w` | https://www.youtube.com/@1MillionWithin5Years/videos | @1MillionWithin5Years | ADDED_TARGET | 450 | UNKNOWN | https://www.youtube.com/@1MillionWithin5Years/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 27 | Tom Talks Money | `UCKqgbX0MOmE5ZzyFpTP524g` | https://www.youtube.com/@TomTalksMoney2k/videos | @TomTalksMoney2k | ADDED_TARGET | 215 | UNKNOWN | https://www.youtube.com/@TomTalksMoney2k/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 28 | Wealth Logic | `UCZ-H-n8fa7NqReTRKe7ByEg` | https://www.youtube.com/@TheWealth_Logic/videos | @TheWealth_Logic | ADDED_TARGET | 155 | UNKNOWN | https://www.youtube.com/@TheWealth_Logic/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |
| 29 | quack doc | `UC2NRf0-PH8IiMq5uA5FHJnA` | https://www.youtube.com/@quackdoc/videos | @quackdoc | ORIGINAL_TARGET | 130 | UNKNOWN | https://www.youtube.com/@quackdoc/about?hl=en&gl=US&persist_hl=1&persist_gl=1 |

**Total public uploads across all 29 channels: 4,941** (corrected this checkpoint — re-summing the "Total videos" column above gives 4,941, not the "4,206" previously stated in this document and in the session handoff notes; the per-channel figures themselves were not changed, only the sum). **This is a count of public uploads, not a guaranteed chargeable-result count** — it is the ceiling on chargeable Apify results if every video on every channel were scraped in one batch; actual per-channel Apify result counts may come in lower (e.g. deleted/private/members-only videos are typically not scrapable) and this has not been verified against a live Actor run.

## Phase 4 — Authenticated Apify pricing and balance

**BLOCKED — unresolved.** The Chrome browser extension is signed into a claude.ai account that does not match Claude Code's login, so no authenticated page (old or new Apify account) could be opened. The user confirmed (not independently re-verified this session, since the console could not be opened):
- The previously-used Apify account is exhausted: **$4.28 of $5.00 used**.
- A **second Apify account already exists** and will be used for DS-000026 going forward.

### Phase 4 recovery attempt (this checkpoint, read-only)

Diagnostic steps taken, in order:

1. `mcp__claude-in-chrome__list_connected_browsers` → returned **zero connected browsers** under the current Claude Code account. No browser to select or switch to.
2. `mcp__claude-in-chrome__tabs_context_mcp` → failed with:
   > "Browser extension is not connected: the OAuth token Claude Code is using belongs to a different claude.ai account than the one Claude Code is logged in as. If CLAUDE_CODE_OAUTH_TOKEN is set in your shell or CI profile, unset it (or re-mint it for this account), then run /logout and /login in Claude Code and make sure the browser extension is signed into the same claude.ai account."
3. Checked whether `CLAUDE_CODE_OAUTH_TOKEN` is set in this shell's environment (presence only, no value read/printed): **not set**. This rules out that specific cause for the current process, but does not rule out an account mismatch set up outside this shell (e.g. how the Claude Code app itself was originally authenticated, or which claude.ai account the Chrome extension is signed into).
4. Attempted to read `~/.claude/` config for an account-identifying field (email only, never tokens) to narrow down which account Claude Code is logged in as: **blocked by the Claude Code permission classifier** before any file was read. Did not attempt to work around this.

No credentials, cookies, tokens, or session IDs were requested, printed, or exposed at any point. No sign-out/sign-in flow was available to invoke — the browser extension shows no connected instance at all, so there was nothing to select or reconnect through the advertised flow.

**Conclusion: authenticated Apify verification remains blocked at this checkpoint.** This is a Claude Code account-level fix (re-running `/logout` and `/login` interactively, and confirming which claude.ai account the Chrome extension is signed into) that only the user can perform. **Nothing in Section 4/5 below is final** and no balance or pricing figures were guessed or backfilled with stale values.

*Reference only, NOT used for this proposal's numbers:* the last independently-verified pricing on record in this repo (from the exhausted account, DS-000023–25 preflights) was $4.00 per 1,000 videos written to the dataset, Actor `streamers/youtube-scraper` (Actor ID `h7sDV53CddomktSi5`). This may or may not carry over to the new account and **must be re-confirmed live**, not assumed.

## Phase 5 — Cost allocation

**Cannot be finalized until Phase 4 supplies fresh, new-account pricing and balance — still true as of this checkpoint (browser auth remains blocked, re-verified above).** What can be stated now from Phase 3 data, corrected this checkpoint (previous version of this table had a duplicate rank "4" and one row — The Expensive Part, 26 videos — out of numeric order; both fixed below by re-sorting programmatically rather than by hand):

- **Chargeable results ceiling per channel** = the verified public-upload count in the Phase 3 table (regular+Shorts+live combined, since the split is UNKNOWN — not a guaranteed chargeable-result count, see Phase 3 note above).
- **Cost formula, to apply the moment Phase 4 lands real numbers:**
  ```
  estimated_cost = chargeable_results × authenticated_price
  reserve = $0.30 unless newly authorized otherwise
  usable_balance = current_balance - reserve
  ```
  Every "PENDING" cell below becomes `cumulative_videos × authenticated_price_per_video` once Phase 4 supplies `authenticated_price_per_video` — no other recalculation is needed. **Do not substitute the stale $0.19/channel average or the reference-only $4.00/1,000-videos figure from the exhausted account as an authorization value; both must be re-confirmed live against the new account.**
- **Smallest-catalog-first ordering** (ascending by verified total videos), with a running cumulative-video total so the largest complete allocation within `usable_balance` can be read off directly once pricing lands (find the last row whose `cumulative videos × authenticated_price ≤ usable_balance`; everything after that row is deferred):

| Rank | Channel | Canonical ID | Total videos | Cumulative videos | Estimated cost |
|---|---|---|---:|---:|---|
| 1 | Millionaire Problems | `UCQnC6FoEgp4VcmbPTsO9VRQ` | 9 | 9 | PENDING |
| 2 | Overhead | `UCmzMVqE2c-yPv7vmjThk4CA` | 10 | 19 | PENDING |
| 3 | David Explains Money | `UC2ExrTzlNc8uNmNXodWOC-A` | 11 | 30 | PENDING |
| 4 | The Expensive Part | `UCe2TLO3VWaMP8EthzGjSG6Q` | 26 | 56 | PENDING |
| 5 | Nostalgic Wheels | `UC3itSU41yG8jSOk8UudxoaQ` | 27 | 83 | PENDING |
| 6 | The Career Machine | `UChGiil8Qsg7qdJ0tZsQo2VA` | 27 | 110 | PENDING |
| 7 | Tom - Lazy Dividend Investor | `UCUhTFmf6v8Kk2-ofFD2udkg` | 41 | 151 | PENDING |
| 8 | Neu | `UChS4VG1jXDcxDnUvwcMcxtg` | 42 | 193 | PENDING |
| 9 | Finance Simplified | `UCogYxvdGc8i7qfjPct1c-Bg` | 68 | 261 | PENDING |
| 10 | Bernard | `UC_FStSURaDad8-xo6jH1j4Q` | 82 | 343 | PENDING |
| 11 | Fasted Fred | `UC91LLjU9cbyLBOjSxWR3cMg` | 87 | 430 | PENDING |
| 12 | Chat History | `UCicVSNyM7PMXEzdoAsTB02w` | 99 | 529 | PENDING |
| 13 | Rick Finance | `UCDLINT0o_8a0kObYN5bBqUw` | 112 | 641 | PENDING |
| 14 | Max Invests | `UCXSpMZ1S5In6aRCyWdM5CAw` | 118 | 759 | PENDING |
| 15 | Casually Explained | `UCr3cBLTYmIK9kY0F_OdFWFQ` | 123 | 882 | PENDING |
| 16 | quack doc | `UC2NRf0-PH8IiMq5uA5FHJnA` | 130 | 1,012 | PENDING |
| 17 | Parentitude | `UCJ8_5EeAN8fg0JIhxgHKndw` | 135 | 1,147 | PENDING |
| 18 | Wealth Logic | `UCZ-H-n8fa7NqReTRKe7ByEg` | 155 | 1,302 | PENDING |
| 19 | Brick Body | `UCq1V-pmuLDjjTrgFyzxYQ5g` | 189 | 1,491 | PENDING |
| 20 | Casual Finance | `UCrNfRFWnLC3tCy1TnyhVQ7g` | 191 | 1,682 | PENDING |
| 21 | The Wise Future | `UC5OaD2jizn_ZFQrB6jzXo4g` | 204 | 1,886 | PENDING |
| 22 | Tom Talks Money | `UCKqgbX0MOmE5ZzyFpTP524g` | 215 | 2,101 | PENDING |
| 23 | Brofessor Stein | `UCZqJKUTmgB-cffFSzL3ENJA` | 220 | 2,321 | PENDING |
| 24 | Alicia Invests | `UCFPfloFwa6X2UddqRH83rAA` | 229 | 2,550 | PENDING |
| 25 | Mark - Retired at 55 | `UCegPlgZVNg0g1pAzZtGH4dw` | 328 | 2,878 | PENDING |
| 26 | Parenting Hacks | `UC4eR2RUwoQrYEgbzReQV3HA` | 352 | 3,230 | PENDING |
| 27 | Ivan Invests | `UCDokTQePVxNZUqmzevDM7NQ` | 435 | 3,665 | PENDING |
| 28 | Tom - Lazy Investor | `UCHKwo7_qXD8ixLZmpPlIb_w` | 450 | 4,115 | PENDING |
| 29 | Chill Dude Explains | `UCYwOOHF1BZ_hqPVnLnrT_fw` | 826 | 4,941 | PENDING |

- **Total across all 29 = 4,941 public uploads** (corrected — see Phase 3; verified by script, not hand-summed).
- **Complete-batch alternative:** launching all 29 at once = up to 4,941 chargeable results (ceiling, may be lower in practice), cost PENDING (Phase 4).
- **Uncertainty carried forward:** the regular-video/Shorts/livestream split is UNKNOWN for every channel (Phase 3), so the true chargeable-result count per channel could differ from the public-upload count shown here if the Actor prices or filters by content type — this cannot be resolved without either a live Actor run or the YouTube Data API, neither of which has been used.
- **$0.30 reserve** carried forward per prior DS-000023/24/25 preflight convention, to be re-confirmed with the user for the new account.
- **Deferred channels and additional credit required:** cannot be computed without Phase 4's authenticated balance and price. Once available, deferred channels = every row after the last one satisfying `cumulative videos × authenticated_price ≤ usable_balance`; additional credit required = `(4,941 × authenticated_price) - current_balance`, if positive, to cover all 29 in one batch.

## Phase 6 — Explicit non-launch statement

- **No Actor was launched. No credits were spent.** All Phase 3 lookups used unauthenticated public HTTPS requests to `youtube.com`, not Apify.
- DS-000026 does not exist as a dataset record, manifest, or Actor run anywhere in the repository.
- No raw evidence (`data/raw/`) outside the newly-created `data/raw/channel-data/DS-000026/preflight/` directory was touched; no existing dataset (`DS-000020`–`DS-000025`) was modified.
- No `git commit` or `git push` was performed.
- **This document is incomplete pending Phase 4.** It will be revised once the Chrome-extension login is fixed and a fresh authenticated Apify Console check on the new account can run.

## Phase 7 — Continuation handoff (browser auth still blocked)

**Exact browser error observed:**
> Browser extension is not connected: the OAuth token Claude Code is using belongs to a different claude.ai account than the one Claude Code is logged in as. If CLAUDE_CODE_OAUTH_TOKEN is set in your shell or CI profile, unset it (or re-mint it for this account), then run /logout and /login in Claude Code and make sure the browser extension is signed into the same claude.ai account.

**Safe checks already attempted (all read-only, no credentials touched):**
- `list_connected_browsers` → 0 browsers connected.
- `tabs_context_mcp` → account-mismatch error above.
- `CLAUDE_CODE_OAUTH_TOKEN` presence check in this shell → not set here.
- Read of `~/.claude/` for account email → blocked by permission classifier, not pursued further.

**What the next session needs to do, in order:**
1. User runs `/logout` then `/login` in Claude Code interactively, confirming the claude.ai account used matches the one the Chrome extension is signed into.
2. Re-check the Chrome extension's signed-in account (its own UI, not via this session) and re-sign-in there if it's on a different account.
3. Re-run `mcp__claude-in-chrome__list_connected_browsers` — expect at least one browser listed once accounts match.
4. Navigate (read-only) to the Apify Console → confirm authenticated account identity, current balance, `streamers/youtube-scraper` pricing, Actor input schema, subtitle/transcript pricing, and whether AI transcription is billed separately. Screenshot/save each as timestamped evidence under `data/raw/channel-data/DS-000026/preflight/`.
5. Fill in Phase 4/5 of this document with real numbers, compute the 29-channel cost table and allocation, and only then decide inclusion/deferral.
6. Continue to **not** click `Save & start` and **not** launch DS-000026 until the user explicitly authorizes it.

**Blockers:** Chrome extension / Claude Code claude.ai account mismatch, unresolved. No balance, pricing, or cost table could be produced this session.

## Phase 8 — Second checkpoint (2026-09-15, this continuation)

Re-ran the only safe diagnostic available (`mcp__claude-in-chrome__list_connected_browsers`) at the start of this continuation, before touching anything else. **Result: 0 browsers connected — identical to Phase 7.** No new sign-in attempt, tab open, or Apify navigation was made, per the standing rule ("if zero browsers are connected... stop immediately"). This session did not repeat the `tabs_context_mcp` call or the `~/.claude/` read, since both already produced their answer (account mismatch; permission-blocked) at the prior checkpoint and re-running them would add no new information.

**No database was rebuilt this checkpoint** (the registry-validator rebuild mentioned in `FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md` was a separate, prior session's action on the git-ignored `youtube_channel_registry.db`; this checkpoint did not re-run that validator and makes no rebuild claim of its own).

This checkpoint's work was limited to: (1) re-verifying the browser-auth blocker is unchanged, (2) correcting the arithmetic and ranking errors in Phases 1, 3, and 5 listed at the top of this document, and (3) not launching Apify, not spending credits, and not committing. **The next session still needs to perform Phase 7's numbered steps 1–6 — nothing here changes that.**

## Phase 9 — Relationship to `FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md` (2026-09-15, cleanup checkpoint)

Both untracked reports were compared line-by-line this checkpoint. They are **not duplicates** — different scope, both retained:

- **`FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md`** is the authoritative **full 69-channel repository audit**: Git/SQLite integrity, dataset-ledger validation, full pytest run (341 passed), package-format inventory, the complete 69-row coverage table, 67-submission reconciliation, visual-evidence and intelligence-output coverage. None of this is reproduced here. Its own §15 DS-000026 sub-section is explicitly labeled non-authoritative by that document itself.
- **This document** is the narrower, more current **DS-000026-specific preflight**: it has a live-fetched, verified 29-channel public-upload count (4,941, via unauthenticated `/about`-page HTTPS requests) that did not exist when the other report was written — that report's §13/§15.2 states these counts as "not available," which is now superseded by this document's Phase 3. This document is also the one satisfying every Phase-3 completeness requirement (29 identity-only channels, 4,941 verified uploads, split-unavailable statement, balance/pricing-blocked statement, no-launch/no-credit/no-Save&start statements, exact next step).
- **Errata on the other report:** its §15.2 ("not available") and §15.5/§15.9/§15.11 rough $0.19/channel-based dollar estimates ($5.51 total, ≈$5.10 additional credit) are superseded for planning purposes by this document's real per-channel counts and its explicit warning not to use that stale average as an authorization value. The other report is left byte-for-byte unmodified (per "preserve historical audit evidence") — this note is the cross-reference instead of an edit to that file.
- **Decision:** preserve both files untracked. This document is the one proposed for commit (see repository-cleanup report for the commit decision); the other remains untracked as a preserved historical audit, not proven redundant.
