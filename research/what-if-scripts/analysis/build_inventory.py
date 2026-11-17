"""Phase 1 inventory + coverage ledger for the What If? 83-transcript script study.
Read-only over DS-000017. Stable IDs V001..V083 = chronological by publish date
(ties broken by video id). Run: python3 research/what-if-scripts/analysis/build_inventory.py
"""
import hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "data/raw/competitors/DS-000017"
TX = RAW / "apify/mzl5dCHF81LbcBamS/transcripts"
OUT = Path(__file__).resolve().parent
SCRIPTS = OUT.parent

def grams(t, n=8):
    w = re.findall(r"[a-z0-9']+", t.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

def secs(d):
    h, m, s = map(int, d.split(":")); return h * 3600 + m * 60 + s

vids = sorted(json.loads((RAW / "dataset.json").read_text()), key=lambda v: (v["date"], v["id"]))
fmt = {"video": "long", "shorts": "shorts"}
script_file = {p.stem.split("-", 1)[1]: p for g in ("long", "shorts") for p in (SCRIPTS / g).glob("*.md")}
rows, shas, G = [], {}, {}
for i, v in enumerate(vids, 1):
    src = TX / f"{v['id']}.txt"; raw = src.read_text(); sha = hashlib.sha256(src.read_bytes()).hexdigest()
    G[v["id"]] = grams(raw)
    subs = v.get("subtitles") or [{}]
    rows.append(dict(vid=f"V{i:03d}", id=v["id"], file=src.name, script=str(script_file[v["id"]].relative_to(SCRIPTS)),
                     title=v["title"], format=fmt[v["type"]], date=v["date"][:10], duration=v["duration"],
                     words=len(raw.split()), wps=round(len(raw.split()) / max(secs(v["duration"]), 1), 2),
                     language=subs[0].get("language"), caption_type=subs[0].get("type"),
                     timestamps="none (plaintext transcript; srtUrl null)",
                     ends_clean=bool(re.search(r"[.?!\"”’)\]]\s*$", raw.strip())), sha=sha, dup_of=shas.get(sha)))
    shas.setdefault(sha, f"V{i:03d}")
# cross-video overlap: share of a video's 8-grams found in any other transcript
for r in rows:
    best = max(((len(G[r["id"]] & G[o["id"]]) / max(len(G[r["id"]]), 1), o["vid"]) for o in rows if o is not r), default=(0, None))
    r["max_overlap"], r["overlap_with"] = round(best[0], 3), best[1]
ledger = {r["vid"]: {"id": r["id"], "status": "NOT_STARTED", "audit": None} for r in rows}
lp = OUT / "coverage_ledger.json"
if lp.exists():  # keep progress
    old = json.loads(lp.read_text()); ledger.update({k: old[k] for k in old if k in ledger})
lp.write_text(json.dumps(ledger, indent=1) + "\n")
(OUT / "inventory.json").write_text(json.dumps(rows, indent=1) + "\n")
L = ["# Deliverable 1 — Dataset inventory (What If?, CH-000004, DS-000017)\n",
     "Stable IDs are chronological by publish date. Words/sec = words ÷ listed duration (an estimate of narration density, not a timing measurement). "
     "Overlap = share of the transcript's 8-word sequences that also appear in another transcript (duplication check).\n",
     "| VID | Video ID | Format | Published | Duration | Words | W/s | Lang | Captions | Ends clean | Overlap (with) | Title |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['vid']} | `{r['id']}` | {r['format']} | {r['date']} | {r['duration']} | {r['words']:,} | {r['wps']} | {r['language']} | {r['caption_type']} | {'yes' if r['ends_clean'] else 'NO'} | {r['max_overlap']:.0%} ({r['overlap_with']}) | [{r['title']}](../{r['script']}) |")
exact = [r for r in rows if r["dup_of"]]
L += ["", f"Readable transcripts: {len(rows)}. Exact duplicates (same SHA-256): {len(exact)}. "
      f"Videos with ≥30% 8-gram overlap: {sum(r['max_overlap'] >= .3 for r in rows)}. No transcript carries timestamps."]
(OUT / "01_INVENTORY.md").write_text("\n".join(L) + "\n")
assert len(rows) == 83 and len(set(r["sha"] for r in rows)) == len(rows) - len(exact)
print(len(rows), "exact dups", len(exact), "overlap>=.3:", [(r["vid"], r["overlap_with"], r["max_overlap"]) for r in rows if r["max_overlap"] >= .3])
