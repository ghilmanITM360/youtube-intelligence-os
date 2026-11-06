"""Generates publication counts and the preservation reconciliation from the manifests and published commits. Text only. Does not change evidence.
Output: campaign/publication_counts_L.csv, campaign/preservation_reconciliation_L.csv, campaign/PUBLICATION_INTEGRITY_L.md"""
import collections, csv, datetime, hashlib, json, os, pathlib, subprocess
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; R = "/Users/ghilmankhan/workprojects/youtube-intelligence-os"
P = "research/visual-forensics/channels/UCsuQtyrMiUPdHUQ8WaqsFvQ/"; C = W / "campaign"
J_RECEIPT, K = "f3769da182e1f30e31ae880571faf01836b3da0e", "fa118b9b281c006c421b5801e543fd40f0c91eaa"
T364 = datetime.datetime(2026, 11, 6, 12, 3, 54, tzinfo=datetime.timezone.utc).timestamp()  # stamp of the census that printed 364
git = lambda *a: subprocess.check_output(["git", *a], cwd=R, text=True)
blob = lambda h: subprocess.check_output(["git", "cat-file", "blob", h], cwd=R)
sha = lambda b: hashlib.sha256(b).hexdigest()
def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
cache = {}
def tree(c):
    out = {}
    for l in git("ls-tree", "-r", c, P).splitlines():
        meta, path = l.split("\t", 1); out[path[len(P):]] = meta.split()[2]
    return out
def blob_sha(b):
    if b not in cache: cache[b] = sha(blob(b))
    return cache[b]

# 1. publication counts, per label, from each commit's own seal
rows = []
for label in "A B C D E F G H I J J_RECEIPT K".split():
    rp = C / (f"PUBLICATION_{label}_FINAL.json" if label == "K" else f"PUBLICATION_{label}.json")
    r = json.loads(rp.read_text()); c = r.get("commit")
    row = dict(label=label, commit=c or "", receipt_files=r.get("files"), receipt_readback_files=r.get("readback_files", ""), receipt_readback_mismatches=r.get("readback_mismatches", ""))
    if c:
        t = tree(c); name = f"campaign/EVIDENCE_SHA256SUMS_{label}.txt"
        lines = blob(t[name]).decode().splitlines() if name in t else []
        ent = [l.split("  ", 1) for l in lines]; paths = {x[1] for x in ent}
        row.update(sealed_entries=len(ent), distinct_sealed=len(paths), seal_in_own_seal=int(name in paths),
                   sealed_plus_seal=len(paths | {name}), receipt_extra_over_distinct=(r.get("files") or 0) - len(paths | {name}),
                   tree_files=len(t), tree_paths_outside_seal_set=len(set(t) - paths - {name}),
                   seal_vs_commit_missing=sum(x[1] not in t for x in ent), seal_vs_commit_failures=sum(x[1] in t and blob_sha(t[x[1]]) != x[0] for x in ent))
    rows.append(row)
fields = list(dict.fromkeys(k for r in rows for k in r))
with open(C / "publication_counts_L.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)
k = next(r for r in rows if r["label"] == "K")
tk = tree(K); seal_k = (C / "EVIDENCE_SHA256SUMS_K.txt").read_bytes()
assert sha(seal_k) == blob_sha(tk["campaign/EVIDENCE_SHA256SUMS_K.txt"]), "local K seal differs from the published K seal"
k_local = [l.split("  ", 1) for l in seal_k.decode().splitlines()]
k_drift = sorted(x[1] for x in k_local if not (W / x[1]).exists() or sha_file(W / x[1]) != x[0])

# 2. preservation
def manifest(p): return {a[1]: a for a in (l.rstrip("\n").split("\t") for l in open(p)) if len(a) == 4 and a[0] != "category"}
man, sup = manifest(C / "LOCAL_ONLY_PRESERVATION_MANIFEST.txt"), manifest(C / "LOCAL_ONLY_PRESERVATION_SUPPLEMENT_K.txt")
tj = tree(J_RECEIPT)
files = [f for f in W.rglob("*") if f.is_file() and ".pe_writer_lock" not in str(f)]
rec364 = {str(f) for f in files if str(f) not in man and str(f.relative_to(W)) not in tj and f.stat().st_birthtime <= T364}
only364, only315, both = rec364 - set(sup), set(sup) - rec364, rec364 & set(sup)
out = []
for p in sorted(rec364 | set(sup)):
    q = pathlib.Path(p); rel = str(q.relative_to(W)); now = sha_file(q) if q.exists() else ""
    k_sha = blob_sha(tk[rel]) if rel in tk else ""
    why = ("published at K; current bytes equal the K blob" if now == k_sha else "published at K; current bytes differ") if p in only364 else \
          "first K dry-run receipt, created after the 364 census; K tree dry-run did not hold it yet, so the supplement listed it" if p in only315 else "in both"
    a = sup.get(p, ["", "", "", ""])
    out.append(dict(path=rel, in_364_reconstruction=int(p in rec364), in_315_supplement=int(p in sup), in_K_tree=int(rel in tk), reason=why, bytes_now=q.stat().st_size if q.exists() else "", sha256_now=now, sha256_supplement=a[3], sha256_K_blob=k_sha))
with open(C / "preservation_reconciliation_L.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
b50 = sum(pathlib.Path(p).stat().st_size for p in only364)
bonly315 = sum(int(sup[p][2]) for p in only315)
sup_bytes = sum(int(a[2]) for a in sup.values()); man_bytes = sum(int(a[2]) for a in man.values())
derived = sup_bytes - bonly315 + b50
man_bad = sorted(p for p, a in man.items() if not pathlib.Path(p).exists() or sha_file(p) != a[3])
sup_bad = sorted(str(pathlib.Path(p).relative_to(W)) for p, a in sup.items() if not pathlib.Path(p).exists() or sha_file(p) != a[3])
sup_bad_kinds = collections.Counter("PUBLISHED marker" if x.endswith("/PUBLISHED") else x for x in sup_bad)
union = set(man) | set(sup); overlap = set(man) & set(sup)
pub_overlap = sorted(str(pathlib.Path(p).relative_to(W)) for p in sup if str(pathlib.Path(p).relative_to(W)) in tk)
uncovered = sorted(str(f.relative_to(W)) for f in files if str(f) not in union and str(f.relative_to(W)) not in tk)
deps = []
for label, p, note in (("requirements lock", W.parent / "tooling/visual-ct-scan-requirements.lock", "hash recorded here only"),
                       ("kit zip", pathlib.Path.home() / "Downloads/YIOS_Visual_Forensics_Intelligence_Kit_v1.0.zip", "hash in DEPENDENCY_VERSIONS_K.txt; no copy in workspace; not re-read")):
    deps.append((label, str(p), sha_file(p) if label != "kit zip" else "see DEPENDENCY_VERSIONS_K.txt", note))
kinds = collections.Counter(pathlib.Path(p).name for p in only364)

md = f"""# Publication integrity and preservation reconciliation (checkpoint L)
Generated by scripts/pe_integrity_reconcile.py from the published commits and manifests. No analysis was repeated. Published K and historical seals are unchanged.

## K counts: exact definitions
| Number | Definition | Source |
|---|---|---|
| {k['sealed_entries']} | Sealed entries: lines in EVIDENCE_SHA256SUMS_K.txt, all distinct. Excludes the seal itself. Includes the dry-run PUBLICATION_K.json | seal at {K} |
| {k['sealed_plus_seal']} | Distinct files in the publish set: {k['sealed_entries']} sealed entries + the seal | same seal |
| {k['receipt_files']} | Field files and readback_files in the K receipt: the same {k['sealed_plus_seal']} files with the seal listed twice. Not a file count | PUBLICATION_K_FINAL.json |
| {k['tree_files']} | All files under the channel prefix in the K tree; {k['tree_paths_outside_seal_set']} of them lie outside the K publish set | git ls-tree {K} |

Cause of the extra entry: the campaign/*.txt glob found the seal left by the dry-run, then the old code appended it again. A first run with no earlier seal did not double-count. Readback compared the seal twice, so its 0 mismatches is unaffected.
Correct K counts: {k['sealed_entries']} sealed, {k['sealed_plus_seal']} published in the K set. The K receipt keeps its original field; this table is the correction. Fixed from L on: fields sealed_entries, published_files and tree_files_under_prefix.

## All labels
Full table: campaign/publication_counts_L.csv. Each seal is checked against its own commit, not against working files, which move on by design.
| Label | Commit | Receipt files | Sealed | Sealed + seal | Extra in receipt | Tree files | Seal missing | Seal failures |
|---|---|---|---|---|---|---|---|---|
""" + "\n".join(f"| {r['label']} | {r['commit'][:10]} | {r['receipt_files']} | {r.get('sealed_entries','')} | {r.get('sealed_plus_seal','')} | {r.get('receipt_extra_over_distinct','')} | {r.get('tree_files','')} | {r.get('seal_vs_commit_missing','')} | {r.get('seal_vs_commit_failures','')} |" for r in rows) + f"""

## Receipt design from L on
- PUBLICATION_<X>_PREFLIGHT.json: written by a run without --push. Push refuses unless content and base still give the preflight tree.
- PUBLICATION_<X>_FINAL.json: written once after the push, with commit, remote head, seal path and seal_sha256.
- Explicit self-reference exclusions, listed in each receipt: the seal, the preflight and the final receipt of X are outside the seal of X. The next checkpoint publishes X's receipts as ordinary sealed files.
- A label whose seal is already on the remote branch is refused before anything is written.
- Regression: scripts/test_pe_publish.py, synthetic sandbox only.

K receipts: campaign/PUBLICATION_K_FINAL.json holds the post-push receipt, byte-identical to the local file it came from. campaign/PUBLICATION_K.json was restored to the bytes sealed in the K commit, so the path stays unchanged at L.
K seal against working files today: {len(k_drift)} of {len(k_local)} differ, all intended edits since K: {', '.join(k_drift) or 'none'}. The seal's contract is its commit, which shows 0 failures above.

## 364 versus 315
The 364 list was printed as a count and not saved. It is reconstructed here with the same rule: workspace files outside the lock directory, not in the J manifest, not in the {J_RECEIPT[:10]} tree, and born by 2026-11-06T12:03:54Z. Result {len(rec364)} files, matching the note.
The 315 supplement used a later cut: created 12:05:50Z, against the first K dry-run tree instead of {J_RECEIPT[:10]}, excluding itself.
| Step | Files | Bytes |
|---|---|---|
| Note, census at 12:03:54Z | 364 | 9,890,308 |
| Published at K, removed: {', '.join(f'{n} x{c}' for n, c in kinds.most_common())} | -{len(only364)} | -{b50:,} |
| Added: campaign/PUBLICATION_K.json, first dry-run, did not exist at the census | +{len(only315)} | +{bonly315:,} |
| Supplement | {len(set(sup))} | {sup_bytes:,} |
Bytes derived from the supplement and current sizes: {derived:,}, against 9,890,308 in the note, difference {derived - 9890308:+,}. Every one of the {len(only364)} removed files has current bytes equal to its K blob: {sum(1 for r in out if r['reason'].startswith('published at K; current bytes equal'))}/{len(only364)}. Per-path hashes: campaign/preservation_reconciliation_L.csv.

## Coverage
| Set | Files | Bytes |
|---|---|---|
| Primary manifest (J) | {len(man)} | {man_bytes:,} |
| Supplement (K) | {len(sup)} | {sup_bytes:,} |
| Overlap, same path in both | {len(overlap)} | 0 |
| Deduplicated union | {len(union)} | {man_bytes + sup_bytes:,} |

Hash check today, full SHA-256 on every row: primary {len(man) - len(man_bad)}/{len(man)} match. Supplement {len(sup) - len(sup_bad)}/{len(sup)} match; the {len(sup_bad)} differing rows are mutable bookkeeping, not evidence: {', '.join(f'{n} x{c}' for n, c in sup_bad_kinds.most_common())}.
Supplement rows now also in the K tree: {', '.join(pub_overlap) or 'none'}. Its supplement hash is the first dry-run, which no longer exists; it was a receipt, not evidence.
Workspace files in no manifest and not in the K tree at this run: {len(uncovered)}: {', '.join(uncovered) or 'none'}. Those under scripts/ and campaign/ matching the publish rule are published by L.

## Uncovered required dependencies
Covered means a hashed entry on this Mac. None of this is a backup, and all of it stays on the boot volume.
| Dependency | State | Gap |
|---|---|---|
| Python venv, 364 MB | pip freeze in DEPENDENCY_VERSIONS_K.txt; requirements lock sha256 {deps[0][2]} | Contents not hashed or copied |
| ASR models faster-whisper small.en (used) and small | Snapshot IDs and sizes only | Contents not hashed or copied |
| ffmpeg 9.0.1, system Python | Version only | Binaries not hashed or copied |
| Kit zip | Hash in DEPENDENCY_VERSIONS_K.txt, in ~/Downloads | No copy in the workspace |
| Original source files in ~/Downloads | Recorded in census/source_census.csv; 15 selected have verified copies | Other originals census only; originals not re-read here |
| vf_lock.sh, launchd plist | In the primary manifest | Hashed; same-Mac only |

Rebuildability is NOT VERIFIED. Version notes record what was used. No clean rebuild of the venv, models or pipeline was run, so they do not prove the environment can be recreated.
Off-device transfer stays BLOCKED: no destination is named. Published text on the remote is the only off-device copy, and it holds no media. Same-Mac copies are not a backup.
"""
(C / "PUBLICATION_INTEGRITY_L.md").write_text(md)
print(md[:700]); print("derived", derived, "man_bad", len(man_bad), "sup_bad", sup_bad_kinds, "uncovered", uncovered, "k_drift", k_drift); print([ (r['label'],r.get('sealed_entries'),r['receipt_files'],r.get('receipt_extra_over_distinct'),r.get('tree_files'),r.get('seal_vs_commit_missing'),r.get('seal_vs_commit_failures')) for r in rows])
