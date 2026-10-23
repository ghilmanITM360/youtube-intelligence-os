# Machine A — Saturday October 24, 2026 start

This is the same 1,612-video Finance project and existing Finance branch/PR #36. Follow this guide from the HOME MacBook without relying on Machine B chat history. Machine B's [release](FINANCE_WRITER_OWNERSHIP.md) becomes effective only when the release commit is published. Machine A is **not yet accepted**. Do not start NICK_165 corrections or a new audit until the gates below pass.

## A. Identity, resources and preservation preflight

Expected checkout: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`. Confirm actual Mac/user with the owner if they differ; do not silently use Machine B paths. Use live `get_usage_limits` before expensive work and after each atomic phase. At >=90% five-hour or >=95% weekly usage, or a serious context warning, stop starting expensive phases, preserve checksums and a truthful continuation. Context percentage may be unavailable. Do not use reset credits or paid services.

Run these read-only checks, saving outputs outside the repository in a collision-safe dated directory. Do not publish credentials or `.env` contents.

```sh
cd /Users/ghilmankhan/workprojects/youtube-intelligence-os
pwd
hostname
whoami
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git rev-parse HEAD
git rev-parse --abbrev-ref '@{upstream}'
git status --porcelain=v1 --untracked-files=all
git worktree list --porcelain
git stash list --format='%H %gd %s'
git for-each-ref --format='%(objectname) %(refname)'
git ls-files --others --exclude-standard
git ls-files --others --ignored --exclude-standard
gh auth status
git ls-remote origin refs/heads/research/finance-economics-intelligence
gh pr view 36 --repo ghilmanITM360/youtube-intelligence-os --json state,isDraft,headRefOid,headRefName
```

Require correct remote and branch, upstream `origin/research/finance-economics-intelligence`, OPEN/DRAFT PR and no staged/modified tracked files. Preserve all untracked/ignored evidence, stash and backup refs; list paths without reading secrets. No unique path may collide with incoming tracked files. Inspect other worktrees and active app chats/processes; coordinate with the owner if another Finance writer is active. No process-list result proves remote exclusion. Do not auto-stash/pop, reset, rebase, switch away from dirty work, prune or delete evidence.

Historical Machine A SHA `7e70f061aae849e9929b531c4bc855b23edda179` is not today's target. Read live GitHub first. If wrong branch, local-only work, unexpected stash/backup ownership or dirty tracked files: preserve and investigate; do not manufacture a clean state.

## B. Non-pruning fetch and strict fast-forward

Only after the preflight succeeds, fetch the exact existing branch, with no force or prune:

```sh
git -c fetch.prune=false -c fetch.pruneTags=false fetch --no-prune origin refs/heads/research/finance-economics-intelligence:refs/remotes/origin/research/finance-economics-intelligence
git rev-list --left-right --count HEAD...origin/research/finance-economics-intelligence
git merge-base --is-ancestor HEAD origin/research/finance-economics-intelligence
```

The left count must be zero and ancestry command exit 0. A nonzero left count is local-only Finance history and blocks automatic update; preserve it and reconcile with the owner. Recheck remote/PR live heads equal the fetched target; if changed, repeat read/fetch gates safely before continuing.

Check exact and parent/child path collisions against **all** current nontracked and ignored paths before fast-forward:

```sh
python3 - <<'PY'
import subprocess
run=lambda *a:subprocess.check_output(['git',*a]).decode().split('\0')
local={p for p in run('ls-files','-z','--others','--exclude-standard') if p}
local|={p for p in run('ls-files','-z','--others','--ignored','--exclude-standard') if p}
target={p for p in run('ls-tree','-r','-z','--name-only','origin/research/finance-economics-intelligence') if p}
collisions=[(p,t) for p in local for t in target if p==t or p.startswith(t+'/') or t.startswith(p+'/')]
assert not collisions, 'Preserve and resolve local evidence collisions: '+repr(collisions)
print('No untracked/ignored target collisions')
PY
git merge --ff-only origin/research/finance-economics-intelligence
git rev-parse HEAD
git rev-parse origin/research/finance-economics-intelligence
git ls-remote origin refs/heads/research/finance-economics-intelligence
gh pr view 36 --repo ghilmanITM360/youtube-intelligence-os --json state,isDraft,headRefOid
```

Require Machine A local HEAD = fetched origin = live GitHub Finance HEAD = PR #36 HEAD, and OPEN/DRAFT. If a required object is an LFS pointer, use the installed Git LFS tooling to materialize only the required registry path, then hash it:

```sh
git lfs version
git lfs pull --include='data/catalog/youtube_channel_registry.db' --exclude=''
```

Do not regenerate or substitute the frozen registry DB. Preserve differing local files before any recovery; no automatic overwrite. Recheck tracked cleanliness, stash hashes, backup refs and worktree registrations after update. Expected changes are only the fast-forwarded canonical branch/upstream and its new files.

## C. Non-destructive research validation

Read [Friday handoff](FINANCE_WEEKEND_HANDOFF_2026-10-23.md), [checkpoint](FINANCE_WEEKEND_CHECKPOINT_2026-10-23.json), [audit method](VIDEO_AUDIT_METHODOLOGY_REVIEW.md), [methods](METHODS.md), current first section of [RESUME_HERE](RESUME_HERE.md), and [pending correction backlog](NICK_165_PENDING_CORRECTIONS.md).

The following Friday-byte gate is for initial acceptance **before any Saturday canonical write**. Sunday uses Saturday's actual published checkpoint instead.

```sh
.venv/bin/python --version
.venv/bin/python - <<'PY'
import pathlib,json,hashlib,zipfile,sqlite3
root=pathlib.Path.cwd();base=root/'research/finance-economics-intelligence'
p=json.loads((base/'FINANCE_WEEKEND_CHECKPOINT_2026-10-23.json').read_text())
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
for name,digest in {**p['canonical_hashes'],**p['immutable_source_hashes']}.items():
 assert sha(root/name)==digest, name
frozen=json.loads((base/'audit-baseline/MANIFEST.json').read_text())
assert len(frozen['source_hashes'])==26
assert p['immutable_source_hashes']==frozen['source_hashes']
a=[json.loads(s) for s in (base/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()]
assert len(a)==len({r['Video_ID'] for r in a})==966
assert sum(all(v.startswith('COMPLETE_') for v in r['statuses'].values()) for r in a)==441
n=p['next_untouched_original'];row=next(r for r in a if r['Video_ID']==n['video_id'])
assert row['script']['review_scope']=='NOT_REVIEWED'
with zipfile.ZipFile(root/n['archive']) as z:
 raw=z.read(n['member']);assert hashlib.sha256(raw).hexdigest()==n['member_sha256']
c=sqlite3.connect(f'file:{root}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
text=c.execute('select transcript_text from transcripts where youtube_video_id=?',(n['video_id'],)).fetchone()[0]
assert hashlib.sha256(text.encode()).hexdigest()==n['canonical_text_sha256'];c.close()
print('Friday canonical bytes, 26 fingerprints and next transcript PASS')
PY
```

Require project Python 3.12 (previously 3.12.14). If `.venv` is absent/broken, inspect `pyproject.toml`/`uv.lock` and use the established frozen project environment; do not silently fall back to an incompatible system Python or alter lockfiles. Verify Pillow/image tooling. Use `load_workspace_dependencies` to locate this Mac's bundled Node and openpyxl/artifact libraries; Machine B cache paths are not portable. Verify openpyxl import and `@oai/artifact-tool` package presence before accepting responsibility to rebuild the workbook.

Established validators normally overwrite their reports. For acceptance, redirect only those two report writes to a temporary directory, keeping canonical files untouched:

```sh
.venv/bin/python - <<'PY'
import pathlib,sys,tempfile
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path('research/finance-economics-intelligence').resolve()))
import validate_audit_966 as audit,validate_research as bounded
out=pathlib.Path(tempfile.mkdtemp(prefix='yios-machine-a-validation-'))
write=pathlib.Path.write_text
allowed={audit.BASE/'VALIDATION_966.json',bounded.BASE/'VALIDATION.json'}
def redirect(path,*args,**kwargs):
 assert path in allowed, 'Unexpected write: '+str(path)
 return write(out/path.name,*args,**kwargs)
with patch.object(pathlib.Path,'write_text',redirect):
 audit.validate();bounded.main()
print('Validation reports:',out)
PY
.venv/bin/python -m unittest discover -s research/finance-economics-intelligence -p 'test_*.py'
git diff --check
git status --porcelain=v1 --untracked-files=all
```

Friday Machine B ran 34 Finance tests successfully; do not claim historical Machine A's 149 tests freshly passed. Validator PASS is structural, not semantic proof of all claims. Workbook hash verifies exact Friday bytes; tests cover population/projection/formula contracts. Do not rebuild merely to sync. Verify exactly one authoritative combined Excel exists; old inspection sidecars are not another workbook.

Check the [portable package](channel-intelligence/nick-invests/2026-10-23/PORTABLE_PATHS.md) for original thumbnails and source paths. All required source archives are Git-tracked; current local bytes still need checks. For NICK_166 the actual thumbnail was not registered on Machine B. Inspect existing Machine A evidence registries; if absent, verify the registered URL and network ability to fetch that single image before accepting. No full video/audio is required for limited-evidence audits. A missing required image blocks thumbnail completion; a mere URL is not image evidence. Do not claim editing/audio/retention inspection from plaintext.

## D. Publish sole-writer acceptance

Only when identity, Git, preservation, required evidence, runtime/workbook tooling and validators pass and Machine B release is published:

1. Update [FINANCE_WRITER_OWNERSHIP.md](FINANCE_WRITER_OWNERSHIP.md) to `MACHINE_A_SOLE_WRITER_ACCEPTED`, with UTC timestamp, actual host/user/path, accepted full live SHA, PR state, hashes/test results and preserved local evidence. Keep release history.
2. Recheck live branch has not moved; inspect and stage **only** that intended document. Commit and push normally to the same Finance branch; do not create a replacement PR.
3. Verify the acceptance commit's local/origin/live/PR equality and clean status. If push or validation fails, do not write canonical research. No concurrent writer is authorized.

## E. First new audit: NICK_166

After acceptance, derive the next actual untouched ID again from the ledger/frozen order. Friday expectation: **`T3HINW7Nv14`**, “The REAL Cost of Being Average in America”. If it differs due to verified newer published work, follow that actual checkpoint; do not redo completed work.

Canonical transcript: `data/extracted/channel-data/DS-000022/packages/nick-invests/NickInvests_Transcripts_363_Videos.zip::214_T3HINW7Nv14_The_REAL_Cost_of_Being_Average_in_America.txt`; canonical SHA `7e753ab1db2e3ac0415702b1cc5b05b9f0b7d1fae035c829298dbad58a852c83`. Header-bearing member SHA is separate in checkpoint. Extract/read without modifying archive. Hash verification is not a full transcript read.

Create `audit-batches/NICK_166.json` and `NICK_166_READ_RECEIPTS.json` only after doing the research. Use current NICK_165 schema and validator's REQUIRED/SCOPES/strict receipt rules. No copying of another video's conclusions.

1. **Title:** exact source title, audience/problem, hook/promise, specificity, emotion, accuracy, script alignment and named peer comparisons; no inferred search-demand certainty.
2. **Thumbnail:** locate/reuse actual original bytes first; otherwise acquire only the registered image and record source URL/access date, file bytes/hash/dimensions. Inspect native and appropriate mobile size; document text, objects, composition, readability, relation to title/script. Preserve originals; never substitute a guessed design. On HTTP 429 stop new requests and record unavailable state.
3. **Script:** read the entire canonical stored string in bounded contiguous ranges. Record canonical UTF-8 hash/bytes/character count, first/last witnesses, exact archive/member/hash/bytes/lines, complete coverage ranges, opening/ending words, beat map, loops/examples/mechanisms, CTA and limitations. Automatic untimed text is not certified complete narration; timing stays `OPENING_WORDS_ONLY`; audio_verified false unless actual audio inspected. Audit material financial/statistical claims with dated primary sources, population/units/return assumptions, arithmetic and publication applicability; preserve access failures honestly.
4. **Topic:** audience problem, economic mechanism, novelty, corpus angle, same-channel competition and demand hypothesis. Separate observed data from interpretation.
5. **Performance:** use frozen metadata only, same channel/format/snapshot and stored ages. Lifetime views/day; eligible target/peers age >=7; peer age 0.5–2× target; other nearest-age peers sorted age-distance then Video ID; up to ten, at least five and positive median. STRONG >=2, WEAK <0.5, else TYPICAL. Reproduce exact ten IDs/denominator/ratio/tier and first-five sensitivity, never overwrite frozen labels or invent ratio for ineligible dates. Inspect stored rounding/tie behavior in baseline and comparisons code.
6. **Virality:** combine public outcome, topic, timing, competition, format/channel context, alternative explanations and original-content lesson. Label descriptive/causal limits. Private impressions/CTR/retention/satisfaction and historical thumbnail tests are unknown. Events may cite only registered EVENT_SOURCES IDs; add honest dated primary receipts separately, never invent event linkage.

Only fully supported dimensions receive COMPLETE_LIMITED_EVIDENCE. Missing evidence stays explicit; don't fabricate full completion. NICK_165 corrections remain a separate pending backlog, not the first default task.

## F. Assemble, validate, rebuild sole workbook, publish

After the authored batch and strict receipts are complete:

```sh
.venv/bin/python research/finance-economics-intelligence/build_audit_966.py
.venv/bin/python research/finance-economics-intelligence/validate_audit_966.py
.venv/bin/python research/finance-economics-intelligence/validate_research.py
.venv/bin/python research/finance-economics-intelligence/build_combined_workbook_data.py > /tmp/yios-finance-combined-payload.json
```

Do not run baseline rebuilding or ingestion. Review precise ledger/component changes against accepted parent: only intended video(s), no population/source drift. Rebuild **only** `FINANCE_1612_COMBINED_INTELLIGENCE.xlsx` with existing builder. Locate bundled dependencies using `load_workspace_dependencies`; set the task variables below to returned local paths (not guessed paths). The builder invokes `python3`, so place the verified project environment first on PATH. Run in a fresh temporary directory with builder and sibling formatting module copied from the accepted checkout; link its `node_modules` to the returned bundle. Canonical source scripts remain unchanged.

```sh
# Assign task_node and task_node_modules from this Mac's dependency-tool response.
# Verify both paths before running. This step intentionally writes the sole canonical workbook.
task_build_dir=$(mktemp -d /tmp/yios-finance-workbook.XXXXXX)
cp research/finance-economics-intelligence/build_workbook_1612.mjs "$task_build_dir/"
cp research/finance-economics-intelligence/workbook_formatting.mjs "$task_build_dir/"
ln -s "$task_node_modules" "$task_build_dir/node_modules"
PATH="$PWD/.venv/bin:$PATH" "$task_node" "$task_build_dir/build_workbook_1612.mjs" "$PWD/research/finance-economics-intelligence"
.venv/bin/python -m unittest discover -s research/finance-economics-intelligence -p 'test_*.py'
"$task_node" research/finance-economics-intelligence/test_workbook_formatting.mjs
git diff --check
```

If an existing test pins the prior audited count/status, update only its expectation after independently verifying the intentional new research count. Do not loosen tests or alter frozen source data. Builder performs artifact recalculation/count checks/error scan and writes four `/tmp/finance-1612-*.png` opening views; inspect each. Independently check exported workbook IDs/966 research projections/statuses/count caches against JSONL using read-only openpyxl or artifact tools, check no formula errors/object placeholders, and hash the final workbook. Native Excel recalculation is untested unless actually run. No second authoritative Excel.

Update the leading `RESUME_HERE.md` checkpoint with actual last/next ID, counts, source/receipt hashes, validation results, data limitations and live resource checkpoint. Recheck all 26 immutable hashes and previous unaffected research. Review exact intended file list and secrets/large-file risk, then stage each path explicitly (batch/receipts/image, ledger, seven projections, validation reports, sole workbook, focused test expectations and continuation documentation as warranted). Do not use `git add .` or indiscriminate staging.

```sh
git diff --cached --name-status
git diff --cached --check
git ls-remote origin refs/heads/research/finance-economics-intelligence
# Require remote still equals the accepted parent; stop/reconcile if it moved.
# Commit only after the complete atomic audit passes local checks.
git commit -m 'research: audit next original Finance video'
git push origin HEAD:refs/heads/research/finance-economics-intelligence
git rev-parse HEAD
git rev-parse origin/research/finance-economics-intelligence
git ls-remote origin refs/heads/research/finance-economics-intelligence
gh pr view 36 --repo ghilmanITM360/youtube-intelligence-os --json state,isDraft,headRefOid,statusCheckRollup
```

Require local/origin/live/PR equality. Normal push only, never force; stop if remote changes. Keep PR OPEN/DRAFT; do not merge/close/replace it. Existing CI is **CI_BLOCKED_BILLING** with zero-step payment/spending-limit annotation. Do not manually rerun Actions; local checks are not CI success. Inspect any naturally triggered check honestly.

## G. Resource stop and evidence preservation

Check live five-hour/weekly usage before each new video/expensive build and after publication. At gates, finish only current safe atomic work; preserve source bytes, exact read progress, hashes and pending dimensions externally and in a truthful continuation. Publish validated completed work when safe; never label an unfinished audit complete. Record any unpushed commit and local-only evidence owner/location. Do not consume reset credits, buy acquisitions, upload raw media or run unrelated rebuilds.

## H. Sunday continuation

Start from Saturday's **actual newest published SHA**, not Friday's original SHA or count. Read current writer state and leading RESUME_HERE, verify clean checkout/local-origin-live-PR equality, required evidence and frozen fingerprints. Reuse existing receipts; don't redo completed videos. If Machine A remains sole accepted writer, no transfer back-and-forth is required between Saturday and Sunday; still check competing writers and resources. Friday exact JSONL/workbook hashes are historical once legitimate Saturday research advances them.

## I. Sunday end / Monday return

Publish all completed validated weekend work on the same branch. Record actual final full SHA in an external technical result and resolve the containing release commit from Git for the durable handoff (avoid pretending a commit can embed its own hash). Record final counts, last/next original IDs, exact JSONL/workbook and 26-source checks, receipts, local-only incomplete work, preserved refs/stashes/media, billing limits and dependency gaps.

Update writer state to **MACHINE_A_RELEASED_AWAITING_MACHINE_B_ACCEPTANCE**, normally commit/push and independently confirm equality; then stop Finance writes. Machine B must independently inspect its local collisions/refs/stashes/evidence, non-pruning fetch and strict-fast-forward to the actual weekend head, run bounded validators and source/tooling gates, and publish **MACHINE_B_SOLE_WRITER_ACCEPTED** before research resumes. There is no preassigned Monday SHA and no automatic ownership return. A failed/partial handback is documented; it never authorizes two writers.
