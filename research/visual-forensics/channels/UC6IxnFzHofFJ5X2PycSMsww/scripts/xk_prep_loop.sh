#!/bin/bash
# keep prepping videos as ingest finishes; exits when all selected are prepped
WS=$HOME/YIOS-local-audits/xkcd-whatif
while true; do
  left=0
  for id in $(cat $WS/selection/ingest_order.txt); do
    V=$WS/videos/$id
    [ -f $V/tables/sheet_index.csv ] && continue
    left=1
    [ -f $V/INGEST_DONE ] && $WS/scripts/xk_prep.sh rv1 "$id"
  done
  [ $left = 0 ] && { echo ALL_PREPPED; exit 0; }
  sleep 30
done
