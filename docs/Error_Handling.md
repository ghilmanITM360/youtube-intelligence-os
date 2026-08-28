# Error Handling

A design specification for how the YouTube Intelligence OS should classify and respond to errors. No error class here is implemented as code yet — this defines the vocabulary and rules future implementation must follow.

## Governing principles

```text
FAIL LOUDLY ON DATA CORRUPTION

CONTINUE SAFELY ON NON-CRITICAL PARTIAL FAILURES

NEVER FAKE SUCCESS
```

A future user-facing error must be specific (names the actual file/dataset/step), actionable (says what a human can do next), non-destructive (never "fixes" the problem by silently deleting, overwriting, or reinterpreting the source), and provenance-aware (says which source/record is affected, not just "an error occurred").

## Error classes

For each class: severity, retryability, whether processing continues, whether human review is required, what gets logged, and whether it may ever be silently ignored.

| Class | Severity | Retryable | Processing continues? | Human review required? | Never silently ignored because |
|---|---|---|---|---|---|
| `SourceNotFound` | High | No | Halt for that source | Yes | The requested path may not exist, or may be a near-miss of a real path (as this task required checking) — guessing is worse than asking. |
| `UnreadableSource` | High | Sometimes (permissions) | Halt for that source | Yes | Silent skip would produce an inventory that looks complete but isn't. |
| `UnsupportedFile` | Low | No | Continue, record as Unknown | Only if volume is high | A merely-unsupported type is not corruption; forcing a category would be worse. |
| `ArchiveError` | High | No | Halt for that archive | Yes | A malformed archive may hide data loss elsewhere in the set. |
| `UnsafeArchive` | Critical | No | Halt for that archive, refuse extraction | Yes | Path traversal, zip bombs, and symlink escapes are safety issues, not data issues (`docs/Security.md` §7). |
| `HashFailure` | Critical | Yes (retry once) | Halt for that file | Yes | Without a hash, duplicate/revision detection cannot be trusted at all. |
| `DuplicateDetected` | Info | N/A | Continue, record relationship | No | Expected outcome, not a failure — but must be recorded, never silently deduplicated away. |
| `ProbableDuplicate` | Low | N/A | Continue, flag for review | Yes | Byte-level certainty is absent; a human (or stronger evidence) must confirm. |
| `RevisionDetected` | Info | N/A | Continue, record relationship | Sometimes | Which revision is authoritative is often a human judgment call. |
| `ClassificationUncertain` | Low | N/A | Continue, record as Unknown/Uncategorized | Sometimes | `docs/DATA_CLASSIFICATION.md` already requires this rather than forcing a wrong class. |
| `ExtractionFailure` | Medium | Yes | Continue for other files, halt for this one | If repeated | One bad PDF must not stop an entire batch, but must not be silently dropped either. |
| `OCRFailure` | Medium | Yes | Continue, mark unreadable | If repeated | Matches the "use UNKNOWN, never invent" rule already used for illegible screenshot values in this task's own findings. |
| `TranscriptFailure` | Medium | Yes | Continue, mark missing | If systemic | The Phase 0.5 evidence set already contains a real instance: one of 159 videos has no transcript because YouTube had no captions — recorded as missing, not fabricated. |
| `MalformedData` | High | No | Halt for that record | Yes | A malformed CSV/JSON row silently coerced to "closest guess" corrupts every downstream derivation. |
| `MissingProvenance` | Critical | No | Halt for that record | Yes | A fact with no traceable source violates the provenance model outright (`docs/Database.md` §1). |
| `EvidenceConflict` | High | No | Continue, flag both records | Yes | Two sources disagree (e.g. two near-identical guide PDFs with different content) — resolving in favor of either without review is a fabrication risk. |
| `UnsupportedClaim` | High | No | Continue, tag as `SUSPECT` | Yes | A number or claim with no visible measurement behind it (`docs/Database.md` §1, `SUSPECT` state) — matches the forensic report's own discipline of marking unmeasurable claims as such rather than inventing them. |
| `ResearchFailure` | Medium | Yes | Continue for other sources | If repeated | A single failed web fetch should not invalidate an entire research pass. |
| `WebFetchFailure` | Medium | Yes | Continue | If repeated | Network/service failures are expected and must not be conflated with data corruption. |
| `RateLimit` | Low | Yes (backoff) | Pause, resume | No, unless persistent | Expected operational condition under §6 of `docs/Security.md`. |
| `CostCapExceeded` | Critical | No | Halt before Actor invocation when planned cost exceeds the approved cap; halt ingestion if finalized billing exceeds it | Yes | Paid acquisition must never silently exceed the explicit ceiling. |
| `AmbiguousIdentity` | High | No | Halt channel merge/registration | Yes | Similar names alone cannot prove that screenshot evidence and a live channel are the same competitor. |
| `PromptInjectionRisk` | Critical | No | Halt the offending prompt/step | Yes | Detected embedded instructions in fetched/scraped content must never be silently executed or silently discarded — they must be surfaced (`docs/Security.md` §5, `docs/Prompts.md` §3). |
| `ToolFailure` | Medium | Depends on tool | Continue if tool is non-essential to the step | If it recurs | External tool failures (`docs/TOOLS_INSTALLED.md`) must not be conflated with application-data errors. |
| `PartialIngestion` | High | No | Halt, report exactly what completed | Yes | A half-copied dataset must never be recorded as fully ingested. |
| `ManifestValidationFailure` | High | No | Halt for that manifest | Yes | An invalid manifest breaks the traceability the whole inventory system depends on. |
| `DatabaseFailure` | Critical | Depends | Halt | Yes | Not applicable until Phase 10, but reserved now so it is not designed as an afterthought later. |
| `PermissionFailure` | High | No | Halt for that action | Yes | Especially relevant to the read-only guarantee over external source folders (`docs/Security.md` §1, `docs/DECISIONS.md` Decision 010). |
| `SecurityViolation` | Critical | No | Halt immediately | Yes | Covers anything in `docs/Security.md` — secret exposure, unsafe archive behavior, credential misuse. Always the highest priority to surface. |

## Rules that cut across every class

- **`Critical` and most `High` severity classes halt** rather than continue in a degraded, unverifiable state — this is the "fail loudly on data corruption" principle in practice.
- **`Info` and most `Low` severity classes continue**, because they represent expected, non-corrupting conditions (a duplicate, an unsupported file type) — this is "continue safely on non-critical partial failures."
- **No class may be silently absorbed into a generic success message.** A batch that partially failed must report exactly what succeeded and what didn't (`PartialIngestion` exists specifically to prevent "fake success").
- Every logged error must name the specific file, dataset, or record it concerns — a global "processing failed" message with no target is not compliant with this specification.
- Human review requirements listed above are minimums; a future implementation may require review in additional cases but may not remove a review requirement marked "Yes" here without an explicit decision recorded in `docs/DECISIONS.md`.
