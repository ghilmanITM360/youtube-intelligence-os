#!/usr/bin/env python3
"""Value-safe secret scan for tracked text files; never prints matched values."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private_key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    "aws_access_key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "google_api_key": re.compile(rb"AIza[0-9A-Za-z_-]{35}"),
    "apify_token_assignment": re.compile(rb"APIFY_TOKEN\s*[=:]\s*['\"]?[A-Za-z0-9_-]{20,}"),
}


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).split(b"\0")
    findings: list[tuple[str, str]] = []
    for raw_path in tracked:
        if not raw_path:
            continue
        relative = raw_path.decode("utf-8", errors="surrogateescape")
        path = ROOT / relative
        try:
            data = path.read_bytes()
        except (OSError, MemoryError):
            continue
        if b"\0" in data[:8192]:
            continue
        for secret_type, pattern in PATTERNS.items():
            if pattern.search(data):
                findings.append((secret_type, relative))
    for secret_type, relative in findings:
        print(f"{secret_type}: {relative}")
    print(f"tracked_secret_findings={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
