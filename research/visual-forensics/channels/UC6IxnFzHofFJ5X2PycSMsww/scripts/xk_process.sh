#!/bin/bash
# validate reviewer -> build -> finalize -> report -> matrix. Usage: xk_process.sh <id> <agent_id>  (review/primary_spotcheck.json must exist)
set -e
WS=$HOME/YIOS-local-audits/xkcd-whatif; id=$1; AG=$2; R=rv1_$id; V=$WS/videos/$id
cd "$V"; [ -f review/primary_spotcheck.json ] || { echo "spotcheck missing"; exit 1; }
[ -f review/primary_corrections.csv ] && python3 -I $WS/scripts/xk_correct.py . $R
python3 -I $WS/scripts/xk_validate_review.py . $R $AG
A=review/$R/annotations.csv; [ -f review/$R/annotations_corrected.csv ] && A=review/$R/annotations_corrected.csv
python3 -I $WS/scripts/xk_build.py . $A $R > /dev/null
python3 -I $WS/scripts/xk_finalize.py . --art-done
python3 -I $WS/scripts/xk_report.py . $R
python3 -I $WS/scripts/xk_matrix.py $WS > /dev/null
echo "$(date -u +%FT%TZ) $id processed reviewer=$R agent=$AG" >> $WS/campaign/progress_log.txt
