import {KokoroTTS} from 'kokoro-js';
import {env} from '@huggingface/transformers';
import fs from 'node:fs';
import path from 'node:path';
import {performance} from 'node:perf_hooks';
env.cacheDir = path.resolve('.cache');
const start=performance.now();
const lines=JSON.parse(fs.readFileSync('tools/narration.json','utf8'));
const tts=await KokoroTTS.from_pretrained('onnx-community/Kokoro-82M-v1.0-ONNX',{dtype:'q8',device:'cpu',revision:'1939ad2a8e416c0acfeecc08a694d14ef25f2231'});
const result=[];
for(const [i,line] of lines.entries()){
 const before=performance.now();
 const audio=await tts.generate(line.text,{voice:'af_heart',speed:1.04});
 await audio.save(`public/audio/voice-${i}.wav`);
 result.push({...line,file:`voice-${i}.wav`,duration:audio.audio.length/audio.sampling_rate,seconds:(performance.now()-before)/1000});
 console.log(line.id,result.at(-1).duration.toFixed(3));
}
fs.writeFileSync('evidence/voice-generation.json',JSON.stringify({provider:'local Kokoro q8 CPU',model:'onnx-community/Kokoro-82M-v1.0-ONNX',voice:'af_heart',speed:1.04,total_seconds:(performance.now()-start)/1000,lines:result},null,2));
