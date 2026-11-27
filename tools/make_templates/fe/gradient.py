"""Gradient pictures: linear (angle in degrees, 90 = top to bottom, 0 = left to right) or radial (from the middle)."""

import math

import numpy as np
from PIL import Image

from .color import rgba


def draw(w, h, stops, angle=90, radial=False):
    """stops: [("#RRGGBB", position 0..1), ...]. Returns a w x h RGBA picture."""
    stops = [(rgba(c), p) for c, p in stops]
    positions = [p for _, p in stops]
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    if radial:
        t = np.hypot((xs - w / 2) / (w / 2), (ys - h / 2) / (h / 2)) / math.sqrt(2) * math.sqrt(2)
        t = np.clip(t, 0, 1)
    else:
        a = math.radians(angle)
        dx, dy = math.cos(a), math.sin(a)
        corners = [0, w * dx, h * dy, w * dx + h * dy]
        lo, hi = min(corners), max(corners)
        t = (xs * dx + ys * dy - lo) / ((hi - lo) or 1)
    channels = [np.interp(t, positions, [c[i] for c, _ in stops]) for i in range(4)]
    out = np.stack(channels, axis=-1).round().astype(np.uint8)
    return Image.fromarray(out, "RGBA")
