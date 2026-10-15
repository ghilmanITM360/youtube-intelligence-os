"""Original editable illustration primitives; no reference pixels or external assets."""
from html import escape
INK='#292A2D';TEAL='#327C79';GOLD='#E6AF53';CORAL='#C86855';SKIN='#EDC3A2'
def path(d,fill='none',stroke=INK,sw=6):return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def ellipse(x,y,rx,ry,fill,stroke=INK,sw=5):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def text(t,x,y,size=42,color=INK,anchor='middle',font='Chalkboard'):return f'<text x="{x}" y="{y}" font-family="{font}, sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(t)}</text>'
def group(id,s):return f'<g id="{id}">{s}</g>'
def svg(w,h,s):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{s}</svg>'
def limb(points,color,width=28):return path(points,'none',INK,width+9)+path(points,'none',color,width)
def person(identity='sam',pose='stand',expression='warm'):
 color={'sam':TEAL,'june':CORAL,'nora':GOLD}[identity]; parts={}
 if pose=='run':
  legs=limb('M176 380 Q155 440 112 461 L63 442','#45535C',34)+limb('M224 381 Q251 436 283 465 L259 547','#45535C',34)
  shoes=path('M48 427 L76 442 L69 460 Q37 458 26 445 Z','#F4EADC')+path('M242 535 L274 544 L291 566 Q266 578 239 563 Z','#F4EADC')
 elif pose=='sit':
  legs=limb('M175 383 L270 417 L282 551','#45535C',35)+limb('M225 384 L324 410 L340 546','#45535C',35)
  shoes=path('M264 543 L296 544 L311 572 L263 574 Z','#F4EADC')+path('M322 541 L353 539 L371 565 L325 569 Z','#F4EADC')
 else:
  legs=limb('M174 378 Q169 462 151 564','#45535C',35)+limb('M225 378 Q237 460 252 564','#45535C',35)
  shoes=path('M131 554 Q148 550 168 560 L174 585 Q138 594 116 583 Z','#F4EADC')+path('M234 556 L267 555 Q294 571 290 584 L236 585 Z','#F4EADC')
 parts['legs']=legs+shoes
 if pose=='run': left='M143 244 L99 303 L54 276';right='M258 245 L293 305 L342 272';hands=[(54,276),(342,272)]
 elif pose=='point':left='M143 244 L108 318 L104 365';right='M258 244 L302 285 L354 242';hands=[(104,365),(354,242)]
 elif pose=='open':left='M143 244 L100 307 L48 285';right='M258 244 L303 308 L355 283';hands=[(48,285),(355,283)]
 elif pose=='concern':left='M143 244 L106 310 L153 343';right='M258 244 L302 296 L262 326';hands=[(153,343),(262,326)]
 elif pose=='sit':left='M143 244 L120 320 L184 388';right='M258 244 L287 316 L274 393';hands=[(184,388),(274,393)]
 else:left='M143 244 Q112 290 113 364';right='M258 244 Q285 300 283 366';hands=[(113,364),(283,366)]
 parts['rear-arm']=limb(left,color,27)+ellipse(*hands[0],15,20,SKIN)
 parts['torso']=path('M142 220 Q196 204 259 220 Q275 293 268 390 Q201 411 132 389 Q125 303 142 220 Z',color)+path('M171 215 Q196 248 230 215','none','#F4EADC',10)+path('M198 254 L199 380','none',INK,3)+ellipse(201,288,3,3,INK,INK,0)+ellipse(201,326,3,3,INK,INK,0)
 parts['neck']=path('M177 176 L177 219 Q199 240 223 218 L225 174 Z',SKIN)
 head=path('M129 99 Q130 39 193 33 Q261 31 274 100 L269 154 Q259 195 205 204 Q148 202 130 157 Z',SKIN)
 head+=ellipse(126,134,12,19,SKIN)+ellipse(274,134,12,19,SKIN)
 if identity=='sam': hair=path('M130 113 Q110 67 145 48 Q160 37 173 39 L165 65 Q140 67 142 114 Z','#CED0C9')+path('M235 43 Q277 46 275 113 L262 111 Q266 75 239 67 Z','#CED0C9')+path('M172 44 Q196 26 223 43','none',INK,4)
 elif identity=='june':hair=path('M126 151 Q104 78 141 40 Q193 9 247 40 Q286 65 279 163 L258 148 L254 84 Q207 94 162 65 Q137 92 144 151 Z','#C8CEC9')
 else:hair=ellipse(256,40,33,32,'#CDD2CE')+path('M125 119 Q105 53 164 28 Q218 6 260 54 L277 118 L257 102 L242 65 Q208 93 146 77 L144 120 Z','#CDD2CE')
 parts['head-hair']=head+hair
 face=ellipse(170,121,5,7,INK,INK,0)+ellipse(230,121,5,7,INK,INK,0)+path('M201 123 L194 145 L205 147','none',INK,4)
 if expression=='concern':face+=path('M157 103 L178 96 M219 96 L242 103 M179 173 Q199 160 221 172','none',INK,5)
 elif expression=='explain':face+=path('M157 99 Q170 94 181 101 M218 101 Q231 91 242 98','none',INK,4)+ellipse(202,171,12,9,'#78493D')
 else:face+=path('M157 101 Q170 94 181 101 M218 101 Q231 94 242 101 M178 166 Q199 186 222 165','none',INK,4)
 face+=path('M150 149 L159 151 M239 151 L249 149','none',CORAL,3)
 parts['face']=face
 parts['front-arm']=limb(right,color,27)+ellipse(*hands[1],15,20,SKIN)+path(f'M{hands[1][0]-6} {hands[1][1]} l10 5','none',INK,2)
 if pose=='point':parts['front-arm']+=path('M353 235 L373 220','none',INK,10)+path('M353 235 L373 220','none',SKIN,5)
 return 400,620,parts,{'pivot':[200,380],'hands':hands,'feet':[[151,590],[252,590]] if pose not in ('sit','run') else [],'shoulders':[[143,244],[258,244]]}
def swimmer():
 parts={'rear-leg':limb('M435 165 L532 177 L613 149',SKIN,28),'body':path('M198 121 Q323 94 458 147 L443 200 Q327 170 204 180 Z',TEAL),'front-leg':limb('M437 189 L530 222 L616 206',SKIN,30),'rear-arm':limb('M229 129 L295 72 L374 84',SKIN,22),'head':ellipse(164,145,51,48,SKIN)+path('M115 145 Q109 90 159 91 Q203 89 215 130 L183 129 Q142 128 115 145 Z','#C8CEC9')+path('M125 143 L164 139 L170 155 L131 161 Z',TEAL)+path('M136 174 Q152 181 167 172','none',INK,3),'front-arm':limb('M216 165 L139 205 L51 190',SKIN,23)+ellipse(43,189,18,11,SKIN)}
 return 680,290,parts,{'pivot':[340,150],'hands':[[43,189],[374,84]],'feet':[[613,149],[616,206]]}
def prop(name):
 p={};w=h=400
 if name=='heart':p={'heart':path('M200 338 C163 304 56 234 58 151 C60 61 156 47 201 118 C248 46 343 63 346 150 C349 232 241 311 200 338 Z',CORAL),'shine':path('M102 140 Q107 103 142 108','none','#F9E0CF',12)}
 elif name=='intervals':
  w,h=700,280
  p={'baseline':path('M24 212 L675 212','none',INK,4),'work-1':path('M39 211 L39 65 L145 69 L145 211 Z',CORAL)+text('WORK',92,46,26),'rest-1':path('M161 211 L161 157 L269 154 L269 211 Z',TEAL)+text('EASY',215,140,26),'work-2':path('M288 211 L288 66 L394 68 L394 211 Z',CORAL),'rest-2':path('M413 211 L413 156 L520 155 L520 211 Z',TEAL),'work-3':path('M538 211 L538 65 L645 67 L645 211 Z',CORAL),'caption':text('Illustrative pattern — no prescribed dose',350,258,24,font='Arial')}
 elif name=='stopwatch':p={'case':ellipse(200,219,128,132,'#FAF6EB'),'crown':path('M175 72 L175 43 L226 43 L226 72 Z',TEAL),'dial':path('M200 111 L200 130 M307 220 L287 220 M200 326 L200 308 M91 220 L109 220','none',INK,7),'hands':path('M200 147 L200 220 L251 248','none',INK,8),'button':path('M286 99 L311 121','none',INK,18)}
 elif name=='chair':p={'back':path('M81 62 Q73 40 100 39 L261 43 Q280 45 278 72 L270 234 L92 238 Z','#E7DCC7'),'seat':path('M88 231 L299 232 L322 274 L85 277 Z',GOLD),'legs':path('M108 278 L95 374 M285 276 L302 373','none',INK,14)}
 elif name=='clinic':
  w,h=900,500;p={'wall':path('M20 430 L20 70 Q20 42 53 43 L844 43 L860 430','none','#A7B9B1',5),'window':path('M62 94 L222 94 L222 257 L61 257 Z','#EDF4F0')+path('M142 95 L142 255 M62 172 L220 172','none','#A7B9B1',4),'plant':path('M741 427 L723 345 L807 345 L786 428 Z',CORAL)+path('M765 345 L766 237','none',INK,5)+path('M765 298 Q704 294 719 257 Q752 255 765 298 Z',TEAL)+path('M765 272 Q821 263 805 221 Q774 226 765 272 Z',TEAL),'floor':path('M15 438 Q439 428 881 439','none',INK,4)}
 elif name=='park':
  w,h=900,450;p={'path':path('M20 401 Q252 313 460 365 Q650 421 878 346','none','#BCCBC0',22),'tree':path('M707 334 L711 151','none',INK,13)+path('M709 213 Q616 209 642 144 Q601 85 682 66 Q728 15 766 71 Q847 88 795 149 Q822 209 709 213 Z','#D7E3CC'),'grass':path('M35 332 L41 308 L51 334 M529 316 L541 288 L550 317','none',TEAL,5)}
 elif name=='pool':
  w,h=900,470;p={'water':path('M35 147 L858 147 L856 399 Q466 432 37 399 Z','#D9ECEB'),'edge':path('M29 148 L864 148 M34 402 Q448 432 866 402','none',TEAL,7),'ripples':''.join(path(f'M{x} {y} q35 -16 70 0 t70 0','none','#6AABA6',4) for x,y in [(75,220),(325,320),(620,260)]),'ladder':path('M740 218 L740 86 Q762 45 789 84 L788 218 M741 122 L788 122 M741 172 L788 172','none',INK,9)}
 elif name=='joint':p={'upper-bone':path('M142 30 L244 30 L237 146 Q263 162 245 189 Q224 209 201 186 Q174 210 148 188 Q130 167 154 146 Z','#F3E7CF'),'lower-bone':path('M149 217 Q174 198 201 218 Q230 198 251 221 Q265 241 238 257 L247 367 L150 367 L159 256 Q134 238 149 217 Z','#F3E7CF'),'space':path('M140 204 Q202 190 259 207','none',TEAL,7),'ring':ellipse(202,201,111,88,'none',GOLD,8)}
 elif name=='lungs':p={'left':path('M175 98 Q136 60 102 124 Q55 205 75 280 Q111 321 174 282 Z','#A9CDCA'),'right':path('M226 99 Q267 62 301 125 Q348 210 327 280 Q288 319 225 283 Z','#A9CDCA'),'airway':path('M201 39 L201 152 M201 140 L143 207 M201 140 L260 207','none',INK,11),'oxygen':text('O₂',202,367,59,TEAL)}
 elif name=='calendar':
  p={'paper':path('M57 88 L343 84 L348 348 L55 350 Z','#FFF9ED'),'binding':path('M57 145 L343 145 M116 59 L116 109 M280 58 L280 109','none',INK,9),'days':''.join(ellipse(x,y,19,19,TEAL if k in [0,2,4] else '#E5E8DE',INK,2) for k,(x,y) in enumerate([(100,197),(164,197),(229,197),(294,197),(100,265),(164,265),(229,265)])),'note':text('SPEAKER’S LIMIT',200,327,24)}
 elif name=='question':p={'outline':path('M200 34 L365 326 L35 326 Z','#FAE7BC'),'mark':text('?',200,267,160)}
 elif name=='shoe':p={'shoe':path('M70 116 L153 140 L226 199 L335 215 Q379 221 368 287 L42 290 Q30 232 70 116 Z',TEAL),'sole':path('M42 281 L368 278 L370 306 L38 307 Z','#F6EEDC'),'laces':path('M159 170 L196 149 M181 190 L219 169 M206 206 L238 187','none','#F6EEDC',8)}
 elif name=='arrow':p={'line':path('M39 264 Q138 91 302 134','none',INK,8),'tip':path('M271 99 L313 136 L266 162','none',INK,8)}
 else:raise ValueError(name)
 return w,h,p,{'pivot':[w/2,h/2]}
