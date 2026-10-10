# What If rollback

The exact guarded rollback commands live in [integration workflow rollback](WHAT_IF_INTEGRATION_WORKFLOW.md#rollback).

Stage, promotion and query do not write canonical SQLite identities or historical snapshots. Preserve the external source and generated local stage before recovery. For published changes, revert the reviewed merge in a new branch and submit normal PR/CI; never reset shared main or force-push.

Review dependent units and revert newest first. Archive the current ignored stage, regenerate the earlier reviewed contract at its deterministic path, and restore the matching promotion index through a PR. A stage/index mismatch must fail closed until reconciled.

Rollback does not authorize deleting immutable media, required historical evidence or private records from history. Storage/privacy migrations follow [data privacy](DATA_PRIVACY.md).
