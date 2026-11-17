import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'));
console.log((await wb.inspect({kind:'region',sheetId:'Combined Dashboard',range:'A4:H10',maxChars:2000,tableMaxRows:8,tableMaxCols:8})).ndjson);
const blob=await wb.render({sheetName:'Combined Dashboard',range:'A1:H18',scale:1,format:'png'});
await fs.writeFile('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_166/workbook-before.png',new Uint8Array(await blob.arrayBuffer()));
