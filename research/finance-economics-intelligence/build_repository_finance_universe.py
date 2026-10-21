#!/usr/bin/env python3
"""Build the repository-wide Finance/Economics universe from immutable ledgers."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reconciliation-all-repository-2026-10-21"
CASUAL_COMMIT = "fb1e56d03e5ad53086c74247cd2972b262d09b78"
CASUAL_PATH = "research/casually-finance-success-playbook/VIDEO_PERFORMANCE.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def git_blob(commit: str, path: str) -> str:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


FIELDS = [
    "video_id", "channel_id", "channel_name", "channel_url", "niche", "sub_niche",
    "population_layer", "source_dataset", "source_commit", "source_row", "title",
    "video_url", "inclusion_decision", "decision_confidence", "metadata_status",
    "transcript_status", "thumbnail_status", "local_media_status", "audit_status",
    "duplicate_of", "blocker",
]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    baseline = read_csv(ROOT / "audit-baseline/VIDEO_MASTER.csv")
    exp12 = read_csv(ROOT / "expansion-12-channel-2026-10-20/FINANCE_EXPANSION_MASTER.csv")
    monkey = read_csv(ROOT / "expansion-monkey-explains-1999-2026-10-21/FINANCE_EXPANSION_MASTER.csv")
    landscape = read_csv(ROOT / "LANDSCAPE_VIDEOS.csv")
    casual_text = git_blob(CASUAL_COMMIT, CASUAL_PATH)
    casual = list(csv.DictReader(io.StringIO(casual_text)))
    audits = {json.loads(line)["identity"]["Video_ID"]: json.loads(line) for line in
              (ROOT / "VIDEO_AUDIT_966.jsonl").read_text(encoding="utf-8").splitlines() if line}

    prior_ids = {r["Video_ID"] for r in baseline} | {r["video_id"] for r in exp12} | {r["video_id"] for r in monkey}
    landscape_ids = {r["Video_ID"] for r in landscape}
    casual_ids = {r["Video_ID"] for r in casual}
    assert [len(baseline), len(exp12), len(monkey), len(landscape), len(casual)] == [966, 197, 63, 180, 206]
    assert not (landscape_ids & prior_ids or casual_ids & prior_ids or landscape_ids & casual_ids)

    rows: list[dict[str, object]] = []
    for i, r in enumerate(baseline, 2):
        a = audits[r["Video_ID"]]
        done = all(v == "COMPLETE_LIMITED_EVIDENCE" for v in a.get("statuses", {}).values())
        rows.append(dict(zip(FIELDS, [r["Video_ID"], r["Channel_ID"], r["Channel"],
            f'https://www.youtube.com/channel/{r["Channel_ID"]}', "FINANCE_ECONOMICS", r.get("Topic_tags_provisional", "UNCLASSIFIED"),
            "FROZEN_ORIGINAL_966", r["Dataset"], "FROZEN_BASELINE_MANIFEST", f"audit-baseline/VIDEO_MASTER.csv:{i}", r["Title"], r["URL"],
            "INCLUDE", "HIGH", "AVAILABLE", a.get("script", {}).get("availability", "UNKNOWN"),
            "AVAILABLE" if a.get("thumbnail", {}).get("image_path") else "URL_OR_NOT_AVAILABLE", "SEE_MEDIA_REGISTRY",
            "DEEP_AUDIT_COMPLETE" if done else "NOT_DEEP_AUDITED", "", "" if done else "FROZEN_ORDER_AUDIT_PENDING"])))
    for layer, source, records in [
        ("EXPANSION_12_CHANNEL_197", "expansion-12-channel-2026-10-20/FINANCE_EXPANSION_MASTER.csv", exp12),
        ("EXPANSION_MONKEY_63", "expansion-monkey-explains-1999-2026-10-21/FINANCE_EXPANSION_MASTER.csv", monkey),
    ]:
        for i, r in enumerate(records, 2):
            rows.append(dict(zip(FIELDS, [r["video_id"], r["channel_id"], r["channel_name"], r["channel_url"], "FINANCE_ECONOMICS",
                r.get("scope_label", "UNCLASSIFIED"), layer, source, r.get("acquisition_commit") or r.get("source_commit", ""), f"{source}:{i}",
                r["title"], r["watch_url"], "INCLUDE", r.get("decision_uncertainty") or r.get("decision_confidence", "HIGH"), "AVAILABLE",
                r.get("transcript_status") or ("AVAILABLE" if r.get("captions_or_transcript_available") == "true" else "NOT_REGISTERED"),
                r.get("thumbnail_status") or "URL_AVAILABLE", "SEE_MEDIA_REGISTRY", r["analysis_completion"], "", "INDIVIDUAL_DEEP_AUDIT_PENDING"])))

    additions: list[dict[str, object]] = []
    for i, r in enumerate(landscape, 2):
        row = dict(zip(FIELDS, [r["Video_ID"], r["Channel_ID"], r["Channel"], f'https://www.youtube.com/channel/{r["Channel_ID"]}',
            "FINANCE_ECONOMICS", "CHANNEL_SCOPED_FINANCE_ECONOMICS", "REPOSITORY_RECONCILIATION_2026_10_21",
            "LANDSCAPE_VIDEOS.csv", "4d3f4e76608b3ca34f9f0e5450de5a9521640eba", f"LANDSCAPE_VIDEOS.csv:{i}", r["Title"],
            f'https://www.youtube.com/watch?v={r["Video_ID"]}', "INCLUDE", "MEDIUM", "TITLE_AND_SNAPSHOT_AVAILABLE", "NOT_REGISTERED",
            "NOT_REGISTERED", "NOT_REGISTERED", "METADATA_ONLY_NOT_DEEP_AUDITED", "", "DESCRIPTION_TRANSCRIPT_THUMBNAIL_NOT_REGISTERED"])); additions.append(row); rows.append(row)
    for i, r in enumerate(casual, 2):
        row = dict(zip(FIELDS, [r["Video_ID"], "UCrNfRFWnLC3tCy1TnyhVQ7g", "Casually Finance", "https://www.youtube.com/channel/UCrNfRFWnLC3tCy1TnyhVQ7g",
            "FINANCE_ECONOMICS", r.get("Topic_Family", "UNCLASSIFIED"), "REPOSITORY_RECONCILIATION_2026_10_21", CASUAL_PATH, CASUAL_COMMIT,
            f"{CASUAL_PATH}:{i}", r["Title"], r["URL"], "INCLUDE", r.get("Confidence", "MEDIUM"), "AVAILABLE",
            "PARTIAL_SELECTED_FORENSICS" if "SELECTED" in r.get("Content_Format", "") else "NOT_REGISTERED", "REFERENCE_AVAILABLE" if r.get("Thumbnail_Reference") else "URL_METADATA_ONLY",
            "NOT_REGISTERED", "METADATA_ONLY_NOT_DEEP_AUDITED", "", "FULL_INDIVIDUAL_DEEP_AUDIT_PENDING"])); additions.append(row); rows.append(row)

    # Candidate directory: enumerated video channels plus repository-verified identity-only finance targets.
    channels: dict[str, dict[str, str]] = {}
    for r in rows:
        channels[str(r["channel_id"])] = {"channel_id": str(r["channel_id"]), "channel_name": str(r["channel_name"]), "channel_url": str(r["channel_url"]),
            "status": "VIDEO_DATASET_INCLUDED", "eligible_video_count": "0", "source": str(r["source_dataset"]), "notes": ""}
    for cid, count in Counter(str(r["channel_id"]) for r in rows).items(): channels[cid]["eligible_video_count"] = str(count)
    targets = read_csv(ROOT.parent.parent / "data/manifests/YOUTUBE_CHANNEL_TARGETS.csv")
    keywords = ("finance", "invest", "money", "retire", "dividend")
    for t in targets:
        if t["extraction_status"] == "NOT_EXTRACTED" and any(k in (t["channel_name"] + " " + t["current_handle"]).lower() for k in keywords):
            channels.setdefault(t["canonical_channel_id"], {"channel_id": t["canonical_channel_id"], "channel_name": t["channel_name"],
                "channel_url": t["canonical_url"], "status": "IDENTITY_ONLY_NEEDS_DATA", "eligible_video_count": "0",
                "source": "data/manifests/YOUTUBE_CHANNEL_TARGETS.csv", "notes": "No repository video corpus; no videos inferred."})
    supplied = read_csv(ROOT / "expansion-12-channel-2026-10-20/CHANNEL_CLASSIFICATION_SUMMARY.csv")
    for s in supplied:
        cid = s["channel_id"]
        if cid not in channels:
            channels[cid] = {"channel_id": cid, "channel_name": s["channel_name"], "channel_url": f"https://www.youtube.com/channel/{cid}",
                "status": "VIDEO_DATASET_EXCLUDED_AFTER_INDIVIDUAL_CLASSIFICATION", "eligible_video_count": s.get("eligible_rows", "0"),
                "source": "expansion-12-channel-2026-10-20/FINANCE_INCLUSION_CROSSWALK.csv", "notes": "Complete source retained; no eligible unique additions."}

    medium = [r for r in read_csv(ROOT / "expansion-monkey-explains-1999-2026-10-21/FINANCE_INCLUSION_CROSSWALK.csv")
              if r["finance_decision"] == "INCLUDE" and r["decision_confidence"] == "MEDIUM"]
    review = [{"video_id": r["video_id"], "title": r["title"], "description": r["description"], "prior_decision": "INCLUDE",
               "review_decision": "INCLUDE", "review_confidence": "MEDIUM", "evidence_review": "TITLE_AND_DESCRIPTION_REVIEWED",
               "transcript_status": "NOT_REGISTERED", "reason": "Direct economic/business mechanism remains present, but no transcript is registered; confidence is not upgraded."} for r in medium]

    write_csv(OUT / "FINANCE_UNIVERSE.csv", rows, FIELDS)
    write_csv(OUT / "NEW_ELIGIBLE_ADDITIONS.csv", additions, FIELDS)
    write_csv(OUT / "CHANNEL_DIRECTORY.csv", sorted(channels.values(), key=lambda x: (x["channel_name"].lower(), x["channel_id"])),
              ["channel_id", "channel_name", "channel_url", "status", "eligible_video_count", "source", "notes"])
    write_csv(OUT / "MONKEY_MEDIUM_CONFIDENCE_REVIEW.csv", review,
              ["video_id", "title", "description", "prior_decision", "review_decision", "review_confidence", "evidence_review", "transcript_status", "reason"])
    validation = {"status": "PASS", "original": len(baseline), "expansion_12_channel": len(exp12), "expansion_monkey": len(monkey),
        "prior_total": len(prior_ids), "landscape_additions": len(landscape_ids), "casually_finance_additions": len(casual_ids),
        "new_additions": len(additions), "combined_total": len(rows), "unique_video_ids": len({r["video_id"] for r in rows}),
        "pairwise_overlap": 0, "deep_complete_original": sum(r["audit_status"] == "DEEP_AUDIT_COMPLETE" for r in rows),
        "remaining_deep_audit": sum(r["audit_status"] != "DEEP_AUDIT_COMPLETE" for r in rows), "medium_monkey_reviewed": len(review),
        "casual_source_commit": CASUAL_COMMIT, "casual_source_sha256": sha(casual_text.encode()),
        "landscape_source_sha256": sha((ROOT / "LANDSCAPE_VIDEOS.csv").read_bytes())}
    assert validation["combined_total"] == validation["unique_video_ids"] == 1612
    assert validation["deep_complete_original"] == 430 and validation["remaining_deep_audit"] == 1182
    (OUT / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    hashes = {p.name: sha(p.read_bytes()) for p in sorted(OUT.glob("*")) if p.name != "FILE_CHECKSUMS_SHA256.json"}
    (OUT / "FILE_CHECKSUMS_SHA256.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
