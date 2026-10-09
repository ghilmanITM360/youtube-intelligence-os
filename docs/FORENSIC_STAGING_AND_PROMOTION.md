# Forensic staging and promotion

The current implementation uses a read-only adapter, deterministic normalized staging and a reviewed promotion index. The authoritative executable commands and current counts live in [What If integration workflow](WHAT_IF_INTEGRATION_WORKFLOW.md#data-flow-and-durable-local-staging).

Staging is generated at `data/staging/what-if-forensic/v1.0.0/`, ignored by Git. Configure `YIOS_WHAT_IF_CORPUS_ROOT`; source media stays external. The deterministic manifest records accepted, held and rejected rows, table checksums and catalog identity digest. A separate lifecycle receipt records creation time and manifest checksum. Do not hand-edit either artifact.

Run stage twice and promotion twice. Repeated identical input reports UNCHANGED. Promotion revalidates bytes, provenance, identities and observation keys; conflicts fail rather than overwrite an existing index. Unresolved and verified-but-unregistered sources remain held.

[Editing/Visual consumption](WHAT_IF_INTEGRATION_WORKFLOW.md#promotion-and-editingvisual-consumption) queries all eight approved MASTER tables and produces cited hypotheses. Historical authored blueprints remain preserved; the orchestrator extends its generated production blueprint with matching forensic guidance. Missing staging retains fallback behavior; tampered staging fails closed.

For future forensic channels, establish a separately reviewed source contract, canonical identity crosswalk, release validation and channel-specific promotion index first. The present adapter/query routing is What If-specific; generic multi-channel forensic ingestion is not implemented. Never reuse CH-000004 evidence as another channel's observations.
