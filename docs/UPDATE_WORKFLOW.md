# What If update workflow

Use the exact [candidate-generation and diff commands](WHAT_IF_INTEGRATION_WORKFLOW.md#review-an-update-before-promotion) in the authoritative integration workflow. Preserve the current external corpus, ignored stage and reviewed index before generating a candidate.

1. Validate the immutable source release and all media hashes.
2. Review identity changes against independently acquired exact YouTube IDs and channel ownership. Keep unresolved sources held; the forensic importer never registers videos.
3. Generate a separate candidate stage and index. Inspect counts, holds, checksums, release, transformation and identity differences.
4. Run focused tests, catalog/provenance validators and the full distributable suite. Verify second-run idempotency and no historical snapshot changes.
5. Publish reviewed contract/index/derived-output changes through an isolated branch, commit, push, PR, green CI and exact-head merge. Replace the local generated stage only with the matching validated candidate.

Official channel refresh remains externally blocked: no YouTube Data API credential or existing uploads acquisition implementation is available. The [identity section](WHAT_IF_INTEGRATION_WORKFLOW.md#identity-refresh-and-unresolved-sources) states the required official sequence and current unresolved candidates. Do not substitute title-only matching or an unapproved paid acquisition.

For recovery, use [rollback](ROLLBACK.md). Never edit recorded hashes to hide a mismatch.
