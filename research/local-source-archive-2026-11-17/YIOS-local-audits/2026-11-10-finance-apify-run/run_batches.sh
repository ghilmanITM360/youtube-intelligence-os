#!/bin/zsh
# usage: zsh run_batches.sh <first_run_no>  — one worker, 40-ID batches from PENDING_IDS.txt, export+validate after each, stops on rate limit
cd "${0:A:h}"; n=$1
while [ -s transcripts/PENDING_IDS.txt ]; do
  ids=$(head -40 transcripts/PENDING_IDS.txt | paste -sd, -)
  log=transcripts/backfill_run$n.log
  echo "=== run$n start $(date -u +%FT%TZ) ids=$(echo $ids | tr , '\n' | wc -l)" >> $log
  uv run --no-project --with yt-dlp python -I transcript_backfill.py --only "$ids" >> $log 2>&1; rc=$?
  python3 -I export_transcripts.py >> $log 2>&1 && python3 -I validate_and_pending.py >> $log 2>&1 || { echo "CHECKPOINT_FAILED run$n" >> $log; exit 3; }
  shasum -a 256 transcripts/export/* > transcripts/export/CHECKPOINT_run$n.sha256
  echo "=== run$n end $(date -u +%FT%TZ) rc=$rc" >> $log
  [ $rc -ne 0 ] && { echo "STOPPED rc=$rc (rate limit / error) at run$n" >> $log; exit $rc; }
  k=$(echo "$ids" | tr , '\n' | wc -l); still=$(echo "$ids" | tr , '\n' | grep -cxFf transcripts/PENDING_IDS.txt)
  [ $still -eq $k ] && { echo "NO_PROGRESS run$n" >> $log; exit 4; }
  n=$((n+1)); sleep 30
done
echo "QUEUE_EMPTY" >> transcripts/backfill_run$n.log
