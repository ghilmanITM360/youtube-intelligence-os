"""Organize xkcd's What If? (CH-000004, DS-000017) transcripts into long-form and Shorts scripts.

Read-only over raw evidence; writes derived Markdown next to this file.
Reformat only: caption line-wraps are joined into paragraphs, [bracket] cues become
their own lines. No words are added, removed or reworded.
Run: python3 research/what-if-scripts/build_scripts.py
"""
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data/raw/competitors/DS-000017"
TX = RAW / "apify/mzl5dCHF81LbcBamS/transcripts"
OUT = Path(__file__).resolve().parent
GROUPS = {"video": "long", "shorts": "shorts"}


def to_script(raw: str) -> str:
    paras, buf = [], []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.fullmatch(r"\[[^\]]+\]", line):  # stage cue like [intro], [music]
            if buf:
                paras.append(" ".join(buf)); buf = []
            paras.append(f"*{line}*")
            continue
        buf.append(line)
        if re.search(r"[.?!][\"'”’)]?$", line):  # sentence end -> paragraph break
            paras.append(" ".join(buf)); buf = []
    if buf:
        paras.append(" ".join(buf))
    return "\n\n".join(paras)


def main():
    videos = json.loads((RAW / "dataset.json").read_text())
    index = {g: [] for g in GROUPS.values()}
    for v in sorted(videos, key=lambda v: v["date"]):
        g = GROUPS[v["type"]]
        src = TX / f"{v['id']}.txt"
        raw = src.read_text()
        sha = hashlib.sha256(src.read_bytes()).hexdigest()
        n = len(index[g]) + 1
        name = f"{n:02d}-{v['id']}.md"
        body = (
            f"# {v['title']}\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Video ID | `{v['id']}` |\n| URL | {v['url']} |\n| Format | {g} |\n"
            f"| Published | {v['date'][:10]} |\n| Duration | {v['duration']} |\n"
            f"| Views (at acquisition) | {v['viewCount']:,} |\n| Words | {len(raw.split()):,} |\n"
            f"| Source | `{src.relative_to(ROOT)}` |\n| Source SHA-256 | `{sha}` |\n\n"
            f"## Script\n\n{to_script(raw)}\n"
        )
        (OUT / g).mkdir(exist_ok=True)
        (OUT / g / name).write_text(body)
        index[g].append((name, v, len(raw.split())))

    lines = [
        "# xkcd's What If? scripts (CH-000004)\n",
        "Derived from DS-000017 (Apify, acquired 2026-08-31). Raw transcripts are unchanged; "
        "these files only reflow caption line-wraps into paragraphs. Ordered oldest to newest. "
        "Regenerate with `python3 research/what-if-scripts/build_scripts.py`.\n",
        "Not included: `9VG0yqq_PHM` and `X97DDWvxaqQ` (identity verified, transcript pending; "
        "see `docs/evidence/what-if-identity-2026-10-11/`).\n",
    ]
    for g, rows in index.items():
        lines.append(f"\n## {g.title()} ({len(rows)})\n\n| # | Published | Duration | Views | Words | Title |\n|---|---|---|---|---|---|")
        for name, v, w in rows:
            lines.append(f"| {name[:2]} | {v['date'][:10]} | {v['duration']} | {v['viewCount']:,} | {w:,} | [{v['title']}]({g}/{name}) |")
    (OUT / "README.md").write_text("\n".join(lines) + "\n")
    assert sum(map(len, index.values())) == len(videos) == 83
    print({g: len(r) for g, r in index.items()})


if __name__ == "__main__":
    main()
