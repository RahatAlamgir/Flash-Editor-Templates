"""Writes the `.fe` file: a zip with project.json, preview.png and images/N.webp (lossless, cropped to the painted part)."""

import io
import json
import os
import zipfile

from PIL import Image

PREVIEW_SIZE = 480


def _webp(image):
    buffer = io.BytesIO()
    image.save(buffer, "WEBP", lossless=True, quality=100, method=6)
    return buffer.getvalue()


def _layer_json(layer, pixels_name, x, y):
    data = {
        "Name": layer["name"], "Opacity": layer["opacity"], "Visible": True, "Locked": False,
        "BlendMode": layer["blend"], "Pixels": pixels_name, "ExtendedX": 0, "ExtendedY": 0, "PixelsX": x, "PixelsY": y,
        "RestoreX": 0, "RestoreY": 0,
    }
    if layer["object"] is not None:
        data["Object"] = layer["object"]
    data["MaskEnabled"] = True
    return data


def _composite(page, scale_to=None):
    canvas = Image.new("RGBA", (page.width, page.height), (0, 0, 0, 0))
    for layer in page.layers:
        picture = layer["canvas"]
        if layer["opacity"] < 1:
            picture = picture.copy()
            picture.putalpha(picture.getchannel("A").point(lambda v, o=layer["opacity"]: round(v * o)))
        canvas.alpha_composite(picture)
    if scale_to:
        scale = scale_to / max(page.width, page.height)
        canvas = canvas.resize((max(1, round(page.width * scale)), max(1, round(page.height * scale))), Image.LANCZOS)
    return canvas


def write(path, pages, presentation=False):
    """pages: list of Page. Returns the number of bytes written."""
    images = []  # webp bytes, in the order of the numbers used in project.json

    def store(picture):
        images.append(_webp(picture))
        return f"images/{len(images) - 1}.webp"

    page_json = []
    for page in pages:
        layers = []
        for layer in page.layers:
            canvas = layer["canvas"]
            if layer.get("full"):
                opaque = canvas.getchannel("A").getextrema() == (255, 255)
                name = store(canvas.convert("RGB") if opaque else canvas)
                layers.append(_layer_json(layer, name, 0, 0))
                continue
            bounds = canvas.getchannel("A").getbbox()
            if bounds is None:
                layers.append(_layer_json(layer, store(Image.new("RGBA", (1, 1), (0, 0, 0, 0))), 0, 0))
                continue
            layers.append(_layer_json(layer, store(canvas.crop(bounds)), bounds[0], bounds[1]))
        page_json.append({"Name": page.name, "Width": page.width, "Height": page.height,
                          "ActiveLayer": len(layers) - 1, "VerticalGuides": [], "HorizontalGuides": [],
                          "Layers": layers})
    project = {"Format": "flash-project", "Version": 3, "Pages": page_json, "ActivePage": 0, "Width": 0, "Height": 0,
               "ActiveLayer": 0, "Layers": []}
    if presentation:
        project["ProjectType"] = "presentation"
    preview = io.BytesIO()
    _composite(pages[0], PREVIEW_SIZE).save(preview, "PNG")
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("project.json", json.dumps(project, indent=1), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("preview.png", preview.getvalue(), compress_type=zipfile.ZIP_STORED)
        for i, data in enumerate(images):
            z.writestr(f"images/{i}.webp", data, compress_type=zipfile.ZIP_STORED)
    return os.path.getsize(path)
