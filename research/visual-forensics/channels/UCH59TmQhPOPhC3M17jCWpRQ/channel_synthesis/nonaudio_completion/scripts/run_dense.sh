PY=~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3; H=~/YIOS-local-audits/barely-evolved/channel_synthesis/nonaudio_completion
for v in uPQcyookL0Y mNLNb-Z4T0M GNaBxt_zIRA; do $PY $H/scripts/dense_motion.py "$(ls ~/Downloads/videos\ in\ mp3/BarelyEvolved-MP4/*$v*.mp4)" $H/dense/DENSE_MOTION_$v.csv 2>/dev/null & done; wait
