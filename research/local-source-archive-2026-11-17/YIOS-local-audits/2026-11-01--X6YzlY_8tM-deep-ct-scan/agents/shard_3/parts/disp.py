D=[]
def d(id,v,desc,m,conf): D.append({"id":id,"verdict":v,"desc":desc,"matches_candidate":m,"confidence":conf})
d("SD006","REAL_STATE_CHANGE","Stick figure plus black logo at cut-2 replaced by a framed video cutaway (man at podium, banknotes flying) at the cut frame.","EP0188","HIGH")
d("SD007","REAL_STATE_CHANGE","Centred smiling stick figure replaced by narrow-poster strip plus a large grey carton at the cut frame.","EP0206","HIGH")
d("SD008","REAL_STATE_CHANGE","Poster plus big carton replaced by red 'The kinda bad' heading and an open carton with a rocket peeking out.","EP0207","HIGH")
d("SD009","REAL_STATE_CHANGE","Bow-tie character and speech bubble at cut-2 replaced by a huge upright rocket at the cut frame, then a tilted rocket.","EP0211","HIGH")
d("SD010","REAL_STATE_CHANGE","Character and bubble still visible at cut-2; rocket already large and rotating at cut and post frames.","EP0211","HIGH")
for i in range(11,19):
    d("SD%03d"%i,"REAL_MOTION","Same rocket spinning rapidly: orientation differs by large angles in each of the three tiles while it scales down.","EP0211","HIGH")
d("SD019","REAL_STATE_CHANGE","Small upright rocket at cut-2 replaced by a very large Earth globe at cut frame, globe remains large.","EP0212","HIGH")
d("SD020","REAL_STATE_CHANGE","Small rocket at cut-2 replaced by large globe at cut and post frames.","EP0212","HIGH")
for i in range(21,35):
    d("SD%03d"%i,"REAL_MOTION","Cartoon globe progressively shrinks across the three tiles (zoom-out); no composition change.","EP0212","HIGH")
d("SD035","REAL_STATE_CHANGE","Centred smiling stick figure replaced by poster strip plus large grey carton labelled 3.","EP0222","HIGH")
d("SD036","REAL_STATE_CHANGE","Heart-eyed character, carton, DEBT/FEE papers and money bag replaced by red 'The good' label, open carton and satellite with passenger.","EP0229","HIGH")
d("SD037","REAL_STATE_CHANGE","Scene with open carton, black round badge and satellite replaced by full-bleed black card with white wordmark and lens flares.","EP0229","HIGH")
d("SD038","REAL_STATE_CHANGE","Black wordmark card at cut-2 replaced by white canvas (black badge slides in a few frames later).","EP0229","HIGH")
