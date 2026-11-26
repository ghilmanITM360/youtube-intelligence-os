"""Seam-free, pole-safe procedural noise: evaluated in 3D on the unit sphere, so an equirectangular
texture built from it wraps at the antimeridian and has no pinching at the poles by construction."""
import numpy as np
from scipy import ndimage


def sphere_dirs(w, h):
    """Unit vectors for the pixel centres of a w x h equirect map (u=0 at lon -180, row 0 at lat +90)."""
    lon = (np.arange(w, dtype=np.float32) + .5) / w * 2 * np.pi - np.pi
    lat = np.pi / 2 - (np.arange(h, dtype=np.float32) + .5) / h * np.pi
    cl, sl = np.cos(lat)[:, None], np.sin(lat)[:, None]
    return np.stack([cl * np.cos(lon)[None], np.broadcast_to(sl, (h, w)), cl * np.sin(lon)[None]], 0), lat


def noise3(p, freq, seed):
    """Smooth value noise (cubic) at points p (3,...) in [-1,1]^3; roughly in [-1,1]."""
    n = int(np.ceil(2 * freq)) + 6
    lat = np.random.default_rng(seed).uniform(-1, 1, (n, n, n)).astype(np.float32)
    c = (p * freq + n / 2).reshape(3, -1)
    return ndimage.map_coordinates(lat, c, order=3, mode='nearest').reshape(p.shape[1:])


def fbm(p, base, octaves, seed, gain=.5, lac=2.0):
    out = np.zeros(p.shape[1:], np.float32); amp = 1.0; f = base; tot = 0
    for o in range(octaves):
        out += amp * noise3(p, f, seed + 31 * o); tot += amp; amp *= gain; f *= lac
    return out / tot
