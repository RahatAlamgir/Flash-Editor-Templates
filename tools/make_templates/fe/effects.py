"""Things baked into pictures: soft shadows and arrows (they become plain picture layers, not objects)."""

import math

from PIL import Image, ImageChops, ImageDraw, ImageFilter

from .color import rgba


def shadow_of(canvas, dx, dy, blur, color="#000000", opacity=0.6):
    """A blurred, shifted, one-colour copy of whatever is painted on `canvas` (a page-sized RGBA picture)."""
    alpha = canvas.getchannel("A")
    alpha = ImageChops.offset(alpha, dx, dy)
    # offset() wraps around; blank the wrapped edges
    if dx > 0:
        ImageDraw.Draw(alpha).rectangle([0, 0, dx - 1, alpha.height], fill=0)
    if dy > 0:
        ImageDraw.Draw(alpha).rectangle([0, 0, alpha.width, dy - 1], fill=0)
    if blur:
        alpha = alpha.filter(ImageFilter.GaussianBlur(blur))
    alpha = alpha.point(lambda v: round(v * opacity))
    r, g, b, _ = rgba(color)
    out = Image.new("RGBA", canvas.size, (r, g, b, 0))
    out.putalpha(alpha)
    return out


def arrow(size, start, end, color, width, outline="#ffffff", outline_width=0):
    """A bold arrow from start to end on a page-sized transparent picture. Drawn big and shrunk for smooth edges."""
    s = 3
    w, h = size
    big = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    (x1, y1), (x2, y2) = start, end
    angle = math.atan2(y2 - y1, x2 - x1)
    head = width * 2.6
    bx, by = x2 - math.cos(angle) * head, y2 - math.sin(angle) * head  # where the shaft meets the head
    nx, ny = -math.sin(angle), math.cos(angle)
    shaft = [(x1 + nx * width / 2, y1 + ny * width / 2), (bx + nx * width / 2, by + ny * width / 2),
             (bx - nx * width / 2, by - ny * width / 2), (x1 - nx * width / 2, y1 - ny * width / 2)]
    tip = [(bx + nx * head * 0.9, by + ny * head * 0.9), (x2, y2), (bx - nx * head * 0.9, by - ny * head * 0.9)]
    for poly in (shaft, tip):
        pts = [(x * s, y * s) for x, y in poly]
        d.polygon(pts, fill=rgba(color))
        if outline_width:
            d.line(pts + [pts[0]], fill=rgba(outline), width=outline_width * s, joint="curve")
    # outline lines were drawn over the fill; paint the fill again inside so only the outer half shows
    for poly in (shaft, tip):
        d.polygon([(x * s, y * s) for x, y in poly], fill=rgba(color))
    return big.resize((w, h), Image.LANCZOS)


def crescent(size, color, thickness=0.27):
    """A crescent moon picture (size x size, the horns pointing up-right): a full circle with a shifted circle cut out."""
    s = 3
    big = size * s
    outer = Image.new("L", (big, big), 0)
    ImageDraw.Draw(outer).ellipse([0, 0, big - 1, big - 1], fill=255)
    cut = Image.new("L", (big, big), 0)
    shift = big * thickness
    ImageDraw.Draw(cut).ellipse([shift, -big * 0.06 + big * 0.02, shift + big * 0.92, big * 0.86], fill=255)
    mask = ImageChops.subtract(outer, cut).resize((size, size), Image.LANCZOS)
    picture = Image.new("RGBA", (size, size), rgba(color))
    picture.putalpha(mask)
    return picture
