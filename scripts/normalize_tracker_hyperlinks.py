#!/usr/bin/env python3
"""Convert HYPERLINK formulas to portable native XLSX hyperlinks."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.workbook.properties import CalcProperties


HYPERLINK = re.compile(r'^=HYPERLINK\("((?:[^"]|"")*)","((?:[^"]|"")*)"\)$', re.IGNORECASE)


def normalize(path: Path) -> int:
    workbook = load_workbook(path, data_only=False)
    changed = 0
    for sheet in workbook.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                if not isinstance(cell.value, str):
                    continue
                match = HYPERLINK.match(cell.value)
                if not match:
                    continue
                url, label = (value.replace('""', '"') for value in match.groups())
                cell.value = label
                cell.hyperlink = url
                cell.style = "Hyperlink"
                changed += 1
    if workbook.calculation is None:
        workbook.calculation = CalcProperties()
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.calculation.calcMode = "auto"
    workbook.save(path)
    workbook.close()
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    changed = normalize(args.workbook)
    if changed == 0:
        raise SystemExit("No HYPERLINK formulas found; tracker generator contract changed unexpectedly.")
    print(f"Normalized {changed} hyperlinks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
