# YIOS audit: owner report

Machine A, `Ghilmans-Laptop.local`. Audit start 2026-11-05 16:57Z. Final remote check 2026-11-06 03:36:58Z.

Yeh machine Machine A hai, kyunke host, user aur checkout path coordination records se milte hain. Folder name se yeh faisla nahi kiya.

**Audit ki halat:** accessible scope cover ho gaya. Lekin **poora nahi**, kyunke 5,767 list nahi mili aur Machine B yahan se nahi dekhi ja sakti. Yeh dono BLOCKED hain. Depth ki had neeche "Kya nahi hua" mein hai.

## 1. Sab se zaroori baatein

### Machine A par kaunsa pehle ka missing data mila
- Machine B ki 1,000 file identities mein se **988 yahan disk par same hash ke saath hain**.
- Purani 370 "match nahi hui" files mein se **358 mil gayin**. Yeh 358 usi 988 ke andar hain, is liye inhein jama nahi karna. Union 988, intersection 358.
- **Baqi 12 (Finance/NICK) is Mac ki disk par nahi hain, lekin GitHub par mil gayin.** Maine mirror ke bytes se SHA-256 nikal kar match kiya. 10 files `research/portable-recovery/machine-b-2026-11-02/` mein PR #36 tip `f115285b` par hain. Purana `VIDEO_AUDIT_966.jsonl` aur `FINANCE_1612_COMBINED_INTELLIGENCE.xlsx` Git history mein commit `7e70f061` par hain. Poori list: `TWELVE_FINANCE_NICK_FILES.csv`.
- **Casually Finance ke `o3FQcd91MIs` aur `Uumnx2Fo6cE` ki 1,009 external evidence files**, jinhein Machine B ne unavailable likha tha, sab yahan disk par hain. GitHub par in mein se koi nahi.

### Kaunsa unique kaam abhi sirf local hai
Is Mac par **29,526 unique hashes, 17.14 GB logical** aise hain jo GitHub par nahi. Sab se ahem:
1. **Casually Finance — Video006:** workspace `2026-11-01--xtqbRt94TTw-deep-ct-scan` (3,028 files, 592 MB), `Casual-Finance-Video006-EP0002-…` (234 MB), `…followup-…` (37 MB, abhi badal raha hai).
2. **Video006 checkpoint U commit `df22c7e0`:** GitHub par nahi, aur canonical repo mein kisi ref ya reflog mein bhi nahi, is liye wahan prune ho sakta hai. U ki saari 28 files GitHub par hain. Commit aur tree ek bundle mein bhi hain: `Casual-Finance-Video006-progress-20261105T1844Z/Casual-Finance-Video006-U-V-recovery.bundle`, sha `b01faae0…6af4`. Maine use scratch mein khol kar U ka commit aur tree `ae621dfe` tasdeeq kiye. Yeh bundle bhi isi Mac par hai.
3. Source media, `~/Downloads/videos in mp3` (4.1 GB): GitHub par sirf chand LFS payloads hain.
4. `yio-cf-editing-forensics-local-evidence` 4.46 GB, Barely Evolved 1.83 GB, `dr rehan video` 1.42 GB, xkcd What If 1,867 files, Primitive Education 1,512 files aur uska checkpoint J.
5. Git mein: stash `5b6c3042` aur branch `backup/decode-15cbe9f-original` (Decode Your Heart ke 11 blobs sirf yahan).

Yeh sab **ek hi Mac par hain**. Same-Mac copies backup nahi. Sirf `Macintosh HD` mounted hai. Oct 26–29 ka Google Drive backup is audit mein dobara verify nahi hua, is liye off-device status **UNKNOWN**.

### 5,767 hash comparison: BLOCKED
**List nahi mili, is liye yeh comparison nahi hua.**
- Search: 6 YIOS roots ki 9,345 files (hash count aur row count dono), badi CSVs ke category subsets (qareeb tareen 5,753, yeh match nahi), remote ki saari refs, Claude aur Codex logs.
- `5,767` jahan mila, woh SHA ka hissa ya data value tha, hash list nahi.
- **Zaroorat:** us file ka naam aur file khud. Yeh number jis report se aaya, wahan se milegi. Filename mujhe kisi record mein nahi mila.
- Qareeb tareen candidate: Machine B `~/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1/machine_a_transfer_requirements.csv`, 2,135,841 bytes, sha `3f34ca4e…f393`. Lekin us mein 5,092 entries likhi hain, 5,767 nahi, aur file is Mac par nahi hai. Yeh sirf andaza hai.

Is ke badle jo accessible tha woh compare kiya. **Yeh 5,767 ka substitute nahi:**

| List | Sirf disk | Disk + GitHub | Sirf GitHub | Dono par nahi |
|---|---|---|---|---|
| Machine B inventory, 3,986 hashes | 2,589 | 647 | 330 | **420 (642 MB)** |
| Published manifests, 11,398 hashes | 6,735 | 3,974 | 655 | 34 |

Woh 420 sirf Machine B ki list mein hain, jin mein `Archive.zip` 394.9 MB aur `local_branches.bundle` 65 MB shamil hain. Machine B par abhi hain ya nahi: UNKNOWN.

### GitHub se kya restore hota hai (verified)
Maine alag mirror banaya: no alternates, no promisor. Final pin par **50 heads aur 54 PR refs** mirror se bilkul match.
- Reachable objects mein missing **0**. Local clone ke 752 missing objects sab mirror mein hain. Yeh corruption nahi, partial clone ke gaps hain.
- Full fsck 22:48Z par exit 0. Baad ke fetch ke baad connectivity fsck aur 3 packs ka verify-pack exit 0.
- **LFS 38 of 38 payloads** waqai download hue, hash match, 0 mismatch, 2.38 GB.
- Worktree restore test sirf 3 refs par hua: `main`, Finance, Knowledge Navigation. Baqi refs ke objects verify hue, lekin un ka checkout test nahi hua.

**GitHub se wapas nahi aata:** upar wala local-only data, zyada tar raw media, frames, aur Machine B ki files. Local fsck pass hona remote restore ka saboot nahi, aur `.rev` warning ko haath nahi lagaya: same hash, cosmetic.

### Coding/CI ke khule masle
- **Finance PR #36:** wajah pakki. `validate.yml:59` ki allowlist mein `reference_knowledge.db` nahi. Tests 462 pass ho jate hain, phir yeh step fail. Yeh ek line ka fix hai, faisla aap ka.
- **"Ready allowlist patch" mujhe kahin nahi mila:** na kisi ref mein, na stash, patch file ya logs mein. Machine B ka pata nahi. Branch ya path nahi bata sakta.
- **PR #37, 38, 39, 41, 43, 44:** logs nahi mile, wajah UNKNOWN. PR #36 wali wajah in par nahi lagayi.
- **Validators kamzor hain, maine isolated copy par saabit kiya:** comparison file ko `{}` kar do, gate phir bhi pass. Jaali title witness pass. Plan mein `"x"` ya `"."` likho, pass. Asli data mein 57 of 57 title witnesses sahi nikle, yani masla gate mein hai, data mein abhi nahi mila.
- **Framework plan check optional hai,** aur hosted CI `validate_audit_966` ya framework tests nahi chalata.
- Local tests: main 460, Finance 462, Knowledge Navigation 460 pass (1 skip each). Yeh hosted result nahi.
- Video006 ke W2–W4 mein 4 JPG Git mein gaye, jo text-only rule ke khilaf hai. Worker ko pata hai.

### Scheduler ke masle (Primitive Education)
- Pehle 17 runs mein **completed research cycle 0** hai. BUSY 3, logged WAIT 1, **inferred WAIT / unverified outcome 10**, source-access failure 2, supervised test 1. Woh test unattended cycle nahi tha.
- **Downloads blocker scheduled context mein fix saabit nahi hua.** Akhri scheduled probe 12:54Z par BLOCKED tha. Baad mein files copy hui, lekin kisi scheduled run ne unhein nahi parha. Ab `HOLD_NO_EXECUTABLE_WORK` scheduler ko rok raha hai. Interactive held-out kaam scheduler fix nahi.
- Alag baat: Casually Finance ka scheduled task waqai kaam kar raha hai, W1–W4 receipts ke mutabiq.

## 2. Channel status (final pin par)

Har channel ka pura status `CHANNEL_RESEARCH_STATUS.csv` mein hai.

| Channel | Authoritative checkpoint | Scope aur halat | Blocker | Agla valid kaam |
|---|---|---|---|---|
| **Casually Finance — Video006** | W4 `5e497970`. T aur V is ke purane ancestors hain | 35 ka roster, 0/35 certified; queue pending 627; listening 0 s; CT_SCAN_COMPLETE false | Codex lock active; listening; JPG masla | SUB010 → EP0018 → SUB011…, lock release ke baad |
| **Primitive Education** | Remote I `4f4cfd64`; J abhi local | 15 videos, sab VISUAL_ANALYSIS_PARTIAL | Audio; off-device destination | Worker J publish kare; phir aap ka faisla |
| **Barely Evolved** | N18 `95866052` | 3 videos partial; `4X3xd3MDZro` out of scope; lock free | Listening; `STATUS.json` purana | Aap scope batayein |
| **xkcd What If** | P `a7e3057b` | 91 census, 32 selected, partial; RT4 sirf 8-frame sample | Listening; Phase 7 scope | Current worker ka follow-up |
| **Finance / Nick Invests** | PR #36 `f115285b` | 558 of 1,612 limited evidence; 0 full; reanalysis 26 pending review, 532 pending | CI; writer confirm nahi | `15Gr4BAJi00` writer confirm ke baad |
| **Thumbnail research** | `6c6e8900` | Deferred | `Archive.zip` Machine B par | Aap ka faisla |

Koi channel listening ya production approved nahi. ASR listening nahi, aur measured frames poora inspection nahi.

Baqi branches ki detail `BRANCH_REF_MATRIX.csv` mein hai: 199 rows, sirf `backup/decode` branch local-only hai. Local Finance ref purana hai, ahead nahi.

## 3. Pehle kya karein
1. Off-device destination batayein. 17.14 GB ek hi Mac par hai.
2. 5,767 list ya uska source dein.
3. Machine B par 420 hashes check karwayein.
4. `reference_knowledge.db` par faisla karein, aur allowlist ek line ka kaam hai.
5. Video006 ke JPG aur U commit par faisla karein.

Baqi ranked list aur resume dependencies: `DISCREPANCIES_AND_NEXT_ACTIONS.md`.

## 4. Audit ne kya badla, kya nahi
- **Before/after:** canonical checkout HEAD `f4dc5d14` same, 3 untracked paths same. Finance worktree `9c6f42fb` clean. Stash aur worktrees same. `.rev` same.
- **Doosron ki tabdeeliyan, audit ki nahi:** `origin/*` tracking refs aur `refs/codex/turn-diffs` badle, kyunke doosre workers push kar rahe thay ("update by push"). Live: Video006 Codex, Primitive Education, xkcd What If ke locks. Timeline: `DISCREPANCIES_AND_NEXT_ACTIONS.md`.
- Audit ne koi source edit, push, merge, lock operation, scheduler change ya cleanup nahi ki. Sirf canonical read kiya.
- **Meri galtiyan jo theek ki:** pehle kaha tha V local-only hai; ghalat, V GitHub par hai aur U us ka parent nahi, sibling hai. Test failures meri test setup se thay. "No lock" wala note bhi galat tha. Mirror par recheck fetch se uske 4 heads aage gaye; yeh sirf audit ki copy hai, aur purani pin `raw/refs/mirror_refs.txt` mein safe hai.

## 5. Kya nahi hua
- 5,767 comparison: BLOCKED.
- Machine B: UNKNOWN. Drive backup: dobara verify nahi hua.
- Purani streams (Senior Health, Dr Rehan, Casual Economics, Monkey Explains) ki acceptance dobara score nahi ki, sirf branch aur file level dekha.
- Productions ko files aur branches tak dekha. Renders chala kar approve nahi kiye, aur delivery manifests ka ek ek check nahi hua.
- Runs 21–25 row by row classify nahi hue.
- Har channel ka status worker files par mabni hai. Maine research dobara score nahi ki.
- Workers abhi chal rahe hain, is liye yeh report 03:36–03:38Z ki tasveer hai.
