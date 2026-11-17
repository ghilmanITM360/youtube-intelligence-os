# Existing clones and worktrees

Bounded discovery found one independent YIOS repository and its two linked worktrees. The main root already existed; no clone/worktree was created. Search roots and depth limits are in `discovery.json`. No claim is made about unrelated folders or external volumes.

| Path / branch | Full HEAD | Upstream / delta | State |
| --- | --- | --- | --- |
| /Users/ghilmanislam360/.codex/worktrees/yios-dual-machine/youtube-intelligence-os / codex/yios-dual-machine-coordination | 205fc7ebadcbde6b5104e9cb2be53de8951511a8 | origin/codex/yios-dual-machine-coordination / 0 ahead 0 behind | CLEAN |
| /Users/ghilmanislam360/Documents/youtube-intelligence-os / research/finance-economics-intelligence | 223f44981ee174988574e86d5e23ae83ee60ee5d | origin/research/finance-economics-intelligence / 0 ahead 0 behind | CLEAN |
| /Users/ghilmanislam360/Documents/youtube-intelligence-os/.claude/worktrees/finance-audits-machine-b-0044ae / claude/finance-audits-machine-b-0044ae | 223f44981ee174988574e86d5e23ae83ee60ee5d | origin/research/finance-economics-intelligence / 0 ahead 0 behind | CLEAN |

Shared common directory: `/Users/ghilmanislam360/Documents/youtube-intelligence-os/.git`. It is counted once, not once per worktree. No hardlinked inode duplicates were detected by the census; APFS clone extent sharing is unknown. Logical file duplication is not a measurement of reclaimable physical space.

| Role | Logical bytes before / files | Keep/reuse assessment |
| --- | --- | --- |
| Coordination implementation/testing worktree | 1,447,290,728 / 4,803 | KEEP_DISTINCT_TOOLING_ROLE_SECOND_MAC_ACCEPTANCE_PENDING |
| Primary Finance checkout and local evidence/runtime | 1,542,452,423 / 6,171 | KEEP_CANONICAL_AND_LOCAL_DEPENDENCIES |
| Finance Claude writer-assigned worktree | 1,444,690,827 / 4,691 | LOGICAL_CHECKOUT_DUPLICATE_AT_SAME_HEAD_BUT_WRITER_ASSIGNMENT_UNKNOWN_KEEP |

The primary and Claude Finance checkouts are exact Git-HEAD duplicates, but have different local runtime/evidence and writer assignments. The primary has1,493ignored paths at checkpoint, the coordination worktree108, and Claude11. Ignored files are individually classified in `local_path_classifications.csv`. There are no nonignored untracked files or local-only branch commits. The large local stash and external media/preservation archives remain separate dependencies.

The primary is needed for current source/catalog/runtime/evidence access. Coordination is needed to retain the tested separate tooling implementation until real receiving-Mac acceptance. The Claude worktree is a possible future consolidation candidate after its owning session releases it and ignored paths are reviewed; it was not removed. A clean Git tree or published commit does not prove a worktree is disposable.

Local process inspection and the supported Codex chat snapshot identified this audit as the active YIOS task. Other YIOS chats seen were `notLoaded`; that is not a writer release. Claude Desktop/Codex service processes are present. No separate research/ffmpeg/validator writer process or live Git mutation lock was established at preflight. Machine A and other client activity remain unknown. Existing Finance ownership records conflict across branch roles: canonical retains Machine B sole-writer history, Machine A continuation declares separate owner-directed execution without verified Machine B release. No authority was silently transferred.

Source paths in this checkout resolve to registered DS workbooks/ZIPs and real LFS registry bytes. Media is under `Documents/YIOS-Media-Library`; all 456registered bytes were verified. CT001–005 source videos exist here, but the complete Machine A frames/audio/reviewer working sets mostly do not. The `.env`, two empty legacy DBs, ignored raw acquisition files, external preservation directories and stash were retained. Full worktree/clone rows and dependencies are in CSV/JSON companions.
