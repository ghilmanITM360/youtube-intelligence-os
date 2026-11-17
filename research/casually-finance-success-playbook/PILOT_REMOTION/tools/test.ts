import assert from 'node:assert/strict';
import {key, solveLeg, poseAt, POSES, PoseName} from '../src/motion';
assert.equal(key(0,[[0,2],[10,8]]),2);
assert.equal(key(10,[[0,2],[10,8]]),8);
assert.equal(key(5,[[0,2],[10,8]]),5);
for(const name of ['shrug','point','hold'] as const){
 const p=POSES[name];
 for(const side of [-1,1]){
  const hip={x:side*30,y:p.hipY}, foot={x:side*56,y:410};
  const knee=solveLeg(hip,foot,95,95,side);
  assert.ok(Math.abs(Math.hypot(knee.x-hip.x,knee.y-hip.y)-95)<1e-6);
  assert.ok(Math.abs(Math.hypot(knee.x-foot.x,knee.y-foot.y)-95)<1e-6);
 }
}
assert.deepEqual(poseAt(34,'point'),poseAt(34,'point'));
console.log('PASS keyframe endpoints/midpoint, fixed bone lengths, deterministic pose');
import timeline from '../src/timeline.json';
import {pushIn,pullOut,panAcross} from '../src/camera-presets';
const sequence:PoseName[]=['shrug','hold','point','point','hold','point','shrug','hold'];
for(let frame=0;frame<1260;frame++){
 const i=timeline.findIndex(t=>frame>=t.from&&frame<t.endFrame),t=timeline[i];
 assert.ok(i>=0);assert.ok(t.voiceEnd<=t.endFrame/30);
 const p=poseAt(frame-t.from,sequence[i],sequence[Math.max(0,i-1)]);
 for(const side of [-1,1]){
  const hip={x:side*30,y:p.hipY},foot={x:side*56,y:410};const knee=solveLeg(hip,foot,95,95,side);
  assert.ok(Number.isFinite(knee.x)&&Number.isFinite(knee.y));
  assert.ok(Math.abs(Math.hypot(knee.x-hip.x,knee.y-hip.y)-95)<1e-6);
  assert.ok(Math.abs(Math.hypot(knee.x-foot.x,knee.y-foot.y)-95)<1e-6);
 }
}
assert.equal(pushIn(0,100).scale,1);assert.equal(pushIn(100,100).scale,1.025);
assert.equal(pullOut(0,100).scale,1.025);assert.equal(pullOut(100,100).scale,1);
assert.equal(panAcross(100,100).x,-24);
console.log('PASS 1260-frame leg reach/length/finite values, timeline coverage, camera endpoints');
