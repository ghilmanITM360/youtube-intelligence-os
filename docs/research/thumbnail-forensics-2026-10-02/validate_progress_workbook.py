"""Read-only validation of dynamic research dashboard and native XLSX features."""
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from reconcile_packaging_progress import dashboard_payload

NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def validate(root):
    root = Path(root)
    payload = dashboard_payload(root)
    summary = json.loads((root / 'packaging-progress-summary.json').read_text())
    with zipfile.ZipFile(root / 'PACKAGING-PROGRESS.xlsx') as archive:
        shared = [''.join(s.itertext()) for s in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('m:si', NS)]
        sheets = []
        for index in range(1, 12):
            document = ET.fromstring(archive.read(f'xl/worksheets/sheet{index}.xml'))
            cells = {}
            for cell in document.findall('.//m:sheetData/m:row/m:c', NS):
                value = cell.findtext('m:v', default='', namespaces=NS)
                if cell.get('t') == 's':
                    value = shared[int(value)]
                elif cell.get('t') == 'inlineStr':
                    value = ''.join(cell.find('m:is', NS).itertext())
                assert value not in ('#REF!', '#DIV/0!', '#VALUE!', '#NAME?', '#NUM!', '#SPILL!', '#CALC!')
                cells[cell.get('r')] = value
            sheets.append((document, cells))
        assert len(ET.fromstring(archive.read('xl/workbook.xml')).find('m:sheets', NS)) == 11
        for cell, key, actual in [('E11', 'titles', summary['titles']['done']), ('H11', 'thumbnails', summary['thumbnails']['verified']), ('B15', 'packages', summary['packages']['audited']), ('E15', 'qa', summary['packages']['qa_sampled']), ('E7', 'channels_complete', summary['channels']['complete'])]:
            assert int(float(sheets[0][1][cell])) == payload['totals'][key] == actual, cell
        for index, column, records in [(1, 'B', payload['queue']), (2, 'D', payload['master'])]:
            document, cells = sheets[index]
            ids = [cells[f'{column}{n}'] for n in range(2, len(records) + 2)]
            assert len(ids) == len(set(ids)) == len(records)
            assert document.find('m:sheetViews/m:sheetView/m:pane', NS) is not None
            assert document.find('m:tableParts', NS) is not None
        assert any(rule.get('type') == 'dataBar' for rule in sheets[0][0].findall('.//m:cfRule', NS))
        assert any(rule.get('type') == 'dataBar' for rule in sheets[1][0].findall('.//m:cfRule', NS))
        current = payload['current_channel']
        assert sheets[3][1]['B15'] == current['next_Video_ID']
        assert int(float(sheets[3][1]['B13'])) == current['remaining_videos']
        assert summary['current_channel'] == current
    return dict(sheets=11, channel_rows=len(payload['queue']), video_rows=len(payload['master']), totals=payload['totals'], native_features='PASS', native_excel_recalculation='NOT_RUN')

if __name__ == '__main__':
    print(json.dumps(validate(Path(__file__).resolve().parent)))
