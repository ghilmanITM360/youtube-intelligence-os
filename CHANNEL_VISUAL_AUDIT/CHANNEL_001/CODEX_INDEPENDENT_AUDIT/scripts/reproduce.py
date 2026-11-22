"""Read original evidence tables and native files. Run from the worktree root."""
import collections
import csv
import json
import pathlib
import random
import re
import statistics
import subprocess

root = pathlib.Path(__file__).resolve().parent.parent
base = root.parent
out = root / "measurements"
media = pathlib.Path.home() / "workprojects/videos in mp3/CasuallyFinance"

def read(path):
    with path.open(newline="") as source:
        return list(csv.DictReader(source))

def write(path, rows):
    with path.open("w", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def quantiles(values):
    return [round(v, 4) for v in statistics.quantiles(values, n=4, method="inclusive")]

raw = read(base / "COVERAGE_MATRIX.csv")
hashes = dict(line.rstrip("\n").split("  ", 1)[::-1] for line in (out / "physical_sha256.txt").open())
groups = collections.Counter(hashes.values())
reference = pathlib.Path("research/visual-audit/CHANNEL_001_CasuallyFinance")
profiles = read(reference / "21_AUTO_MOTION_PROFILE_ALL_VIDEOS.csv") + read(reference / "22_IDLESS_MOTION_PROFILE.csv")
coverage, per_video, delays, durations = [], [], [], []
callout = re.compile(r"RED_ELLIPSE|RED_ARROW|RED_CIRCLE|HIGHLIGHT|UNDERLINE|RED_CROSS|RED_X|YELLOW", re.I)
evidence = re.compile(r"statista|EIA|SEC|NEWS|ARTICLE|HEADLINE|SCREENSHOT|SCREEN|DOC|_IMG|IMG_|CHART|NEWSPAPER|REPORT|TWEET|REDDIT|FORUM|PAGE|PHOTO|LOGO|STOCK_CARD|TABLE|WEBSITE", re.I)

def tags(state):
    assets = state["asset_ids"].split(";")
    return (any(evidence.search(a) and not callout.search(a) for a in assets),
            any(callout.search(a) for a in assets))

for row in raw:
    file = media / row["title"]
    digest = hashes.get(str(file), "")
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
        "stream=width,height,avg_frame_rate,duration", "-of", "json", file
    ]))["streams"][0]
    fmt = "long" if probe["width"] > probe["height"] else "short"
    ws = pathlib.Path(row["evidence"].split(";")[0])
    manifest = ws / "source_manifest.json"
    identity = json.loads(manifest.read_text()) if manifest.is_file() else {}
    video = identity.get("video_id", row["source_id"])
    shot_file, state_file = ws / "shot_ledger.csv", ws / "visual_states.csv"
    if not state_file.is_file():
        state_file = next((p for key in (video, digest[:8])
                           if (p := base / "MULTI_VIDEO_MEASUREMENTS" / f"states_{key}.csv").is_file()),
                          state_file)
    shots = read(shot_file) if shot_file.is_file() else []
    states = read(state_file) if state_file.is_file() else []
    asr = sorted((ws / "audio").glob("*small_en.json"))
    level = {"L3v":"visual gate reported", "L2":"partial state measurement",
             "L1":"coarse motion / structural evidence", "L0":"inventory"}[row["level"]]
    if state_file.is_file() and row["level"] == "L1":
        level = "partial state measurement and ledger" if shots else "partial state measurement"
    if video == "gG239LrksH4":
        level = "unfinished workspace / structural evidence"
    if asr:
        level += "; ASR available, alignment provisional"
    coverage.append(dict(source_id=video, inventory_id=row["source_id"], filename=file.name, sha256=digest,
                         manifest_match=digest == row["sha256"], byte_copies=groups[digest],
                         format=fmt, width=probe["width"], height=probe["height"],
                         fps=probe["avg_frame_rate"], duration=probe.get("duration", ""), canonical_level=row["level"],
                         audit_category=level, shot_rows=len(shots), state_rows=len(states),
                         artifact=str(state_file) if state_file.is_file() else row["evidence"], asr_file=str(asr[0]) if asr else ""))
    if fmt != "long" or not asr or row["level"] != "L3v":
        continue
    flags = [tags(state) for state in states]
    spans = [(float(s["start_pts_seconds"]), float(s["end_pts_seconds"])) for s in states]
    for i, (ev, _) in enumerate(flags):
        if ev:
            index = next((j for j in range(i + 1, min(i + 6, len(states))) if flags[j][1]), None)
            delays.append(dict(video=video, evidence_state=states[i]["visual_state_id"],
                               evidence_assets=states[i]["asset_ids"], start=spans[i][0],
                               following_state=states[index]["visual_state_id"] if index is not None else "",
                               following_assets=states[index]["asset_ids"] if index is not None else "",
                               delay=round(spans[index][0] - spans[i][0], 2) if index is not None else ""))
    segments = json.loads(asr[0].read_text())["segments"]
    sentences, pending = [], []
    for segment in segments:
        for word in segment.get("words", []):
            pending.append(word)
            if len(pending) >= 4 and word["word"].strip().endswith((".", "?", "!")):
                sentences.append(pending)
                pending = []
    if pending:
        sentences.append(pending)
    stats = collections.Counter()
    for sentence in sentences:
        sentence_text = "".join(word["word"] for word in sentence)
        number = bool(re.search(r"\d|percent|million|billion|trillion|dollar", sentence_text, re.I))
        overlap = [f for f, (start, end) in zip(flags, spans)
                   if start < sentence[-1]["end"] and end > sentence[0]["start"]]
        subtype = "num" if number else "other"
        stats[subtype] += 1
        stats[subtype + "_ev"] += any(f[0] for f in overlap)
        stats[subtype + "_call"] += any(f[1] for f in overlap)
        stats["no_overlap"] += not overlap
    lengths = [float(s["end_pts_seconds"]) - float(s["start_pts_seconds"]) for s in shots]
    durations.extend(lengths)
    per_video.append(dict(video=video, **{k: stats[k] for k in (
        "num", "other", "num_ev", "other_ev", "num_call", "other_call", "no_overlap")},
        missing_word_segments=sum(not s.get("words") for s in segments), shots=len(shots),
        shot_median=round(statistics.median(lengths), 4),
        cuts_per_min=round((len(shots) - 1) * 60 / float(probe["duration"]), 4)))

write(root / "02_COVERAGE_RECONCILIATION.csv", coverage)
write(out / "per_video.csv", per_video)
write(out / "lag_pairs.csv", delays)
values = [r["delay"] for r in delays if r["delay"] != ""]
summary = dict(files=len(coverage), unique_hashes=len(groups),
               hashes_matching=sum(r["manifest_match"] for r in coverage),
               profile_table_rows=len(profiles),
               shot_rows=sum(r["shot_rows"] for r in coverage),
               lag=dict(eligible=len(delays), matches=len(values), videos=len({r["video"] for r in delays if r["delay"] != ""}),
                        minimum=min(values), quartiles=quantiles(values), maximum=max(values)),
               long_shots=dict(n=len(durations), quartiles=quantiles(durations), maximum=max(durations)))
rng = random.Random(103)
for key in ("ev", "call"):
    def lifts(rows):
        n, m = [sum(r[k] for r in rows) for k in ("num", "other")]
        a, b = [sum(r[k + "_" + key] for r in rows) for k in ("num", "other")]
        return (a / n) / ((a + b) / (n + m)), (a / n) / (b / m)
    sims = list(zip(*(lifts(rng.choices(per_video, k=len(per_video))) for _ in range(5000))))
    summary[key] = dict(lifts=lifts(per_video),
                        bootstrap_95=[[round(x, 4) for x in statistics.quantiles(s, n=40, method="inclusive")[1::36]] for s in sims],
                        leave_one_out=[list(map(min, zip(*(lifts(per_video[:i] + per_video[i + 1:]) for i in range(len(per_video)))))),
                                       list(map(max, zip(*(lifts(per_video[:i] + per_video[i + 1:]) for i in range(len(per_video))))))])
print(json.dumps(summary, indent=2))
