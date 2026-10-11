"""Preserve unsupported native XLSX features after Artifact Tool cell authoring.

Only authored cell values/formulas and recalculated caches are transplanted.
All original formatting, data bars, panes, filters and native package parts remain.
"""
import io
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def strings(archive):
    if 'xl/sharedStrings.xml' not in archive.namelist():
        return []
    return [''.join(node.itertext()) for node in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('m:si', NS)]

def preserve(path, baseline):
    path = Path(path)
    original = zipfile.ZipFile(baseline)
    authored = zipfile.ZipFile(path)
    shared = strings(authored)
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as saved:
        for item in original.infolist():
            content = original.read(item.filename)
            if re.fullmatch(r'xl/worksheets/sheet\d+.xml', item.filename):
                cells = {cell.get('r'): cell for cell in ET.fromstring(authored.read(item.filename)).findall('.//m:sheetData/m:row/m:c', NS)}
                def replace(match):
                    raw = match.group(0)
                    address = re.search(r'\br="([A-Z]+\d+)"', raw).group(1)
                    cell = cells.get(address)
                    if cell is None:
                        return raw
                    # Keep the original cell style/metadata; use authored scalar/formula.
                    start = raw[:raw.index('>') + 1].replace('/>', '>')
                    prefix = re.match(r'<((?:\w+:)?)c\b', raw).group(1)
                    start = re.sub(r' t="[^"]*"', '', start)
                    kind = cell.get('t')
                    value = cell.findtext('m:v', namespaces=NS)
                    formula = cell.find('m:f', NS)
                    body = ''
                    if formula is not None:
                        body += ET.tostring(formula, encoding='unicode').replace('ns0:', '').replace(' xmlns:ns0="' + NS['m'] + '"', '')
                    else:
                        existing_formula = re.search(r'<(?:\w+:)?f\b[^>]*>.*?</(?:\w+:)?f>', raw, flags=re.S)
                        if existing_formula:
                            body += existing_formula.group(0)
                    if kind in ('s', 'inlineStr'):
                        text = shared[int(value)] if kind == 's' else ''.join(cell.find('m:is', NS).itertext())
                        start = start[:-1] + ' t="inlineStr">'
                        body += '<is><t>' + text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') + '</t></is>'
                    elif value is not None:
                        if kind:
                            start = start[:-1] + ' t="' + kind + '">'
                        body += '<v>' + value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') + '</v>'
                    if prefix:
                        body = re.sub(r'<(/?)(f|v|is|t)\b', lambda tag: '<' + tag.group(1) + prefix + tag.group(2), body)
                    return start + body + '</' + prefix + 'c>'
                content = re.sub(r'<(?:\w+:)?c\b[^>]*?/>|<(?:\w+:)?c\b[^>]*>.*?</(?:\w+:)?c>', replace, content.decode(), flags=re.S).encode()
            saved.writestr(item, content)
    authored.close()
    original.close()
    path.write_bytes(output.getvalue())

if __name__ == '__main__':
    import sys
    preserve(sys.argv[1], sys.argv[2])
