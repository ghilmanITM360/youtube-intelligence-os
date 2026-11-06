"""Isolated restore test: export the published commit (git archive, no clone or checkout), lay the hashed local-only rows on top, verify, then list what the live workspace holds that a restore would lose.
Usage: python3 -I pe_restore_test.py restore <root> <commit> <label>
       python3 -I pe_restore_test.py compare <root> <label>
Read-only on the live workspace except writing campaign/restore_test_<label>_*. Text receipts only."""
import csv, hashlib, json, os, pathlib, re, shutil, subprocess, sys
WS = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; REPO = "/Users/ghilmankhan/workprojects/youtube-intelligence-os"
PREFIX = "research/visual-forensics/channels/UCsuQtyrMiUPdHUQ8WaqsFvQ"
C = WS / "campaign"
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def manifest_rows(name):
    return [r for r in csv.reader(open(C / name), delimiter="\t") if len(r) == 4 and r[0] != "category" and not r[0].startswith("#")]

def restore(root, commit, label):
    R = root / "restored"; R.mkdir(parents=True)
    a = subprocess.Popen(["git", "archive", commit, PREFIX], cwd=REPO, stdout=subprocess.PIPE)
    subprocess.check_call(["tar", "-x", "--strip-components=4", "-C", str(R)], stdin=a.stdout); assert a.wait() == 0
    git_files = {str(p.relative_to(R)) for p in R.rglob("*") if p.is_file()}
    media = [f for f in git_files if f.endswith((".mp4", ".wav", ".jpg", ".png"))]
    seal = next(iter(sorted(R.glob("campaign/EVIDENCE_SHA256SUMS_M.txt"))))
    final = json.load(open(C / "PUBLICATION_M_FINAL.json"))
    rows = []; seal_lines = seal.read_text().splitlines()
    for l in seal_lines:
        h, f = l.split("  ", 1); p = R / f
        rows.append(("GIT_SEAL", f, p.stat().st_size if p.exists() else "", h, sha(p) if p.exists() else "", "OK" if p.exists() and sha(p) == h else "FAIL"))
    # Local-only rows are copied from the live path and checked against the hash the manifest recorded.
    for name in ("LOCAL_ONLY_PRESERVATION_MANIFEST.txt", "LOCAL_ONLY_PRESERVATION_SUPPLEMENT_K.txt"):
        for cat, path, size, h in manifest_rows(name):
            p = pathlib.Path(path)
            rel = str(p.relative_to(WS)) if p.is_relative_to(WS) else "_external/" + p.name
            d = R / rel
            if not p.exists():
                rows.append((cat, rel, "", h, "", "MISSING")); continue
            now = sha(p)
            if d.exists() and rel in git_files:
                st = "IN_GIT_SAME" if sha(d) == h else "IN_GIT_NEWER"
            else:
                d.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, d)
                st = "OK" if sha(d) == h else "DRIFT_SINCE_MANIFEST"
            rows.append((cat, rel, p.stat().st_size, h, now, st))
    w = csv.writer(open(C / f"restore_test_{label}_files.csv", "w", newline="")); w.writerow(("layer", "path", "bytes", "expected_sha256", "actual_sha256", "status")); w.writerows(rows)
    # What a restore from Git + both manifests would lose today.
    restored = {str(p.relative_to(R)) for p in R.rglob("*") if p.is_file()}
    lost = []
    for p in WS.rglob("*"):
        rel = str(p.relative_to(WS))
        if p.is_file() and rel not in restored and not rel.startswith(".pe_writer_lock") and "restore_test_" not in rel:
            lost.append((rel, p.stat().st_size, sha(p)))
    w = csv.writer(open(C / f"restore_test_{label}_uncovered.csv", "w", newline="")); w.writerow(("path", "bytes", "sha256")); w.writerows(sorted(lost))
    count = {}
    for r in rows: count[(r[0], r[5])] = count.get((r[0], r[5]), 0) + 1
    print(json.dumps(dict(commit=commit, git_files=len(git_files), media_in_git=len(media), seal_lines=len(seal_lines), seal_sha_matches_final=sha(seal) == final["seal_sha256"],
                          status={f"{a}/{b}": n for (a, b), n in sorted(count.items())}, restored_files=len(restored), restored_bytes=sum((R / f).stat().st_size for f in restored), uncovered_files=len(lost), uncovered_bytes=sum(l[1] for l in lost)), indent=1))

# Paths and run-time fields that legitimately differ; everything else must match byte for byte.
def normal(b, root):
    t = b.decode("utf-8", "replace")
    t = t.replace(str(root / "rbhome/YIOS-local-audits/primitive-education"), "<WS>").replace(str(WS), "<WS>")
    t = re.sub(r'"[^"\n]*(?:/source_media/|/srcshim/|PrimitiveEducation-MP4/)[^"\n]*"', '"<SRC>"', t)
    t = re.sub(r"\S*(?:/source_media/|/srcshim/)\S*", "<SRC>", t); t = re.sub(r"/Users/\S*PrimitiveEducation-MP4/[^\n]*", "<SRC>", t); t = re.sub(r"[^\n]*srcshim/[^\n]*", "<SRC>", t)
    t = re.sub(r'"runtime_s": [\d.]+', '"runtime_s": 0', t)
    return t

def compare(root, label):
    B = root / "rbhome/YIOS-local-audits/primitive-education/videos"; rows = []
    SKIP = (".jpg", ".png")  # image bytes are compared too, but counted apart below
    for v in sorted(p for p in (WS / "videos").iterdir() if p.is_dir()):
        names = {str(p.relative_to(v)) for p in v.rglob("*") if p.is_file()} | {str(p.relative_to(B / v.name)) for p in (B / v.name).rglob("*") if p.is_file()}
        for n in sorted(names):
            a, b = v / n, B / v.name / n
            if not b.exists(): st = "NOT_REBUILT"
            elif not a.exists(): st = "ONLY_IN_REBUILD"
            elif sha(a) == sha(b): st = "IDENTICAL"
            elif not n.endswith(SKIP) and normal(a.read_bytes(), root) == normal(b.read_bytes(), root): st = "IDENTICAL_AFTER_PATHS"
            else: st = "DIFFERENT"
            rows.append((v.name, n, st))
    w = csv.writer(open(C / f"restore_test_{label}_rebuild.csv", "w", newline="")); w.writerow(("video", "path", "status")); w.writerows(rows)
    c = {}
    for _, n, st in rows:
        key = (re.sub(r"(frames/[^/]+)/.*", r"\1/*", re.sub(r"review/rv1_[^/]+", "review/rv1", n)), st); c[key] = c.get(key, 0) + 1
    print(json.dumps({f"{st} {k}": n for (k, st), n in sorted(c.items(), key=lambda x: (x[0][1], x[0][0]))}, indent=0))

if __name__ == "__main__":
    if sys.argv[1] == "restore": restore(pathlib.Path(sys.argv[2]), sys.argv[3], sys.argv[4])
    else: compare(pathlib.Path(sys.argv[2]), sys.argv[3])
