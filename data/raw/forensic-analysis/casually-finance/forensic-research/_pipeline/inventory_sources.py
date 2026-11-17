"""Phase B (part 1): read-only inventory of every candidate local media file.

Sources scanned (never modified): loose '* - Casual Finance (*).mp4' files in ~/Downloads and every .mp4 inside CasuallyFinance.zip.
Zip-only entries are extracted ONLY to the scratch work dir (read-only analysis copy) so ffmpeg can seek them.
Usage: python3 -B inventory_sources.py <OUT_DIR> <WORK_DIR>
"""
import csv, hashlib, json, re, subprocess, sys, zipfile, zlib
from pathlib import Path

DL = Path("/Users/ghilmankhan/Downloads")
ZIP = DL / "CasuallyFinance.zip"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()


def crc32(p):
    c = 0
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): c = zlib.crc32(b, c)
    return c & 0xFFFFFFFF


def probe(p):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(p)], capture_output=True, text=True).stdout or "{}")
    v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), {})
    a = [s for s in j.get("streams", []) if s.get("codec_type") == "audio"]
    num, den = (v.get("avg_frame_rate") or "0/1").split("/")
    fps = round(float(num) / float(den), 3) if float(den) else None
    w, h = v.get("width"), v.get("height")
    return dict(duration_sec=round(float(j.get("format", {}).get("duration", 0)), 3), width=w, height=h, fps=fps,
                video_codec=v.get("codec_name"), audio_codec=(a[0].get("codec_name") if a else None), audio_tracks=len(a),
                audio_channels=(a[0].get("channels") if a else None), audio_sample_rate=(a[0].get("sample_rate") if a else None),
                aspect_ratio=(f"{w}:{h}" if w else None), orientation=("VERTICAL_9x16" if w and h and h > w else "HORIZONTAL_16x9" if w else None),
                bit_rate=j.get("format", {}).get("bit_rate"), nb_frames=v.get("nb_frames"))


def decode_check(p):
    r = subprocess.run(["ffmpeg", "-nostats", "-v", "error", "-i", str(p), "-f", "null", "-", "-progress", "pipe:1"], capture_output=True, text=True)
    outs = [l for l in r.stdout.splitlines() if l.startswith("out_time_us=")]
    dec = round(int(outs[-1].split("=")[1]) / 1e6, 3) if outs else None
    errs = [l for l in r.stderr.splitlines() if l.strip()]
    return dict(decode_rc=r.returncode, decoded_duration_sec=dec, decode_error_lines=len(errs), decode_error_sample=(errs[0][:160] if errs else ""))


def title_of(name):
    t = re.sub(r"\.mp4$", "", name)
    t = re.sub(r"\s*\(\d+\)$", "", t)
    t = re.sub(r" - Casual Finance \(\d+p, h264\)$", "", t)
    return t


def main(out_dir, work_dir):
    out_dir, work_dir = Path(out_dir), Path(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    zf = zipfile.ZipFile(ZIP)
    zipinfo = {Path(i.filename).name: i for i in zf.infolist() if i.filename.endswith(".mp4") and not i.filename.startswith("__MACOSX")}
    rows = []
    loose = sorted(DL.glob("* - Casual Finance (*).mp4"))
    loose_names = set()
    for p in loose:
        loose_names.add(p.name)
        # zip names mangle non-ASCII (’ -> ???); compare by size+crc instead of name
        crc = crc32(p)
        zmatch = [n for n, i in zipinfo.items() if i.CRC == crc and i.file_size == p.stat().st_size]
        rows.append(dict(origin="LOOSE_IN_DOWNLOADS", path=str(p), filename=p.name, title_from_filename=title_of(p.name), size_bytes=p.stat().st_size,
                         crc32=f"{crc:08x}", zip_entry_match=";".join(zmatch) or "NONE"))
    matched_zip = {r["zip_entry_match"] for r in rows}
    for n, i in zipinfo.items():
        if any(n in m.split(";") for m in matched_zip): continue
        dest = work_dir / "zip_only" / n
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(i) as s, open(dest, "wb") as d: d.write(s.read())
        crc = crc32(dest)
        rows.append(dict(origin="ZIP_ONLY_EXTRACTED_TO_WORKDIR", path=str(dest), filename=n, title_from_filename=title_of(n), size_bytes=dest.stat().st_size,
                         crc32=f"{crc:08x}", zip_entry_match=f"{n} (crc_zip={i.CRC:08x}, match={crc == i.CRC})"))
    for r in rows:
        r["sha256"] = sha256(r["path"])
        r.update(probe(r["path"]))
        r.update(decode_check(r["path"]))
        print(r["filename"][:60], r["duration_sec"], r["width"], r["height"], r["decode_rc"], r["decoded_duration_sec"], flush=True)
    # SHA duplicates
    by = {}
    for r in rows: by.setdefault(r["sha256"], []).append(r["filename"])
    for r in rows: r["duplicate_of_sha"] = ";".join(x for x in by[r["sha256"]] if x != r["filename"])
    cols = list(rows[0].keys())
    for r in rows:
        for c in r:
            if c not in cols: cols.append(c)
    with open(out_dir / "00_MANIFEST" / "SOURCE_FILES_raw.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    print("rows", len(rows))


if __name__ == "__main__":
    main(*sys.argv[1:3])
