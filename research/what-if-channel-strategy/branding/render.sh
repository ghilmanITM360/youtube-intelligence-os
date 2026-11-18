#!/bin/sh
# Rasterise SVGs to PNG at exact YouTube sizes with headless Chrome (system fonts: Avenir Next, Menlo).
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
r() { "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
      --window-size="$2,$3" --screenshot="$PWD/$1.png" "file://$PWD/$1.svg" >/dev/null 2>&1; }
r logo_profile 800 800
r watermark 300 300
r banner 2560 1440
r banner_safe_area_check 2560 1440
r thumbnail_sample_day25 1280 720
