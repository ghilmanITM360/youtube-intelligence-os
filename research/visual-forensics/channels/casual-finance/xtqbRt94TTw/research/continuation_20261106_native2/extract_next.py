from pathlib import Path
code=(Path(__file__).parent/'extract_native.py').read_text().split('window(680,684')[0]
exec(compile(code,'extract_native.py','exec'))
window(1115,1165,set(range(1115,1166,3))|{1119,1120,1121,1122,1140,1141,1142,1155,1156,1157,1158,1159,1160,1161},'coin_notes_1115_1165')
window(1225,1230,set(range(1225,1231)),'sub031')
