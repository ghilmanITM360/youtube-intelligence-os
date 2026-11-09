#!/bin/zsh
# Visual Forensics writer lock v3. Token-owned, mkdir-atomic, lease + process identity.
#   acquire <label> [run_id] [task]  -> ACQUIRED token=<T> | BUSY ... (exit 1)
#   heartbeat <token>                -> renews lease
#   release <token>                  -> RELEASED | NOT_OWNER | NOT_HELD (idempotent, never touches others' lock)
#   status                           -> FREE | HELD <receipt>
#   recover [--session-dead]         -> reclaims only with proof: owner pid dead/reused, or (no pid) lease expired AND --session-dead
# Owner PID = nearest actual claude/codex executable ancestor (ps comm, never command text).
# Token API stays compatible. Ambiguous legacy PID death requires expired lease + --session-dead.
L=${VF_LOCK_DIR:-$HOME/YIOS-local-audits/.vf_writer_lock}
LOG=${VF_LOCK_LOG:-$HOME/YIOS-local-audits/.vf_lock_events.log}
LEASE=${VF_LEASE_SECONDS:-2700}
now() { date -u +%FT%TZ; }
log() { echo "$(now) $*" >> $LOG; }
field() { grep "^$1=" "$L/receipt" 2>/dev/null | head -1 | cut -d= -f2-; }
pstart() { ps -o lstart= -p "$1" 2>/dev/null | sed 's/  */ /g'; }
owner_pid() {
  local p=$PPID c
  while [ -n "$p" ] && [ "$p" -gt 1 ]; do
    c=$(ps -o comm= -p "$p" 2>/dev/null)
    case "${c:t}" in claude|codex) echo "$p"; return 0;; esac
    p=$(ps -o ppid= -p "$p" 2>/dev/null | tr -d ' ')
  done
  return 1
}
case "$1" in
 acquire)
  [ -z "$2" ] && { echo "usage: acquire <label> [run_id] [task]"; exit 2; }
  op=$(owner_pid)
  [ -n "$op" ] && [ -n "$(pstart "$op")" ] || { echo "REFUSED: no live session executable ancestor"; exit 1; }
  if mkdir "$L" 2>/dev/null; then
    t=$(uuidgen)
    { echo "schema=3"; echo "owner_identity=executable_ancestor"; echo "token=$t"; echo "label=$2"; echo "host=$(hostname -s)"; echo "run_id=${3:-none}"; echo "task=${4:-unspecified}"
      echo "pid=$op"; echo "pid_start=$( [ -n "$op" ] && pstart $op )"; echo "acquired=$(now)"; echo "heartbeat=$(now)"; echo "heartbeat_epoch=$(date +%s)"
    } > "$L/receipt.tmp" && mv "$L/receipt.tmp" "$L/receipt"
    log "ACQUIRE label=$2 run=${3:-none} pid=$op"; echo "ACQUIRED token=$t"
  else
    hb=$(field heartbeat_epoch); age=$(( $(date +%s) - ${hb:-0} ))
    echo "BUSY: label=$(field label) run=$(field run_id) acquired=$(field acquired) lease_age_s=$age"; exit 1
  fi;;
 heartbeat)
  [ "$(field token)" = "$2" ] && [ -n "$2" ] || { echo NOT_OWNER; exit 1; }
  sed -i '' -e "s/^heartbeat=.*/heartbeat=$(now)/" -e "s/^heartbeat_epoch=.*/heartbeat_epoch=$(date +%s)/" "$L/receipt"; echo RENEWED;;
 release)
  [ -d "$L" ] || { echo NOT_HELD; exit 0; }
  if [ -n "$2" ] && [ "$(field token)" = "$2" ]; then log "RELEASE label=$(field label)"; rm -f "$L/receipt" "$L/receipt.tmp" "$L/owner"; rmdir "$L" && echo RELEASED
  else echo NOT_OWNER; exit 1; fi;;
 status)
  [ -d "$L" ] || { echo FREE; exit 0; }
  [ -f "$L/receipt" ] && { echo "HELD"; grep -v '^token=' "$L/receipt"; } || echo "HELD (legacy/no receipt): $(cat $L/owner 2>/dev/null)";;
 recover)
  [ -d "$L" ] || { echo FREE; exit 0; }
  [ -f "$L/receipt" ] || { echo "REFUSED: no receipt, identity unknown (manual verification needed)"; exit 1; }
  [ "$(field host)" = "$(hostname -s)" ] || { echo "REFUSED: other or unknown host; local PID cannot prove owner death"; exit 1; }
  pid=$(field pid); ps0=$(field pid_start); hb=$(field heartbeat_epoch); age=$(( $(date +%s) - ${hb:-0} ))
  if [ -n "$pid" ]; then
    cur=$(pstart $pid)
    if [ -n "$cur" ] && [ "$cur" = "$ps0" ]; then echo "REFUSED: owner pid $pid still alive (same start) -> ACTIVE"; exit 1; fi
    if [ "$(field schema)" != 3 ] || [ "$(field owner_identity)" != executable_ancestor ]; then
      [ "$age" -gt "$LEASE" ] && [ "$2" = "--session-dead" ] || { echo "REFUSED: legacy PID may be a short-lived shell; require expired lease AND --session-dead after session audit"; exit 1; }
    fi
    why="owner pid $pid dead or reused (start '$ps0' vs '$cur')"
  elif [ "$age" -gt "$LEASE" ] && [ "$2" = "--session-dead" ]; then why="no pid, lease expired (${age}s) and session verified dead by caller"
  else echo "REFUSED: no pid proof; need lease>${LEASE}s (age ${age}s) AND --session-dead"; exit 1; fi
  mkdir -p $(dirname $L)/.vf_recovered; mv "$L" "$(dirname $L)/.vf_recovered/lock-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  log "RECOVER label=$(grep ^label= $(dirname $L)/.vf_recovered/lock-*-$$/receipt | cut -d= -f2) why=$why"; echo "RECOVERED: $why";;
 *) echo "usage: vf_lock.sh acquire|heartbeat|release|status|recover"; exit 2;;
esac
