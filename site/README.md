# YIOS data browser

Read-only local website over the canonical DB. Python stdlib only, no install, no build step.

```bash
git pull && git lfs pull          # source DBs are tracked (the registry one via LFS)
python3 site/server.py            # first run builds data/catalog/yios_canonical.db (~1 min), then serves
# open http://127.0.0.1:8020
```

- The canonical DB is gitignored and rebuilt from the tracked source DBs, so every machine builds its own identical copy
  (`logical_sha256` in `data/manifests/yios-canonical-sources.json` proves it).
- Files only preview if they exist in your checkout; media outside git (see `docs/LOCAL_MEDIA_AVAILABILITY.md`) shows "not present".
- Viewers: `.md` rendered, `.csv/.tsv` sortable table, `.json/.jsonl` table or tree, `.gz` shown decompressed, images/audio/video inline.
- Another port: `--port 8030`. Another DB: `YIOS_CANONICAL_DB=/path/to.db`.

## What each page shows
- **Overview**: totals, uploads per year, biggest channels, how complete each field is.
- **Channels**: a scatter of every channel (videos vs typical views) and a sortable table with a per-channel uploads sparkline.
- **Channel report** (six tabs, with a dropdown to jump between channels): *Overview* (numbers, views-over-time chart, heat map, thumbnails), *Videos* (every video, sortable), *Titles* (which words and title features go with more views, long-form only), *Transcripts* (what the channel talks about, search and read inside the page), *Analyses & files* (every report, table, JSON and image about the channel, opened inline), *Data & sources* (completeness, source names, disagreements).
- **Videos**: filters (channel, type, year, transcript, specific file), title search and full-text search inside transcripts.
- Results are cached in memory per DB version and sent gzip-compressed, so every page after the first load answers in about a millisecond.

## File viewers
Markdown, CSV/TSV, JSON/JSONL, Excel (.xlsx, every sheet), Word (.docx text), SQLite (.db, first rows of every table), ZIP (file list), PDF (inline), images, audio and video open in the page. `.npz` and other binary formats have no preview (use Open raw / Download). Excel and Word are read with the Python standard library only; formulas are shown as their stored values.
Channels with no collected videos (about a third of the 263) show an explanation instead of empty charts; the Channels page can filter to them.

## Research page and Ask AI
- **Research** (`#/research`): full-text search over about 8,800 research documents (reports, audits, playbooks, forensic analyses, studies) and 6,960 transcripts, ranked, with inline viewers. Each channel also has a **Research** tab: documents that contain its ids come first, documents that only mention its name are marked as leads.
- **Ask AI** (`#/ask`): a chat that answers only from evidence tools (find channels, channel overview, list videos, read a video and its transcript, search research, read a document, read-only SQL). Answers cite `[file: path]`, `[video: id]`, `[channel: id]` as links, label fact vs interpretation vs hypothesis, and can be exported as Markdown. It cannot change any data.
- The search index is `data/catalog/yios_search.db` (gitignored, about 370 MB, built in about 20 s by `scripts/build_yios_search_index.py`; the site builds it on first run).
- **Choose the model with environment variables before `python3 site/server.py`** (keys are never stored in the repo):

```bash
export ANTHROPIC_API_KEY=...            # Anthropic API (YIOS_MODEL optional, default claude-sonnet-5-5)
# or a local / OpenAI-compatible server, e.g. Ollama:
export YIOS_LLM_BASE_URL=http://localhost:11434/v1 YIOS_LLM_MODEL=llama3.1
```
With neither set the chat still works as search only and nothing leaves the machine. With a model set, the question and the excerpts the tools return are sent to that provider.
