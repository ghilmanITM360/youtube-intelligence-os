import { homedir } from "node:os";
const { FileBlob, SpreadsheetFile } = await import(process.env.ARTIFACT_TOOL_PATH ?? `${homedir()}/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs`);

const path = "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Analytical_Workbook.xlsx";
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(path));
for (const range of [
  "Dashboard!A1:F30", "Own-Channel Analytics!A1:H30", "Thumbnail Forensics!A1:P10",
  "Google Trends Research!A1:H30", "Root-Cause Hypotheses!A1:H30", "Evidence Gaps!A1:H30",
  "Video Evidence Register!A1:P8", "Research Checkpoint!A1:H30",
]) {
  const out = await workbook.inspect({ kind: "table", range, include: "values,formulas", tableMaxRows: 30, tableMaxCols: 20 });
  process.stdout.write(`\n### ${range}\n${out.ndjson}\n`);
}
