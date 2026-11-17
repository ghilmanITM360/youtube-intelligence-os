# RT-V3-S03 worker notes
- Read only SPEC_GIVEN_TO_WORKER.json; no other files/folders opened.
- render.py -> rt.mp4 (179 frames, 1920x1080, 30000/1001, h264 yuv420p; ffprobe verified).
- Background: static textured 2x canvas, affine zoom about (960,50), s(i) = linear interp of camera_scale_table.
- Teacher layer (teacher, stone lectern top, pointer, mouth) is a premultiplied-alpha sprite composited in screen space; head (1700,380)->(1640,470), k 1.00->1.45 by camera progress, clamped after f58.
- Pointer poses: down f0-63; lift to raised f64; taps f72-73, f96-97, f120-121, f146-147 (4 taps), else raised. Mouth toggles every 6 frames from f12.
- Chalk text "topic: sabre cat" (Snell Roundhand) ~60% board width; at f178 spans x ~540-1380 px, left end well over 80 px from the edge.
- Checked frames 0,30,58,100,178 (check_f*.png, montage.png): teacher fully visible at right edge, text fully in frame.
- timeline.json holds per-frame scale/teacher k/position plus pose and mouth event frames.
