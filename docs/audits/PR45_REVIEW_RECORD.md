# PR #45 review record, 2026-11-06

**Reviewer:** one fresh-context Sonnet subagent, read-only, at `223b21ac`. It is independent of this PR's author session but is not a human review, and no one outside the author's tooling has reviewed this PR. The author triaged its findings.

## Findings
| # | Finding | Resolution |
|---|---|---|
| 1 | TITLE witness accepted any substring, such as `a` | Fixed: the whole title, or two or more whole words of it |
| 2 | List or dict `assessment_mode` or `judgment` raised `TypeError` | Fixed: returns an error |
| 3 | Guard missed `-journal`, `.sqlite`, and uppercase `.DB`, `-WAL`, `-SHM`, `.Pyc` | Fixed |
| 3a | Guard allows nested `outputs/` | Not a defect: 341 tracked raw-evidence files live there. Test added |
| 4 | Superseded rules could be implemented | Fixed; they can still be declined through an exception |
| 5 | Missing database raised `OperationalError` in both gates | Fixed: returns a gate failure |
| 6 | `RESUME_HERE.md` keeps old "Machine B sole writer" notes | Left alone: dated history in the Finance writer's file. `AGENTS.md` governs |
| 7 | Framework-claim test did not check the rejection reason | Fixed: asserts the message. Replacing the message makes the test fail |

The author's own check found two more:
- `tests/test_ci_workflow_gates.py` hard-coded the xkcd registry count, so a legitimate registration would have failed it. It now checks the census total.
- The identity contract wrongly said Primitive Education had no full metadata. PR #39 has all 45, and the contract now records it.

## Checks that passed without change
Finance gates run before the registry rebuild. The provenance and registry validators and the full suite run after it. `validate_audit_966.py` deliberately does not run after the rebuild, because it pins the committed bytes. Generic runs need neither framework flag. All 57 title witnesses and the real comparisons pass without edits.

## Tests
New tests were run on the old code first and failed: 5 in the framework file and 7 guard cases. After the fixes, the full suite gives 484 passed, 1 skipped on Python 3.12.14, plus 26 framework tests. Ruff, the secret scan, `check-all` and `validate_audit_966.py` pass. See the PR for the hosted result. `actionlint` was not run.

## Remaining limits
- All these gates are structural. A long meaningless sentence, or a two-word title fragment that is irrelevant to the rule, still passes. Only a reader can judge meaning.
- Plan provenance is page-level, not rule-level.
- `THUMBNAIL_OBSERVATION` text is unverified analyst text.
- **Registry pin:** `validate_audit_966.py` freezes the registry DB hash, so with this gate on, any registry change fails CI until the owner decides how a new registry version relates to the audit baseline. See `docs/VISUAL_FORENSICS_IDENTITY_CONTRACT.md`.

## Addendum: frozen registry separation (`9c31d952`)
Not independently reviewed: same author session, tests only.

The frozen audit reads `audit-baseline/youtube_channel_registry.frozen.db`, an LFS pointer to the original `39e7a28b…` object. `MANIFEST.json` and `BASELINE_VALIDATION.json` are unchanged. `validate_audit_966.py --current-registry` runs after the CI rebuild and requires the live registry to keep every audited video and transcript.

Local trials in a disposable clone with real Git history, CI order:

| Tree | Gates | Suite |
|---|---|---|
| Head | Pass | 495 passed, 1 skipped |
| Head + PR #20 (registry `5538db9f…`) | Pass | 494 passed, 1 failed, 1 skipped |
| Head + #37, #43, #39 | Pass | 495 passed, 1 skipped; the 3 earlier ledger failures came from the non-Git export |
| Head + #20, pinned copy overwritten by the live DB | Frozen audit fails `source drift` | Not run |

The one failure is the crosswalk test: it requires a crosswalk rebuild, because #20 registers two listed xkcd videos. Rebuild it when #20 is integrated.

Limit: `check-all` still reads the live registry, so a changed witnessed transcript fails there. That is intended.
