# V8 Option A versus B — proposal only

**Recommend Option B, conditional on explicit owner approval, the source writer's read window and fresh resource/privacy gates. No transfer is authorized or executed.**

| Alternative | Files | Payload bytes | 100,000-byte control allowance ceiling | Benefit |
| --- | ---: | ---: | ---: | --- |
| A minimum | 2 | 1,033,903 | 1,133,903 | Addresses the two selected identities with no proven independent copy |
| B durable set | 8 | 1,111,045 | 1,211,045 | A plus a dedicated independently verified private recovery copy of six authored documents |

B adds only **77,142 bytes** (about 75.33 KiB, 7.46% over A). It adds a separate recovery copy beyond the observation-time iCloud receipts. A is reasonable only if the owner intentionally defers durable preservation of those six documents. These alternatives are not additive. Neither is complete YIOS recovery coverage.

## Exact refreshed scope

All eight canonical local files were read once with before/after stable inode/size/mtime checks; **8/8 SHA-256 and size matches**, **1,111,045 bytes**. This refresh did not read iCloud providers, edit the sources, or release ownership. Evidence: `evidence/EIGHT_SOURCE_REFRESH.json`.

| Exact local source | Bytes | SHA-256 | Independent recovery evidence |
| --- | ---: | --- | --- |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/TRANSCRIPT_COVERAGE.md` | 8,048 | `301eb86e20e2057109fe53950cb961c301c9182e621b39c81a0c3842785660c9` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/TITLE_DNA.md` | 8,868 | `f2bab75425b65d0e839c1daea02d5319bcc47fabb7bbc6d13e5a4e54203b7d69` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/FINAL_SHORT_SCRIPT.md` | 8,999 | `093038ce0281a8446deff4074b3ae63b24f1aaaac679c806d809e2795bc4e3ed` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/TOPIC_RESEARCH.md` | 12,674 | `63903e6f15a7f11b619f4eaeeafe50be3e3d4737eabfb6c04d7cb033a6c111fc` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/SCRIPT_DNA.md` | 17,602 | `a24884173488a1caf07556c028e2d31a425a82fa7efd42776303e1e298b89f2f` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/SOURCE_REGISTER.csv` | 20,951 | `2d2beb988fef3ef26e8d4afea4a277de288a94889faef9a706271a36b13b5aa6` | Observation-time iCloud full-byte match; current provider availability/retention unverified |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os/output/chair-stand-safety/source/source.mp3` | 275,181 | `249ddc6f81da7c9e094317d245e9f96d790b040a7651133ce1785a2c802dbbef` | No proven independent recovery copy |
| `/Users/ghilmankhan/yios-git-recovery/cleanup-2026-10-13/local-only-history.bundle` | 758,722 | `45e478dabaee04278fdb10ed25f0f9ec9ab4ceea9fa9656746b9898a39689442` | No proven independent recovery copy |

The six iCloud full-byte observations are preserved at `/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z/evidence/ICLOUD_SIX_SCRIPT_COPIES.json` and covered by the immutable prior seal. Their current on-demand accessibility and immutable version retention remain **UNVERIFIED** after the earlier provider stall. No additional iCloud read was attempted. Local copies on this same Mac do not establish independent-machine disaster recovery.

## Bundle prerequisites — not standalone

The unchanged bundle's recorded 28-object pack checksum and claimed local commit/stash objects passed the prior bounded verification. Its two declared base commits are:

- `e25dc63fc101390867ebf1495bba726ba9797fb6`
- `31ea9a53a6b4c9a1b74a3478ce16e510fdf06e10`

Eight external delta prerequisites were required by the prior pack decoder:

- `0ce8db22f0b2466c16df9e0f4a66a9a544f5f2a5`
- `6641cf244bb260a5d614c8443b719feffa63f13f`
- `33cd57b958d1d04c8d6b1f733d4d98c0f7d4c61f`
- `12c6f5b4e40e545d80edcd3649cd934aac0ab5a1`
- `961c4e7323ef6c4f0a3e8e57177ab6db072d34e3`
- `7d164f79e9ec45922b36b289a6d29dd4dd8f0cb0`
- `1e76bd8400857f8ba00fc9db663f7a2b41a27c53`
- `a60767f77750d1a1a705f91745e3a5731c4561cf`

Prior remote API commit metadata existed for both base commits, and the local decoder could read the prerequisite objects. That does not prove independent full closure after this Mac is lost. Preserve the bundle now if approved; separately authorize a bounded clean independent restore experiment with verified prerequisite closure, storage ceiling and no writes to the production object database. No clone, fetch, test restore or new bundle was made in this task. Bundle preservation benefits local commit/stash recovery but must not be described as standalone recovery.

## Future transfer decision, still blocked

Proposed destination: a new distinct private V8 child under existing owner-only `yios` folder `1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr`, using authenticated **kgk2930@gmail.com**. Suggested child name `V8-selected-recovery-2026-10-27` is a proposal, not an existing object or authorization. Owner must approve this exact child/scope and source-read window; Finance and protected Visual Forensics ownership remain unchanged.

If separately approved and gates pass, recheck eight source hashes/stability; prove exact destination owner/Restricted privacy; reconcile existing exact identities before any upload; upload only the selected scope and bounded controls; independently retrieve each full raw remote file and compare length/SHA-256; preserve actual IDs/parent/privacy/readback receipts. Archive/wrapper checks do not substitute for raw bytes. Do not upload a current catalog or the discovery candidate list. Any changed source hash or destination/account mismatch stops execution.

V7's 12,000,000,000-byte physical ceiling has historical headroom **5,667,070,738 bytes** before V8. B plus the 100,000-byte allowance would add at most **1,211,045 bytes**, making prospective physical bytes **6,334,140,307**, if nothing else changed. The owner account's fresh quota remains unavailable; historical rounded quota supported a conservative 7.6 GB free floor and 5.6 GB after its 2 GB reserve, but these are not current measurements. Local disk is currently below the 5 GB reserve. No execution should start under these resource conditions.

## Remaining LFS proposal — separate authorization

Thirteen full-byte verified LFS receipts remain sealed (**192,210,838 bytes**). Remaining **16 OIDs / 976,973,901 bytes** are listed exactly in `REMAINING_LFS_RECOVERY_GAPS.csv`. Eight have prior independently verified Drive originals (**223,141,535 bytes**) but their LFS transport bytes were not read. Eight lack complete independent recovery proof (**753,832,366 bytes**); an offer or pointer is not a full-byte recovery proof.

| Priority | High-risk exact LFS SHA-256 OID | Bytes | Saved path |
| --- | --- | ---: | --- |
| 1 | `bf5c4f46b17d020074b39cb621de6c21d71a74adc154790552d746e9d34ca0d6` | 11,635,244 | `projects/dr-rehan-test-videos/project/audio/sfx.wav` |
| 2 | `184532b9ae5d06faa3f9c8d2edc8a60f78ce076c1a55687a5264843f184716d7` | 28,230,734 | `projects/dr-rehan-test-videos/V1/Calf_Pain_PAD_FINAL.mp4` |
| 3 | `d0047986a7b5d560909ecb64cb8bbea8c316eefa03d05012f0dfff7481912a9b` | 29,991,732 | `projects/dr-rehan-test-videos/V2/Calf_Pain_PAD_FINAL_v2.mp4` |
| 4 | `ea7c986b23758f4b72a731d1df77630191711ea532b3cf537b26259d47dc1e6d` | 127,995,904 | `data/catalog/youtube_channel_registry.db` |
| 5 | `28f898cdd475b11b45bcced815c0ff70a15cf738d8a4810efcbce818ccd380cd` | 131,878,912 | `data/catalog/youtube_channel_registry.db` |
| 6 | `63c1f8948fc5d53cc0a973e3e60790a51475bde9b59b4790f1dc0ae387e3f39a` | 141,352,960 | `data/catalog/youtube_channel_registry.db` |
| 7 | `5538db9f6b08a6dbbdc92cc568198dc721d52037917c14b946401c58fb82d33f` | 141,373,440 | `data/catalog/youtube_channel_registry.db` |
| 8 | `48ffb558adf40ac793bdb8c798bf2ee9b536fa77453fe196c247f07c51951b0b` | 141,373,440 | `data/catalog/youtube_channel_registry.db` |

**Proposed Wave 1:** retrieve only priorities 1–3, sequentially, **69,857,710 payload bytes**, under a newly explicit **70,000,000-byte payload ceiling**. This is a new budget request; the old 200,000,000-byte budget has only **4,608,869 bytes** remaining after its 195,391,131-byte conservative upper bound and cannot fund even the smallest remaining object. Require ≥5 GB Mac reserve throughout, fresh usage/credits checks and an owner-approved durable evidence destination; preserve prior scratch originals and never delete them for space.

**Proposed Wave 2:** only after owner review of Machine B/prerequisite evidence, approve one of the five exact historical catalog OIDs at a time, smallest first, under an explicit per-object **160,000,000-byte payload ceiling** and stop/checkpoint after each full size/hash comparison. Further versions need separately confirmed scope/budget; no bulk command. A verified newer catalog is not a substitute for an older OID. Prefer already independently covered Drive originals for the other eight and defer redundant LFS transport tests.

No LFS or other recovery payload was downloaded in this reconciliation. Known 29 identities are not a complete all-history census: the historical missing Git blob `793ee3c02688ed7f3275b3f1026d9fd5f683d714` limitation remains unresolved. No fetch/repair was attempted.
