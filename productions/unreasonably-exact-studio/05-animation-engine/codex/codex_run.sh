#!/bin/zsh
# usage: tools/codex_run.sh RUN "prompt" img1 [img2 ...]   (run from project root; codex works in codex_handoff/)
RUN=$1; P=$2; shift 2; IMGS=(); for i in "$@"; do IMGS+=(-i "$i"); done
cd "$(dirname $0)/../codex_handoff" && mkdir -p runs/$RUN && \
/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex exec -C . -c model_reasoning_effort="high" --skip-git-repo-check -s workspace-write "${IMGS[@]}" -- "$(cat runs/COMMON_RULES.txt)

$P" < /dev/null > runs/$RUN/codex.log 2>&1
echo "$RUN exit $?"
