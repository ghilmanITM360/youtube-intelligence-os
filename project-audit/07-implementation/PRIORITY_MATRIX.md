# Priority Matrix

| Priority | Quick (≤ 1 day) | Large (> 1 day) |
|---|---|---|
| **Critical** | 1.1 off-device backup of local-only evidence · 1.2 commit untracked work | 1.5 finance CI gates (#45) · 1.6 DB policy · 2.1-2.2 read model · 4.1-4.5 M1 core screens |
| **High** | 1.3 drop duplicate gate commit · 1.4 merge green/doc PRs · 3.1 persona check · 3.2 palette | 1.7 unstack Senior Health · 2.3-2.5 insights/plans/workstreams + API contract · 3.3 prototype · 4.6 plans · 5.1-5.3 charts |
| **Medium** | 1.8 branch cleanup · 1.9 A5/D2/package fixes · 2.6 Datasette spike | 3.4 kitchen sink · 5.4 secondary screens · 5.5 forensics timeline · 6.1 review queue |
| **Optional** | 6.2 dry-run refresh · 6.3 agent prompt copy | 6.4 My Channel · 6.5 remote access |

```mermaid
quadrantChart
  title Value vs effort
  x-axis Low effort --> High effort
  y-axis Low value --> High value
  quadrant-1 Plan carefully
  quadrant-2 Do now
  quadrant-3 Fill-ins
  quadrant-4 Defer
  Backup local evidence: [0.1, 0.95]
  Commit untracked work: [0.08, 0.8]
  Finance CI gates: [0.35, 0.85]
  DB policy: [0.45, 0.85]
  Read model: [0.7, 0.95]
  Datasette spike: [0.15, 0.65]
  M1 core screens: [0.8, 0.9]
  Branch cleanup: [0.15, 0.4]
  Review queue: [0.6, 0.55]
  Remote access: [0.65, 0.2]
  My Channel: [0.55, 0.3]
```
