import os, subprocess, sys, tempfile, glob, json
REPO = "/Users/ghilmankhan/workprojects/youtube-intelligence-os"
AUD = os.path.expanduser("~/YIOS-local-audits")
PARENT = "7cba97ef38708e5f3cd23a69d4983dcc283da21c"
LIST = "/private/tmp/claude-501/-Users-ghilmankhan--claude-spares-spare-tC0PSh/92a64383-a56a-4972-8982-7352392eedaa/scratchpad/cf15_files.txt"
BASE = "research/visual-forensics/channels/casual-finance"
OK_EXT = {".md", ".json", ".csv", ".txt", ".py", ".log", ".tsv"}
OK_NOEXT = {"EVIDENCE_SHA256SUMS"}
entries = {}
for line in open(LIST):
    vid, rel = line.rstrip("\n").split("\t")
    wsdir = rel.split("/")[0]
    sub = rel[len(wsdir) + 1:]
    entries[f"{BASE}/{vid}/visual_ct_scan_20261108/{sub}"] = os.path.join(AUD, rel)
# EVIDENCE_SHA256SUMS files (no extension) per workspace
for vid in open(LIST).read().split("\n"):
    pass
vids = sorted({l.split("\t")[0] for l in open(LIST) if l.strip()})
for vid in vids:
    ws = glob.glob(os.path.join(AUD, f"*-{vid}-deep-ct-scan"))[0]
    for fn in os.listdir(ws):
        if fn in OK_NOEXT and os.path.isfile(os.path.join(ws, fn)):
            entries[f"{BASE}/{vid}/visual_ct_scan_20261108/{fn}"] = os.path.join(ws, fn)
M = os.path.join(AUD, "CASUALLY_FINANCE_35_VIDEO_TARGET_20261104")
for fn in ["visual_complete_ledger.json", "count_complete.py", "working_list_15_v1.json", "MILESTONE_15_CHECKPOINT.md"]:
    entries[f"{BASE}/_visual_milestone_15/{fn}"] = os.path.join(M, fn)
for p in sorted(glob.glob(os.path.join(AUD, "tooling/cf15/*.py"))):
    entries[f"{BASE}/_visual_milestone_15/tooling_cf15/{os.path.basename(p)}"] = p

# guards
bad = []
for t, p in entries.items():
    ext = os.path.splitext(t)[1].lower()
    name = os.path.basename(t)
    if not os.path.isfile(p) or os.path.islink(p): bad.append(("notfile", t))
    elif not (ext in OK_EXT or name in OK_NOEXT): bad.append(("ext", t))
    elif os.path.getsize(p) > 4_000_000: bad.append(("big", t))
    elif "/frames/" in p or "/audio/" in p and ext not in (".json", ".log", ".txt"): bad.append(("dir", t))
if bad:
    print("GUARD_FAIL", bad[:10]); sys.exit(1)
exist = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", PARENT, BASE], capture_output=True, text=True).stdout.split("\n")
over = [t for t in entries if t in set(exist)]
if over:
    print("WOULD_OVERWRITE", over[:10]); sys.exit(1)
print("entries", len(entries), "bytes", sum(os.path.getsize(p) for p in entries.values()))

idx = tempfile.mktemp(prefix="cf15idx_")
env = dict(os.environ, GIT_INDEX_FILE=idx)
def git(*a, inp=None):
    r = subprocess.run(["git", "-C", REPO, *a], env=env, input=inp, capture_output=True, text=True)
    if r.returncode: print(r.stderr); sys.exit(2)
    return r.stdout.strip()
git("read-tree", PARENT)
paths = list(entries.values())
hashes = git("hash-object", "-w", "--stdin-paths", inp="\n".join(paths) + "\n").split("\n")
assert len(hashes) == len(paths)
info = "".join(f"100644 {h}\t{t}\n" for h, t in zip(hashes, entries))
git("update-index", "--add", "--index-info", inp=info)
tree = git("write-tree")
msg = ("Casual Finance visual CT_SCAN milestone 15/15: text-only artifacts for 15 videos\n\n"
       "Visual-only contract (ASR-only audio, AV sign-off BLOCKED). count_complete.py: VERIFIED_COMPLETE 15 / target 15 (roster 35).\n"
       "No media, frames or audio included.\n\n"
       "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\n")
commit = git("commit-tree", tree, "-p", PARENT, "-m", msg)
os.remove(idx)
json.dump({"commit": commit, "tree": tree, "parent": PARENT, "entries": {t: h for h, t in zip(hashes, entries)}},
          open(os.path.join(os.path.dirname(LIST), "cf15_commit.json"), "w"))
print("COMMIT", commit, "TREE", tree)
