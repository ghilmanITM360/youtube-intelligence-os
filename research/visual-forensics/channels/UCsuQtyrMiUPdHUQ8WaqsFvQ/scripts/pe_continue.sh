#!/bin/zsh
# Primitive Education continuation gatekeeper (launchd, every 30 min). No model call until a wake time is due.
# Order: complete -> next-wake -> lock -> sources/disk -> meter (weekly first) -> launch one headless worker.
WS=$HOME/YIOS-local-audits/primitive-education; C=$WS/campaign; LOG=$C/scheduler.log; WAKE=$C/next_wake_epoch
export PATH=$HOME/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin
export VF_LOCK_DIR=$WS/.pe_writer_lock VF_LOCK_LOG=$WS/.pe_lock_events.log; LK=$HOME/YIOS-local-audits/vf_lock.sh
say() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
# One-time model-free receipt that launchd context can read the verified copies.
[ -f $C/.source_probe_done ] || { if perl -e 'alarm 6; exec @ARGV' head -c 16 $WS/source_media/RmTdnXHbI8s.mp4 > /dev/null 2>&1; then say "PROBE source_media read OK (launchd context)"; touch $C/.source_probe_done; else say "PROBE source_media read FAILED"; fi; }
# Owner-visible hold: nothing executable without a new capability; no model call. Delete the file to resume.
[ -f $C/HOLD_NO_EXECUTABLE_WORK ] && { say "HOLD $(head -1 $C/HOLD_NO_EXECUTABLE_WORK)"; exit 0; }
if [ -f $C/CAMPAIGN_COMPLETE ]; then say "COMPLETE -> disabling"; launchctl bootout gui/$(id -u)/com.yios.primitive-education-continue; exit 0; fi
[ -f $WAKE ] && [ "$(date +%s)" -lt "$(cat $WAKE)" ] && exit 0
if [ "$($LK status | head -1)" != FREE ]; then
  r=$($LK recover 2>&1 | head -1); case "$r" in RECOVERED*) say "lock $r";; *) say "SKIP lock held: $r"; exit 0;; esac
fi
# Sources: verified copies in the workspace (campaign/SOURCE_MEDIA_COPIES.json). Downloads triggers a TCC prompt nobody can answer unattended (tccd AUTHREQ_PROMPTING 2026-11-05 12:27Z), so this script must not touch it.
[ -s $WS/source_media/RmTdnXHbI8s.mp4 ] && head -c 16 $WS/source_media/RmTdnXHbI8s.mp4 > /dev/null && [ -f $WS/selection/selection_v1.json ] || { say "BLOCK sources/workspace missing"; exit 0; }
free=$(df -g $HOME | tail -1 | awk '{print $4}'); [ "$free" -ge 5 ] || { say "BLOCK disk ${free}GiB"; exit 0; }
u=$($WS/scripts/pe_usage.sh) || { say "SKIP usage UNKNOWN"; date -v+30M +%s > $WAKE; exit 0; }
read w wr f fr <<< "$(/usr/bin/python3 -c "import json,sys;d=json.loads(sys.argv[1]);print(d['seven_day'],d['seven_day_reset'],d['five_hour'],d['five_hour_reset'])" "$u")"
say "usage $u"
if /usr/bin/python3 -c "import sys;sys.exit(0 if float('$w')>=0.95 else 1)"; then say "SUSPEND weekly $w until $wr+5m"; echo $((wr+300)) > $WAKE; exit 0; fi
if /usr/bin/python3 -c "import sys;sys.exit(0 if float('$f')>=0.85 else 1)"; then say "WAIT five-hour $f until $fr+5m"; echo $((fr+300)) > $WAKE; exit 0; fi
if [ -f $C/.supervised_test ]; then
  say "SUPERVISED TEST start"; cd $WS && claude -p "Reply with the single word READY then the value of the final_status column of the first row of campaign/campaign_ledger.csv." --model haiku --allowedTools "Read" --max-turns 3 --setting-sources "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' < /dev/null >> $C/scheduler_test_output.txt 2>&1; say "SUPERVISED TEST exit $?"; rm -f $C/.supervised_test; exit 0
fi
say "LAUNCH worker"; t0=$(date +%s)
cd $HOME/workprojects/youtube-intelligence-os && claude -p "$(cat $C/RESUME_PROMPT.md)" --model claude-opus-5-5 --permission-mode acceptEdits --allowedTools "Read,Write,Edit,Bash,Agent,Glob,Grep" --output-format json < /dev/null > $C/worker_last.json 2>> $C/worker_stderr.log
rc=$?; say "WORKER exit $rc after $(( $(date +%s)-t0 ))s"
# crash-loop guard: a quick failure waits 2 h rather than relaunching on every 30-min tick
if [ $rc -ne 0 ] && [ $(( $(date +%s)-t0 )) -lt 300 ]; then date -v+2H +%s > $WAKE; say "quick failure -> wait 2h"; fi
