"""Encoder-absorbed-frame audit: pict type, period, peak px/maxdiff. Writes tables/encoder_audit.json. Usage: python3 -I pe_enc_audit.py <video_dir>"""
import csv, json, sys, pathlib, statistics as st
V = pathlib.Path(sys.argv[1]); c = json.load(open(V / "tables/detector_calibration.json")); E = c["encoder_artifact_frames"]
M = {int(r["frame"]): r for r in csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv"))}
gaps = [b - a for a, b in zip(E, E[1:])]
o = dict(n=len(E), I=sum(M[f]["pict"] == "I" for f in E), median_gap=st.median(gaps) if gaps else None, max_px12=max((int(M[f]["px_diff_ge12"]) for f in E), default=0), max_maxdiff=max((int(M[f]["max_abs_diff"]) for f in E), default=0))
(V / "tables/encoder_audit.json").write_text(json.dumps(o)); print(V.name, o)
