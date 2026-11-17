"""Add native OOXML hyperlinks for a feature unavailable in Artifact Tool."""
import sys,json,posixpath
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import xml.etree.ElementTree as E
p=Path(sys.argv[1]);links=json.loads(Path('/private/tmp/cf-office-hyperlinks.json').read_text())
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';rel='http://schemas.openxmlformats.org/officeDocument/2006/relationships';pkg='http://schemas.openxmlformats.org/package/2006/relationships'
E.register_namespace('',ns);E.register_namespace('r',rel)
with ZipFile(p) as z:parts={n:z.read(n) for n in z.namelist()}
workbook=E.fromstring(parts['xl/workbook.xml']);rs=E.fromstring(parts['xl/_rels/workbook.xml.rels']);targets={r.attrib['Id']:r.attrib['Target'] for r in rs}
names={s.attrib['name']:posixpath.normpath(posixpath.join('xl',targets[s.attrib['{'+rel+'}id']])).lstrip('/') for s in workbook.find('{'+ns+'}sheets')}
for name,part in names.items():
 matches=[x for x in links if x['sheet']==name]
 if not matches:continue
 sheet=E.fromstring(parts[part]);hs=sheet.find('{'+ns+'}hyperlinks')
 if hs is None:
  hs=E.Element('{'+ns+'}hyperlinks');children=list(sheet);before={'printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst'};idx=next((i for i,c in enumerate(children) if c.tag.split('}')[-1] in before),len(children));sheet.insert(idx,hs)
 rp=posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels');rels=E.fromstring(parts[rp]) if rp in parts else E.Element('{'+pkg+'}Relationships')
 for i,x in enumerate(matches):
  rid='officeEvidence'+str(i);E.SubElement(hs,'{'+ns+'}hyperlink',{'ref':x['cell'],'{'+rel+'}id':rid});E.SubElement(rels,'{'+pkg+'}Relationship',{'Id':rid,'Type':rel+'/hyperlink','Target':x['url'],'TargetMode':'External'})
 parts[part]=E.tostring(sheet,encoding='utf-8',xml_declaration=True);parts[rp]=E.tostring(rels,encoding='utf-8',xml_declaration=True)
temp=p.with_suffix('.tmp.xlsx')
with ZipFile(temp,'w',ZIP_DEFLATED) as z:
 for n,b in parts.items():z.writestr(n,b)
temp.replace(p)
print(json.dumps({'native_hyperlinks':len(links),'file':str(p)}))
