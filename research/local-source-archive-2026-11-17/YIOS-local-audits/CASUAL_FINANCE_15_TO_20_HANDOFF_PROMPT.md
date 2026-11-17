# Casual Finance — visual analysis 15 → 20 (continuation prompt)

Tum Casual Finance visual CT_SCAN kaam continue kar rahe ho. **15/15 videos verified aur published hain.** Tumhara target: **5 aur distinct videos complete karke 20/20**, milestone verify karna, phir scoped checkpoint push. 20 par ruk jao (25 baad mein, owner ke kehne par).

## Owner priority aur contract
- Casual Finance owner ki pehli priority hai. Ek video tabhi count hota hai jab uske Visual CT Scan skill ke saare required visual checks (scene, timing, motion, on-screen text, composition, evidence locators) pass hon.
- Contract: **visual-only CT_SCAN**. Audio sirf ASR hai (`ASR_UNCERTIFIED`), isliye AV sign-off BLOCKED rehta hai (owner ne accept kiya). Audio/AV ko alag track karo, count mein mat jodo.
- Excluded: Casual Economics, xtqbRt94TTw (Video006, alag campaign), Oct-20 ke 38 Shorts.

## Paths (same Mac)
- Repo: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`. Checkout, branch, index ko mat chhuo. Koi worktree/clone nahi, koi merge nahi, koi PR nahi, force push nahi.
- Evidence folder: `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/`
  - `visual_complete_ledger.json` (15 entries; `next_milestone` ko 20 karna hai)
  - `count_complete.py` (verified count), `working_list_15_v1.json` (reserve list), `MILESTONE_15_CHECKPOINT.md`, `source_identity_baseline_v1.json` (source SHA-256)
- Operations doc (local, kisi branch par nahi): `~/YIOS-local-audits/VISUAL_FORENSICS_OPERATIONS.md` — pehle padho.
- Skill: `visual-ct-scan` (references 01–14 padho, mode `CT_SCAN`).
- Tooling: `~/YIOS-local-audits/tooling/cf15/` (`asr.py`, `sheets.py`, `publish_milestone_tree.py`), venv `tooling/visual-ct-scan-venv/bin/python3 -I`.
- Per-video workspace: `~/YIOS-local-audits/<date>-<id>-deep-ct-scan/`. Template: sabse latest `2026-11-08-dPoDyl9Ys38-deep-ct-scan` (structure, scripts, outputs copy karo).

## Videos (isi order mein, ek-ek karke)
1. 7K991LgY3tc
2. WCS1bK3KB3U
3. KTnp2OlQJHA
4. Im-N3K9Pnf0
5. gG239LrksH4

Agar koi video blocked ho (source missing, SHA mismatch, validator fail): exact blocker log karo aur reserve se agla lo: -RMZszjZSNE, 0ll9rEtoRrs, 5umJ63d3rzQ, -X6YzlY_8tM, DgbHW0IqHrI. (Last teen ke purane partial folders branch par hain; naya kaam `visual_ct_scan_20261108/` subfolder mein jaata hai, isliye collision nahi.)

## Usage gates (har video se pehle live check: five-hour, phir weekly)
- Naya video sirf tab shuru karo jab five-hour usage ~50% ya usse neeche ho.
- 85% five-hour = checkpoint. 90% = koi naya video/reviewer/extraction nahi. 95% = seal, publish, ruko. Weekly par 95% same rule.
- Credits kabhi spend ya reset mat karo.

## Har video ka recipe
1. Usage check. `~/YIOS-local-audits/vf_lock.sh status` (FREE hona chahiye), phir `acquire <label>` aur token rakho. Kaam ke baad `release <token>`.
2. Source SHA-256 `source_identity_baseline_v1.json` se verify karo.
3. CT_SCAN karo: native timestamps, sub-second event ledger, shots/states, motion, on-screen text, composition, evidence locators. Mandatory outputs skill ke hisaab se (`source_manifest.json`, `coverage.json`, `shot_ledger.csv`, `visual_event_ledger.csv`, `visual_ct_scan_report.md`, `quality_gate.json`, `continuation_handoff.md` etc.).
4. Technical notes: `fullres_changed_px_thr25` frame_metrics mein canonical hai. Multi-frame episodes ke last frame par cut chhup sakta hai (gap check ≥8,000 px). Onset EXACT ke liye ≥20 px, warna BOUND. ASR: `python3 -E tooling/cf15/asr.py wav out.json`. Validator ke liye overview sheets chahiye (`sheets.py ... overview 220`); agar dekhi nahi to disclose karo. cf15 scripts ka cwd = workspace.
5. Validator **42/42** pass hona chahiye. Uske baad hi ledger mein entry add karo (`video_id`, `workspace`, `gate_file`, `validation_json`) aur `count_complete.py` dobara chalao.
6. Max ek targeted reviewer, koi long background job ya polling loop nahi, unrelated kaam nahi.

## Milestone 20 aur publish
- Jab `count_complete.py` ne `VERIFIED_COMPLETE 20 / target 20` diya: ledger mein `next_milestone: 20` set karo, `MILESTONE_20_CHECKPOINT.md` likho (count, video list, kya publish/nahi hua, disclosures).
- Scoped, text-only checkpoint, operations doc ke hisaab se: git plumbing (temp `GIT_INDEX_FILE`, `commit-tree`, normal push `${C}:refs/heads/research/casually-finance-editing-forensics` — zsh mein `${C}:` likhna). Publisher: `tooling/cf15/publish_milestone_tree.py` copy karke use karo. PARENT = `2697d3c6dfda5c744aa1e995235143858f14471d`, prefix `_visual_milestone_20`, commit message mein "20/20".
- Sirf md/json/csv/txt/py/log/tsv/EVIDENCE_SHA256SUMS. **Koi MP4, frames, wav nahi.** Add-only, koi overwrite nahi (WOULD_OVERWRITE aaye to ruko). Push ke baad remote readback (har blob hash compare, 0 mismatch) aur lock release.
- `timeout` command is Mac par nahi hai; plain `git push` chalao.

## Reporting (chhota rakho)
Verified count, naye completed video IDs, blockers, agla video. Kuch bhi un-verified ho to saaf likho.
