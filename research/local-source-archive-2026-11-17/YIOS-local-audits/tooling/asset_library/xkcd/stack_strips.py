import cv2, numpy as np, sys, glob, pathlib
d = pathlib.Path(sys.argv[1]); fs = sorted(glob.glob(str(d / "strip_*.png")))
ims = [cv2.imread(f) for f in fs]; w = max(i.shape[1] for i in ims)
ims = [cv2.copyMakeBorder(i, 0, 8, 0, w - i.shape[1], cv2.BORDER_CONSTANT, value=(0, 0, 255)) for i in ims]
out = np.vstack(ims); s = min(1.0, 2400 / out.shape[0]); cv2.imwrite(str(d / "strips_all.png"), cv2.resize(out, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)); print([pathlib.Path(f).stem for f in fs], out.shape)
