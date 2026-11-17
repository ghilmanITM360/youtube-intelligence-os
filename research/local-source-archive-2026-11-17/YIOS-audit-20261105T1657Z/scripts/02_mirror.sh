#!/bin/zsh
# Independent receiving clone: no alternates, no hardlinks, no LFS smudge. Writes only under the audit dir.
A=$HOME/YIOS-audit-20261105T1657Z; S=$A/raw/remote/status.txt; U=https://github.com/ghilmanITM360/youtube-intelligence-os.git
export GIT_LFS_SKIP_SMUDGE=1
echo "start $(date -u +%FT%TZ)" > $S
git ls-remote $U > $A/raw/remote/ls_remote_pre_clone.txt 2>>$S
echo "ls-remote-exit $? lines=$(wc -l < $A/raw/remote/ls_remote_pre_clone.txt)" >> $S
perl -e 'alarm 3000; exec @ARGV' git -c gc.auto=0 -c maintenance.auto=false clone --mirror --no-hardlinks --no-tags --quiet $U $A/scratch/remote_mirror.git > $A/raw/remote/clone.log 2>&1
echo "clone-exit $? $(date -u +%FT%TZ)" >> $S
cd $A/scratch/remote_mirror.git && echo "alternates: $(ls objects/info/alternates 2>/dev/null | wc -l) refs: $(git for-each-ref | wc -l)" >> $S
git config --get-regexp '^remote\.origin\.(promisor|partialclonefilter|fetch)' >> $S
du -sh . >> $S
