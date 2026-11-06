"""Dependency-aware hash manifest of LOCAL-ONLY assets (never published to Git). Same-Mac storage != off-device backup.
Classes: SOURCE_VIDEO, DERIVED_IMAGE (frames/sheets/strips/review sheets), RENDER_VIDEO, LOCAL_TEXT (per-frame tables, ASR transcripts, logs), AUDIT_TRANSCRIPT.
depends_on names what must exist to regenerate/verify the asset. Writes campaign/LOCAL_ONLY_MANIFEST.csv + _summary.json. Usage: python3 -I xk_local_manifest.py <ws>"""
import csv, json, hashlib, pathlib, sys, collections, datetime
W = pathlib.Path(sys.argv[1]); rows = []
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def add(p, cls, dep, note=""):
    rows.append(dict(path=str(p.relative_to(W)) if str(p).startswith(str(W)) else str(p), sha256=h(p), bytes=p.stat().st_size, cls=cls, depends_on=dep, published="no", note=note))
sh = json.load(open(W / "campaign/source_hashes_all_2026-11-06.json"))
for v in sorted((W / "videos").iterdir()):
    sp = v / "evidence/source_path.txt"
    if sp.exists():
        p = pathlib.Path(sp.read_text().strip())
        if p.exists(): add(p, "SOURCE_VIDEO", "original download; ground truth for everything under videos/%s" % v.name, "outside workspace: ~/Downloads/videos in mp3/xkcd Channel")
    for q in sorted(v.rglob("*")):
        if not q.is_file(): continue
        r = q.relative_to(v).as_posix()
        if q.suffix in (".png", ".jpg"): add(q, "DERIVED_IMAGE", f"videos/{v.name}/evidence/source_sha256.txt + scripts/xk_sheets.py|xk_strip.py")
        elif r in ("tables/FULL_FRAME_MEASUREMENTS.csv", "evidence/video_frames_pts.csv") or r.startswith("asr/asr_small_en") or r.startswith("asr/asr_run") or r.startswith("evidence/log_") or r in ("evidence/source_path.txt", "evidence/source_bytes.txt"):
            add(q, "LOCAL_TEXT", f"videos/{v.name}/evidence/source_sha256.txt")
for q in sorted((W / "reconstruction").rglob("*")):
    if q.is_file() and q.suffix in (".mp4", ".png", ".jpg"):
        att = q.parts[len(W.parts) + 2] if len(q.parts) > len(W.parts) + 2 else ""
        add(q, "RENDER_VIDEO" if q.suffix == ".mp4" else "DERIVED_IMAGE", f"reconstruction/{q.parts[len(W.parts)+1]}/{att}/make_rt4.py (published) + criteria sha", "editable source = make_rt4.py")
for q in sorted((W / "campaign/strip_review").rglob("*.jpg")): add(q, "DERIVED_IMAGE", "strip_tasks*.csv")
T = pathlib.Path.home() / ".claude/projects/-Users-ghilmankhan-workprojects-youtube-intelligence-os/ea35c26f-d3c8-4777-8262-12a97339279d/subagents"
for a, role in (("ab1971717b35ac971", "strip_rv2 reviewer transcript (image-read audit evidence)"), ("a99333735515f1c47", "RT4 attempt_1 worker transcript (self-reported reads not audited)")):
    if (T / f"agent-{a}.jsonl").exists(): add(T / f"agent-{a}.jsonl", "AUDIT_TRANSCRIPT", role, "outside workspace; may be rotated by Claude Code")
w = csv.DictWriter(open(W / "campaign/LOCAL_ONLY_MANIFEST.csv", "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
c = collections.Counter(r["cls"] for r in rows)
summ = dict(generated_utc=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), entries=len(rows), by_class=dict(c), total_bytes=sum(r["bytes"] for r in rows),
            backup_status="SAME_MAC_ONLY: no off-device copy verified; this manifest is hashes only, not a backup", source_hash_records=len(sh))
(W / "campaign/LOCAL_ONLY_MANIFEST_summary.json").write_text(json.dumps(summ, indent=1)); print(json.dumps(summ))
