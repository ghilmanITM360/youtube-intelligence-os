#!/bin/zsh
# No model use. Waits for the mirror, then does remaining read-only mechanical audit under this directory only.
A=$HOME/YIOS-audit-20261105T1657Z; cd $A; S=$A/raw/mechanical_status.txt; M=$A/scratch/remote_mirror.git; REPO=$HOME/workprojects/youtube-intelligence-os
export GIT_OPTIONAL_LOCKS=0 GIT_NO_LAZY_FETCH=1 GIT_LFS_SKIP_SMUDGE=1
st(){ echo "$* $(date -u +%FT%TZ)" >> $S; }
limit(){ perl -e '$t=shift;alarm $t;exec @ARGV' "$@"; }
st start
c=0; until grep -q '^clone-exit' raw/remote/status.txt || [ $c -ge 400 ]; do sleep 15; c=$((c+1)); done
st mirror-wait-done "$(grep clone-exit raw/remote/status.txt)"
git -C $M fsck --connectivity-only --no-progress > raw/remote/mirror_fsck.txt 2>&1; st mirror-fsck $?
git ls-remote $M > raw/refs/mirror_refs.txt
limit 90 git -C $REPO ls-remote origin > raw/refs/ls_remote_final.txt 2>raw/refs/ls_remote_final.err; st ls-remote $?
/usr/bin/python3 -I scripts/06_ref_matrix.py > raw/refs/matrix.log 2>&1; st ref-matrix $?
# LFS: pointers across all refs, then fetch real payloads and hash them.
git -C $M lfs ls-files --all --long > raw/lfs/ls_files_all.txt 2>raw/lfs/ls_files.err; st lfs-ls $?
awk '{print $1}' raw/lfs/ls_files_all.txt | sort -u > raw/lfs/oids_short_or_full.txt; wc -l raw/lfs/oids_short_or_full.txt >> $S
[ $(df -g $HOME | tail -1 | awk '{print $4}') -ge 30 ] && { limit 3000 git -C $M lfs fetch --all origin > raw/lfs/fetch.log 2>&1; st lfs-fetch $?; } || st lfs-fetch-SKIPPED-low-disk
find $M/lfs/objects -type f 2>/dev/null | while read f; do print "$(basename $f) $(shasum -a 256 $f | cut -d' ' -f1) $(stat -f %z $f)"; done > raw/lfs/payload_hash_check.txt
awk '{print $1}' raw/lfs/payload_hash_check.txt > raw/lfs/oids.txt; awk '$1!=$2' raw/lfs/payload_hash_check.txt > raw/lfs/payload_MISMATCH.txt; st lfs-verified "$(wc -l < raw/lfs/payload_hash_check.txt) mismatch $(wc -l < raw/lfs/payload_MISMATCH.txt)"
nice -n 10 /usr/bin/python3 -I scripts/07_blob_compare.py > raw/blob/summary.txt 2>&1; st blob-compare $?
# Repo content search across all branch tips (mirror, no worktree).
for r in $(git -C $M for-each-ref --format='%(refname)' refs/heads); do git -C $M grep -lE '5,767|\b5767\b' $r -- '*.md' '*.json' '*.txt' 2>/dev/null; done | sort -u > raw/refs/grep_5767.txt; st grep-5767
# Stash and recovery refs: stat only.
{ git -C $REPO stash list --format='%H %gd %ci %s'; git -C $REPO show --stat --format=%H stash@{0} | tail -30; git -C $REPO log -3 --format='%H %s' refs/stash; for x in refs/yios-candidates/video-003-checkpoint11 refs/yios-candidates/video-003-checkpoint11-final; do echo "$x $(git -C $REPO rev-parse $x)"; done; git -C $REPO for-each-ref refs/codex; } > raw/refs/stash_recovery.txt 2>&1
# Isolated test export of pinned refs; no network, writes only under scratch.
SB="(version 1)(allow default)(deny network*)(deny file-write* (subpath \"$HOME/workprojects\") (subpath \"$HOME/YIOS-local-audits\") (subpath \"$HOME/YIOS-Archive\") (subpath \"$HOME/Downloads\") (subpath \"$HOME/Documents\"))"
PY=$REPO/.venv/bin/python
for r in main research/finance-economics-intelligence codex/casually-finance-knowledge-navigation; do
  n=${r//\//_}; X=$A/scratch/tests/$n; O=$A/raw/tests/$n; mkdir -p $X $O
  sha=$(git -C $M rev-parse refs/heads/$r); echo $sha > $O/sha.txt
  git -C $M archive $sha | tar -x -C $X; st export $r $sha
  for p in $(git -C $M ls-tree -r --name-only $sha -- '*.db'); do
    if head -c 20 $X/$p | grep -q 'git-lfs'; then git -C $M lfs smudge < $X/$p > $X/$p.real 2>>$O/smudge.err && mv $X/$p.real $X/$p; fi
  done
  cd $X; T=$(mktemp -d $A/scratch/tmp.XXXXXX)
  E0="env -u GH_TOKEN -u GITHUB_TOKEN -u ANTHROPIC_API_KEY HOME=$T TMPDIR=$T PYTHONDONTWRITEBYTECODE=1 GIT_CONFIG_GLOBAL=/dev/null"
  run(){ local tag=$1; shift; limit 1500 sandbox-exec -p "$SB" ${=E0} "$@" > $O/$tag.log 2>&1; echo "$tag exit $?" >> $O/results.txt; }
  run ruff $REPO/.venv/bin/ruff check scripts tests
  run compileall $PY -m compileall -q scripts tests
  run rebuild_catalog $PY -m scripts.rebuild_inventory_catalog --database $T/bootstrap.db
  run build_registry $PY -m scripts.build_youtube_channel_registry --write-ledgers
  run validate_ledgers $PY -m scripts.validate_dataset_ledgers
  run validate_registry $PY -m scripts.validate_youtube_channel_registry
  run pytest $PY -m pytest -q -p no:cacheprovider --tb=short
  { git -C $M ls-tree -r --name-only $sha -- '*.db' ; echo ---; git -C $M ls-tree -r --name-only $sha -- '*.db' | grep -vFx -e data/catalog/youtube_inventory.db -e data/catalog/youtube_channel_registry.db; } > $O/db_allowlist.txt
  cd $A; st tests-done $r "$(tr '\n' ';' < $O/results.txt)"
done
# reference DB from Finance tip, audited in scratch copy only.
X=$A/scratch/tests/research_finance-economics-intelligence/data/knowledge/reference_knowledge.db
[ -f $X ] && python3 -c "
import sqlite3,json,sys
c=sqlite3.connect('file:$X?mode=ro',uri=True)
print(json.dumps(dict(integrity=c.execute('PRAGMA integrity_check').fetchone()[0],fk=len(c.execute('PRAGMA foreign_key_check').fetchall()),tables={n:c.execute(f'select count(*) from \"{n}\"').fetchone()[0] for (n,) in c.execute(\"select name from sqlite_master where type='table' and name not like 'sqlite_%' and name not like '%_data' and name not like '%_idx' and name not like '%_docsize' and name not like '%_config' and name not like '%_content'\").fetchall()})))" > raw/db/reference_knowledge.json 2>&1
# after snapshot
{ date -u +%FT%TZ; git -C $REPO for-each-ref --format='%(objectname) %(refname)'; } > after/refs.txt; git -C $REPO worktree list > after/worktrees.txt; git -C $REPO stash list --format='%H %gd' > after/stash.txt; git -C $REPO status --short > after/status_canonical.txt; git -C $HOME/workprojects/yios-finance-machine-a status --short > after/status_finance.txt
st mechanical-done
# usage gate: ends on an observation below 0.70, or after the 22:00Z reset. Ceiling 23:00Z.
CEIL=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-05T23:00:00 +%s); g=ceiling-reached-no-fresh-observation
while [ $(date -u +%s) -lt $CEIL ]; do
  o=$(curl -s -m 3 localhost:37701/api/health | python3 -c "import json,sys,time;v=json.load(sys.stdin)['rateLimits']['five_hour'];age=time.time()*1000-v['observedAt'];print(v['observedAt'],v['utilization'],int(age<900000))" 2>/dev/null)
  set -- ${=o}
  [ -n "$o" ] && [ "$3" = 1 ] && python3 -c "import sys;sys.exit(0 if $2<0.70 or $1>1793916000000 else 1)" && { g="fresh $o"; break; }
  sleep 60
done
st gate "$g"; echo "$g"
