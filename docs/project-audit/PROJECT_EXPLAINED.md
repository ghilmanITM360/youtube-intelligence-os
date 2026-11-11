# Project Explained — YouTube Intelligence OS

**What it is.** A private, evidence-first research workspace (a git repository, not an app) that studies many YouTube channels so the owner can plan new videos with traceable reasons. It stores supplied competitor data, records where each fact came from, and produces content plans whose every claim points back to evidence.

**Why.** To replace guesswork and AI memory with repository evidence: raw files are never edited, each fact has a hash and provenance, and AI-style interpretations are labeled separately from observations (AGENTS.md rules 1–9).

**Who it serves.** The owner (a YouTube creator/operator working across several channels and two Macs) and the AI coding agents that work inside the repo.

**How it works, in order.**
1. Owner supplies data (exports, workbooks, screenshots, transcripts, optional Apify scrapes). Files land in `data/raw/` with SHA-256 hashes.
2. `scripts/` register them into two SQLite databases: an inventory catalog (10 channels, 667 videos, 45,774 files) and a wider channel registry (75 channels, 2,303 videos, searchable transcripts).
3. Five "intelligence" reports analyze topics, packaging (titles/thumbnails), hooks/scripts, editing/visuals, and channel strategy — writing JSON under `data/intelligence/`.
4. `run_youtube_intelligence.py` combines them into a content plan per channel/opportunity, marking anything it can't support as `NOT_AVAILABLE` (e.g., CTR/retention unless real first-party analytics exist).
5. A reference knowledge base (rules from a supplied YouTube-training corpus) can gate plans.
6. Current active work: auditing 1,612 Finance/Economics videos (558 accepted) and re-analyzing them against the reference corpus (26/558 so far), plus visual forensics of Casual Finance videos.

**Stage.** V1 declared complete (2026-10); V2 not started. 462 automated tests pass. Strongest parts: provenance, validators, honesty about missing evidence. Weakest: scale of evidence (few channels per niche), human semantic review backlog, no real first-party data, CI missing the Finance gates, heavy branch/PR sprawl.
