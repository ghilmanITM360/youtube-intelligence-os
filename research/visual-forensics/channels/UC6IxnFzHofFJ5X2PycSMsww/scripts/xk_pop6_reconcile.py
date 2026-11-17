"""Reconcile Pop-6 per-video tables against pop6_quant.csv, loudness_pop6.txt and source hashes. Independent recompute from videos/<id>/tables+evidence.
Writes campaign/pop6_per_video_summary.csv and campaign/POP6_RECONCILIATION.json. Usage: python3 -I xk_pop6_reconcile.py <ws>"""
import csv, json, re, hashlib, statistics as st, sys, pathlib
W = pathlib.Path(sys.argv[1]); ids = json.load(open(W / "selection/selection_v6_pop6.json"))["long_pop6"]
quant = {(r["video_id"], r["rule"]): r for r in csv.DictReader(open(W / "campaign/pop6_quant.csv"))}
loud = dict(re.match(r"(\S+)\s+I:\s*(-?[\d.]+) LUFS", x).groups() for x in open(W / "campaign/loudness_pop6.txt").read().strip().split("|") if x.strip())
sh = json.load(open(W / "campaign/source_hashes_all_2026-11-06.json"))
rows, issues = [], []
for v in ids:
    V = W / "videos" / v; S = list(csv.DictReader(open(V / "tables/segments_v1.csv"))); N = sum(int(s["frames"]) for s in S)
    acts = [s for s in S if s["kind"] == "ACTIVITY"]; holds = [int(s["frames"]) / 24 for s in S if s["kind"] == "HOLD"]
    if [int(s["start_frame"]) for s in S][0] != 0 or any(int(S[i]["start_frame"]) != int(S[i-1]["end_frame"]) + 1 for i in range(1, len(S))): issues.append((v, "segments not contiguous"))
    fp = json.load(open(V / "evidence/ffprobe_full.json")); vs = next(s for s in fp["streams"] if s["codec_type"] == "video")
    nbf = int(vs.get("nb_frames", N)); 
    if nbf != N: issues.append((v, f"frames {N} != ffprobe nb_frames {nbf}"))
    eb = re.search(r"I:\s*(-?[\d.]+) LUFS", (V / "evidence/ebur128.txt").read_text()); lu = eb.group(1) if eb else None
    if lu != loud.get(v): issues.append((v, f"LUFS ebur128 {lu} != loudness_pop6 {loud.get(v)}"))
    rec = (V / "evidence/source_sha256.txt").read_text().split()[0]; p = pathlib.Path((V / "evidence/source_path.txt").read_text().strip())
    real = hashlib.sha256(p.read_bytes()).hexdigest()
    if not (rec == sh[v]["sha256"] == real): issues.append((v, f"sha mismatch rec={rec[:8]} json={sh[v]['sha256'][:8]} disk={real[:8]}"))
    if p.stat().st_size != sh[v]["bytes"]: issues.append((v, "bytes mismatch"))
    calc = dict(Q1=str(round(len(acts) / (N / 24) * 60, 1)), Q3=str(round(st.median(holds), 2)), Q4=str(round(sum(int(s["frames"]) for s in acts) / N, 3)),
                Q5=f"{vs['width']}x{vs['height']} {vs['r_frame_rate']}", Q6=lu, Q7=f"{S[-1]['kind']} {S[-1]['frames']}f")
    for q, x in calc.items():
        if str(quant[(v, q)]["value"]) != str(x): issues.append((v, f"{q} csv {quant[(v, q)]['value']} != recomputed {x}"))
    rows.append(dict(video_id=v, frames=N, duration_s=round(N / 24, 2), segments=len(S), activities=len(acts), holds=len(holds), **{f"{q}_value": calc[q] for q in calc},
                     **{f"{q}_result": quant[(v, q)]["result"] for q in calc}, source_sha256=real, source_bytes=p.stat().st_size))
w = csv.DictWriter(open(W / "campaign/pop6_per_video_summary.csv", "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
tot = sum(1 for r in quant.values() if r["result"] == "PASS"); n = len(quant)
rec = dict(videos=len(ids), quant_rows=n, quant_pass=tot, issues=issues, status="RECONCILED" if not issues and (tot, n) == (116, 120) else "MISMATCH")
(W / "campaign/POP6_RECONCILIATION.json").write_text(json.dumps(rec, indent=1)); print(json.dumps(rec))
