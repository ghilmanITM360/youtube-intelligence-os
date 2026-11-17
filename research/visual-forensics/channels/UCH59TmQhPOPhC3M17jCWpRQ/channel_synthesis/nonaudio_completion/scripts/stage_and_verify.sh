#!/bin/bash
# R20 copy + verify. Usage: stage_and_verify.sh <DEST_DIR> [--same-device-test]
# Copies TRANSFER_MANIFEST_v2.json package_items to <DEST_DIR>/barely-evolved-transfer/, never overwriting a differing file,
# re-hashes at the destination, then runs a representative restore. Originals are only read.
set -euo pipefail
DEST=${1:?destination directory required}; MODE=${2:-}
N="$HOME/YIOS-local-audits/barely-evolved/channel_synthesis/nonaudio_completion"; M="$N/portability/TRANSFER_MANIFEST_v2.json"
SRCDEV=$(stat -f %d "$HOME/Downloads/videos in mp3/BarelyEvolved-MP4"); mkdir -p "$DEST"; DSTDEV=$(stat -f %d "$DEST")
if [ "$SRCDEV" = "$DSTDEV" ] && [ "$MODE" != "--same-device-test" ]; then echo "REFUSED: $DEST is on the source device (not off-device durable storage)"; exit 2; fi
T="$DEST/barely-evolved-transfer"; mkdir -p "$T"
python3 - "$M" "$T" <<'EOF'
import json, sys, shutil, hashlib, os
m = json.load(open(sys.argv[1])); T = sys.argv[2]
for i in m['package_items']:
    d = os.path.join(T, i['package_path']); os.makedirs(os.path.dirname(d), exist_ok=True)
    if os.path.exists(d):
        if hashlib.sha256(open(d, 'rb').read()).hexdigest() != i['sha256']: sys.exit(f'REFUSED: existing differing file {d}')
        continue
    shutil.copy2(i['local_path'], d)
EOF
cp "$M" "$N/portability/TRANSFER_SHA256SUMS.txt" "$T/"
( cd "$T" && shasum -a 256 -c TRANSFER_SHA256SUMS.txt ) > "$T/VERIFY_SHA256.log"
grep -c ': OK$' "$T/VERIFY_SHA256.log" | xargs echo "sha256 OK:"
python3 - "$M" "$T" <<'EOF'
import json, sys, subprocess, os
m = json.load(open(sys.argv[1])); T = sys.argv[2]; bad = 0
for i in m['package_items']:
    if i['kind'] == 'SOURCE_MP4' or i['package_path'].endswith('RT-V1-P01/rt.mp4'):
        n = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', os.path.join(T, i['package_path'])], capture_output=True, text=True).stdout.strip()
        ok = i.get('expected_decoded_frames') in (None, int(n or -1)); bad += not ok
        print('restore', 'OK' if ok else 'FAIL', n, i['package_path'])
sys.exit(bad)
EOF
echo "VERIFIED $(date -u +%FT%TZ) $T $MODE"
