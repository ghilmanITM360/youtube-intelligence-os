# YIOS actual SSD cleanup plan — Machine A, 2026-10-29

## Faisla

**CERTIFIED ELIGIBLE:** 33 V7 ke generated archive wrappers, 0.739 GiB allocated blocks. Owner in exact paths ko manual deletion ke liye review kar sakta hai. **Koi file delete nahi hui.** APFS clone sharing measure nahi hui; actual space saving 0 se 0.739 GiB tak ho sakti hai, guarantee nahi. Preflight `df -g` ne 14 GiB free dikhaya; final `df -k` 15,651,724 KiB (14.93 GiB) dikhata hai. Dono measures ki rounding alag hai. Koi deletion nahi hui: **authorized cleanup se freed space 0 bytes**. Machine B access nahi; uska saving **unknown**.

**POTENTIAL, abhi blocked:** CF `_work` 1.071 GiB; What If Downloads ki 2,467 exact common files 0.648 GiB; V7 Batch 35 wrappers 0.456 GiB. Inhein certified total mein shamil nahi kiya. **PROTECTED:** 38 Shorts evidence 4.154 GiB; current source aur active forensics ka hissa hai.

## 1. Verified manual deletion shortlist

Sirf `YIOS_VERIFIED_DELETION_CANDIDATES.csv` ki **MANUAL_DELETE_REVIEW** rows. Ye {'batch-0033': 19, 'batch-0034': 5, 'batch-0036': 9} ke selected V7 `.tar.gz` wrappers hain. Har row mein absolute path, SHA-256, Drive object ID, batch receipt aur allocated bytes hain. 33/33 local SHA V7 map se match; 33/33 current Drive metadata ID, name, size, owner matched; current metadata read full payload SHA ka substitute nahi, payload proof 2026-10-26 ke independent retrieval receipts se aata hai; 33/33 batch receipts `VERIFIED` aur uploaded = independently retrieved bytes; 2,290 members remote decompression SHA verified; archive reconciliation `PASS`. `04035-forensic-JsK53moCyZA-part01.tar.gz` ko alag scratch mein physically restore karke full SHA/member check bhi pehle pass hua. Baqi objects ki full remote byte retrieval documented hai, magar har object ka separate on-disk restore nahi kiya gaya.

Yeh **sirf local generated wrappers** ki review hai; original Shorts arrays, frames, audio, V7 manifests, batch receipts, exception records aur Drive objects ko delete na karein. Historical receipts mein local wrapper paths rahenge; agar future recovery script ko same path chahiye, pehle remote object ID se us wrapper ko restore karna hoga. Repo ke current docs/code mein selected wrapper path dependency nahi mili; V7 backup process active nahi dikha. Source owner/active session ka protected forensic work untouched raha.

## 2. Blocked high-value cleanup, savings rank

| Rank | Exact group | Occupied blocks | Evidence found | Missing smallest safe check |
|---|---|---:|---|---|
| 1 | `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/_work` | 1.071 GiB | 1,267 staging files; two `gray.u8` alone ~0.88 GiB. PR21 excludes `_work`. | Pin script/input hashes; exact bounded regeneration of representative streams; owner confirms no active stage references. |
| 2 | `/Users/ghilmankhan/Downloads/video data of what if` exact common children | 0.648 GiB | 2,467 same relative paths and exact SHA in workprojects. Four Downloads-only files and one changed `.DS_Store` remain. | Confirm CapCut/Brain/source path use; verify original video backup and restore for representative media; APFS clone sharing. No whole-folder deletion. |
| 3 | V7 `selected-evidence-packages-20261026` Batch 35 wrappers | 0.456 GiB | Local SHA/remote map match, but Batch 35 historical exceptions remain. | Reconcile exception/dedup identities and direct restore before any review. |

## 3. Four target folders: actual evidence

**Casually Finance derived folder:** 2,037 files fully hashed. PR21 tree comparison: 688 exact blobs, 51 changed historical versions, 1298 absent from matching PR21 path. Local deep report 6,538 characters versus PR21 report 29,404; same first five section headings, later PR21 adds QA/primary-source research; local text also differs inside old sections. Is liye older report ko disposable nahi kaha. Local-only `_pipeline` scripts, metadata snapshot aur `_work` ko provenance/derivation proof tak rakhein. Koi new small file is pass mein publish nahi ki gayi: 51 changed versions ko current PR21 se automatically overwrite ya merge karna evidence-safe nahi.

**V7 local audit folder:** 1,781 files fully hashed. 57 direct remote objects match; 53 selected wrappers mein se 33 review eligible, 20 Batch 35 hold. 3 CT packages (Video 003 samet), Finance publication package, receipts, member manifests aur incident history protected. Batch 31/35 exceptions preserved.

**What If:** Downloads 2,472, workprojects 2,877 files. 2,467 exact common; 4 Downloads-only (3 generated PNG, workbook); 409 workprojects-only; `.DS_Store` differs. Workprojects Brain/source remains authority, PR44 selected navigation published, full originals ko PR44 coverage mat samjhein. Exact file list `WHAT_IF_RELATIVE_SHA_COMPARISON.csv` mein.

**38 Shorts:** 393 files fully hashed; 392/393 V7 map exact, last `.DS_Store` unmapped. Full 4.15 GiB **protected**, even when remote backup matches: forensic pipeline/source-owner and full recovery obligations remain.

## 4. Single authority, Git, private originals

Current main YIOS repo/PR21/PR36/PR44 mein koi source change is investigation mein nahi hua. Casually Finance navigation pehle hi `f4dc5d14d6ad03c1edd92e48fac779e7a8555fc5` par publish hai. PR21 `043b85bf58f84fb6a1c8981d54e3b233faa6a928`, PR44 `f345abdef43d54ebde98251cfa4fafb6403c52be`. Finance PR36 ka writer Machine B hai; uske 1,612 records untouched. Original MP4, audio, frames, arrays, CapCut source aur active Video 003 external/private storage mein rakhein. Git pointers ya summary ko media recovery mat samjhein.

## 5. Owner ke liye next action

CSV mein `MANUAL_DELETE_REVIEW` filter karke exact 33 wrappers dekhein. Whole V7 folder delete na karein. Agar owner actual deletion choose kare, pehle corresponding Drive ID/receipt save rakhein; deleted wrapper restore karne ke liye same Drive bytes aur SHA compare karein. Batch 35, `_work`, What If copy, Shorts evidence, old research export/audit receipts aur Git recovery ko filhal na chhuyein. Machine B ko us Mac par alag verify karna zaroori hai.
