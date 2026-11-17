#!/bin/sh
# Install the AI-slop gate pre-commit hook for this clone and all its worktrees: sh .githooks/install.sh
# A shim (not a symlink, not core.hooksPath) so each checkout runs its OWN .githooks/pre-commit and the
# Git LFS hooks already in .git/hooks keep working.
h="$(git rev-parse --git-common-dir)/hooks/pre-commit"
if [ -e "$h" ] || [ -L "$h" ]; then
  grep -q 'AI-slop gate shim' "$h" 2>/dev/null || { echo "Refusing to overwrite existing $h; add the shim lines by hand."; exit 1; }
fi
printf '%s\n' '#!/bin/sh' '# AI-slop gate shim (installed by .githooks/install.sh)' \
  'f="$(git rev-parse --show-toplevel)/.githooks/pre-commit"' '[ -x "$f" ] || exit 0' 'exec "$f"' > "$h"
chmod +x "$h" && echo "installed $h"
