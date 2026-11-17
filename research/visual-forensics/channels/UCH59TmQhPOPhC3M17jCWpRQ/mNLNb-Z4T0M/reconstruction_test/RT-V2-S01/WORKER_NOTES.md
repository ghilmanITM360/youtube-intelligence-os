# RT-V2-S01 worker notes
- Procedural cv2 render (render.py -> rt.mp4 via ffmpeg pipe, h264 yuv420p, 208 frames, 1920x1080, 30000/1001).
- Static background drawn once: pale sky, two outlined hills, olive grass, winding two-tone river, 3 trees, tiny 5-roof village on horizon. Jittered 4-7px near-black outlines, flat fills.
- Camera fully static (same bg array every frame). f0-40: 8 tiny water ripple dashes flicker, nothing else.
- Labels "bugs" f55, "mud" f85, "rotten fish" f115: white Hershey-script text with dark outline, dotted arrow + item (dots / brown blob / grey fish). Pop-in over 5 frames.
- Drift: each group moves toward horizon and shrinks (smoothstep) from max(70,appear) to f195, order preserved.
- Character: sad closed-eye person chest up, enters from bottom f140, floats up/shrinks, ends small near centre f207.
- Unmet/approx: water ~44% (measured mask) ok; label font is Hershey script (not a true handwriting font); labels shrink to small/overlapping near the horizon by ~f190; outline on white text is thin.
