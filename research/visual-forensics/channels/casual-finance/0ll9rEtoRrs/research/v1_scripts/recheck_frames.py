import cv2, os, sys
src, out = sys.argv[1], sys.argv[2]
want = {'S0260': range(14310, 14322), 'S0263': range(14362, 14368), 'S0037': range(1697, 1703)}
cap = cv2.VideoCapture(src)
for sid, rng in want.items():
    for f in rng:
        cap.set(cv2.CAP_PROP_POS_FRAMES, f); ok, im = cap.read()
        if ok: cv2.imwrite(os.path.join(out, f'{sid}_f{f}.jpg'), cv2.resize(im, (640, 360)))
