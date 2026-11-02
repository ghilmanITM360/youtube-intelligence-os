# Ten practical data-use workflows

These are existing files, Git/SQLite operations and repository tools, not a new retrieval service. Start in`/Users/ghilmanislam360/Documents/youtube-intelligence-os`and use`.venv/bin/python`, not the broken systemPython. Commands below read existing evidence; production-authoring examples are instructions for a later authorized task and were not executed during this audit. Always retain branch/SHAwith a result.

## 1. Find all research for a channel

Real input:Nick Invests,YouTube channel`UCXzNNA2ngRpRiWvyA7eGd6w`. Query the actual registry and inspect the channel package:

```sh
.venv/bin/python - <<'PY'
import sqlite3
c=sqlite3.connect('file:data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
rows=c.execute('SELECT youtube_video_id,title FROM videos WHERE canonical_channel_id=?',('UCXzNNA2ngRpRiWvyA7eGd6w',)).fetchall()
print(len(rows)); print(rows[:3])
PY
```

Expected363registered video rows. Read`research/finance-economics-intelligence/channel-intelligence/nick-invests/2026-10-23/README.md`,then filter`VIDEO_AUDIT_966.jsonl`byChannel_ID. Canonical has194completed Nick originals; the supplementary report is an older dated synthesis and is not current completion authority. For Casually Finance use the separate navigation branch's`research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md`with`git show origin/codex/casually-finance-knowledge-navigation:exact/path`; its pinned corpus/CTlinks distinguish overlaps and private dependencies.

## 2. Retrieve a complete available package for one video

Real input`XJ4ls6r2MCE`(NICK_185). Retrieve its row and named packet/receipts:

```sh
.venv/bin/python - <<'PY'
import json
from pathlib import Path
b=Path('research/finance-economics-intelligence')
r=next(json.loads(l) for l in (b/'VIDEO_AUDIT_966.jsonl').read_text().splitlines() if json.loads(l)['Video_ID']=='XJ4ls6r2MCE')
print(r['batch_id'],r['statuses']);print(r['script']['source']);print(r['thumbnail'])
for name in ['NICK_185.json','NICK_185_READ_RECEIPTS.json','NICK_185_VALIDATION.json']: print(b/'audit-batches'/name)
PY
```

Read those threeJSONfiles,then the exact`thumbnail.image_path`and canonical transcript source. Nick's archive is`data/extracted/channel-data/DS-000022/packages/nick-invests/NickInvests_Transcripts_363_Videos.zip`;`TRANSCRIPT_COVERAGE.csv`and receipts map members/Text_SHA256. Actual transcript text is queryable from registry`transcripts`byyoutube_video_idwithis_placeholder=0. A complete limited-evidence text/thumbnail package does not include verified source audio/MP4/listening/private analytics. Use JSONL/receipts for full structured content; Excel is a checked projection.

For the newer separate branch,read without switching:

```sh
git show origin/codex/finance-machine-a-owner-directed:research/finance-economics-intelligence/audit-batches/NICK_278.json
git show origin/codex/finance-machine-a-owner-directed:research/finance-economics-intelligence/audit-batches/NICK_278_READ_RECEIPTS.json
```

## 3. Compare strong, typical and weak videos

Real same-channel examples in`VIDEO_MASTER.csv`:CrayonCapital`1GowFTjbUnk`NVIDIA(9.76573×STRONG),`9r-45QPLl-Y`Petrodollar(1.27641×TYPICAL),`AKrjI9m6fpk`Epstein(0.37936×WEAK),frozen2026-09-13snapshot.

```sh
.venv/bin/python - <<'PY'
import csv
with open('research/finance-economics-intelligence/VIDEO_MASTER.csv') as f:
 for r in csv.DictReader(f):
  if r['Video_ID'] in ['1GowFTjbUnk','9r-45QPLl-Y','AKrjI9m6fpk']: print({k:r[k] for k in ['Video_ID','Title','Performance_tier','Lifetime_rate_ratio','Peer_Video_IDs','Metric_snapshot_date']})
PY
```

Then compare their authored JSONLsections and`PERFORMANCE_SENSITIVITY.csv`; expected explicit peer IDs and frozen metric basis. Tiers describe lifetime public rate against a cohort; they are not causal explanations, current views, private retention or guaranteed success.

## 4. Compare title, thumbnail, topic and script patterns

Use the same three IDs in`TITLE_ANALYSIS_966.csv`,`THUMBNAIL_ANALYSIS_966.csv`,`TOPIC_ANALYSIS_966.csv`,`SCRIPT_ANALYSIS_966.csv`,plus`TITLE_FORMULA_LIBRARY.md`,`SCRIPT_FORMULA_LIBRARY.md`,`VIRALITY_PATTERNS_AND_COUNTEREXAMPLES.md`. Filter CSV rows byVideo_ID withPythoncsvas above; retrieve actual image paths from JSONL and compare at native/mobile sizes only when the image exists. Output: side-by-side evidence/analyst interpretations and counterexamples. The shared“ExplainedLikeYou're5”grammar spans different performance tiers; it does not prove title formula caused views. Unreviewed rows/statuses and stale synthesis dates remain explicit.

## 5. Retrieve financial claims with sources

Real inputNICK_185. Its packet`reviews[0].script.claim_audit`contains16claim groups. Its read receipt has2primary-source receipts and2calculations. For the tax/bandwidth examples read exactassessment,source_ids and matchingreceipt.source_id, includingaccess_scope / limitations/publication_applicability. A verified source can contradict the creator's numeric claim; a direct-source label alone is not a VERIFIED claim verdict. Latest Machine A NICK_265+adds confidence labels that distinguish direct primary inspection, snippets, recall and unavailable sources.

Audit convenience indexes:`finance/claims.csv`,`finance/primary_source_receipts.csv`,`finance/calculation_receipts.csv`. They point back to exactexistingpacket paths/refsand preserve uncertainty. These are audit retrieval tables, not a new production interface. Expected output: creator assertion +stored-ASRwitness +analyst assessment +source/locator/date/limitation +calculationreceipt. Older narrative claim audits are not fully machine-queryable; absence of saved primary bytes prevents independent offline source entailment verification. No new financial fact-check was run here.

## 6. Retrieve channel visual grammar and editing DNA

Casually Finance older corpus:

```sh
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/VISUAL_DNA.md
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/MOTION_DNA.md
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/EDITING_DNA.md
```

Join each statement toper-video SOURCE.json/QA.json/STATES.csv/SHOTS.csv/MOTIONS.csvand confidence. Later CT00176-state report is`research/visual-forensics/channels/casual-finance/o3FQcd91MIs/research/v2/visual_ct_scan_report_v2.md`; CT002has`STATE_BY_STATE_VISUAL_FORENSICS.md`. CT003–005are on the editing branch and partial. Output: descriptive channel grammar +timed/source-row evidence. Do not treat16older structural packages,38 Shorts and5CTcases as independent/disjoint samples; audio and much native evidence remain unavailable.

## 7. Build an original storyboard and asset plan from published research

Read existing`docs/intelligence/CASUALLY_FINANCE_STORYBOARD_TEST.md`on`origin/codex/casually-finance-knowledge-navigation`and sourceDNAabove. It is a real navigation/storyboard example, not new forensic evidence. Assemble a later original storyboard with columns: sourcevideo/version/row/time → observedfact → analystinterpretation/uncertainty → originalscene/narration/asset/motion → requiredverification. Consult existing production branches for editable scene/asset/QApatterns,not accepted research counts.

Expected output: an original storyboard and asset plan grounded in general patterns, independently sourced financial claims and original art/voice/timing. Reusing source footage/artwork/dialogue/distinctive sequences is not a substitute for original production. The V1orchestrator exists at`scripts/run_youtube_intelligence.py`; if used later it requires a real existingchannel+opportunityIDand an externaloutputdir. No inventedRAG/API/unifiedchannelinterface is claimed and no content plan was generated today.

## 8. Identify what is missing before production

For a concrete CTvideo read its`QUALITY_GATE`/`PORTABLE_MANIFEST`/`EXTERNAL_EVIDENCE_MANIFEST`,then matchsourceSHAinthisaudit`media_integrity.csv`andmissingentriesin`machine_a_transfer_requirements.csv`. For a Finance video inspectall 6statuses,source_receipts/limitations,thumbnailpath/hashandprivate_metrics. Readproduction`PRODUCTION_STATUS.json`/qaVALIDATIONonitsownbranch. Output: source/claim/image/audio/asset/rights/QAavailability checklist for that package. Existing visual-only/partial status cannot become full AVacceptance because the source MP4exists. Do not rerun measurement or acquire media solely because a reference path is stale.

## 9. Resume the correct next research task

No research task was resumed during this audit. Read the live branch's `FINANCE_WRITER_OWNERSHIP.md`, `FINANCE_PROGRESS_CHECKPOINT.json` and latest `RESUME_HERE.md`, then verify its remote head and writer ownership before any write. Canonical Finance names NICK_186 `XP-26tqGFXc`; Machine A's separate branch already completed it and currently names NICK_279 `pTyMmSZ2EVs`. Reconcile publication and writer handback before selecting a queue. Do not restart accepted work from an older handoff.

The old Casually Finance Shorts pilot queue and CT003 checkpoint 6 guidance are stale. Current published gates are CT003 checkpoint 11, CT004 P and CT005 J. New CT006 B needs its actual unpublished workspace and current writer record; the older PR21 package cannot resume the new reviewers.

Coordination tooling exists in the separate existing coordination worktree. Read its `docs/YIOS_TWO_MAC_WORKFLOW.md`. The nonproduction test claim tips are RELEASED; they do not release protected legacy writers. Seventeen passing local tests do not establish actual second-Mac acceptance. Expected output is the correct existing queue and explicit ownership gate, not a new scheduled task.

## 10. Transfer or reconstruct the environment here

The existing checkout and runtime are usable: project Python 3.12.14, openpyxl, Pillow, pytest, Node, ffmpeg/ffprobe and Git LFS. No new clone or worktree is needed. Check the frozen hashes and `lfs_presence.csv` before deciding whether any missing LFS payload is needed. A later necessary exact path can be fetched with existing Git LFS, for example `git lfs fetch origin <branch> --include=<exact-path>`. This was not run for the six unneeded missing versions. Materialize only the intended absent file and verify its OID/hash; preserve any differing frozen source.

Use `YIOS_MEDIA_ROOT=/Users/ghilmanislam360/Documents/YIOS-Media-Library` in the consumer environment and read the media branch's registry. Older `data/local-channel-media` paths are stale. Preserve the private `.env`; do not copy credentials into Git or reports. Obtain only the required missing CT evidence from the documented Machine A roots, stage it, compare hashes and preserve collisions. Source MP4s for CT001–005 already exist here. The older CT006 source can be streamed from its existing ZIP; compare the newer checkpoint's source fingerprint first.

Install numpy, Whisper or PySceneDetect only if a future authorized forensic task requires them, in a compatible environment. System Python 3.14 has an XML runtime failure and is outside the project contract. A future workbook/document rebuild should locate bundled dependencies using the supported workspace-dependency loader instead of another Mac's cache path. No environment repair, regeneration, redownload, research wave or V2 infrastructure was needed for this audit.

Expected output is a usable existing Git/runtime/source map and a task-specific transfer/dependency list. The exact missing paths, hashes, known sizes and UNKNOWN fields are in the portability appendices.
