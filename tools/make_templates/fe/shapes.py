"""Draws shapes on a transparent picture. The numbers are the app's own shape numbers (project.json "Shape")."""

import math

from PIL import Image, ImageDraw

from .color import rgba

RECTANGLE, ELLIPSE, TRIANGLE, STAR, DIAMOND, HEXAGON, BURST = 0, 1, 2, 3, 15, 26, 29
KINDS = {"rectangle": RECTANGLE, "ellipse": ELLIPSE, "triangle": TRIANGLE, "star": STAR, "diamond": DIAMOND,
         "hexagon": HEXAGON, "burst": BURST}

SUPERSAMPLE = 3  # draw bigger, shrink: smooth edges


def _star_points(w, h, points, inner, first_angle=-90):
    cx, cy = w / 2, h / 2
    out = []
    for i in range(points * 2):
        radius = 1.0 if i % 2 == 0 else inner
        angle = math.radians(first_angle + i * 180 / points)
        out.append((cx + math.cos(angle) * radius * w / 2, cy + math.sin(angle) * radius * h / 2))
    return out


def outline(kind, w, h, points=5, inner=0.5):
    """Corner points (in a w x h box) of a polygon shape."""
    if kind == TRIANGLE:
        return [(w / 2, 0), (w, h), (0, h)]
    if kind == DIAMOND:
        return [(w / 2, 0), (w, h / 2), (w / 2, h), (0, h / 2)]
    if kind == HEXAGON:
        return [(w * 0.25, 0), (w * 0.75, 0), (w, h / 2), (w * 0.75, h), (w * 0.25, h), (0, h / 2)]
    if kind == STAR:
        return _star_points(w, h, points, inner)
    if kind == BURST:  # 16 spikes, a spike points right, dips at 82 % of the radius (measured from the app's own badge)
        return _star_points(w, h, 16, 0.825, first_angle=0)
    raise ValueError(f"unsupported shape {kind}")


def draw(kind, w, h, fill, radius=0, points=5, inner=0.5):
    """A w x h RGBA picture holding the filled shape."""
    s = 1 if (kind == RECTANGLE and not radius) else SUPERSAMPLE
    big = Image.new("RGBA", (max(1, round(w * s)), max(1, round(h * s))), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    color = rgba(fill)
    box = [0, 0, w * s - 1, h * s - 1]
    if kind == RECTANGLE:
        if radius:
            d.rounded_rectangle(box, radius=min(radius, w / 2, h / 2) * s, fill=color)
        else:
            d.rectangle(box, fill=color)
    elif kind == ELLIPSE:
        d.ellipse(box, fill=color)
    else:
        d.polygon([(x * s, y * s) for x, y in outline(kind, w, h, points, inner)], fill=color)
    return big if s == 1 else big.resize((max(1, round(w)), max(1, round(h))), Image.LANCZOS)
