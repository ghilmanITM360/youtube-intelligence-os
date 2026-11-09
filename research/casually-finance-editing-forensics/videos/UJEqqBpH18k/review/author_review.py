import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('UJEqqBpH18k',2206)
A.scenes([
(0,"MUNDER DIFFLIN sign with a bond tag, red arrow, then bag and document","headline; sign; bond; arrow; bag; caption","PR_MUNDER,PR_BOND,OV_REDARROW,PR_BAG,PR_DOC","Buyers who didn't ask the price are being replaced"),
(57,"Green-tie man with bubble 'Wait, but how much is that worth?'","headline; figure; bubble; caption","CH_OFFICIAL,OV_BUBBLE","The new buyers ask the price"),
(112,"Fed committee page: zoom and scroll, host pointing, yellow highlight","headline; article (zoom/scroll); host; highlight; caption","SS_FED_PAGE,CH_HOST,OV_HIGHLIGHT","The Fed's bond desk: ownership shifted to price-sensitive private investors"),
(593,"Bond tag and red timeline; bills pop one by one","headline; bond; timeline; bills; caption","PR_BOND,OV_TIMELINE,PR_BILLS","Term premium as the extra charge"),
(749,"Timeline with bag and a struck-through 'thirty years' written on","headline; timeline; bag; text write-on; caption","PR_BOND,OV_TIMELINE,PR_BAG,TY_RED_NOTE","Tying money up for 30 years instead of 30 days"),
(813,"UK map character; Office for Budget Responsibility sign slides in","headline; UK map character; OBR sign; caption","CH_UKMAP,SS_OBR_SIGN","UK OBR found a similar thing"),
(900,"UK map character with a gilt certificate","headline; UK map character; certificate; caption","CH_UKMAP,PR_GILT","Known as gilts"),
(1007,"Blue 'Gilts' card beside the UK character","headline; UK character; card; caption","CH_UKMAP,SS_GILT_CARD","Definition card"),
(1029,"Report text page with highlight; UK character","headline; text page; highlight; UK character; caption","SS_OBR_TEXT,OV_HIGHLIGHT,CH_UKMAP","Pension funds hold gilts worth ~27% of GDP, falling to under 6%"),
(1344,"Sad figure: 'and cause damage'","headline; figure; caption","CH_FIG","Shifts this size cause damage"),
(1406,"OBR chart with host pointing: about GBP 22 billion per year","headline; chart; host; caption","SS_OBR_CHART,CH_HOST","80 bp higher rates would cost 22 billion pounds a year"),
(1726,"Country-map ensemble; 'a global trend' with yield charts","headline; map characters; chart strip; caption","CH_MAPS,SS_YIELD_CHARTS","A global trend through every major economy"),
(1865,"Figure with tray and Japan-map character: 'Load me some?' 'Alrighty'","headline; figure; Japan character; bubbles; caption","CH_FIG,CH_JAPAN,OV_BUBBLE","Governments still auction; buyers changed"),
(2018,"Yield chart with red/blue lines; then auction chart with figures and cash","headline; chart; figures; cash; caption","SS_DB_CHART,SS_AUCTION_CHART,CH_FIG,PR_CASH","Buyers who care about the price they pay"),
(2166,"Brown-haired figure thinking, then holding cash: 'and they want a better price'","headline; figure; cash; caption (end)","CH_OFFICIAL,PR_CASH","Closing: buyers want a better price")])
A.event("S01",2,19,"OVERLAY_POP","red arrow beside bond tag","Arrow animates beside the bond tag (≈18 frames).","SE001",conf="MEDIUM")
A.event("S01",56,56,"POP_IN","bag and document","Bag and document appear in one frame.","SE003; ev_01",conf="HIGH")
A.event("S02",79,79,"OVERLAY_POP","bubble 'Wait, but how much is that worth?'","Bubble appears in one frame.","SE004",conf="HIGH")
A.event("S03",138,150,"CAMERA_SCROLL_ZOOM","Fed page","Page scrolls/zooms over ~12 frames.","SE006; ev_01",conf="MEDIUM")
A.event("S03",157,163,"CAMERA_SCROLL_ZOOM","Fed page","Second small scroll/zoom (6 frames).","SE007; ev_01",conf="MEDIUM")
A.event("S03",184,205,"CAMERA_SCROLL_ZOOM","Fed page","Page zooms to the paragraph over ~21 frames; host pops at f204.","SE008; ev_01",conf="MEDIUM")
A.event("S03",592,592,"HIGHLIGHT_SWEEP","yellow highlight","Highlight on 'term premium' in one frame.","SE009 neighbour",conf="LOW")
A.event("S04",609,698,"POP_IN","bills on timeline","Bills pop at f609, f634, f658, f682, f698 (intervals ~25 frames).","SE010-014; ev_01",conf="HIGH")
A.event("S05",749,786,"TEXT_WRITE_ON","struck-through 'thirty years' text","Text grows over the timeline for ~38 frames.","SE015; ev_01",conf="MEDIUM")
A.event("S06",837,857,"SLIDE_IN","Office for Budget Responsibility sign","Sign slides in from the left over ~20 frames beside the UK character.","SE017; ev_01",conf="MEDIUM")
A.event("S07",935,935,"POP_IN","gilt certificate","Certificate appears in one frame.","SE019; ev_01",conf="HIGH")
A.event("S08",1007,1007,"POP_IN","Gilts card","Card appears in one frame.","SE020; ev_01",conf="HIGH")
A.event("S09",1029,1029,"POP_IN","text page","Page appears at the cut.","SE021; ev_01",conf="HIGH")
A.event("S12",1726,1763,"CAMERA_SCROLL_ZOOM","country ensemble and charts","Ensemble and chart strip enter/shift over ~38 frames.","SE025; ev_01",conf="LOW")
A.event("S13",1769,1801,"CAMERA_SCROLL_ZOOM","ensemble and charts","Second shift over ~33 frames.","SE026; ev_01",conf="LOW")
A.event("S13",1865,1865,"POP_IN","figure and Japan character","Figure and Japan-map character replace the ensemble.","SE027; ev_02",conf="HIGH")
A.event("S14",1964,1964,"OVERLAY_POP","bubble 'Alrighty'","Bubble text changes.","SE029; ev_02",conf="HIGH")
A.event("S14",2018,2018,"POP_IN","yield chart","Chart replaces the scene.","SE030; ev_02",conf="HIGH")
A.event("S15",2123,2123,"POP_IN","auction chart figures","Second figure and cash appear.","SE032; ev_02",conf="HIGH")
A.event("S15",2190,2190,"POP_IN","cash in hand","Bill appears in the figure's hand.","SE034; ev_02",conf="HIGH")
A.write(headline="We Have No Control Over the Bond Market")
