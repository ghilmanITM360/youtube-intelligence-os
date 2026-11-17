import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SpreadsheetFile, Workbook } from '@oai/artifact-tool';

// Usage: bundled-node tools/export_workbooks.mjs [database.json] [output-directory]
// Every source key is retained. Objects/arrays become JSON; text over Excel's
// cell limit is split into numbered continuation columns, never truncated.
const workspace = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const inputPath = path.resolve(process.argv[2] || path.join(workspace, 'WhatIf_Complete_Extraction/what_if_complete_database.json'));
const outputDir = path.resolve(process.argv[3] || path.dirname(inputPath));
const database = JSON.parse(await fs.readFile(inputPath, 'utf8'));
const previewDir = path.join(outputDir, '_verification', 'workbook_previews');
await fs.mkdir(previewDir, { recursive: true });
const specs = [
  ['Questions', 'questions', ['question_id', 'chapter_title', 'original_question', 'verification_status', 'section_type', 'submitted_by', 'pdf_page_start', 'pdf_page_end', 'printed_page_start', 'printed_page_end', 'short_answer_summary', 'detailed_scientific_explanation']],
  ['Chapters', 'chapters', ['chapter_id', 'chapter_title', 'section_type', 'pdf_page_start', 'pdf_page_end']],
  ['Scientific facts', 'scientific_facts', ['fact_id', 'question_id', 'fact', 'statement']],
  ['Calculations', 'calculations', ['calculation_id', 'question_id', 'description', 'equation']],
  ['Figures', 'figures', ['figure_id', 'question_id', 'pdf_page', 'description']],
  ['References', 'references', ['reference_id', 'question_id', 'citation', 'url']],
  ['Quality status', 'quality_status', ['check', 'status', 'details']],
];
const report = { input: inputPath, generated_at: new Date().toISOString(), sheets: [], exports: [] };
function records(value) {
  if (Array.isArray(value)) return value.map(row => row && typeof row === 'object' && !Array.isArray(row) ? row : { value: row });
  if (value && typeof value === 'object') return Object.entries(value).map(([check, details]) => ({check, details}));
  return value === undefined || value === null ? [] : [{value}];
}
function columnName(index) {
  let result = '';
  for (let n = index + 1; n; n = Math.floor((n - 1) / 26)) result = String.fromCharCode(65 + (n - 1) % 26) + result;
  return result;
}
function normalize(value) {
  if (value === null || value === undefined) return null;
  if (typeof value === 'object') return JSON.stringify(value);
  return value;
}
function splitText(value) {
  if (typeof value !== 'string') return [value];
  const chunks = [];
  for (let offset = 0; offset < value.length;) {
    let end = Math.min(value.length, offset + 30000);
    if (end < value.length && /[\uD800-\uDBFF]/.test(value[end - 1])) end--;
    chunks.push(value.slice(offset, end));
    offset = end;
  }
  return chunks.length ? chunks : [''];
}
function addDataSheet(workbook, [name, key, preferred]) {
  const rows = records(database[key]);
  if (key === 'quality_status' && database.metadata) rows.push({check: 'Source metadata', details: database.metadata});
  const available = new Set(rows.flatMap(Object.keys));
  const fields = [...preferred.filter(key => available.has(key)), ...[...available].filter(key => !preferred.includes(key))];
  if (!fields.length) fields.push('No records');
  const parsed = rows.map(row => Object.fromEntries(fields.map(field => [field, splitText(normalize(row[field]))])));
  const columns = fields.flatMap(field => Array.from({length: Math.max(1, ...parsed.map(row => row[field].length))}, (_, part) => ({field, part, label: part ? `${field} (continued ${part + 1})` : field})));
  const sheet = workbook.worksheets.add(name);
  const endCol = columnName(columns.length - 1);
  const matrix = [columns.map(c => c.label), ...parsed.map(row => columns.map(c => {
    const v = row[c.field][c.part] ?? null;
    return typeof v === 'string' && v.startsWith('=') ? `'${v}` : v;
  }))];
  sheet.getRange(`A1:${endCol}${matrix.length}`).values = matrix;
  const used = sheet.getRange(`A1:${endCol}${matrix.length}`);
  used.format.font = {name: 'Arial', size: 10, color: '#233044'};
  used.format.wrapText = true;
  used.format.verticalAlignment = 'top';
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(1);
  sheet.getRange(`A1:${endCol}1`).format = {fill: '#263B53', font: {name: 'Arial', size: 10, bold: true, color: '#FFFFFF'}, wrapText: true, horizontalAlignment: 'center', verticalAlignment: 'center', rowHeight: 38};
  for (let i = 0; i < columns.length; i++) {
    const col = columnName(i);
    const field = columns[i].field;
    const width = /(^|_)id$|page|count/.test(field) ? 18 : /title|status|type|submitted/.test(field) ? 30 : 68;
    sheet.getRange(`${col}1:${col}${matrix.length}`).format.columnWidth = width;
  }
  if (rows.length) {
    sheet.getRange(`A2:${endCol}${matrix.length}`).format.autofitRows();
    const table = sheet.tables.add(`A1:${endCol}${matrix.length}`, true, `WhatIf_${key}`);
    table.showFilterButton = true;
  }
  return {name, source_key: key, records: rows.length, columns: columns.length, split_columns: columns.filter(c => c.part).length};
}
async function verifyAndExport(workbook, entries, filename, renderSamples) {
  workbook.recalculate();
  for (const entry of entries) {
    const end = columnName(Math.min(entry.columns, 4) - 1);
    const range = `A1:${end}${Math.min(entry.records + 1, 4)}`;
    const inspection = await workbook.inspect({kind:'table', range: `'${entry.name}'!${range}`, include:'values,formulas', tableMaxRows:4, tableMaxCols:4, maxChars:2500});
    await fs.writeFile(path.join(previewDir, `${entry.name.replaceAll(' ', '_')}.inspect.ndjson`), inspection.ndjson);
    if (renderSamples) {
      const preview = await workbook.render({sheetName:entry.name, range, scale:1, format:'png'});
      await fs.writeFile(path.join(previewDir, `${entry.name.replaceAll(' ', '_')}.png`), new Uint8Array(await preview.arrayBuffer()));
    }
  }
  const errors = await workbook.inspect({kind:'match', searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!', options:{useRegex:true,maxResults:20}, maxChars:3000});
  report.formula_error_scan = errors.ndjson;
  const target = path.join(outputDir, filename);
  await fs.mkdir(path.dirname(target), {recursive:true});
  await (await SpreadsheetFile.exportXlsx(workbook)).save(target);
  report.exports.push(target);
}
const workbook = Workbook.create();
for (const spec of specs) report.sheets.push(addDataSheet(workbook, spec));
await verifyAndExport(workbook, report.sheets, 'what_if_complete_database.xlsx', true);
const questionsWorkbook = Workbook.create();
const questionsEntry = addDataSheet(questionsWorkbook, specs[0]);
await verifyAndExport(questionsWorkbook, [questionsEntry], '01_ALL_QUESTIONS/all_questions.xlsx', false);
await fs.writeFile(path.join(previewDir, 'verification_report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
