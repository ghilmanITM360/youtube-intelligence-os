"""Checkpoint publication via external GIT_INDEX_FILE (no checkout, no worktree, normal push, never force).
Usage: python3 -I xk_publish.py <checkpoint_label> [--push]
Publishes text evidence from the xkcd workspace (no media, no jpg/png, no wav) under
research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/ on branch research/xkcd-whatif-visual-forensics."""
import json, sys, hashlib, subprocess, os, pathlib, datetime
X = sys.argv[1]; PUSH = "--push" in sys.argv
WS = pathlib.Path.home() / "YIOS-local-audits/xkcd-whatif"; REPO = "/Users/ghilmankhan/workprojects/youtube-intelligence-os"
BR = "research/xkcd-whatif-visual-forensics"; PREFIX = "research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/"
run = lambda *a, **k: subprocess.check_output(a, cwd=REPO, text=True, **k).strip()
INCLUDE = ["census/census.csv", "census/census_summary.json", "census/tab_listings.json", "census/catalog_ch000004_ids.json",
           "selection/*.json", "selection/*.txt", "campaign/*", "scripts/*.py", "scripts/*.sh", "scripts/*.md"]
VID = ["source_manifest.json", "coverage.json", "shot_ledger.csv", "visual_event_ledger.csv", "audio_visual_alignment.csv",
       "visual_ct_scan_report.md", "reconstruction_blueprint.md", "quality_gate.json", "continuation_handoff.md",
       "tables/state_ledger.csv", "tables/segments_v1.csv", "tables/detector_calibration.json", "tables/palette_measured.json",
       "tables/sheet_index.csv", "tables/scenedetect_candidates.csv", "evidence/source_sha256.txt", "evidence/ffprobe_full.json", "evidence/ebur128.txt",
       "asr/asr_small_en.json", "asr/asr_vs_catalog_caption.json", "review/*.csv", "review/*.json", "review/*/*", "review_brief_*.md"]
files = set()
for g in INCLUDE: files |= {p for p in WS.glob(g) if p.is_file()}
for v in sorted((WS / "videos").iterdir()):
    if not (v / "quality_gate.json").exists(): continue  # publish only built videos
    for g in VID: files |= {p for p in v.glob(g) if p.is_file()}
files = sorted(p for p in files if p.suffix not in (".jpg", ".png", ".mp4", ".wav", ".index") and "/raw/" not in str(p))
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
seal = WS / f"campaign/EVIDENCE_SHA256SUMS_{X}.txt"
seal.write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(WS)}\n" for p in files if p != seal))
files.append(seal)
remote = run("git", "ls-remote", "origin", f"refs/heads/{BR}").split()
base = remote[0] if remote else run("git", "ls-remote", "origin", "refs/heads/main").split()[0]
run("git", "cat-file", "-e", base)  # must exist locally
idx = WS / f"campaign/.{X}_publication.index"; idx.unlink(missing_ok=True)
env = dict(os.environ, GIT_INDEX_FILE=str(idx)); run("git", "read-tree", base, env=env)
for p in files:
    run("git", "update-index", "--add", "--cacheinfo", "100644", run("git", "hash-object", "-w", str(p)), PREFIX + str(p.relative_to(WS)), env=env)
tree = run("git", "write-tree", env=env); paths = run("git", "diff", "--name-only", base, tree).splitlines()
assert paths and all(x.startswith(PREFIX) for x in paths), "scope violation"
assert not any(x.endswith((".jpg", ".png", ".mp4", ".wav")) for x in paths)
rec = dict(checkpoint=X, prepared_utc=now, branch=BR, base=base, base_is_new_branch_from_main=not remote, tree=tree,
           files=len(files), changed_paths=len(paths), seal=str(seal.relative_to(WS)))
if PUSH:
    msg = f"research: xkcd What If visual forensics checkpoint {X}\n\nText evidence only (no media). Seal {seal.name}.\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
    commit = run("git", "commit-tree", tree, "-p", base, "-m", msg)
    now_remote = run("git", "ls-remote", "origin", f"refs/heads/{BR}").split()
    assert (now_remote[0] if now_remote else None) == (remote[0] if remote else None), "remote moved; re-run"
    subprocess.check_call(["git", "push", "origin", f"{commit}:refs/heads/{BR}"], cwd=REPO)
    after = run("git", "ls-remote", "origin", f"refs/heads/{BR}").split()[0]
    assert after == commit, (after, commit)
    # readback: compare every published blob on the remote commit tree with local hashes
    run("git", "fetch", "origin", f"refs/heads/{BR}")
    bad = 0
    for p in files:
        b = subprocess.run(["git", "cat-file", "blob", f"{after}:{PREFIX}{p.relative_to(WS)}"], cwd=REPO, capture_output=True).stdout
        bad += hashlib.sha256(b).hexdigest() != hashlib.sha256(p.read_bytes()).hexdigest()
    rec.update(commit=commit, remote_head=after, readback_files=len(files), readback_mismatches=bad)
    for v in (WS / "videos").iterdir():
        if (v / "quality_gate.json").exists(): (v / "PUBLISHED").write_text(f"checkpoint {X} commit {after} branch {BR}\n")
idx.unlink(missing_ok=True)
(WS / f"campaign/PUBLICATION_{X}.json").write_text(json.dumps(rec, indent=1)); print(rec)
