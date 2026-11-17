"""Write videos/<id>/quality_gate_visual_v1.json from closure_v1 evidence. usage: closure_gate_v1.py <id> <status> [failing_gate=blocker ...]"""
import json, subprocess, sys, pathlib
v, status = sys.argv[1], sys.argv[2]; fails = dict(a.split("=", 1) for a in sys.argv[3:])
b = pathlib.Path.home() / f"YIOS-local-audits/xkcd-whatif/videos/{v}"; c = json.load(open(b / "closure_v1/checks.json"))
assert c["V1"]["pass"] and c["V2"]["pass"], "identity/coverage failed"
names = ["V1_source_identity", "V2_full_temporal_overview", "V3_candidate_shots_verified", "V4_meaningful_state_timing", "V5_motion_design_review", "V6_creative_design_review", "V7_production_blueprint"]
g = {n: ("PARTIAL: " + fails[n[:2]]) if n[:2] in fails else "PASS" for n in names}
assert (status == "VISUAL_ANALYSIS_COMPLETE") == (not fails)
for f in ["CLOSURE.md", "reconstruction_blueprint_v2.md"]: assert (b / "closure_v1" / f).exists(), f
q = {"video_id": v, "source_sha256": c["V1"]["sha_recomputed"], "contract": "asset_library/_channel/ct_closure/VISUAL_CLOSURE_CONTRACT_v1.md (sha a54b6c3c)",
     "generated_utc": subprocess.run(["date", "-u", "+%FT%TZ"], capture_output=True, text=True).stdout.strip(), "visual_gates": g,
     "evidence": {"V1_V2": "closure_v1/checks.json", "V3": "shot_ledger.csv + native before/after frames (closure_v1/native)", "V4": "closure_v1/CLOSURE.md §V4 + strip_*.png",
                  "V5": "rv1 every-frame activity views + closure_v1/activity_curves.csv + checks.json hold stillness", "V6": "closure_v1/holds_*.jpg (viewed) + CLOSURE.md §V6", "V7": "closure_v1/reconstruction_blueprint_v2.md"},
     "separate_not_required": {"visual_script_mapping": "PARTIAL (ASR_UNCERTIFIED)", "audio_human_listening": "BLOCKED_CAPABILITY", "final_av_signoff": "BLOCKED", "render_test": "NOT_DONE"},
     "final_video_status": status, "status_scope": "visual-only; implies nothing about sound", "ct_scan_complete": False, "full_av_signoff": False,
     "reviewer": "claude deepvf-ct1 (single model reviewer; no human second review)"}
json.dump(q, open(b / "quality_gate_visual_v1.json", "w"), indent=1); print(v, status, q["generated_utc"])
