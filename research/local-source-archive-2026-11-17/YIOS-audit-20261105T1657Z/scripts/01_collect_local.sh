#!/bin/zsh
# Read-only evidence collection plus usage gate. Writes only under $A/raw.
# No model usage. No git writes: no fetch, gc, repack, prune or fsck --lost-found.
A=/Users/ghilmankhan/YIOS-audit-20261105T1657Z
R=$A/raw
REPO=$HOME/workprojects/youtube-intelligence-os
export GIT_OPTIONAL_LOCKS=0
setopt NULL_GLOB
limit() { perl -e '$t=shift; alarm $t; exec @ARGV' "$@"; }
stamp() { date -u +%FT%TZ; }
echo "start $(stamp)" > $R/collect_status.txt

# --- orphan .rev
O=$R/orphan_rev; mkdir -p $O
P=$REPO/.git/objects/pack; B=pack-8d9357e755ad7b7ae3a2fa62a866d13502003c23
{
  stamp; git --version; git -C $REPO config --get core.multiPackIndex; git -C $REPO config --get pack.writeReverseIndex
  echo "--- matching files"; ls -lTn $P/$B.* 2>&1
  echo "--- stat"; stat -f '%N size=%z mtime=%Sm birth=%SB' $P/$B.rev 2>&1
  echo "--- sha256"; shasum -a 256 $P/$B.rev 2>&1
  echo "--- header (magic/version/hash-id)"; xxd -l 12 $P/$B.rev 2>&1
  echo "--- pack dir counts"
  for e in pack idx rev mtimes bitmap keep promisor; do print "$e $(ls $P/*.$e 2>/dev/null | wc -l)"; done
  ls $P | grep -Ev '^pack-[0-9a-f]+\.(pack|idx|rev|mtimes|bitmap|keep|promisor)$'
  echo "--- files per pack without .pack or .idx"
  for f in $P/pack-*.*; do s=${f%.*}; [ -e $s.pack ] && [ -e $s.idx ] || print $f; done
  echo "--- newest pack dir entries"; ls -lTt $P | head -12
  echo "--- count-objects"; git -C $REPO count-objects -v 2>&1
  echo "--- gc.log"; ls -l $REPO/.git/gc.log 2>&1
} > $O/inspect.txt 2>&1
echo "fsck-start $(stamp)" >> $R/collect_status.txt
nice -n 15 perl -e 'alarm 1200; exec @ARGV' git -C $REPO fsck --full --no-dangling --no-reflogs --no-progress > $O/fsck_full.txt 2>&1
echo "fsck-exit $? $(stamp)" >> $R/collect_status.txt

# --- Primitive Education scheduler raw evidence (file facts only)
M=$R/primitive_scheduler; mkdir -p $M
PE=$HOME/YIOS-local-audits/primitive-education
{
  stamp; launchctl print gui/$(id -u)/com.yios.primitive-education-continue 2>&1 | grep -E 'state|runs|last exit|program|stdout|stderr|run interval|calendar|Minute|Hour'
  ls -lT $PE/campaign/launchd_* 2>&1; wc -lc $PE/campaign/launchd_* 2>&1
} > $M/facts.txt 2>&1

# --- local-only inventory: path, size, mtime. No hashing yet.
I=$R/inventory; mkdir -p $I
for pair in archive:$HOME/YIOS-Archive local_audits:$HOME/YIOS-local-audits private_backups:$HOME/Documents/yios-private-backups git_recovery:$HOME/yios-git-recovery recovery_status:$HOME/workprojects/yios-recovery-status finance_work:$HOME/finance-work-machine-a; do
  n=${pair%%:*}; d=${pair#*:}
  [ -e $d ] && find $d -type f -not -name .DS_Store -print0 2>$I/$n.err | xargs -0 stat -f '%z%t%Sm%t%N' -t '%FT%T' > $I/$n.tsv 2>>$I/$n.err
done
GIT_OPTIONAL_LOCKS=0 git -C $REPO ls-files -z --others --ignored --exclude-standard | tr '\0' '\n' > $I/canonical_ignored_untracked_paths.txt 2>$I/canonical_ignored.err
wc -l $I/*.tsv $I/canonical_ignored_untracked_paths.txt > $I/counts.txt 2>&1
# Candidate manifests by name, across the listed YIOS roots and repo evidence.
cat $I/*.tsv | cut -f3 | grep -iE 'missing|unavailable|forensic.*(hash|manifest)|manifest|sha256|checksum|inventory' > $I/manifest_candidates.txt
# Name-only YIOS media search outside those roots; contents not opened.
find $HOME/Downloads $HOME/Movies $HOME/Desktop -maxdepth 5 \( -iname '*primitive*' -o -iname '*yios*' -o -iname '*barely*evolved*' -o -iname '*casually*finance*' -o -iname '*xkcd*' -o -iname '*what*if*' \) 2>$I/named_elsewhere.err > $I/named_elsewhere.txt
echo "inventory-done $(stamp)" >> $R/collect_status.txt

# --- current remote state: read-only, no local ref writes
perl -e 'alarm 120; exec @ARGV' git -C $REPO ls-remote origin > $R/ls_remote_origin.txt 2>$R/ls_remote_origin.err
echo "ls-remote-exit $? lines=$(wc -l < $R/ls_remote_origin.txt) $(stamp)" >> $R/collect_status.txt

# --- usage gate: wait for a rate-limit observation made after the reported reset
RESET_MS=1793899200000   # 2026-11-05T17:20:00Z, from health.rateLimits.five_hour.resetsAt
CEIL=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-05T17:50:00 +%s)
result=ceiling-reached-no-fresh-observation
while [ $(date -u +%s) -lt $CEIL ]; do
  o=$(curl -s -m 3 localhost:37701/api/health | python3 -c "import json,sys;v=json.load(sys.stdin)['rateLimits']['five_hour'];print(v['observedAt'],v['utilization'],v['resetsAt'])" 2>/dev/null)
  [ -n "$o" ] && [ ${o%% *} -gt $RESET_MS ] && { result="fresh-observation $o"; break; }
  sleep 30
done
ls -ld $HOME/YIOS-local-audits/.vf_writer_lock > $R/lock_at_gate.txt 2>&1
echo "gate $result $(stamp)" | tee -a $R/collect_status.txt
