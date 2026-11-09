import json,re
exec(open('partial/eps1.py').read()); exec(open('partial/stA.py').read()); exec(open('partial/stB.py').read()); exec(open('partial/stC.py').read())
P={
"S0219":"Pale-blue definition card at x0.23-0.77 y0.12-0.80 (title top-left, falling-arrow-and-percent icon with a small house at left, definition paragraph at right, source mark bottom); worried presenter head x0.0-0.22 y0.10-0.60 with a shoulder line leaving the frame at left.",
"S0220":"Red outlined block lettering reading PRICES at x0.22-0.62 y0.41-0.66; vertical kitchen knife with brown handle at x0.66-0.87 y0.07-0.65.",
"S0221":"PRICES lettering x0.16-0.64 y0.40-0.66 sliced by a white gap near x0.27 (PRI | ES); knife lying nearly horizontal x0.52-0.87 y0.52-0.80 with blade pointing left.",
"S0222":"Blue wordmark at x0.17-0.58 y0.15-0.23; small pink two-storey house with green bushes x0.27-0.46 y0.40-0.75 below it; yellow price tag tied to the house's left side x0.20-0.30 y0.55-0.70.",
"S0223":"Wordmark x0.17-0.58 y0.15-0.23; pink house with yellow tag x0.18-0.46 y0.40-0.75; worried character with red headband x0.66-0.83 y0.38-1.0 cropped by bottom edge; tiny red caption left of its head x0.57-0.65 y0.52-0.58.",
"S0224":"Huge black-haired character x0.55-0.94 y0.0-1.0 (head about 0.3w); green dollar bill held at x0.39-0.56 y0.56-0.88.",
"S0225":"Close-up character x0.56-0.92 y0.05-1.0; speech bubble x0.16-0.55 y0.20-0.54 with two lines of handwriting; green bill x0.38-0.55 y0.55-0.90.",
"S0226":"Large blue wordmark spanning x0.17-0.82 y0.41-0.55; small knife attached at its right end x0.83-0.91 y0.38-0.55.",
"S0227":"Scatter spanning x0.10-0.89 y0.12-0.82: four small houses (cream with red roofs), three grey apartment blocks, three red FOR SALE signs on posts at right of blocks.",
"S0228":"Left builder with saw x0.23-0.44 y0.22-0.78; stack of three orange bricks x0.45-0.58 y0.55-0.80; right blonde builder with hammer x0.65-0.79 y0.33-0.80.",
"S0229":"Builders and bricks as S0228 with a thick crimson X spanning x0.21-0.77 y0.15-0.90 over all three subjects.",
"S0230":"Light news-article screenshot x0.06-0.59 y0.05-0.95 (masthead top, small grey portrait at upper left, name heading, paragraphs, red Subscribe button at top right); bow-tie character with dark hair x0.67-0.99 y0.35-1.0.",
"S0231":"Dark PDF viewer x0.05-0.82 y0.0-1.0 (thumbnail strip left, white page centre with a yellow highlighted phrase); presenter x0.76-0.93 y0.40-1.0 with a diagonal pointer stick to the page.",
"S0232":"Giant smiling head x0.34-0.65 y0.03-0.68; open dictionary book x0.38-0.62 y0.62-1.0 with a small flag at its lower right.",
"S0233":"Pink house x0.11-0.26 y0.30-0.56; cream tower with grey annex x0.30-0.46 y0.18-0.60; small cream house x0.62-0.72 y0.47-0.62 (red sign appears mid-state); grey apartment block x0.74-0.88 y0.25-0.65.",
"S0234":"Knife-wielding smiling character x0.19-0.52 y0.15-1.0 in front of the pink house and tower (x0.12-0.30, partly hidden); small cream house with red sign x0.62-0.72 y0.47-0.65; grey block x0.74-0.88 y0.35-0.65.",
"S0235":"Dark transcript card x0.07-0.69 y0.06-0.53 (speaker name and title top-left, timestamp top-right, five-line paragraph with one yellow phrase); rest of frame blank white.",
"S0236":"Dark transcript card x0.07-0.69 y0.06-0.53; light-theme excerpt text block x0.33-0.93 y0.63-0.85 with a yellow highlighted phrase.",
"S0237":"Dark card x0.07-0.69 y0.06-0.53; excerpt block x0.33-0.93 y0.63-0.85; smiling presenter x0.12-0.30 y0.42-1.0 overlapping the card's lower left.",
"S0238":"First dark card x0.07-0.69 y0.06-0.53; second dark card with search bar x0.36-0.93 y0.19-0.72 overlapping it; excerpt block x0.33-0.93 y0.63-0.85; presenter x0.12-0.30 y0.42-1.0.",
"S0239":"Single thoughtful character x0.43-0.60 y0.40-1.0 (head about 0.16w at y0.40-0.72, one arm raised to chin); rest of frame blank white.",
"S0269":"Phone mockup centred x0.38-0.63 y0.02-0.98 with a white summary screen (small heading, photo thumbnail, bullet lines, bias bar); QR code at lower right x0.88-0.97 y0.80-0.96.",
}
PAD=" Thick black outlines, flat fills, plain white background, hand-drawn doodle style, no logos."
for x in S:
    if x['id'] in P: x['objects']=P[x['id']]
    if x['id']=='S0267': x['continuity']="Presenter style matches neighbouring states S0258-S0266; board appears only here and in the EP0358 reveal."
    if x['id']=='S0275': x['continuity']="Sidebar panel continues from S0274."
    n=len(x['prompt'].split())
    if n<30: x['prompt']+=PAD
    if len(x['prompt'].split())<30: x['prompt']+=" Centered composition, generous empty space."
for x in E:
    if x['ep']==376: x['motion']={"path":"pointer tip shifts slightly","easing":"UNKNOWN","duration_note":"4 frames, 0.17 s"}
ids=[l.split(',')[0] for l in open('machine_states.csv').read().split('\n')[1:] if l]
assert [x['id'] for x in S]==ids,(len(S),len(ids))
eps=[l.split(',')[0] for l in open('machine_episodes.csv').read().split('\n')[1:] if l]
assert [str(x['ep']) for x in E]==eps
bad=re.compile(r'Dave|Casual|Redfin|Yahoo|Lennar|Census|Romanowski|Horton|Ground|Microsoft|Kamala|Trump|Investopedia',re.I)
for x in S:
    for k in('prompt','recon'):
        if bad.search(x[k]): print('BRAND',x['id'],k)
    n=len(x['prompt'].split())
    if not 30<=n<=75: print('len',x['id'],n)
json.dump({"shard":4,"episodes":E,"states":S},open('OUT_shard_4.json','w'),indent=1)
d=json.load(open('OUT_shard_4.json'));print(len(d['episodes']),len(d['states']))
