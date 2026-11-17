#!/usr/bin/env python3
"""Build the versioned MonkeyExplains1999 Finance classification layer.

PR #38's 76-row public VIDEO_MASTER.csv is the source authority. The frozen
966-video baseline and the existing 197-row expansion are read-only inputs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "expansion-monkey-explains-1999-2026-10-21"
SOURCE_COMMIT = "f176aa2861cd93913b977e6159a4e00f4eabeacc"
SOURCE_PATH = "research/monkey-explains-1999/VIDEO_MASTER.csv"

# Every public PR #38 Video ID appears in exactly one scope set. Inclusion is
# based on that row's title and description, never inferred from channel name.
SCOPES = {
    "CORPORATE_FINANCE_AND_AI_ECONOMICS": {
        "jkg3EdgDomA", "IcF5bkUqPEk", "VhY4CwtKOXI", "HoMjC5lG6Sk",
        "PolXkEFii0I", "JIjYxq1Mrd0", "_TMPLVQAHWE", "DS6p9pEwCPs",
        "NwlK1JNTcVc", "aFBzmWYxTrI", "JOdT__l2JW0", "TNeFuLVGcF0",
        "eXbZrx5XW_k", "sy4HzG_qzKw", "vS_jHcn44E8", "0F_g33QeVNU",
        "9_3u5CBH6Ao", "LfQIJgU_W2w",
    },
    "MACROECONOMICS_AND_PUBLIC_FINANCE": {
        "5x5IaKO6R5I", "xrB226MIYyc", "yDAXLQf0JWM", "9vpo6p-7J1I",
        "pNCikeQLUIU", "GQG-yWSSdDk", "t8XaaB2pweI", "ZI3jXGJKRNM",
        "zhut9AwrLCA", "uhTPO2d1-Sg", "-VIePVPmMGw", "Bzko_V-a13M",
        "68t0UQTpk8o", "IfOREULEqRU", "ZyHwdD26BtY", "rgm0ZDdNLOA",
        "C2K-FryxkW8", "fw0z4xdJNww", "Jz7pmE66OqE", "bz0OGtrkjv0",
        "DU_12IG1Tq8", "-KYcpnbWw7w", "bPHZkC1XLcE",
    },
    "BUSINESS_AND_INDUSTRY_ECONOMICS": {
        "ynXi_xdGbEY", "5Frw2nTsFQg", "l3yWpDmRXk8", "KEstu4enF88",
        "TSJQ8SjcTPk", "jnywipYaaeA", "AQfVMwa5uds", "zLDMOAlWLfc",
    },
    "FINANCE_INVESTING_AND_FINANCIAL_CRIME": {
        "JY-mDrPh5nY", "BHg5pLQmIew", "v1s5qXyxmVo", "hn5RqOTOlhk",
        "xTFdCPKduy4", "6sz9FpHgAWU", "Z1uq829DXlg", "JZEK8JBPbo4",
        "Au_o2muXosc", "RI_Ghw97qRM", "d_Qctc0Pc5s", "dHy07B-UHkE",
        "U5Iq4EGSZ78", "_DB-LtipBss",
    },
}

EXCLUDED = {
    "VY9zxl-YqGo": "OUT_OF_SCOPE_PLATFORM_POLICY",
    "ktOignjy2TE": "OUT_OF_SCOPE_CONSUMER_PRODUCT_COMMENTARY",
    "OQgRqLUmvPk": "OUT_OF_SCOPE_POLITICAL_CRIME",
    "84YaEDQMY1c": "OUT_OF_SCOPE_LEGAL_POLITICS",
    "cCc5sgsrtCc": "OUT_OF_SCOPE_DEFENSE_AND_AI_POLICY",
    "Y41XmFbsG2s": "OUT_OF_SCOPE_SOCIAL_MEDIA_CULTURE",
    "aK-6iq0cdbo": "OUT_OF_SCOPE_GEOPOLITICS",
    "mVRXhCkrtf8": "OUT_OF_SCOPE_SOCIAL_MEDIA_POLICY",
    "UqaDQHAIlts": "OUT_OF_SCOPE_CYBERSECURITY",
    "PejedlEOsh0": "OUT_OF_SCOPE_POLITICAL_PROTEST",
    "Zj4Turqu1EU": "OUT_OF_SCOPE_ONLINE_SAFETY",
    "cvKe_WYeITU": "OUT_OF_SCOPE_GENERAL_TECHNOLOGY",
    "v-2hJnwK5yw": "OUT_OF_SCOPE_CRIME_EXPLAINER",
}

MEDIUM_CONFIDENCE = {
    "jkg3EdgDomA", "TNeFuLVGcF0", "5Frw2nTsFQg", "KEstu4enF88",
    "uhTPO2d1-Sg", "TSJQ8SjcTPk", "Bzko_V-a13M", "6sz9FpHgAWU",
    "rgm0ZDdNLOA", "zLDMOAlWLfc",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def import_source() -> None:
    data = subprocess.check_output(["git", "show", f"{SOURCE_COMMIT}:{SOURCE_PATH}"])
    OUT.mkdir(exist_ok=True)
    (OUT / "FULL_CHANNEL_SOURCE.csv").write_bytes(data)


def classification(video_id: str) -> tuple[str, str, str, str]:
    if video_id in EXCLUDED:
        return (
            "EXCLUDE", "HIGH", EXCLUDED[video_id],
            "The actual title and description make a non-finance subject primary; incidental business, money, or economic language is insufficient.",
        )
    for scope, ids in SCOPES.items():
        if video_id in ids:
            confidence = "MEDIUM" if video_id in MEDIUM_CONFIDENCE else "HIGH"
            return (
                "INCLUDE", confidence, scope,
                "The actual title and description directly address finance, economics, markets, public finance, labor, trade, corporate finance, or an industry business model.",
            )
    raise ValueError(f"Unclassified public Video ID: {video_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--import-source", action="store_true", help="Materialize PR #38 CSV from its immutable commit")
    args = parser.parse_args()
    if args.import_source:
        import_source()

    source_path = OUT / "FULL_CHANNEL_SOURCE.csv"
    if not source_path.exists():
        raise SystemExit("Missing FULL_CHANNEL_SOURCE.csv; run once with --import-source")
    rows = read_csv(source_path)
    baseline = read_csv(HERE / "audit-baseline" / "VIDEO_MASTER.csv")
    prior = read_csv(HERE / "expansion-12-channel-2026-10-20" / "FINANCE_EXPANSION_MASTER.csv")
    baseline_ids = {row["Video_ID"] for row in baseline}
    prior_ids = {row["video_id"] for row in prior}
    source_ids = {row["video_id"] for row in rows}
    declared = set().union(*SCOPES.values(), EXCLUDED)

    if len(rows) != 76 or len(source_ids) != 76:
        raise SystemExit("PR #38 public collection must contain exactly 76 unique videos")
    if source_ids != declared:
        raise SystemExit(f"Classification coverage mismatch: missing={sorted(source_ids-declared)} extra={sorted(declared-source_ids)}")
    if Counter(row["video_type"] for row in rows) != {"REGULAR": 61, "SHORT": 15}:
        raise SystemExit("PR #38 public format split is not 61 REGULAR + 15 SHORT")
    if any(row["availability_status"] != "PUBLIC_ACCESSIBLE_AT_RETRIEVAL" for row in rows):
        raise SystemExit("Restricted/non-public record found in the 76-row public source")
    if len(baseline_ids) != 966 or len(prior_ids) != 197 or baseline_ids & prior_ids:
        raise SystemExit("Existing 966 + 197 population contract failed")

    crosswalk = []
    additions = []
    duplicates = []
    for row in rows:
        decision, confidence, scope, reason = classification(row["video_id"])
        duplicate_layer = "NONE"
        if row["video_id"] in baseline_ids:
            duplicate_layer = "FROZEN_966"
        elif row["video_id"] in prior_ids:
            duplicate_layer = "EXISTING_197"
        disposition = "INCLUDE_UNIQUE_EXPANSION" if decision == "INCLUDE" and duplicate_layer == "NONE" else ("DUPLICATE_PRIOR_POPULATION" if duplicate_layer != "NONE" else "OUT_OF_SCOPE")
        classified = {
            "video_id": row["video_id"], "channel_id": row["channel_id"],
            "channel_name": row["channel_name"], "video_type": row["video_type"],
            "title": row["title"], "description": row["description"],
            "finance_decision": decision, "decision_confidence": confidence,
            "scope_label": scope, "decision_reason": reason,
            "duplicate_layer": duplicate_layer, "expansion_disposition": disposition,
            "analysis_completion": "METADATA_ONLY_NOT_DEEP_AUDITED",
            "source_commit": SOURCE_COMMIT,
            "raw_dataset_row_locator": row["raw_dataset_row_locator"],
        }
        crosswalk.append(classified)
        if duplicate_layer != "NONE":
            duplicates.append(classified)
        if disposition == "INCLUDE_UNIQUE_EXPANSION":
            additions.append({**row, **classified})

    crosswalk_fields = list(crosswalk[0])
    write_csv(OUT / "FINANCE_INCLUSION_CROSSWALK.csv", crosswalk, crosswalk_fields)
    write_csv(OUT / "DUPLICATE_OVERLAP_WITH_PRIOR_POPULATION.csv", duplicates, crosswalk_fields)
    master_fields = list(rows[0]) + [field for field in crosswalk_fields if field not in rows[0]]
    write_csv(OUT / "FINANCE_EXPANSION_MASTER.csv", additions, master_fields)

    eligible = sum(row["finance_decision"] == "INCLUDE" for row in crosswalk)
    excluded = len(rows) - eligible
    combined_ids = baseline_ids | prior_ids | {row["video_id"] for row in additions}
    summary = [{
        "channel_name": rows[0]["channel_name"], "channel_id": rows[0]["channel_id"],
        "public_captured": str(len(rows)), "regular": "61", "shorts": "15",
        "restricted_excluded_from_public_count": "45", "finance_eligible": str(eligible),
        "prior_population_duplicates": str(len(duplicates)),
        "unique_finance_additions": str(len(additions)), "finance_excluded": str(excluded),
        "classification_basis": "INDIVIDUAL_VIDEO_TITLE_DESCRIPTION_METADATA",
    }]
    write_csv(OUT / "CHANNEL_CLASSIFICATION_SUMMARY.csv", summary, list(summary[0]))

    validation = {
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_branch": "research/monkey-explains-1999-metadata",
        "source_commit": SOURCE_COMMIT,
        "source_pr": 38,
        "source_public_video_master_sha256": sha256(source_path),
        "public_rows": len(rows), "public_unique_video_ids": len(source_ids),
        "regular": 61, "shorts": 15, "restricted_excluded_from_public_count": 45,
        "finance_eligible": eligible, "prior_population_duplicates": len(duplicates),
        "finance_excluded": excluded, "unique_finance_additions": len(additions),
        "frozen_original_unique_ids": len(baseline_ids),
        "existing_expansion_unique_ids": len(prior_ids),
        "combined_unique_research_population": len(combined_ids),
        "original_deep_complete": 429,
        "original_remaining": len(baseline_ids) - 429,
        "existing_expansion_deep_complete": 0,
        "monkey_expansion_deep_complete": 0,
        "combined_not_deep_audited_or_remaining": len(combined_ids) - 429,
        "next_original_video_id": "R_E6OOnF9e4",
        "checks": {
            "public_76_unique": len(rows) == len(source_ids) == 76,
            "format_split_61_plus_15": Counter(row["video_type"] for row in rows) == {"REGULAR": 61, "SHORT": 15},
            "all_public_at_retrieval": all(row["availability_status"] == "PUBLIC_ACCESSIBLE_AT_RETRIEVAL" for row in rows),
            "all_ids_classified_once": source_ids == declared,
            "baseline_966_unchanged": len(baseline_ids) == 966,
            "existing_197_unchanged": len(prior_ids) == 197,
            "prior_layers_disjoint": not baseline_ids & prior_ids,
            "new_additions_disjoint": not ({row["video_id"] for row in additions} & (baseline_ids | prior_ids)),
            "population_reconciles": len(combined_ids) == 966 + 197 + len(additions),
            "new_metadata_not_deep_audited": all(row["analysis_completion"] == "METADATA_ONLY_NOT_DEEP_AUDITED" for row in additions),
        },
    }
    if not all(validation["checks"].values()):
        validation["status"] = "FAIL"
    (OUT / "EXPANSION_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    provenance = {
        "source_branch": "research/monkey-explains-1999-metadata",
        "source_commit": SOURCE_COMMIT, "source_pr": 38,
        "source_path": SOURCE_PATH, "source_sha256": sha256(source_path),
        "acquisition_repeated": False, "raw_evidence_mutated": False,
        "restricted_records_imported": False,
        "classification_basis": "Each public row's actual title and description.",
        "limitations": [
            "Metadata classification is not a deep audit.",
            "No transcript, thumbnail binary, private analytics, or restricted record was imported.",
            "MEDIUM-confidence inclusions require transcript-level review before substantive findings.",
        ],
    }
    (OUT / "SOURCE_PROVENANCE.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    checksums = {path.name: sha256(path) for path in sorted(OUT.iterdir()) if path.is_file() and path.name != "FILE_CHECKSUMS_SHA256.json"}
    (OUT / "FILE_CHECKSUMS_SHA256.json").write_text(json.dumps(checksums, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
