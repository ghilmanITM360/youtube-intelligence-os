#!/usr/bin/env python3
"""Casual Finance (@CasuallyFinance) complete video inventory + local download tracker.

Metadata-only: reads yt-dlp JSON receipts (never downloads media), scans local media
folder + ZIP read-only, ffprobes/hashes them, matches to video IDs, writes XLSX/CSV/JSON.

usage: build_inventory.py --enum DIR --prior DIR --media DIR --zip FILE --out DIR
  enum  : dir with videos.jsonl, shorts.jsonl (yt-dlp --flat-playlist) and full/<id>.json
  prior : dir with the Oct-11 forensic metadata (all-videos-metadata.csv, SOURCE_FILES.csv) - optional
"""
import argparse, csv, datetime as dt, hashlib, json, os, re, subprocess, tempfile, zipfile, unicodedata
from pathlib import Path
import xlsxwriter

CHANNEL_ID = "UCrNfRFWnLC3tCy1TnyhVQ7g"
CHANNEL_NAME = "Casual Finance"
CHANNEL_URL = "https://www.youtube.com/@CasuallyFinance"
DUR_TOL = 2.0  # seconds, local ffprobe duration vs YouTube metadata
NA, UNK = "NOT_AVAILABLE", "UNKNOWN"
NOW = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(p)],
                       capture_output=True, text=True)
    if r.returncode:
        return None, r.stderr.strip()[:200]
    j = json.loads(r.stdout)
    v = next((s for s in j["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), None)
    return dict(
        duration=float(j["format"].get("duration", 0)), vcodec=v and v["codec_name"], acodec=a and a["codec_name"],
        w=v and v.get("width"), h=v and v.get("height"),
        fps=v and round(eval(v["avg_frame_rate"]), 2) if v and v.get("avg_frame_rate", "0/0") != "0/0" else None,
    ), None


def decode_ok(p):
    """full decode to null; returns (ok, error_line_count)"""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-f", "null", "-"], capture_output=True, text=True)
    return r.returncode == 0 and not r.stderr.strip(), len(r.stderr.splitlines())


def norm(s):
    s = unicodedata.normalize("NFKD", s).lower()
    s = re.sub(r"[‘’'`]", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return s.strip()


def local_stem(name):
    s = re.sub(r"\.(mp4|mov|mkv|webm|m4v)$", "", name, flags=re.I)
    s = re.sub(r"-SnapYT\.App$", "", s)
    s = re.sub(r" - Casual Finance \((\d+p), h264\)( \(\d+\))?$", "", s)
    s = re.sub(r" \(\d+\)$", "", s)
    return s


def hhmm(sec):
    if sec is None:
        return UNK
    return f"{int(sec)//3600:02d}:{(int(sec)%3600)//60:02d}"


def hms(sec):
    return UNK if sec is None else f"{int(sec)//3600:02d}:{(int(sec)%3600)//60:02d}:{int(sec)%60:02d}"


def main():
    ap = argparse.ArgumentParser()
    for a in ("enum", "prior", "media", "zip", "out"):
        ap.add_argument("--" + a, required=a != "prior")
    A = ap.parse_args()
    enum, out, media, zpath = Path(A.enum), Path(A.out), Path(A.media), Path(A.zip)
    out.mkdir(parents=True, exist_ok=True)

    # ---------- immutability baseline for source files ----------
    src_before = {str(p): (p.stat().st_size, int(p.stat().st_mtime)) for p in list(media.iterdir()) + [zpath]}

    # ---------- 1. channel population ----------
    tab_of, enum_errors = {}, []
    for tab in ("videos", "shorts"):
        for l in open(enum / f"{tab}.jsonl"):
            d = json.loads(l)
            tab_of[d["id"]] = tab
    vids = {}
    for vid, tab in tab_of.items():
        f = enum / "full" / f"{vid}.json"
        if f.exists() and f.stat().st_size:
            d = json.JSONDecoder().raw_decode(f.read_text())[0]  # first object only
            d["_retrieved"] = dt.datetime.fromtimestamp(f.stat().st_mtime, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            vids[vid] = d
        else:
            err = (enum / "full" / f"{vid}.err")
            enum_errors.append((vid, err.read_text()[:200] if err.exists() else "no response"))

    prior_ids = {}
    if A.prior:
        pr = Path(A.prior)
        for r in csv.DictReader(open(pr / "all-videos-metadata.csv")):
            prior_ids[r["video_id"]] = r
        prior_src = {r["sha256"]: r for r in csv.DictReader(open(pr / "SOURCE_FILES.csv"))}
    else:
        prior_src = {}

    # ---------- 2. local media scan ----------
    exts = {".mp4", ".mov", ".mkv", ".webm", ".m4v"}
    files = []  # dict per local media file / zip entry
    work = Path(tempfile.mkdtemp(prefix="cf_zip_"))
    for p in sorted(media.iterdir()):
        if p.suffix.lower() in exts:
            files.append(dict(kind="FOLDER", path=p, name=p.name, zip=None, entry=None))
    with zipfile.ZipFile(zpath) as z:
        for zi in z.infolist():
            if zi.filename.startswith("__MACOSX") or zi.is_dir() or Path(zi.filename).suffix.lower() not in exts:
                continue
            tgt = work / re.sub(r"[^\w.-]", "_", zi.filename)
            with z.open(zi) as s, open(tgt, "wb") as d:
                d.write(s.read())
            files.append(dict(kind="ZIP", path=tgt, name=Path(zi.filename).name, zip=zpath.name, entry=zi.filename, crc=zi.CRC))
    for f in files:
        f["size"] = f["path"].stat().st_size
        f["sha"] = sha256(f["path"])
        f["probe"], f["probe_err"] = probe(f["path"])
        f["decode_ok"], f["decode_errs"] = decode_ok(f["path"]) if f["probe"] else (False, -1)
        f["rel"] = f"Downloads/CasuallyFinance/{f['name']}" if f["kind"] == "FOLDER" else f"Downloads/{zpath.name}!{f['entry']}"

    # ---------- 3. match ----------
    title_norm = {v: norm(d["title"]) for v, d in vids.items()}
    for f in files:
        stem = norm(local_stem(f["name"]))
        f["stem"] = stem
        dur = f["probe"]["duration"] if f["probe"] else None
        cands = []
        for v, tn in title_norm.items():
            exact = stem == tn
            prefix = (not exact) and len(stem) >= 8 and tn.startswith(stem)
            if (exact or prefix) and dur is not None and abs(vids[v]["duration"] - dur) <= DUR_TOL:
                cands.append((v, "TITLE_EXACT+DURATION" if exact else "TITLE_PREFIX+DURATION"))
        # sha reuse from prior verified manifest
        prior = prior_src.get(f["sha"])
        f["prior_id"] = prior and prior.get("verified_youtube_id")
        if f["prior_id"] and f["prior_id"] in vids and f["prior_id"] not in [c[0] for c in cands]:
            cands = [(f["prior_id"], "PRIOR_SHA256_VERIFIED_ID")]
        elif f["prior_id"] and f["prior_id"] in [c[0] for c in cands]:
            cands = [(f["prior_id"], "PRIOR_SHA256_VERIFIED_ID+TITLE+DURATION")]
        f["cands"] = cands
        if len(cands) == 1:
            f["vid"], f["method"] = cands[0]
        else:
            f["vid"], f["method"] = None, ("AMBIGUOUS" if cands else "NO_MATCH")

    # group by sha (identical bytes, e.g. folder file + zip copy)
    by_sha = {}
    for f in files:
        by_sha.setdefault(f["sha"], []).append(f)
    for f in files:
        f["same_bytes"] = len(by_sha[f["sha"]])

    per_vid = {}
    for f in files:
        if f["vid"]:
            per_vid.setdefault(f["vid"], []).append(f)

    # ---------- 4. rows ----------
    def pick_primary(fs):
        ok = [x for x in fs if x["probe"] and x["probe"]["vcodec"] and x["decode_ok"]]
        ok.sort(key=lambda x: (x["kind"] != "FOLDER", -(x["probe"]["h"] or 0), -x["size"]))
        return ok[0] if ok else sorted(fs, key=lambda x: x["kind"] != "FOLDER")[0]

    rows = []
    for vid, d in sorted(vids.items(), key=lambda kv: (-(kv[1].get("timestamp") or 0), kv[0])):
        tab = tab_of[vid]
        vtype = "LIVESTREAM" if (d.get("was_live") or d.get("live_status") not in (None, "not_live")) else ("SHORT" if tab == "shorts" else "VIDEO")
        ts = d.get("timestamp")
        t = dt.datetime.fromtimestamp(ts, dt.timezone.utc) if ts else None
        fs = per_vid.get(vid, [])
        status, notes, miss = "NOT_DOWNLOADED", "", []
        prim = None
        if fs:
            prim = pick_primary(fs)
            valid = prim["probe"] and prim["probe"]["vcodec"] and prim["decode_ok"]
            if valid and prim["kind"] == "FOLDER":
                status = "DOWNLOADED_VERIFIED"
            elif valid:
                status = "ZIP_ONLY_VERIFIED"
            else:
                status = "FOUND_UNVERIFIED"
        elif d.get("availability") not in (None, "public"):
            status = "UNAVAILABLE_SOURCE"
        avail = (d.get("availability") or UNK).upper()
        if status == "NOT_DOWNLOADED":
            notes = "No local media matched by ID/title+duration in scanned scope. Acquisition requires separate authorization."
        elif status in ("DOWNLOADED_VERIFIED", "ZIP_ONLY_VERIFIED"):
            notes = f"Identity via {prim['method']}; {len(fs)} local file(s) for this video."
        thumb = d.get("thumbnail") or (d["thumbnails"][-1]["url"] if d.get("thumbnails") else NA)
        thumb = f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" if False else thumb
        m = {k: d.get(k) for k in ("description", "tags", "categories", "language", "like_count", "comment_count", "view_count")}
        for k, v in m.items():
            if v in (None, "", []):
                miss.append(k)
        if not t:
            miss.append("upload_time")
        row = {
            "Channel Name": CHANNEL_NAME, "Channel ID": CHANNEL_ID, "Video ID": vid,
            "Video Title": d["title"], "YouTube Video URL": f"https://www.youtube.com/watch?v={vid}",
            "Channel URL": CHANNEL_URL, "Video Type": vtype,
            "Upload Date": t.strftime("%Y-%m-%d") if t else (d.get("upload_date") or UNK),
            "Upload Time (UTC)": t.strftime("%H:%M:%S") if t else NA,
            "Duration (HH:MM)": hhmm(d.get("duration")), "Views": d.get("view_count"), "Likes": d.get("like_count"),
            "Comments": d.get("comment_count"), "Description": d.get("description") or NA,
            "Tags/Keywords": "; ".join(d.get("tags") or []) or NA, "Category": "; ".join(d.get("categories") or []) or NA,
            "Language": d.get("language") or UNK, "Thumbnail URL": thumb, "Thumbnail File Path": NA,
            "Transcript Available (Yes/No/Unknown)": "No", "Transcript Language": NA, "Transcript File Path": NA,
            "Download Status": status,
            "Local Video File Name": prim["name"] if prim else NA,
            "Local Video File Path": prim["rel"] if prim else NA,
            "ZIP/Archive Name": next((x["zip"] for x in fs if x["zip"]), NA),
            "Archive Entry Path": next((x["entry"] for x in fs if x["entry"]), NA),
            "File Extension": prim["path"].suffix.lower() if prim else NA,
            "File Size (MB)": round(prim["size"] / 1048576, 2) if prim else None,
            "Resolution": f"{prim['probe']['w']}x{prim['probe']['h']}" if prim and prim["probe"] else NA,
            "FPS": prim["probe"]["fps"] if prim and prim["probe"] else None,
            "Video Codec": prim["probe"]["vcodec"] if prim and prim["probe"] else NA,
            "Audio Codec": prim["probe"]["acodec"] if prim and prim["probe"] else NA,
            "SHA256": prim["sha"] if prim else NA,
            "File Verification Result": (f"ffprobe OK; full decode {'OK' if prim['decode_ok'] else 'ERRORS'}; local {prim['probe']['duration']:.1f}s vs YT {d['duration']}s" if prim and prim["probe"] else (NA if not prim else "ffprobe FAILED")),
            "Duplicate/Variant Count": len({x["sha"] for x in fs}) if fs else 0,
            "Video Availability": avail,
            "Metadata Source": "yt-dlp watch-page extraction (metadata only; tab enumeration + per-video)",
            "Metadata Retrieved At": d["_retrieved"], "Last Verified At": NOW,
            "Missing Information": ", ".join(miss) if miss else "None",
            "Notes/Action Required": notes,
            # extras
            "Duration (sec)": d.get("duration"), "Match Method": prim["method"] if prim else NA,
            "Source Tab": tab, "In Oct-11 Forensic Enumeration": "Yes" if vid in prior_ids else ("No" if prior_ids else UNK),
            "Transcript Note": f"YouTube auto-captions listed: {'yes' if d.get('automatic_captions') else 'no'}; no local transcript file in scanned scope",
        }
        rows.append(row)
    for i, r in enumerate(rows, 1):
        r["Serial Number"] = i

    # historical/unavailable: previously indexed but absent from current listing
    hist = [dict(video_id=v, title=r["title"], published_at=r["published_at"]) for v, r in prior_ids.items() if v not in vids]

    # missing-list priority by view percentile
    miss_rows = [r for r in rows if r["Download Status"] not in ("DOWNLOADED_VERIFIED", "ZIP_ONLY_VERIFIED")]
    vs = sorted((r["Views"] or 0) for r in miss_rows)
    q75 = vs[int(len(vs) * .75)] if vs else 0
    q25 = vs[int(len(vs) * .25)] if vs else 0
    for r in miss_rows:
        v = r["Views"] or 0
        r["_prio"] = "HIGH" if v >= q75 or r["Video Type"] == "VIDEO" else ("LOW" if v <= q25 else "MEDIUM")

    # unmatched / duplicates rows
    uni = []
    for f in files:
        role = None
        vid = f["vid"]
        if not vid:
            role = "UNMATCHED" if f["method"] == "NO_MATCH" else "MATCH_UNCERTAIN"
        else:
            prim = pick_primary(per_vid[vid])
            if f is prim:
                role = "PRIMARY_COPY_OF_ZIP" if f["same_bytes"] > 1 and f["kind"] == "FOLDER" else None
            else:
                role = "IDENTICAL_BYTES_DUPLICATE" if f["sha"] == prim["sha"] else "QUALITY/ENCODE_VARIANT"
        if role or f["same_bytes"] > 1:
            uni.append((f, role or "IDENTICAL_BYTES_DUPLICATE"))

    # ---------- 5. machine-readable ----------
    cols = ["Serial Number", "Channel Name", "Channel ID", "Video ID", "Video Title", "YouTube Video URL", "Channel URL", "Video Type", "Upload Date",
            "Upload Time (UTC)", "Duration (HH:MM)", "Views", "Likes", "Comments", "Description", "Tags/Keywords", "Category", "Language",
            "Thumbnail URL", "Thumbnail File Path", "Transcript Available (Yes/No/Unknown)", "Transcript Language", "Transcript File Path",
            "Download Status", "Local Video File Name", "Local Video File Path", "ZIP/Archive Name", "Archive Entry Path", "File Extension",
            "File Size (MB)", "Resolution", "FPS", "Video Codec", "Audio Codec", "SHA256", "File Verification Result", "Duplicate/Variant Count",
            "Video Availability", "Metadata Source", "Metadata Retrieved At", "Last Verified At", "Missing Information", "Notes/Action Required",
            "Duration (sec)", "Match Method", "Source Tab", "In Oct-11 Forensic Enumeration", "Transcript Note"]
    with open(out / "CASUALLY_FINANCE_VIDEO_INVENTORY.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    json.dump(dict(generated_at=NOW, channel_id=CHANNEL_ID, channel_url=CHANNEL_URL, count=len(rows),
                   enumeration_complete=not enum_errors, enumeration_errors=enum_errors,
                   historical_not_in_current_listing=hist,
                   videos=[{k: r[k] for k in cols} for r in rows]),
              open(out / "CASUALLY_FINANCE_VIDEO_INVENTORY.json", "w"), indent=1, ensure_ascii=False)
    with open(out / "metadata_receipt.jsonl", "w") as fh:  # compact source receipt (no formats/heatmap)
        for vid, d in vids.items():
            keep = {k: d.get(k) for k in ("id", "title", "description", "duration", "timestamp", "upload_date", "view_count", "like_count",
                                          "comment_count", "tags", "categories", "language", "availability", "live_status", "was_live",
                                          "media_type", "thumbnail", "channel_id", "webpage_url")}
            keep.update(tab=tab_of[vid], retrieved_at=d["_retrieved"])
            fh.write(json.dumps(keep, ensure_ascii=False) + "\n")
    local_rows = [dict(kind=f["kind"], rel=f["rel"], name=f["name"], size=f["size"], sha256=f["sha"], video_id=f["vid"] or "", method=f["method"],
                       duration=f["probe"]["duration"] if f["probe"] else None, res=f"{f['probe']['w']}x{f['probe']['h']}" if f["probe"] else "",
                       vcodec=f["probe"]["vcodec"] if f["probe"] else "", acodec=f["probe"]["acodec"] if f["probe"] else "",
                       decode_ok=f["decode_ok"], same_bytes=f["same_bytes"], prior_verified_id=f["prior_id"] or "") for f in files]
    with open(out / "LOCAL_MEDIA_SCAN.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, list(local_rows[0])); w.writeheader(); w.writerows(local_rows)

    # ---------- 6. workbook ----------
    wb = xlsxwriter.Workbook(out / "CASUALLY_FINANCE_COMPLETE_VIDEO_DOWNLOAD_INVENTORY.xlsx", {"strings_to_urls": False})
    F = lambda **k: wb.add_format({"font_name": "Calibri", "font_size": 10, "valign": "top", **k})
    hdr = F(bold=True, bg_color="#1F3864", font_color="white", text_wrap=True, border=1)
    wrap, plain = F(text_wrap=True), F()
    link = F(font_color="blue", underline=1)
    num, dec, big = F(num_format="#,##0"), F(num_format="0.00"), F(bold=True, font_size=20, align="center")
    title = F(bold=True, font_size=16, font_color="#1F3864")
    STAT = {"DOWNLOADED_VERIFIED": "#C6EFCE", "ZIP_ONLY_VERIFIED": "#DDEBF7", "NOT_DOWNLOADED": "#FFC7CE", "AUDIO_ONLY": "#FFEB9C",
            "TRANSCRIPT_ONLY": "#FFEB9C", "FOUND_UNVERIFIED": "#FFE699", "UNAVAILABLE_SOURCE": "#D9D9D9", "MATCH_UNCERTAIN": "#FFE699"}

    def table(ws, name, headers, data, widths, linkcols=(), numcols=(), deccols=(), wrapcols=(), start=0):
        n = len(data)
        for r, row in enumerate(data, start + 1):
            for c, h in enumerate(headers):
                v = row.get(h)
                if v is None:
                    ws.write_blank(r, c, None, plain) if False else ws.write(r, c, "", plain)
                elif c in linkcols and isinstance(v, str) and v.startswith("http"):
                    ws.write_url(r, c, v, link, v)
                elif c in numcols and isinstance(v, (int, float)):
                    ws.write_number(r, c, v, num)
                elif c in deccols and isinstance(v, (int, float)):
                    ws.write_number(r, c, v, dec)
                else:
                    ws.write(r, c, str(v)[:32000] if isinstance(v, str) else v, wrap if c in wrapcols else plain)
        ws.add_table(start, 0, start + max(n, 1), len(headers) - 1,
                     {"name": name, "style": "Table Style Medium 2", "columns": [{"header": h, "header_format": hdr} for h in headers]})
        for c, wd in enumerate(widths):
            ws.set_column(c, c, wd)
        ws.set_row(start, 32)
        ws.freeze_panes(start + 1, 2)

    # --- Sheet 1 dashboard (created first, filled after ALL VIDEOS exists) ---
    dash = wb.add_worksheet("DASHBOARD")
    wsA = wb.add_worksheet("ALL VIDEOS")
    allcols = cols[:43]
    widths = [8, 14, 26, 14, 42, 38, 30, 11, 11, 10, 9, 11, 9, 9, 50, 30, 12, 9, 38, 14, 12, 12, 14, 22, 38, 42, 18, 40, 9, 9, 11, 8, 9, 9, 22, 40, 9, 12, 28, 20, 20, 24, 40]
    table(wsA, "tblAll", allcols, rows, widths, linkcols=(5, 6, 18), numcols=(11, 12, 13), deccols=(29,), wrapcols=(4, 14, 15, 35, 41, 42))
    extra = ["Duration (sec)", "Match Method", "Source Tab", "In Oct-11 Forensic Enumeration"]
    for i, h in enumerate(extra):  # extras outside the table, to the right
        wsA.write(0, 43 + i, h, hdr)
        for r, row in enumerate(rows, 1):
            wsA.write(r, 43 + i, row[h], plain)
        wsA.set_column(43 + i, 43 + i, 16)
    wsA.conditional_format(1, 23, len(rows), 23, {"type": "no_blanks", "format": F()})
    for s, colr in STAT.items():
        wsA.conditional_format(1, 23, len(rows), 23, {"type": "cell", "criteria": "==", "value": f'"{s}"', "format": wb.add_format({"bg_color": colr})})
    for c in (19, 22, 26, 27, 34):
        wsA.conditional_format(1, c, len(rows), c, {"type": "cell", "criteria": "==", "value": f'"{NA}"', "format": wb.add_format({"font_color": "#999999", "italic": True})})

    # --- Sheet 3 downloaded ---
    wsD = wb.add_worksheet("DOWNLOADED VIDEOS")
    dl = [r for r in rows if r["Download Status"] in ("DOWNLOADED_VERIFIED", "ZIP_ONLY_VERIFIED")]
    dh = ["Serial Number", "Video ID", "Video Title", "YouTube Video URL", "Video Type", "Download Status", "Local Video File Name", "Local Video File Path",
          "ZIP/Archive Name", "Archive Entry Path", "File Size (MB)", "Resolution", "FPS", "Video Codec", "Audio Codec", "Duration (HH:MM)",
          "SHA256", "File Verification Result", "Match Method", "Duplicate/Variant Count"]
    table(wsD, "tblDownloaded", dh, dl, [8, 14, 42, 38, 11, 22, 38, 42, 18, 40, 9, 11, 7, 9, 9, 9, 22, 40, 24, 10], linkcols=(3,), deccols=(10,), wrapcols=(2, 6, 7, 9, 17))

    # --- Sheet 4 missing ---
    wsM = wb.add_worksheet("MISSING VIDEOS")
    mh = ["Video ID", "Video Title", "YouTube Video URL", "Video Type", "Duration (HH:MM)", "Duration (sec)", "Upload Date", "Views", "Thumbnail URL",
          "Download Status", "Reason Missing", "Video Availability", "Acquisition Priority", "Action Required"]
    md = []
    for r in miss_rows:
        md.append({**r, "Reason Missing": "No local media matched (ID/title+duration) in scanned folder or ZIP" if r["Download Status"] == "NOT_DOWNLOADED" else r["Download Status"],
                   "Acquisition Priority": r["_prio"], "Action Required": "Acquire only after owner authorization; then re-run inventory script"})
    md.sort(key=lambda r: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}[r["Acquisition Priority"]], -(r["Views"] or 0)))
    table(wsM, "tblMissing", mh, md, [14, 42, 38, 11, 9, 9, 11, 11, 38, 20, 40, 12, 11, 40], linkcols=(2, 8), numcols=(7,), wrapcols=(1, 10, 13))
    wsM.conditional_format(1, 12, len(md), 12, {"type": "cell", "criteria": "==", "value": '"HIGH"', "format": wb.add_format({"bg_color": "#F8CBAD"})})

    # --- Sheet 5 unmatched & duplicates ---
    wsU = wb.add_worksheet("UNMATCHED & DUPLICATES")
    uh = ["Role", "Local File Name", "Local Path", "ZIP/Archive Entry", "Matched Video ID", "Match Method", "File Size (MB)", "Resolution", "Duration (sec)", "SHA256", "Identical-Bytes Count", "Decode OK", "Note"]
    ud = []
    for f, role in uni:
        note = {"UNMATCHED": "No title+duration candidate; manual identification needed",
                "MATCH_UNCERTAIN": "Multiple candidate videos; manual verification needed",
                "IDENTICAL_BYTES_DUPLICATE": "Same SHA256 as another local file (e.g. folder file and ZIP copy); counted once",
                "PRIMARY_COPY_OF_ZIP": "Primary file; a byte-identical copy also exists in ZIP",
                "QUALITY/ENCODE_VARIANT": "Different bytes for the same video ID (alternate quality/encode)"}[role]
        ud.append({"Role": role, "Local File Name": f["name"], "Local Path": f["rel"], "ZIP/Archive Entry": f["entry"] or "", "Matched Video ID": f["vid"] or "",
                   "Match Method": f["method"], "File Size (MB)": round(f["size"] / 1048576, 2),
                   "Resolution": f"{f['probe']['w']}x{f['probe']['h']}" if f["probe"] else "", "Duration (sec)": round(f["probe"]["duration"], 2) if f["probe"] else None,
                   "SHA256": f["sha"], "Identical-Bytes Count": f["same_bytes"], "Decode OK": "Yes" if f["decode_ok"] else "No", "Note": note})
    ud.sort(key=lambda r: (r["Role"], r["Local File Name"]))
    table(wsU, "tblUnmatched", uh, ud, [26, 44, 50, 44, 14, 28, 9, 11, 10, 22, 10, 8, 50], deccols=(6, 8), wrapcols=(1, 2, 3, 12))

    # --- Sheet 6 sources ---
    wsS = wb.add_worksheet("SOURCES & VERIFICATION")
    srows = [
        ("Channel", f"{CHANNEL_NAME} {CHANNEL_URL} ({CHANNEL_ID})", "Registry: data/manifests/YOUTUBE_CHANNEL_TARGETS.csv (added target, identity VERIFIED 2026-09-14). NOT Casual Economics / Casually Explained."),
        ("Enumeration", "yt-dlp --flat-playlist on /videos and /shorts tabs; /streams tab returned 'channel does not have a streams tab'", f"Retrieved {NOW[:10]}; yt-dlp pagination to exhaustion; {len(vids)} of {len(tab_of)} IDs got full metadata; {len(enum_errors)} failures."),
        ("Per-video metadata", "yt-dlp --skip-download --dump-json per ID", "Receipt: metadata_receipt.jsonl. Likes/comments/views are YouTube values at retrieval time."),
        ("Prior enumeration", "branch codex/casually-finance-forensic-research, Oct-11 snapshot (206 IDs)", f"{len(prior_ids)} prior IDs; {len(hist)} absent from current listing; {len([v for v in vids if v not in prior_ids])} new since Oct-11."),
        ("Prior verified media", "same branch SOURCE_FILES.csv (sha256 + verified_youtube_id)", "Used as extra identity evidence when SHA256 matches."),
        ("Local folder scanned", str(media), f"{sum(1 for f in files if f['kind']=='FOLDER')} media files; read-only."),
        ("ZIP scanned", str(zpath), f"{sum(1 for f in files if f['kind']=='ZIP')} media entries; __MACOSX resource forks ignored; entries extracted to temp for ffprobe/hash only."),
        ("Not available locally", "/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research (Oct-11 workdir)", "Path referenced in repo inventory; does not exist on this machine. Only its committed branch copy was used."),
        ("Identity method", "Local filenames carry NO YouTube ID. Match = normalized title (exact, or truncated SnapYT prefix >=8 chars) AND ffprobe duration within ±2s of YouTube duration; prior SHA256-verified ID takes precedence.", "Title-only matches are never accepted. This is strong but not cryptographic proof; ID not embedded in files."),
        ("Validation", "ffprobe (streams/format) + full ffmpeg decode to null + SHA256", "FOUND_UNVERIFIED if probe/decode fails."),
        ("Transcripts/thumbnails", "Searched scanned scope only", "No local transcript/thumbnail files for these videos were registered; fields set NOT_AVAILABLE / Transcript=No."),
        ("Duration column", "Spec asked HH:MM; Shorts would all read 00:00, so Duration (sec) is added to the right of the table", ""),
        ("Priority rule", "HIGH = long-form VIDEO or views >= 75th pct of missing; LOW = <= 25th pct; else MEDIUM", ""),
        ("Limitations", "Likes/comments/views change; unlisted/private/members-only videos cannot be enumerated from public tabs; count is the PUBLIC accessible population.", f"Enumeration {'COMPLETE for public tabs' if not enum_errors else 'INCOMPLETE'}."),
    ]
    for e in enum_errors:
        srows.append(("Failed request", e[0], e[1]))
    for h in hist:
        srows.append(("Historical (prior-indexed, not in current listing)", h["video_id"], h["title"]))
    sh = ["Item", "Source / Method", "Detail"]
    table(wsS, "tblSources", sh, [dict(zip(sh, r)) for r in srows], [28, 80, 90], wrapcols=(0, 1, 2))

    # --- dashboard ---
    dash.hide_gridlines(2); dash.set_column(0, 0, 38); dash.set_column(1, 4, 16)
    dash.write(0, 0, f"{CHANNEL_NAME} - Video Download Inventory", title)
    dash.write(1, 0, f"{CHANNEL_URL} | channel {CHANNEL_ID} | generated {NOW} | public tabs enumeration {'complete' if not enum_errors else 'INCOMPLETE'}", F(italic=True))
    N = len(rows)
    cnt = lambda s: sum(1 for r in rows if r["Download Status"] == s)
    A_ = "tblAll[Download Status]"
    items = [("Total discovered channel videos", f"=ROWS(tblAll[Video ID])", N)]
    for s in ("DOWNLOADED_VERIFIED", "ZIP_ONLY_VERIFIED", "NOT_DOWNLOADED", "AUDIO_ONLY", "TRANSCRIPT_ONLY", "FOUND_UNVERIFIED", "MATCH_UNCERTAIN", "UNAVAILABLE_SOURCE"):
        items.append((s, f'=COUNTIF({A_},"{s}")', cnt(s)))
    r0 = 3
    dash.write(r0, 0, "Metric", hdr); dash.write(r0, 1, "Count", hdr); dash.write(r0, 2, "% of total", hdr)
    for i, (lab, fm, v) in enumerate(items, r0 + 1):
        dash.write(i, 0, lab, F(bold=i == r0 + 1)); dash.write_formula(i, 1, fm, num, v)
        dash.write_formula(i, 2, f"=B{i+1}/$B${r0+2}", F(num_format="0.0%"), v / N)
    dl_n = cnt("DOWNLOADED_VERIFIED") + cnt("ZIP_ONLY_VERIFIED")
    r = r0 + len(items) + 2
    dash.write(r, 0, "Download completion % (verified + ZIP-only)", F(bold=True))
    dash.write_formula(r, 1, f'=(COUNTIF({A_},"DOWNLOADED_VERIFIED")+COUNTIF({A_},"ZIP_ONLY_VERIFIED"))/ROWS(tblAll[Video ID])', F(num_format="0.0%", bold=True), dl_n / N)
    dash.conditional_format(r, 1, r, 1, {"type": "data_bar", "bar_color": "#63BE7B", "min_type": "num", "min_value": 0, "max_type": "num", "max_value": 1})
    cells = N * len(("Description", "Tags/Keywords", "Category", "Language", "Views", "Likes", "Comments", "Upload Date", "Duration (HH:MM)", "Thumbnail URL"))
    have = sum(1 for rr in rows for k in ("Description", "Tags/Keywords", "Category", "Language", "Views", "Likes", "Comments", "Upload Date", "Duration (HH:MM)", "Thumbnail URL")
               if rr[k] not in (None, "", NA, UNK))
    dash.write(r + 1, 0, "Metadata completeness % (10 core fields, YouTube-sourced)", F(bold=True))
    dash.write_number(r + 1, 1, have / cells, F(num_format="0.0%", bold=True))
    dash.conditional_format(r + 1, 1, r + 1, 1, {"type": "data_bar", "bar_color": "#5B9BD5", "min_type": "num", "min_value": 0, "max_type": "num", "max_value": 1})
    rt = r + 3
    dash.write(rt, 0, "By video type", hdr); dash.write(rt, 1, "Total", hdr); dash.write(rt, 2, "Downloaded/ZIP", hdr); dash.write(rt, 3, "Missing", hdr)
    for i, ty in enumerate(("VIDEO", "SHORT", "LIVESTREAM"), rt + 1):
        tot = sum(1 for x in rows if x["Video Type"] == ty); got = sum(1 for x in rows if x["Video Type"] == ty and x["Download Status"] in ("DOWNLOADED_VERIFIED", "ZIP_ONLY_VERIFIED"))
        dash.write(i, 0, {"VIDEO": "Regular videos", "SHORT": "Shorts", "LIVESTREAM": "Livestreams"}[ty])
        dash.write_formula(i, 1, f'=COUNTIF(tblAll[Video Type],"{ty}")', num, tot)
        dash.write_formula(i, 2, f'=COUNTIFS(tblAll[Video Type],"{ty}",tblAll[Download Status],"DOWNLOADED_VERIFIED")+COUNTIFS(tblAll[Video Type],"{ty}",tblAll[Download Status],"ZIP_ONLY_VERIFIED")', num, got)
        dash.write_formula(i, 3, f"=B{i+1}-C{i+1}", num, tot - got)
    ch = wb.add_chart({"type": "pie"})
    ch.add_series({"name": "Status", "categories": ["DASHBOARD", r0 + 2, 0, r0 + 3, 0] if False else ["DASHBOARD", r0 + 2, 0, r0 + 4, 0],
                   "values": ["DASHBOARD", r0 + 2, 1, r0 + 4, 1], "data_labels": {"percentage": True},
                   "points": [{"fill": {"color": "#70AD47"}}, {"fill": {"color": "#5B9BD5"}}, {"fill": {"color": "#FF7C80"}}]})
    ch.set_title({"name": "Download status"}); ch.set_size({"width": 420, "height": 300})
    dash.insert_chart(r0, 5, ch)
    bc = wb.add_chart({"type": "column", "subtype": "stacked"})
    bc.add_series({"name": "Downloaded/ZIP", "categories": ["DASHBOARD", rt + 1, 0, rt + 3, 0], "values": ["DASHBOARD", rt + 1, 2, rt + 3, 2], "fill": {"color": "#70AD47"}})
    bc.add_series({"name": "Missing", "categories": ["DASHBOARD", rt + 1, 0, rt + 3, 0], "values": ["DASHBOARD", rt + 1, 3, rt + 3, 3], "fill": {"color": "#FF7C80"}})
    bc.set_title({"name": "Coverage by video type"}); bc.set_size({"width": 420, "height": 300})
    dash.insert_chart(rt, 5, bc)
    dash.write(rt + 6, 0, "Note: local files carry no YouTube ID; identity = exact/truncated title + duration (±2s). See SOURCES & VERIFICATION.", F(italic=True, text_wrap=True))
    wb.close()

    # ---------- 7. verification ----------
    src_after = {str(p): (p.stat().st_size, int(p.stat().st_mtime)) for p in list(media.iterdir()) + [zpath]}
    ids = [r["Video ID"] for r in rows]
    st = {}
    for r in rows:
        st[r["Download Status"]] = st.get(r["Download Status"], 0) + 1
    dl_ids = {r["Video ID"] for r in dl}; ms_ids = {r["Video ID"] for r in miss_rows}
    sha_to_vid = {}
    for r in dl:
        sha_to_vid.setdefault(r["SHA256"], set()).add(r["Video ID"])
    checks = {
        "unique_ids_equals_rows": len(set(ids)) == len(ids) == len(tab_of) - len(enum_errors),
        "status_counts_sum_to_total": sum(st.values()) == len(rows),
        "downloaded_missing_disjoint_and_exhaustive": not (dl_ids & ms_ids) and dl_ids | ms_ids == set(ids),
        "every_downloaded_has_valid_media": all(r["File Verification Result"].startswith("ffprobe OK; full decode OK") and len(r["SHA256"]) == 64 for r in dl),
        "urls_match_ids": all(r["YouTube Video URL"] == f"https://www.youtube.com/watch?v={r['Video ID']}" and re.fullmatch(r"[\w-]{11}", r["Video ID"]) for r in rows),
        "zip_copies_not_double_counted": all(len(v) == 1 for v in sha_to_vid.values()),
        "source_files_unmodified": src_before == src_after,
        "csv_json_row_parity": len(list(csv.DictReader(open(out / "CASUALLY_FINANCE_VIDEO_INVENTORY.csv", encoding="utf-8")))) == len(json.load(open(out / "CASUALLY_FINANCE_VIDEO_INVENTORY.json"))["videos"]) == len(rows),
    }
    rep = dict(generated_at=NOW, total=len(rows), status_counts=st, by_type={t: sum(1 for r in rows if r["Video Type"] == t) for t in ("VIDEO", "SHORT", "LIVESTREAM")},
               local_files=len(files), local_unmatched=sum(1 for f in files if not f["vid"]), metadata_pct=round(100 * have / cells, 2),
               download_pct=round(100 * dl_n / N, 2), enum_errors=enum_errors, historical_absent=hist, new_since_oct11=[v for v in vids if v not in prior_ids] if prior_ids else None,
               checks=checks)
    json.dump(rep, open(out / "VERIFICATION.json", "w"), indent=1)
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    main()
