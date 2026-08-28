-- Apify billing metadata can settle shortly after a run reaches SUCCEEDED.
-- Preserve every observed value and mark the reconciled event ledger final.

PRAGMA foreign_keys = ON;

CREATE TABLE apify_run_cost_observations (
    cost_observation_id       TEXT PRIMARY KEY,
    apify_source_run_id       TEXT NOT NULL REFERENCES apify_source_runs(apify_source_run_id),
    observed_at               TEXT NOT NULL,
    usage_total_usd           REAL NOT NULL,
    charged_event_counts_json TEXT,
    event_usage_json          TEXT,
    is_final                  INTEGER NOT NULL CHECK (is_final IN (0, 1)),
    source_locator            TEXT NOT NULL,
    created_at                TEXT NOT NULL,
    notes                     TEXT
);

CREATE INDEX idx_apify_cost_observations_run
    ON apify_run_cost_observations(apify_source_run_id, observed_at);

-- Preserve costs captured by migration 005 before this observation layer existed.
INSERT INTO apify_run_cost_observations
    (cost_observation_id, apify_source_run_id, observed_at, usage_total_usd,
     charged_event_counts_json, event_usage_json, is_final, source_locator,
     created_at, notes)
SELECT printf('APIFYCOST-%06d', ROW_NUMBER() OVER (ORDER BY apify_source_run_id)),
       apify_source_run_id, created_at, run_cost_usd, NULL, NULL, 0,
       'apify_source_runs.run_cost_usd', created_at,
       'Cost observed before charged-event reconciliation was implemented.'
FROM apify_source_runs
WHERE run_cost_usd IS NOT NULL;

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (6, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Append-only Apify run-cost observations for eventual billing reconciliation.');
