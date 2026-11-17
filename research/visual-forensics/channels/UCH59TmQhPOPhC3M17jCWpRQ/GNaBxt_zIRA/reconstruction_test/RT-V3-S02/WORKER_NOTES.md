# RT-V3-S02 worker notes
- Read only SPEC_GIVEN_TO_WORKER.json. Original scene drawn with cv2/PIL on a 3840x2160 canvas (2x), no source frames.
- Camera: M = [[s/2,0,960(1-s)],[0,s/2,50(1-s)]], warpAffine INTER_LINEAR; s from camera_scale_table, odd frames averaged.
- Text "topic: sabre cat" (Snell Roundhand, chalk white) = 60% of board width.
- Final text bbox on screen: x 503..1417, y 340..490 (inside 80px margins).
- Teacher (bald elder, white moustache) is at right and exits the frame to the right during the push; that is a geometric result of the fixed point.
- Pointer: rest pose until f59, then discrete pose swaps at f59,66,68,84,86,100,101,103,122,124,144,146,148 (taps 1-2 frames).
- Mouth open/closed swaps listed in timeline.json.
- f0 is a hard cut to the wide shot. Push f8-58.
- Checked: ffprobe 179 frames, 1920x1080, 30000/1001, h264 yuv420p. Viewed f0,30,58,100,178.
