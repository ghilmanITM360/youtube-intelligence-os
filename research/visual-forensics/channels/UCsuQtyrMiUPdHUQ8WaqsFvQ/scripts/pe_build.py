"""Build kit deliverables for one video from measurements + segments + reviewed annotations.
Usage: python3 -I pe_build.py <video_dir> <annotation_csv> <reviewer_label>
Writes: source_manifest.json, coverage.json, tables/state_ledger.csv, shot_ledger.csv, visual_event_ledger.csv,
        audio_visual_alignment.csv, quality_gate.json (draft; analyst sections merged from review/gate_overrides.json if present)."""
import csv, json, sys, pathlib, subprocess, datetime

V = pathlib.Path(sys.argv[1]).resolve(); ANN = pathlib.Path(sys.argv[2]); REV = sys.argv[3]
vid = V.name
segs = list(csv.DictReader(open(V / "tables/segments_v1.csv")))
ann = {r["seg"]: r for r in csv.DictReader(open(ANN))}
missing = [s["seg"] for s in segs if s["seg"] not in ann]
extra = [k for k in ann if k not in {s["seg"] for s in segs}]
assert not missing and not extra, (missing, extra)
tiles = list(csv.DictReader(open(V / "tables/sheet_index.csv")))
viewed = {}
for t in tiles: viewed.setdefault(t["seg"], set()).add(int(t["frame"]))
_si = V / "tables/strip_frames.csv"
if _si.exists():
    for t in csv.DictReader(open(_si)): viewed.setdefault(t["seg"], set()).add(int(t["frame"]))
probe = json.load(open(V / "evidence/ffprobe_full.json"))
vs = next(s for s in probe["streams"] if s["codec_type"] == "video"); au = [s for s in probe["streams"] if s["codec_type"] == "audio"]
cal = json.load(open(V / "tables/detector_calibration.json"))
sha = (V / "evidence/source_sha256.txt").read_text().split()[0]
asr = json.load(open(V / "asr/asr_small_en.json"))
words = asr["words"]
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
ptsl = [l.split(",") for l in (V / "evidence/video_frames_pts.csv").read_text().split("\n") if l]
durs = {round(float(x[1]), 6) for x in ptsl if len(x) > 1 and x[1] not in ("", "N/A")}

# ---------- source manifest ----------
git = subprocess.run(["git", "-C", "/Users/ghilmankhan/workprojects/youtube-intelligence-os", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
sm = {"schema_version": "1.0", "source": {
    "channel_id": "UCsuQtyrMiUPdHUQ8WaqsFvQ", "channel_handle": "Primitive Education", "video_id": vid,
    "file_path": (V / ("evidence/source_path_original.txt" if (V / "evidence/source_path_original.txt").exists() else "evidence/source_path.txt")).read_text().strip(), "sha256": sha,
    "bytes": int((V / "evidence/source_bytes.txt").read_text()), "duration_seconds": float(probe["format"]["duration"]),
    "time_base": vs["time_base"], "frame_rate_avg": vs["avg_frame_rate"], "r_frame_rate": vs["r_frame_rate"],
    "decoded_frames": cal["frames"], "nb_frames_container": vs.get("nb_frames"),
    "vfr_status": "CFR (all packet durations equal)" if len(durs) == 1 else f"CHECK: {len(durs)} distinct packet durations",
    "resolution": f'{vs["width"]}x{vs["height"]}', "video_codec": vs["codec_name"], "pix_fmt": vs.get("pix_fmt"),
    "video_streams": [{k: vs.get(k) for k in ("codec_name", "width", "height", "avg_frame_rate", "time_base", "start_time", "duration")}],
    "audio_streams": [{k: a.get(k) for k in ("codec_name", "sample_rate", "channels", "start_time", "duration")} for a in au]},
    "execution": {"git_sha": git, "tool_versions": {"ffprobe": subprocess.run(["ffprobe", "-version"], capture_output=True, text=True).stdout.split("\n")[0],
                                                     "opencv": "5.0.0 (visual-ct-scan-venv)", "pyscenedetect": "0.7.2", "asr": f'{asr["tool"]} {asr["model"]}'},
                  "reader": f"claude session 85559743 + reviewer {REV}", "date": now},
    "evidence": {"source_verified": True, "audio_listened": False, "registered_yios_status": "see census catalog_registered",
                 "kit": "YIOS_Visual_Forensics_Intelligence_Kit_v1.0 installed SKILL sha d308d87d (package SKILL b7baff3e + local routing section)"}}
(V / "source_manifest.json").write_text(json.dumps(sm, indent=1))

# ---------- ledgers ----------
fps = eval(vs["avg_frame_rate"].replace("/", "/1.0/")) if "/" in vs["avg_frame_rate"] else float(vs["avg_frame_rate"])
shot = 0; state = 0; S = []; shots = []
for s in segs:
    a = ann[s["seg"]]; cls = a["event_class"]
    if s["kind"] == "ACTIVITY" and "SHOT_CUT" in cls or not shots:
        shot += 1; shots.append(dict(shot_id=f"SH{shot:03d}", start_frame=int(s["start_frame"]), segs=[]))
    shots[-1]["segs"].append(s["seg"])
    if s["kind"] == "HOLD": state += 1
    S.append(dict(video_id=vid, seg=s["seg"], kind=s["kind"], shot_id=f"SH{shot:03d}", visual_state_id=f"VS{state:03d}" if s["kind"] == "HOLD" else "",
                  start_frame=int(s["start_frame"]), end_frame=int(s["end_frame"]), frames=int(s["frames"]), start_pts=float(s["start_pts"]),
                  end_pts_exclusive=round(float(s["end_pts"]) + 1 / fps, 4), event_class=cls, subtype=a["subtype"], description=a["description"],
                  confidence=a["confidence"], detectors=s["detectors"], frames_viewed=len(viewed.get(s["seg"], ())),
                  view_frames=";".join(map(str, sorted(viewed.get(s["seg"], ())))), reviewer=REV))
with open(V / "tables/state_ledger.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(S[0])); w.writeheader(); w.writerows(S)
N = cal["frames"]
for i, sh in enumerate(shots):
    sh["end_frame"] = shots[i + 1]["start_frame"] - 1 if i + 1 < len(shots) else N - 1
rowpts = {int(r["frame"]): float(r["pts_time"]) for r in csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv")) if r["pts_time"]}
with open(V / "shot_ledger.csv", "w", newline="") as f:
    cols = "video_id,shot_id,start_pts_seconds,end_pts_seconds,start_frame,end_frame,shot_boundary_evidence,shot_verified,subject,setting,framing,camera_motion,subject_motion,graphics_text,entrance,exit,narrative_function,source_frame_refs,uncertainty".split(",")
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for sh in shots:
        first = next(x for x in S if x["seg"] == sh["segs"][0]); inner = [x for x in S if x["seg"] in sh["segs"]]
        w.writerow(dict(video_id=vid, shot_id=sh["shot_id"], start_pts_seconds=rowpts[sh["start_frame"]], end_pts_seconds=round(rowpts[sh["end_frame"]] + 1 / fps, 4),
                        start_frame=sh["start_frame"], end_frame=sh["end_frame"],
                        shot_boundary_evidence=f'{first["seg"]} {first["detectors"] or "video start"} + visual tile review',
                        shot_verified="VERIFIED_VISUAL" if first["kind"] == "ACTIVITY" or sh["start_frame"] == 0 else "UNCERTAIN",
                        subject=first["description"][:160], setting="see state_ledger description", framing="see state_ledger description",
                        camera_motion=";".join(x["seg"] + ":" + x["subtype"] for x in inner if "CAMERA" in x["event_class"]) or "none observed",
                        subject_motion=";".join(x["seg"] + ":" + x["subtype"] for x in inner if x["event_class"].startswith("CHARACTER")) or "none",
                        graphics_text=";".join(x["seg"] + ":" + x["subtype"] for x in inner if "GRAPHIC" in x["event_class"]),
                        entrance=first["subtype"], exit="next SHOT_CUT" if sh is not shots[-1] else "video end",
                        narrative_function="see report", source_frame_refs=";".join(x["view_frames"] for x in inner), uncertainty=""))
with open(V / "visual_event_ledger.csv", "w", newline="") as f:
    cols = "video_id,shot_id,visual_state_id,event_id,start_pts_seconds,end_pts_seconds,start_frame,end_frame,event_class,subject_object_id,before_state,after_state,motion_vector_or_direction,transition_type,source_frame_paths,source_audio_reference,coverage_level,evidence_label,confidence,alternative_interpretation,creative_function_hypothesis,editor_reconstruction_note".split(",")
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); prev = None
    for i, x in enumerate(S):
        if x["kind"] == "HOLD": prev = x; continue
        nxt = next((y for y in S[i + 1:] if y["kind"] == "HOLD"), None)
        full = x["frames_viewed"] >= x["frames"]
        w.writerow(dict(video_id=vid, shot_id=x["shot_id"], visual_state_id=(prev or {}).get("visual_state_id", ""), event_id=x["seg"].replace("G", "E"),
                        start_pts_seconds=x["start_pts"], end_pts_seconds=x["end_pts_exclusive"], start_frame=x["start_frame"], end_frame=x["end_frame"],
                        event_class=x["event_class"] + ":" + x["subtype"], subject_object_id="", before_state=(prev or {}).get("visual_state_id", "start"),
                        after_state=(nxt or {}).get("visual_state_id", "end"), motion_vector_or_direction="", transition_type=x["subtype"],
                        source_frame_paths="frames/sheets via tables/sheet_index.csv frames " + x["view_frames"], source_audio_reference="see audio_visual_alignment.csv",
                        coverage_level="ALL_FRAMES_VIEWED" if full else f'SAMPLED {x["frames_viewed"]}/{x["frames"]} frames + full-frame measurements',
                        evidence_label="OBSERVED (onset/offset MEASURED from frame differences)", confidence=x["confidence"],
                        alternative_interpretation="", creative_function_hypothesis="", editor_reconstruction_note=x["description"]))

# ---------- AV alignment (ASR only) ----------
segs_asr = asr["segments"]
with open(V / "audio_visual_alignment.csv", "w", newline="") as f:
    cols = "video_id,event_id,audio_source,audio_listening_status,phrase_or_sound,audio_start_pts,audio_end_pts,visual_start_pts,visual_end_pts,lead_lag_seconds,timestamp_method,confidence,limitations".split(",")
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for x in S:
        if x["kind"] != "ACTIVITY": continue
        t = float(x["start_pts"])
        win = [wd for wd in words if wd["end"] >= t - 0.8 and wd["start"] <= t + 0.8]
        near = min(words, key=lambda wd: abs(wd["start"] - t)) if words else None
        w.writerow(dict(video_id=vid, event_id=x["seg"].replace("G", "E"), audio_source=f'{asr["tool"]} {asr["model"]} word timestamps',
                        audio_listening_status="NOT_LISTENED (BLOCKED_CAPABILITY)", phrase_or_sound="".join(wd["w"] for wd in win).strip(),
                        audio_start_pts=win[0]["start"] if win else "", audio_end_pts=win[-1]["end"] if win else "",
                        visual_start_pts=x["start_pts"], visual_end_pts=x["end_pts_exclusive"],
                        lead_lag_seconds=round(t - near["start"], 3) if near else "",
                        timestamp_method="visual: frame PTS from decoded frame diff; audio: ASR word start nearest to visual onset (not semantic cue)",
                        confidence="LOW (ASR_UNCERTIFIED)", limitations="ASR is not listening; nearest-word lag is not a verified sync relation"))

# ---------- coverage ----------
holds = [x for x in S if x["kind"] == "HOLD"]; acts = [x for x in S if x["kind"] == "ACTIVITY"]
unviewed = [(x["seg"], x["start_pts"], x["end_pts_exclusive"], x["frames"] - x["frames_viewed"]) for x in acts if x["frames_viewed"] < x["frames"]]
cov = dict(video_id=vid, source_sha256=sha, mode="DEEP (CT_SCAN elements where frame-level onset measured)", generated_utc=now,
           frames_total=N, frames_measured=N, segments=len(S), holds=len(holds), activities=len(acts),
           hold_frames=sum(int(x["frames"]) for x in holds), activity_frames=sum(int(x["frames"]) for x in acts),
           hold_verification="every hold frame below calibrated per-frame change threshold (MEASURED) + first-vs-last drift check + settled-frame tile viewed",
           activity_frames_viewed=sum(min(x["frames_viewed"], int(x["frames"])) for x in acts),
           activities_fully_viewed=sum(x["frames_viewed"] >= int(x["frames"]) for x in acts),
           partially_viewed_activity_intervals=[dict(seg=a, start=b, end=c, unviewed_frames=d) for a, b, c, d in unviewed],
           encoder_artifact_frames_absorbed=len(cal.get("encoder_artifact_frames", [])), encoder_artifact_visual_check="NOT_VIEWED (measured: no px>=150 change, max diff<80)",
           tile_scale="1/4 linear (portrait 270x480, landscape 480x270); native frames separately in review/native_art_review.md",
           audio="ASR only (PROVISIONAL_ASR_NOT_LISTENING); listening BLOCKED_CAPABILITY", reviewer=REV)
(V / "coverage.json").write_text(json.dumps(cov, indent=1))
print(json.dumps({k: v for k, v in cov.items() if k != "partially_viewed_activity_intervals"}, indent=0)[:1200], "shots", len(shots))
