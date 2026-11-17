import React from 'react';
import {registerRoot,Composition} from 'remotion';
import {Pilot,CharacterBoard,AssetBoard} from './Pilot';
import {FPS,DURATION} from './story';
const Root=()=>React.createElement(React.Fragment,null,
 React.createElement(Composition,{id:'FixedMortgage',component:Pilot,width:1920,height:1080,fps:FPS,durationInFrames:DURATION}),
 React.createElement(Composition,{id:'CharacterBoard',component:CharacterBoard,width:1920,height:1080,fps:FPS,durationInFrames:1}),
 React.createElement(Composition,{id:'AssetBoard',component:AssetBoard,width:1920,height:1080,fps:FPS,durationInFrames:1}));
registerRoot(Root);
