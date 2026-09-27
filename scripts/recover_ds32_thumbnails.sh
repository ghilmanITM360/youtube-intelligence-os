#!/usr/bin/env bash
set -euo pipefail

repo_root=${1:?repository root required}
dataset="$repo_root/data/raw/competitors/DS-000032/dataset.json"
output_dir="$repo_root/data/raw/competitors/DS-000032/public-browser-2026-09-27/thumbnails"
mkdir -p "$output_dir"

jq -r '.[] | [.id, .thumbnailUrl] | @tsv' "$dataset" |
while IFS=$'\t' read -r video_id thumbnail_url; do
  target="$output_dir/${video_id}.jpg"
  if [[ -s "$target" ]]; then
    continue
  fi
  if ! curl -L --fail --silent --show-error --output "$target" "$thumbnail_url"; then
    fallback="https://i.ytimg.com/vi/${video_id}/hqdefault.jpg"
    curl -L --fail --silent --show-error --output "$target" "$fallback"
  fi
done

find "$output_dir" -type f -name '*.jpg' -size +0c | sort
