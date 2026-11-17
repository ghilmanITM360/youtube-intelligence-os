#!/bin/zsh
# usage: whisper_local.sh <out_dir> <media files...>  — local Whisper small.en, originals read in place
out=$1; shift
for f in "$@"; do
  id=$(echo "$f" | grep -oE '\[[A-Za-z0-9_-]{11}\]\.[a-z0-9]+$' | cut -c2-12)
  [ -s "$out/$id.json" ] && continue
  ~/Library/Python/3.9/bin/whisper "$f" --model small.en --language en --output_format json --output_dir "$out/tmp_$id" --fp16 False >/dev/null 2>"$out/$id.err" \
    && mv "$out/tmp_$id"/*.json "$out/$id.json" && rmdir "$out/tmp_$id" && rm -f "$out/$id.err" && echo "OK $id" || echo "FAIL $id"
done
