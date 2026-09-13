#!/usr/bin/env python3
"""Derive a content-free five-sheet YouTube package template from a workbook."""

from __future__ import annotations

import argparse
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.cell.cell import MergedCell


REQUIRED_SHEETS = ["Channel Overview", "All Videos", "Descriptions", "Verification", "Analysis"]


def build_template(source: Path, output: Path) -> None:
    source = source.resolve()
    output = output.resolve()
    if source == output:
        raise ValueError("Source and output must differ; raw source workbooks are immutable")
    if not source.is_file():
        raise FileNotFoundError(source)

    workbook = load_workbook(source, data_only=False, read_only=False)
    if workbook.sheetnames != REQUIRED_SHEETS:
        raise ValueError(f"Unexpected sheet structure: {workbook.sheetnames!r}")
    for sheet in workbook.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell, MergedCell):
                    continue
                cell.value = None
                cell.comment = None
                cell.hyperlink = None
        sheet.auto_filter.ref = None
        for table_name in list(sheet.tables.keys()):
            del sheet.tables[table_name]

    output.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output)
    workbook.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build_template(args.source, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
