#!/usr/bin/env python3
"""Add the artifact inventory to data/catalog/yios_canonical.db: every git-tracked file (path, kind, role, area, size, git blob sha)
and, where a file's path or text contains a known video_id / channel_id, a link row.

  python3 scripts/build_yios_artifact_inventory.py     # run after build_yios_canonical_db.py build

Links are MENTIONS, not claims: a file that contains a video id is shown as "mentions this video"; whether it analyses it is a
reader's call (AGENTS.md rules 5-6). Only exact ids already in the canonical DB match, so random words do not link. Files whose
content cannot be scanned (images, video, xlsx, oversized) can still link through an id in their path. Read-only on the repo."""
import gzip, os, re, sqlite3, subprocess, sys

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB = f"{R}/data/catalog/yios_canonical.db"
TEXT = {".json", ".jsonl", ".csv", ".tsv", ".md", ".txt", ".yaml", ".yml", ".srt", ".vtt", ".html", ".py", ".sql", ".mjs", ".js", ".ts"}
MAXB = 30_000_000
SKIP = ("/node_modules/", "/.venv/")
FORMAT = {".json": "json", ".jsonl": "jsonl", ".csv": "table", ".tsv": "table", ".xlsx": "table", ".md": "markdown", ".txt": "text",
          ".srt": "transcript", ".vtt": "transcript", ".jpg": "image", ".jpeg": "image", ".png": "image", ".svg": "image", ".webp": "image",
          ".mp4": "video", ".mov": "video", ".mp3": "audio", ".wav": "audio", ".py": "code", ".mjs": "code", ".js": "code", ".sh": "code",
          ".sql": "code", ".html": "html", ".docx": "document", ".pdf": "document", ".db": "database", ".gz": "archive", ".yaml": "config", ".yml": "config"}
ROLE = [  # first keyword found in the lowercase path wins; order matters
    ("transcript", "transcript"), ("thumbnail", "thumbnail"), ("what-if", "what-if study"), ("slop", "slop-risk gate"),
    ("forensic", "forensic analysis"), ("audit", "audit"), ("playbook", "playbook"), ("reanalysis", "reanalysis"),
    ("intelligence", "intelligence report"), ("report", "report"), ("analysis", "analysis"), ("manifest", "manifest"),
    ("/raw/", "raw evidence"), ("/extracted/", "extracted data"), ("productions/", "production"), ("research/", "research")]
VID = re.compile(r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{11}(?![A-Za-z0-9_-])")
CHN = re.compile(r"(?<![A-Za-z0-9_-])UC[A-Za-z0-9_-]{22}(?![A-Za-z0-9_-])")
SCHEMA = """
DROP TABLE IF EXISTS artifacts; DROP TABLE IF EXISTS artifact_links;
CREATE TABLE artifacts(path TEXT PRIMARY KEY, area TEXT, format TEXT, role TEXT, bytes INTEGER, git_blob TEXT, scanned INTEGER,
  videos_mentioned INTEGER, channels_mentioned INTEGER);
CREATE TABLE artifact_links(path TEXT, target_kind TEXT, target_id TEXT, via TEXT, mentions INTEGER, PRIMARY KEY(path, target_kind, target_id, via));
CREATE INDEX idx_links_target ON artifact_links(target_kind, target_id);
"""


def tracked():
    out = subprocess.run(["git", "-C", R, "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout.decode()
    for rec in out.split("\0"):
        if not rec: continue
        meta, path = rec.split("\t", 1)
        _, _, blob, size = meta.split()
        yield path, blob, int(size) if size != "-" else 0


def area(p):
    s = p.split("/")
    return "/".join(s[:2]) if s[0] in ("data", "research") and len(s) > 2 else s[0]


def role(p):
    low = "/" + p.lower()
    return next((r for k, r in ROLE if k in low), "other")


def text_of(path, size):
    ext = os.path.splitext(path)[1].lower()
    gz = ext == ".gz"
    if gz: ext = os.path.splitext(path[:-3])[1].lower()
    if ext not in TEXT or size > MAXB or size == 0: return None
    try:
        op = gzip.open if gz else open
        with op(f"{R}/{path}", "rt", encoding="utf-8", errors="ignore") as f: return f.read(MAXB)
    except (OSError, EOFError): return None


def main():
    db = sqlite3.connect(DB)
    db.executescript(SCHEMA)
    vids = {r[0] for r in db.execute("select video_id from videos")}
    chans = {r[0] for r in db.execute("select channel_id from channels")}
    n = 0
    for path, blob, size in tracked():
        if any(s in "/" + path for s in SKIP): continue
        ext = os.path.splitext(path)[1].lower()
        fmt = FORMAT.get(ext, "other")
        if ext == ".gz": fmt = FORMAT.get(os.path.splitext(path[:-3])[1].lower(), "archive") + "+gz"
        links = {}
        def add(kind, ids, via):
            for i in ids: links[(kind, i, via)] = links.get((kind, i, via), 0) + 1
        add("video", [t for t in VID.findall(path) if t in vids], "path")
        add("channel", [t for t in CHN.findall(path) if t in chans], "path")
        body = text_of(path, size)
        if body is not None:
            add("video", [t for t in VID.findall(body) if t in vids], "content")
            add("channel", [t for t in CHN.findall(body) if t in chans], "content")
        nv = len({k[1] for k in links if k[0] == "video"}); nc = len({k[1] for k in links if k[0] == "channel"})
        db.execute("insert into artifacts values(?,?,?,?,?,?,?,?,?)", (path, area(path), fmt, role(path), size, blob, int(body is not None), nv, nc))
        db.executemany("insert into artifact_links values(?,?,?,?,?)", [(path, k, i, v, c) for (k, i, v), c in links.items()])
        n += 1
    db.commit()
    q = lambda s: db.execute(s).fetchone()[0]
    print(f"artifacts {n}  linked-to-a-video {q('select count(*) from artifacts where videos_mentioned>0')}  "
          f"linked-to-a-channel {q('select count(*) from artifacts where channels_mentioned>0')}  links {q('select count(*) from artifact_links')}")


if __name__ == "__main__":
    if not os.path.exists(DB): sys.exit("build the canonical DB first: scripts/build_yios_canonical_db.py build")
    main()
