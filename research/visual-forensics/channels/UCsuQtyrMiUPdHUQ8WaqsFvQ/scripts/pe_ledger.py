"""Per-video campaign ledger from artifacts on disk (deterministic). Usage: python3 -I pe_ledger.py"""
import csv, json, pathlib
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"
sel = json.load(open(W / "selection/selection_v1.json"))["videos"]
cols = ["queue","video_id","split","format","source_timeline","detection_segmentation","native_art","motion_event","transcript_asr","actual_listening","narration_alignment","asset_inventory","production_spec","independent_review","reconstruction_test","kit_validation","publication","final_status"]
rows = []
for r in sel:
    V = W / "videos" / r["video_id"]; R = V / "review" / f'rv1_{r["video_id"]}'; g = {}
    ex = lambda p: (V / p).exists()
    if ex("quality_gate.json"): g = json.load(open(V / "quality_gate.json"))
    st = "PENDING"
    if ex("INGEST_DONE"): st = "IN_PROGRESS"
    if g: st = g["final_video_status"]
    motion = "PENDING"
    if g: motion = g["gates"]["motion_design_review"]
    pub = (V / "PUBLISHED").read_text().split()[3][:10] if ex("PUBLISHED") else "PENDING"
    rows.append(dict(queue=r["queue"], video_id=r["video_id"], split=r["split"], format=r["displayed_format"],
        source_timeline="PASS" if ex("evidence/source_sha256.txt") and (V / "evidence/source_sha256.txt").read_text().split()[0] == r["sha256"] else "PENDING",
        detection_segmentation="PASS" if ex("tables/segments_v1.csv") else "PENDING",
        native_art="PASS_SAMPLED" if ex("review/native_art_review.md") else "PENDING", motion_event=motion,
        transcript_asr="ASR_UNCERTIFIED" if ex("asr/asr_small_en.json") else "PENDING", actual_listening="BLOCKED_CAPABILITY",
        narration_alignment="ASR_ONLY_NOT_AUDIO_VERIFIED" if (R / "narration_visual.csv").exists() and g else "PENDING",
        asset_inventory="PASS" if (R / "asset_inventory.csv").exists() and g else "PENDING",
        production_spec="DRAFT_NOT_RENDERED" if ex("reconstruction_blueprint.md") else "PENDING",
        independent_review="SAME_FAMILY_SUBAGENT+PRIMARY_SPOTCHECK" if ex("review/primary_spotcheck.json") and g else "PENDING",
        reconstruction_test=g.get("gates", {}).get("reconstruction_test", "PENDING"), kit_validation=g.get("overall", "PENDING"), publication=pub, final_status=st))
with open(W / "campaign/campaign_ledger.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
print({s: sum(x["final_status"] == s for x in rows) for s in {x["final_status"] for x in rows}})
