#!/bin/bash
# Clean per-video rebuild inside an isolated HOME, from the restored scripts and source copies only. No model, no reviewer, no network.
# Usage: pe_rebuild_test.sh <root>         (root already holds restored/ from pe_restore_test.py restore)
#        pe_rebuild_test.sh <root> chain   (after that: review inputs from restored/, then the mechanical post-review scripts)
# Exit code per step is written to <root>/rebuild_steps.csv. HOME is what isolates: every script resolves its workspace from it.
ROOT=$1; REAL=$HOME; H=$ROOT/rbhome; WS=$H/YIOS-local-audits/primitive-education; STEPS=$ROOT/rebuild_steps.csv
if [ "${2:-}" = chain ]; then
  case "$WS" in "$REAL"/YIOS-local-audits/*) echo "refusing live workspace"; exit 1;; esac
  export HOME=$H; cp -R "$ROOT/restored/campaign/." "$WS/campaign/"
  for f in "$ROOT"/restored/source_media/*.mp4; do
    id=$(basename "$f" .mp4); V=$WS/videos/$id; RV=$ROOT/restored/videos/$id; AR=rv1_$id
    cd "$V" || exit 1
    cp -R "$RV/review" .; cp "$RV/tables/strip_frames.csv" "$RV/tables/sheet_index.csv" tables/; [ -f "$RV/tables/chroma_diff.csv" ] && cp "$RV/tables/chroma_diff.csv" tables/
    step() { n=$1; shift; "$@" >> "$ROOT/logs/$id.chain" 2>&1; echo "$id,$n,$?" >> "$STEPS"; }
    [ -f review/primary_corrections.csv ] && step correct python3 -I "$WS/scripts/pe_correct.py" . "$AR"
    A=review/$AR/annotations.csv; [ -f "review/$AR/annotations_corrected.csv" ] && A=review/$AR/annotations_corrected.csv
    step build python3 -I "$WS/scripts/pe_build.py" . "$A" "$AR"
    step finalize python3 -I "$WS/scripts/pe_finalize.py" . --art-done
    step report python3 -I "$WS/scripts/pe_report.py" . "$AR"
    step gate_corrections python3 -I "$WS/scripts/pe_gate_corrections.py" .
  done
  python3 -I "$WS/scripts/pe_ledger.py" >> "$ROOT/logs/ledger.chain" 2>&1; echo "ALL,ledger,$?" >> "$STEPS"; exit 0
fi
mkdir -p "$WS/videos" "$H/YIOS-local-audits/tooling" "$H/YIOS-local-audits/barely-evolved" "$ROOT/srcshim"
cp -R "$ROOT/restored/scripts" "$ROOT/restored/selection" "$WS/"; mkdir -p "$WS/campaign"
# Available dependencies, used read-only by symlink. Not rebuilt: see the report.
ln -s "$REAL/YIOS-local-audits/tooling/visual-ct-scan-venv" "$H/YIOS-local-audits/tooling/visual-ct-scan-venv"
ln -s "$REAL/YIOS-local-audits/barely-evolved/asr-venv" "$H/YIOS-local-audits/barely-evolved/asr-venv"
# Shim 1: pe_ingest.sh hardcodes an absolute ~/Downloads SRCDIR, which HOME does not redirect. Patched in this copy only.
# Shim 2: it globs "*[<id>].mp4", but source_media files are named <id>.mp4.
sed -i '' "s#^SRCDIR=.*#SRCDIR=\"$ROOT/srcshim\"#" "$WS/scripts/pe_ingest.sh"
for f in "$ROOT"/restored/source_media/*.mp4; do id=$(basename "$f" .mp4); ln -s "$f" "$ROOT/srcshim/$id [$id].mp4"; done
export HOME=$H HF_HOME=$REAL/.cache/huggingface HF_HUB_OFFLINE=1
echo "video,step,exit" > "$STEPS"
one() {
  id=$1; V=$WS/videos/$id; L=$ROOT/logs; mkdir -p "$L"; VPY=$H/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
  step() { n=$1; shift; "$@" >> "$L/$id.log" 2>&1; echo "$id,$n,$?" >> "$STEPS"; }
  step ingest bash "$WS/scripts/pe_ingest.sh" "$id"
  step prep bash "$WS/scripts/pe_prep.sh" "$id"
  step native "$VPY" -I "$WS/scripts/pe_native.py" "$V" 3
  step stroke "$VPY" -I "$WS/scripts/pe_stroke.py" "$V"
  step enc_audit python3 -I "$WS/scripts/pe_enc_audit.py" "$V"
}
export -f one; export ROOT WS H STEPS
ls "$ROOT/restored/source_media" | sed 's/\.mp4$//' | xargs -P 3 -I{} bash -c 'one {}'
echo "$(date -u +%FT%TZ) rebuild finished" >> "$ROOT/logs/DONE"
