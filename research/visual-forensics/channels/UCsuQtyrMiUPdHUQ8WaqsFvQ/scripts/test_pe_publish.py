"""Regression test for pe_publish.py receipts. Sandbox only: a synthetic workspace, a throwaway repo and a local bare origin. Never touches the real branch.
Run: python3 -I scripts/test_pe_publish.py"""
import hashlib, json, os, pathlib, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
BR = "research/primitive-education-visual-forensics"; PREFIX = "research/visual-forensics/channels/UCsuQtyrMiUPdHUQ8WaqsFvQ/"
fails = []; passed = 0
def check(name, ok, detail=""):
    global passed
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if ok: passed += 1
    else: fails.append(name)
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
tmp = tempfile.TemporaryDirectory(); T = pathlib.Path(tmp.name)
ws, repo, origin = T / "ws", T / "repo", T / "origin.git"
env = dict(os.environ, PE_WS=str(ws), PE_REPO=str(repo), GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_NOSYSTEM="1", GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
def git(*a, cwd=repo): return subprocess.check_output(["git", *a], cwd=cwd, env=env, text=True, stderr=subprocess.DEVNULL).strip()
def publish(*a): return subprocess.run([sys.executable, "-I", str(HERE / "pe_publish.py"), *a], env=env, capture_output=True, text=True)
def load(p): return json.loads(p.read_text()) if p.exists() else {}
def seal_failures(seal):
    bad = []
    for line in seal.read_text().splitlines():
        h, rel = line.split("  ", 1)
        if not (ws / rel).exists() or sha(ws / rel) != h: bad.append(rel)
    return bad
def remote(): return git("ls-remote", "origin", f"refs/heads/{BR}").split()[0]
def tree_files(c): return set(git("ls-tree", "-r", "--name-only", c, PREFIX).splitlines())

subprocess.check_call(["git", "init", "-q", "--bare", str(origin)], env=env)
repo.mkdir(); git("init", "-q", "-b", "main"); git("remote", "add", "origin", str(origin))
git("commit", "-q", "--allow-empty", "-m", "base"); git("push", "-q", "origin", "main")
for rel, text in (("campaign/NOTE.md", "note\n"), ("campaign/data.json", "{}\n"), ("videos/v1/quality_gate.json", "{}\n"), ("videos/v1/frame.jpg", "x"), ("source_media/v1.mp4", "x")):
    (ws / rel).parent.mkdir(parents=True, exist_ok=True); (ws / rel).write_text(text)
C = ws / "campaign"; seal, pre, fin = C / "EVIDENCE_SHA256SUMS_L.txt", C / "PUBLICATION_L_PREFLIGHT.json", C / "PUBLICATION_L_FINAL.json"

# preflight, twice: on the old code the second run counts the seal twice because the glob finds it
r = publish("L"); check("preflight runs", r.returncode == 0, r.stderr[-300:])
r = publish("L"); check("repeat preflight runs", r.returncode == 0, r.stderr[-300:])
p = load(pre)
check("preflight has its own filename", pre.exists())
check("legacy shared receipt name is gone", not (C / "PUBLICATION_L.json").exists())
check("nothing pushed by preflight", git("ls-remote", "origin", f"refs/heads/{BR}") == "")
entries = len(seal.read_text().splitlines())
check("seal counted once: published_files == sealed_entries + 1", p.get("published_files") == entries + 1 and p.get("sealed_entries") == entries, f"{p} entries={entries}")
sealed_paths = {l.split("  ", 1)[1] for l in seal.read_text().splitlines()}
check("receipts and seal are not in their own seal", not sealed_paths & {"campaign/EVIDENCE_SHA256SUMS_L.txt", "campaign/PUBLICATION_L_PREFLIGHT.json", "campaign/PUBLICATION_L_FINAL.json"}, str(sealed_paths))
check("exclusions are explicit in the preflight", set(p.get("self_reference_exclusions", {})) == {"campaign/EVIDENCE_SHA256SUMS_L.txt", "campaign/PUBLICATION_L_PREFLIGHT.json", "campaign/PUBLICATION_L_FINAL.json"}, str(p.get("self_reference_exclusions")))

# drift between preflight and push is refused
(C / "NOTE.md").write_text("drift\n"); r = publish("L", "--push")
check("push refused when content changed after preflight", r.returncode != 0 and git("ls-remote", "origin", f"refs/heads/{BR}") == "", r.stderr[-200:])
(C / "NOTE.md").write_text("note\n"); publish("L")

# push: the core regression. Nothing sealed may change after the seal is written.
before = {x: sha(ws / x) for x in sealed_paths}; seal_before = sha(seal)
r = publish("L", "--push"); check("push runs", r.returncode == 0, r.stderr[-300:])
head = remote(); f = load(fin)
check("post-publication receipt mutates no sealed file", {x: sha(ws / x) for x in sealed_paths} == before and seal_failures(seal) == [], str(seal_failures(seal)))
check("seal bytes unchanged by push", sha(seal) == seal_before)
check("final receipt has its own filename", fin.exists())
check("final receipt names the exact commit", f.get("commit") == head == f.get("remote_head"), f"{f.get('commit')} {head}")
check("final receipt names the seal and its hash", f.get("seal") == "campaign/EVIDENCE_SHA256SUMS_L.txt" and f.get("seal_sha256") == sha(seal))
got = tree_files(head)
check("tree holds sealed files plus seal, no receipts of this label", got == {PREFIX + x for x in sealed_paths} | {PREFIX + "campaign/EVIDENCE_SHA256SUMS_L.txt"}, str(got))
check("final counts match the tree", f.get("published_files") == len(got) == f.get("tree_files_under_prefix") and f.get("readback_files") == len(got), str(f))
check("readback clean", f.get("readback_mismatches") == 0)
check("no media published", not [x for x in got if x.endswith((".jpg", ".png", ".mp4", ".wav"))])

# a published label cannot be re-sealed
s0, f0 = sha(seal), sha(fin); (C / "NOTE.md").write_text("later\n")
r1 = publish("L"); r2 = publish("L", "--push")
check("published label refused for preflight and push", r1.returncode != 0 and r2.returncode != 0 and remote() == head)
check("refused runs leave seal and final receipt alone", sha(seal) == s0 and sha(fin) == f0)

# next label: earlier receipts become ordinary sealed files, earlier seal stays valid against its commit
r = publish("M"); r2 = publish("M", "--push"); check("next label publishes", r.returncode == 0 and r2.returncode == 0, (r.stderr + r2.stderr)[-300:])
m_seal = (C / "EVIDENCE_SHA256SUMS_M.txt").read_text()
check("next checkpoint seals the prior receipts", "campaign/PUBLICATION_L_FINAL.json" in m_seal and "campaign/PUBLICATION_L_PREFLIGHT.json" in m_seal)
check("L seal unchanged and matches its commit", git("show", f"{head}:{PREFIX}campaign/EVIDENCE_SHA256SUMS_L.txt") + "\n" == seal.read_text())
print(f"{passed} passed, {len(fails)} failed"); sys.exit(1 if fails else 0)
