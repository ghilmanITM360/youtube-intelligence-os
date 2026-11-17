# Importer trial, 2026-11-06

Ran in a disposable clone with real Git history, on PR #45 `9c31d952` + PR #20 `e9b56960` + this branch at `081b8dc0`. Nothing from it was committed. Local runs only; no hosted run has executed this route.

| Step | Result |
|---|---|
| `register_supplied_channel.py`, all four workbooks | Exit 0: DS-000036 to DS-000039, 265 videos, 0 transcripts |
| Registry rebuild, `validate_dataset_ledgers` | Pass |
| `validate_audit_966.py` (frozen), `--current-registry` | Pass |
| Registry videos | Casual Finance 210, xkcd 91, Barely Evolved 4, Primitive Education 45; total 2,570 |
| Zero likes or comments | 0 rows. Unknown values are NULL |
| `validate_youtube_channel_registry` | **Fail, so these rows are not ready to register** |

The validator failure has two parts:

1. Its `EXPECTED` control counts are deliberately pinned, for example `videos: expected 2305, found 2570`. A registration PR has to update them on purpose, as PR #20 does.
2. A real gap: `identity_only_with_videos: expected 0, found 1`. The registry builder keeps Casual Finance in the `IDENTITY_ONLY` group after its videos arrive. The builder must move it before Casual Finance can be registered. That change is not in this PR.

The full pytest suite was not run on this tree, because the validator already fails on it.
