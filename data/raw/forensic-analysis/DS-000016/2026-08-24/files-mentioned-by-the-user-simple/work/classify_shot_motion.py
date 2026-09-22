import json
import math
import sys
from collections import Counter
from pathlib import Path

import cv2
import numpy as np


def estimate_motion(start_path: Path, end_path: Path) -> dict:
    start = cv2.imread(str(start_path), cv2.IMREAD_COLOR)
    end = cv2.imread(str(end_path), cv2.IMREAD_COLOR)
    if start is None or end is None:
        return {"classification": "unavailable", "confidence": "low"}
    gray_start = cv2.cvtColor(start, cv2.COLOR_BGR2GRAY)
    gray_end = cv2.cvtColor(end, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(nfeatures=3000, fastThreshold=7)
    key_start, desc_start = orb.detectAndCompute(gray_start, None)
    key_end, desc_end = orb.detectAndCompute(gray_end, None)
    if desc_start is None or desc_end is None:
        return {"classification": "unresolved_local_or_global_change", "confidence": "low", "matches": 0}
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    pairs = matcher.knnMatch(desc_start, desc_end, k=2)
    matches = [a for a, b in pairs if a.distance < 0.75 * b.distance]
    if len(matches) < 12:
        return {
            "classification": "unresolved_local_or_global_change",
            "confidence": "low",
            "matches": len(matches),
        }
    src = np.float32([key_start[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst = np.float32([key_end[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    matrix, inliers = cv2.estimateAffinePartial2D(
        src,
        dst,
        method=cv2.RANSAC,
        ransacReprojThreshold=2.5,
        maxIters=5000,
        confidence=0.995,
        refineIters=20,
    )
    if matrix is None or inliers is None:
        return {
            "classification": "unresolved_local_or_global_change",
            "confidence": "low",
            "matches": len(matches),
        }
    inlier_ratio = float(np.mean(inliers))
    a, b, tx = matrix[0]
    c, d, ty = matrix[1]
    scale = float(math.sqrt(a * a + b * b))
    rotation = float(math.degrees(math.atan2(b, a)))
    height, width = gray_start.shape
    center = np.array([width / 2, height / 2, 1.0], dtype=np.float64)
    mapped_center = matrix @ center
    center_dx = float(mapped_center[0] - width / 2)
    center_dy = float(mapped_center[1] - height / 2)

    warped = cv2.warpAffine(gray_start, matrix, (width, height), flags=cv2.INTER_LINEAR)
    valid = cv2.warpAffine(np.full_like(gray_start, 255), matrix, (width, height), flags=cv2.INTER_NEAREST)
    mask = valid > 0
    residual = float(np.mean(np.abs(warped[mask].astype(np.float32) - gray_end[mask].astype(np.float32))))

    scale_delta = scale - 1.0
    static = abs(scale_delta) < 0.0025 and abs(center_dx) < 0.8 and abs(center_dy) < 0.8 and residual < 1.2
    if static:
        classification = "static_hold"
    else:
        parts = []
        if scale_delta > 0.007:
            parts.append("digital_push_in")
        elif scale_delta < -0.007:
            parts.append("digital_pull_out")
        if center_dx > 2.0:
            parts.append("content_shifts_right_camera_left")
        elif center_dx < -2.0:
            parts.append("content_shifts_left_camera_right")
        if center_dy > 2.0:
            parts.append("content_shifts_down_camera_up")
        elif center_dy < -2.0:
            parts.append("content_shifts_up_camera_down")
        if not parts:
            parts.append("subtle_global_reframe")
        classification = "+".join(parts)
        if residual > 10.0 or inlier_ratio < 0.45:
            classification += "+possible_local_motion_or_generation_drift"

    confidence = "high" if len(matches) >= 80 and inlier_ratio >= 0.65 else "medium" if len(matches) >= 30 and inlier_ratio >= 0.4 else "low"
    return {
        "classification": classification,
        "confidence": confidence,
        "matches": len(matches),
        "inlier_ratio": round(inlier_ratio, 4),
        "scale_start_to_end": round(scale, 6),
        "rotation_degrees": round(rotation, 4),
        "content_center_dx_px": round(center_dx, 3),
        "content_center_dy_px": round(center_dy, 3),
        "registered_residual_mad": round(residual, 3),
    }


if len(sys.argv) != 3:
    raise SystemExit("Usage: classify_shot_motion.py SHOT_MANIFEST EVIDENCE_DIR")

manifest_path = Path(sys.argv[1])
evidence_dir = Path(sys.argv[2])
frames_dir = evidence_dir / "shot_triplets"
shots = json.loads(manifest_path.read_text(encoding="utf-8"))
for shot in shots:
    start_path = frames_dir / shot["sample_files"]["start"]
    end_path = frames_dir / shot["sample_files"]["end"]
    shot["global_motion_estimate"] = estimate_motion(start_path, end_path)

manifest_path.write_text(json.dumps(shots, indent=2), encoding="utf-8")
counts = Counter(item["global_motion_estimate"]["classification"].split("+")[0] for item in shots)
(evidence_dir / "motion_classification_summary.json").write_text(
    json.dumps({"counts": counts, "shot_count": len(shots)}, indent=2),
    encoding="utf-8",
)
print(json.dumps({"counts": counts, "shot_count": len(shots)}, indent=2))
