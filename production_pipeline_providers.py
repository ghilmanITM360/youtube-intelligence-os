"""Provider contracts for semantic reasoning and image rendering."""
from __future__ import annotations
from pathlib import Path
from typing import Protocol


class ReasoningProvider(Protocol):
    def classify(self, text: str, index: int, count: int) -> str: ...


class ImageGenerator(Protocol):
    def generate(self, prompt: str, output_path: Path) -> bool: ...


class PromptOnlyImageGenerator:
    """Keep prompt and expected path; no credential or external call required."""
    def generate(self, prompt: str, output_path: Path) -> bool:
        return output_path.exists()
