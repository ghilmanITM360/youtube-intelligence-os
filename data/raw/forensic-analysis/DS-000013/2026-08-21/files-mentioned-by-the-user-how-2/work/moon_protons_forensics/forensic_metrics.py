from __future__ import annotations

import re


def frame_time_from_name(name: str) -> float:
    match = re.search(r"frame_(\d+)ms", name)
    if match is None:
        raise ValueError(f"frame filename lacks millisecond timestamp: {name}")
    return int(match.group(1)) / 1000.0


def select_separated_peaks(
    times: list[float], scores: list[float], min_gap: float, limit: int
) -> list[int]:
    ranked = sorted(range(len(times)), key=lambda index: scores[index], reverse=True)
    selected: list[int] = []
    for index in ranked:
        if all(abs(times[index] - times[kept]) >= min_gap for kept in selected):
            selected.append(index)
            if len(selected) == limit:
                break
    return sorted(selected, key=lambda index: times[index])
