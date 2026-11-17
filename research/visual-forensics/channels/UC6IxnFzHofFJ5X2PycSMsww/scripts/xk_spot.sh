#!/bin/bash
# make 0.6-scale copy of a sheet for primary spot-check and print reviewer rows for that sheet. Usage: xk_spot.sh <id> <NN>
WS=$HOME/YIOS-local-audits/xkcd-whatif; V=$WS/videos/$1; SC=/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/d2a98830-292c-4d67-85e5-ec71a232e398/scratchpad
$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 -I -c "import cv2;im=cv2.imread('$V/frames/sheets/SHEET_$2.jpg');cv2.imwrite('$SC/spot_$1_$2.jpg',cv2.resize(im,None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA))"
S=$(awk -F, -v s="SHEET_$2.jpg" '$1==s{print $3}' $V/tables/sheet_index.csv | sort -u | tr '\n' '|' | sed 's/|$//')
grep -E "^($S)," $V/review/rv1_$1/annotations.csv | cut -c1-170; echo "$SC/spot_$1_$2.jpg"
