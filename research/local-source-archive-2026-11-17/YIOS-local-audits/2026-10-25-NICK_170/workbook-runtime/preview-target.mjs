import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'));
const b=await wb.render({sheetName:'Detailed Research',range:'A438:F440',scale:1.2,format:'png'});
await fs.writeFile('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-NICK_170/workbook-target.png',new Uint8Array(await b.arrayBuffer()));
