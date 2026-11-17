"""Local source census: sha256, ffprobe, decoded frame count, display format, letterbox check. Usage: python3 -I pe_census.py"""
import csv, hashlib, json, pathlib, re, subprocess
SRC = pathlib.Path.home() / "Downloads/videos in mp3/PrimitiveEducation-MP4"
OUT = pathlib.Path.home() / "YIOS-local-audits/primitive-education/census"
REG = {r["video_id"]: r for r in csv.DictReader(open(pathlib.Path.home() / "YIOS-local-audits/2026-10-24-seven-channel-visual-forensics-readiness/03_CHANNEL_AND_VIDEO_METADATA_RECONCILIATION.csv")) if r["channel_folder"] == "PrimitiveEducation-MP4"}
rows = []
for p in sorted(SRC.iterdir()):
    if p.name.startswith(".") or not p.is_file(): continue
    m = re.search(r"\[([\w-]{11})\]", p.name); vid = m.group(1) if m else ""
    pr = json.loads(subprocess.run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(p)],capture_output=True,text=True).stdout or "{}")
    st = pr.get("streams", []); v = next((s for s in st if s["codec_type"]=="video"), None); a = next((s for s in st if s["codec_type"]=="audio"), None)
    row = dict(video_id=vid, file=p.name, bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest(), has_video=bool(v), has_audio=bool(a), duration=pr.get("format",{}).get("duration"))
    r = REG.get(vid, {})
    row.update(reg_title=r.get("title_registered",""), reg_published=r.get("published_registered",""), reg_type=r.get("video_type",""), reg_views=r.get("views_snapshot",""), reg_snapshot=r.get("snapshot_date",""), reg_dur=r.get("duration_registered_s",""), identity_class=r.get("identity_class","NOT_IN_REGISTRY"), transcript_status=r.get("transcript_status",""), prior_visual=r.get("visual_status",""))
    if v:
        rot = next((d.get("rotation") for d in v.get("side_data_list",[]) if "rotation" in d), 0)
        w, h = v["width"], v["height"]; dw, dh = (h, w) if abs(int(rot or 0))==90 else (w, h)
        dec = subprocess.run(["ffprobe","-v","error","-count_frames","-select_streams","v:0","-show_entries","stream=nb_read_frames","-of","csv=p=0",str(p)],capture_output=True,text=True)
        err = subprocess.run(["ffmpeg","-v","error","-i",str(p),"-map","0:v:0","-f","null","-"],capture_output=True,text=True).stderr
        # letterbox: crop detect over whole file (samples every ~1 s)
        cd = subprocess.run(["ffmpeg","-v","info","-i",str(p),"-vf","fps=1,cropdetect=limit=24:round=2:reset=0","-an","-f","null","-"],capture_output=True,text=True).stderr
        crops = re.findall(r"crop=(\d+:\d+:\d+:\d+)", cd)
        ar = dw/dh; fmt = "16:9" if abs(ar-16/9)<.02 else "9:16" if abs(ar-9/16)<.02 else "OTHER"
        row.update(codec=v["codec_name"], width=w, height=h, rotation=rot, sar=v.get("sample_aspect_ratio",""), dar=v.get("display_aspect_ratio",""), r_fps=v.get("r_frame_rate"), avg_fps=v.get("avg_frame_rate"), time_base=v.get("time_base"), decoded_frames=dec.stdout.strip().split(",")[0], decode_errors=len(err.splitlines()), displayed_format=fmt, cropdetect_last=crops[-1] if crops else "")
    else:
        row.update(displayed_format="AUDIO_ONLY")
    rows.append(row); print(vid, row["displayed_format"], row.get("width"), row.get("height"), row["duration"], flush=True)
fn = sorted({k for r in rows for k in r})
with open(OUT/"source_census.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=fn); w.writeheader(); w.writerows(rows)
reg_only = sorted(set(REG)-{r["video_id"] for r in rows})
sha = {}
for r in rows: sha.setdefault(r["sha256"],[]).append(r["video_id"])
summary = dict(files=len(rows), unique_ids=len({r["video_id"] for r in rows}), video=sum(r["has_video"] for r in rows), audio_only=[r["video_id"] for r in rows if not r["has_video"]], format_counts={k:sum(r["displayed_format"]==k for r in rows) for k in {r["displayed_format"] for r in rows}}, byte_duplicates=[v for v in sha.values() if len(v)>1], registry_ids_without_local=reg_only, decode_error_files=[r["video_id"] for r in rows if r.get("decode_errors")])
(OUT/"census_summary.json").write_text(json.dumps(summary,indent=1)); print(summary)
