"""Small deterministic helpers shared by the forensic measurement pipeline."""

from __future__ import annotations

import re
from collections.abc import Iterable


FRAME_NAME = re.compile(r"^frame_(\d{7})ms\.jpg$")


def parse_frame_time(filename: str) -> float:
    """Return the requested frame time encoded in an extractor filename."""
    match = FRAME_NAME.fullmatch(filename)
    if match is None:
        raise ValueError(f"not a forensic frame filename: {filename}")
    return int(match.group(1)) / 1000.0


def select_peaks(
    samples: Iterable[tuple[float, float]],
    *,
    threshold: float,
    minimum_distance: float,
) -> list[tuple[float, float]]:
    """Choose strongest non-overlapping peaks and return them in time order."""
    eligible = [sample for sample in samples if sample[1] >= threshold]
    selected: list[tuple[float, float]] = []
    for candidate in sorted(eligible, key=lambda item: (-item[1], item[0])):
        if all(abs(candidate[0] - accepted[0]) >= minimum_distance for accepted in selected):
            selected.append(candidate)
    return sorted(selected)


def prompt_measurement(prompt: str) -> tuple[int, bool]:
    """Return Unicode character count and whether the v7.0 ceiling is met."""
    count = len(prompt)
    return count, count <= 500


def transition_marker() -> str:
    """Return an ASCII marker supported by Pillow's bundled default font."""
    return "->"
