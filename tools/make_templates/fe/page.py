"""One page of a template. Each call adds a layer: its project.json description plus the picture of what it looks like."""

from PIL import Image

from . import gradient as gradient_mod
from . import shapes as shapes_mod
from . import text as text_mod
from .color import rgba, to_json
from .fonts import has_real_bold


def _box(x, y, w, h, rotation=0):
    return {"X": x, "Y": y, "Width": w, "Height": h, "Rotation": rotation}


class Page:
    def __init__(self, width, height, name="Page 1"):
        self.width, self.height, self.name = width, height, name
        self.layers = []  # dicts: {"json": {...}, "image": RGBA picture the size of the page, "bounds": (x, y, w, h)}

    # ---- helpers -------------------------------------------------------------------------------------------------
    def _add(self, name, canvas, obj, opacity, blend="Normal"):
        """canvas: RGBA picture of the whole page holding only this layer at full strength (opacity is stored apart)."""
        self.layers.append({"name": name, "canvas": canvas, "object": obj, "opacity": opacity, "blend": blend})

    def _paste(self, picture, x, y, rotation=0):
        """Put a picture on an empty page-sized canvas at (x, y) (its top-left), turned around its middle."""
        canvas = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        if rotation:
            cx, cy = x + picture.width / 2, y + picture.height / 2
            picture = picture.rotate(-rotation, resample=Image.BICUBIC, expand=True)
            x, y = round(cx - picture.width / 2), round(cy - picture.height / 2)
        canvas.paste(picture, (round(x), round(y)), picture)
        return canvas

    # ---- layers --------------------------------------------------------------------------------------------------
    def background(self, color):
        """A solid page background (a normal layer without an object)."""
        canvas = Image.new("RGBA", (self.width, self.height), rgba(color))
        self._add("Background", canvas, None, 1.0)
        self.layers[-1]["full"] = True

    def gradient(self, stops, angle=90, radial=False, name="Gradient Background", box=None):
        x, y, w, h = box or (0, 0, self.width, self.height)
        picture = gradient_mod.draw(w, h, stops, angle, radial)
        canvas = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        canvas.paste(picture, (x, y))
        first = stops[0][0]
        obj = {
            "kind": "shape", "Shape": 0, "Fill": to_json(first), "StrokeWidth": 0, "CornerRadius": 0, "Points": 5,
            "Inner": 0.5, "Sweep": 270, "GradientBorder": False, "Dash": 0, "ArrowStart": False, "ArrowEnd": False,
            "DashLength": 0, "DashGap": 0, "Closed": False, "Bend": 0, "BendStyle": 0, "Box": _box(x, y, w, h),
            "FlipX": False, "FlipY": False, "BlurAmount": 0,
            "Gradient": {"Stops": [{"Color": to_json(c), "Position": p} for c, p in stops], "Angle": angle,
                         "Radial": radial},
        }
        self._add(name, canvas, obj, 1.0)
        self.layers[-1]["full"] = (w, h) == (self.width, self.height)

    def shape(self, kind, x, y, w, h, fill, radius=0, rotation=0, name=None, opacity=1.0, points=5, inner=0.5):
        number = shapes_mod.KINDS[kind] if isinstance(kind, str) else kind
        picture = shapes_mod.draw(number, w, h, fill, radius, points, inner)
        obj = {
            "kind": "shape", "Shape": number, "Fill": to_json(fill), "StrokeWidth": 0, "CornerRadius": radius,
            "Points": points, "Inner": inner, "Sweep": 270, "GradientBorder": False, "Dash": 0, "ArrowStart": False,
            "ArrowEnd": False, "DashLength": 0, "DashGap": 0, "Closed": False, "Bend": 0, "BendStyle": 0,
            "Box": _box(x, y, w, h, rotation), "FlipX": False, "FlipY": False, "BlurAmount": 0,
        }
        self._add(name or str(kind).title(), self._paste(picture, x, y, rotation), obj, opacity)

    def text(self, text, x, y, size, color, family="Segoe UI", bold=True, width=None, align="left", rotation=0,
             name=None, opacity=1.0, outline=0, outline_color="#000000", letter_spacing=0):
        """x, y: top-left of the text box. width: box width (default: just fits; give it with align="center")."""
        auto_w, box_h = text_mod.measure(text, family, size, bold, letter_spacing)
        box_w = width or auto_w
        picture, pad = text_mod.draw(text, family, size, bold, color, box_w, box_h, align, outline, outline_color)
        obj = {
            "kind": "text", "Text": text, "FontFamily": family, "FontSize": size, "Color": to_json(color),
            "Bold": bool(bold and has_real_bold(family)), "Italic": False, "Align": text_mod.ALIGN[align],
            "OutlineWidth": outline, "LineSpacing": 1, "Arc": 0, "LetterSpacing": letter_spacing, "WordSpacing": 0,
            "Box": _box(x, y, box_w, box_h, rotation), "FlipX": False, "FlipY": False, "BlurAmount": 0,
        }
        if outline:
            obj["OutlineColor"] = to_json(outline_color)
        self._add(name or text.replace("\n", " ")[:40], self._paste(picture, x - pad, y - pad, rotation), obj, opacity)
