#!/bin/bash
# validate -> build -> finalize -> report -> ledger. Usage: pe_process.sh <id> <agent_id>
set -e
WS=$HOME/YIOS-local-audits/primitive-education; id=$1; AG=$2; R=rv1_$id; V=$WS/videos/$id
cd "$V"; [ -f review/primary_spotcheck.json ] || { echo "spotcheck missing"; exit 1; }
[ -f review/primary_corrections.csv ] && python3 -I $WS/scripts/pe_correct.py . $R
python3 -I $WS/scripts/pe_validate_review.py . $R $AG
A=review/$R/annotations.csv; [ -f review/$R/annotations_corrected.csv ] && A=review/$R/annotations_corrected.csv
python3 -I $WS/scripts/pe_build.py . $A $R > /dev/null
python3 -I $WS/scripts/pe_finalize.py . --art-done
python3 -I $WS/scripts/pe_report.py . $R
python3 -I $WS/scripts/pe_ledger.py
echo "$(date -u +%FT%TZ) $id processed reviewer=$R agent=$AG" >> $WS/campaign/progress_log.txt
