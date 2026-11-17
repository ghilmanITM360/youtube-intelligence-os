"""WI-0081 v5 SFX bed (synthetic, deterministic). Quiet by design: every sound sits well below the narration."""
import numpy as np, wave
SR=24000; N=int(98.33*SR); y=np.zeros(N)
rng=np.random.default_rng(81)
def add(t,s,g=1.0):
    i=int(t*SR); s=s[:max(0,N-i)]; y[i:i+len(s)]+=s*g
def tone(f0,f1,d,env=None):
    t=np.arange(int(d*SR))/SR; f=f0*(f1/f0)**(t/d); ph=2*np.pi*np.cumsum(f)/SR; s=np.sin(ph)
    return s*(env(t/d) if env else np.exp(-6*t/d))
def click(d=0.02,f=2500): t=np.arange(int(d*SR))/SR; return (rng.standard_normal(len(t))*0.6+np.sin(2*np.pi*f*t))*np.exp(-t/d*5)
# S3b boiling pops (same bubble table as scenes.js) + faint simmer
for x,P,ph in [(380,.62,0),(450,.78,.25),(530,.66,.1),(600,.84,.4),(660,.7,.5),(720,.6,.3),(490,.9,.55),(570,.74,.15)]:
    k=0
    while True:
        tau=ph+P*(k+0.93)
        if tau>1.28: break
        add(21.87+tau,tone(700-x*.3,250,0.06),0.05); k+=1
t=np.arange(int(1.28*SR))/SR; add(21.87,rng.standard_normal(len(t))*np.convolve(np.ones(1),[1])[0]*0.006*np.minimum(1,t/0.6))
# S3 rising suspense under "eighty degrees ... takes about"
add(24.16,tone(220,900,1.45,lambda u:np.minimum(1,u*3)*(1-u**4)),0.015)
add(24.16,tone(223,905,1.45,lambda u:np.minimum(1,u*3)*(1-u**4)),0.011)
# S4 timer: step ticks, then soft ticking
for tt in [27.77,27.93,28.07,28.21,28.34]: add(tt,click(),0.05)
tt=28.55
while tt<29.1: add(tt,click(0.012,3200),0.02); tt+=0.25
add(29.72,tone(110,60,0.15),0.06)           # 700 W thunk
# S5 bulbs: tink + rising hum
for tt in [31.55,32.05,32.39,32.63,32.85,33.19,33.69]: add(tt,tone(1900,1500,0.12,lambda u:np.exp(-7*u)),0.03)
# S6 microwave: door close, light click, hum + turntable, end beep
add(34.95,click(0.03,300),0.04); add(35.08,click(0.03,300),0.04); add(35.2,tone(140,70,0.12),0.07)
add(35.3,click(0.01,1800),0.04)
t=np.arange(int(1.45*SR))/SR; hum=np.sin(2*np.pi*100*t)+0.5*np.sin(2*np.pi*200*t)+0.15*np.sin(2*np.pi*2*np.pi*t*7)
add(35.5,hum*np.minimum(1,t/0.1)*np.minimum(1,(1.45-t)/0.1),0.012)
add(36.55,tone(1000,1000,0.15,lambda u:1-0*u),0.02)

# ===== v6 additions: quiet action sounds for beats 1-6 and 13-29 =====
def swish(t,d,g,lp=40):
    n=int(d*SR); x=rng.standard_normal(n); x=np.convolve(x,np.ones(lp)/lp,'same'); e=np.sin(np.pi*np.arange(n)/n)**2; add(t,x*e*3,g)
def tick(t,g=0.03,f=3000): add(t,click(0.012,f),g)
def cue(t,f0=700,f1=1100,g=0.02): add(t,tone(f0,f1,0.22,lambda u:np.sin(np.pi*u)**1.5),g)
swish(2.1,1.2,0.012); add(3.05,tone(3200,2900,0.18,lambda u:np.exp(-9*u)),0.035)       # spoon swish, ceramic clink
add(4.27,tone(130,70,0.14),0.05); tick(5.82,0.03,1400); swish(5.9,0.9,0.014)             # "no" thunk, grip, determined turn
swish(8.3,0.9,0.012); cue(14.51,600,900,0.02)                                              # energy, heat lands
swish(18.85,1.15,0.014,lp=12); add(20.3,tone(400,200,0.12),0.03)                          # pour, probe goes in
for i in range(10): tick(37.0+i*0.095,0.012,2200)                                          # gauge needle ticks
tick(38.3,0.035,900); tick(38.56,0.035,800)                                                # hoof steps
t=np.arange(int(3.7*SR))/SR; add(40.5,rng.standard_normal(len(t))*np.exp(-((t-1.9)/0.8)**2)*np.where(t>3.55,0,1)*0.010)  # waterfall swell, ducked for the number
cue(44.15,900,1300,0.02)
tick(46.58,0.03,1400); swish(46.0,2.5,0.008); tick(49.8,0.03); swish(50.2,0.3,0.012,lp=15); cue(52.52,500,800,0.02); swish(56.5,1.5,0.008)
swish(60.4,2.1,0.014,lp=20)
t=np.arange(int(4.7*SR))/SR; add(62.5,np.sin(2*np.pi*np.cumsum(90+t*20)/SR)*0.010*np.minimum(1,t/0.5))   # motor hum, rising
tick(67.6,0.03,1800)
for k in range(30): add(69.5+k*0.057+rng.random()*0.03,click(0.006,2600+rng.random()*800),0.012)  # subtle crackle
for k in range(12): tick(71.4+k*0.27,0.012,900)
for k in range(14): tick(75.2+k*0.22,0.012,1500)
swish(75.2,3.2,0.007,lp=25)
for k in range(10): tick(80.09+k*0.5,0.008,2800)                                            # shared clock ticks
swish(81.18,2.5,0.008); add(82.1,tone(500,250,0.1),0.03); add(82.8,tone(500,250,0.1),0.03); tick(82.92,0.03,1500)
swish(84.1,1.4,0.006,lp=60)
add(86.32,tone(3000,2800,0.15,lambda u:np.exp(-9*u)),0.025); add(88.33,tone(130,70,0.14),0.04); swish(91.0,1.2,0.01)
for k in range(16): tick(93.3+k*0.12,0.008,3500)
swish(96.4,0.3,0.01,lp=15); add(96.8,tone(3000,2700,0.2,lambda u:np.exp(-8*u)),0.035)       # final light clink, then a quiet beat
y=np.clip(y,-0.25,0.25)
w=wave.open('hf/assets/sfx.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y*32767).astype(np.int16).tobytes()); w.close()
vo=wave.open('hf/assets/vo_full.wav'); v=np.frombuffer(vo.readframes(vo.getnframes()),dtype=np.int16).reshape(-1,2).astype(float)/32768 if vo.getnchannels()==2 else np.frombuffer(vo.readframes(vo.getnframes()),dtype=np.int16).astype(float)/32768
v=v.mean(1) if v.ndim==2 else v
def rms(a): return np.sqrt((a**2).mean()+1e-12)
for a,b,n in [(2,4,'clink'),(21.87,23.15,'boil'),(24.16,25.6,'suspense'),(27.77,29.2,'timer'),(31.5,34,'bulbs'),(34.9,37,'microwave'),(40.5,44.2,'waterfall'),(62.5,67.2,'motor'),(69.5,71.2,'crackle'),(75,79,'splash'),(96.3,98,'ending')]:
    i,j=int(a*SR),int(b*SR); print(n,'sfx peak %.3f'%abs(y[i:j]).max(),'sfx rms %.4f'%rms(y[i:j]),'vo rms %.4f'%rms(v[i:min(j,len(v))]),'ratio dB %.1f'%(20*np.log10(rms(y[i:j])/rms(v[i:min(j,len(v))]))))
