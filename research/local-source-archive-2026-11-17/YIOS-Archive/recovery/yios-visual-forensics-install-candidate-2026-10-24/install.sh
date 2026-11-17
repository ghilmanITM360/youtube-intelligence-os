#!/bin/bash
# Run ONLY after the Finance writer handoff is done and owner authorizes. Usage: install.sh /path/to/repo
set -e
R="${1:?repo path}"; C="$(cd "$(dirname "$0")" && pwd)"
cd "$R"
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "tracked changes present; abort"; exit 1; }
[ ! -e .claude/skills/visual-ct-scan ] && [ ! -e CLAUDE.md ] || { echo "target exists; merge manually"; exit 1; }
python3 -I "$C/validate_candidate.py" "$C/repo-overlay" >/dev/null
cp -R "$C/repo-overlay/.claude/skills" .claude/ 2>/dev/null || { mkdir -p .claude && cp -R "$C/repo-overlay/.claude/skills" .claude/; }
cp "$C/repo-overlay/CLAUDE.md" CLAUDE.md
patch -p0 docs/research/README.md < "$C/docs-research-README.patch" || true
python3 -I "$C/validate_candidate.py" "$R"
echo "Installed, not committed. Stage only: .claude/skills/visual-ct-scan CLAUDE.md docs/research/README.md"
