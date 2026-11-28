"""Draws text layers the way the app lays them out (a box as wide as the text, glyphs starting at the box's left)."""

from PIL import Image, ImageDraw

from . import fonts
from .color import rgba

LINE_HEIGHT = 1.36  # box height of one line, in font sizes (the app uses about 1.35-1.375 for Segoe UI)
ALIGN = {"left": 0, "center": 1, "right": 2}


def line_width(font, line, size, letter_spacing):
    """Width of one line. letter_spacing is in percent of the font size, added after every letter."""
    if not letter_spacing:
        return font.getlength(line)
    extra = letter_spacing * size / 100
    return sum(font.getlength(ch) + extra for ch in line)


def measure(text, family, size, bold, letter_spacing=0, italic=False):
    """Width and height of a text box that fits the text, like the app makes."""
    font = fonts.load(family, size, bold, italic)
    lines = text.split("\n")
    width = max(line_width(font, line, size, letter_spacing) for line in lines)
    return round(width), round(size * LINE_HEIGHT * len(lines))


def _draw_line(d, x, y, line, font, size, letter_spacing, fill, kwargs):
    if not letter_spacing:
        d.text((x, y), line, font=font, fill=fill, anchor="la", **kwargs)
        return
    extra = letter_spacing * size / 100
    for ch in line:
        d.text((x, y), ch, font=font, fill=fill, anchor="la", **kwargs)
        x += font.getlength(ch) + extra


def draw(text, family, size, bold, color, box_w, box_h, align="left", outline=0, outline_color="#000000",
         letter_spacing=0, italic=False):
    """RGBA picture of the box (box_w x box_h) with the text inside; glyphs may reach a little outside, so a margin
    of `pad` pixels is kept: the returned picture is (box_w + 2 pad) x (box_h + 2 pad) and `pad` comes back too."""
    pad = int(size * 0.5) + 2
    image = Image.new("RGBA", (box_w + 2 * pad, box_h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(image)
    font = fonts.load(family, size, bold, italic)
    lines = text.split("\n")
    line_h = size * LINE_HEIGHT
    top_offset = (line_h - (font.getmetrics()[0] + font.getmetrics()[1])) / 2  # centre the glyph line in its band
    kwargs = {"stroke_width": outline, "stroke_fill": rgba(outline_color)} if outline else {}
    for i, line in enumerate(lines):
        width = line_width(font, line, size, letter_spacing)
        x = {"left": 0, "center": (box_w - width) / 2, "right": box_w - width}[align]
        _draw_line(d, pad + x, pad + i * line_h + top_offset, line, font, size, letter_spacing, rgba(color), kwargs)
    return image, pad
