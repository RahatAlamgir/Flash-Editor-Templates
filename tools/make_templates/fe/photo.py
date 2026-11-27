"""Photo handling: crop to fill a box, tune colours, blur."""

from PIL import Image, ImageEnhance, ImageFilter


def cover(image, w, h, focus=(0.5, 0.5), zoom=1.0):
    """Scale and crop `image` so it fills w x h. focus: which point of the photo (0..1, 0..1) stays in view."""
    scale = max(w / image.width, h / image.height) * zoom
    big = image.resize((max(w, round(image.width * scale)), max(h, round(image.height * scale))), Image.LANCZOS)
    x = round((big.width - w) * focus[0])
    y = round((big.height - h) * focus[1])
    return big.crop((x, y, x + w, y + h))


def tune(image, contrast=1.0, saturation=1.0, brightness=1.0, blur=0):
    if brightness != 1.0:
        image = ImageEnhance.Brightness(image).enhance(brightness)
    if contrast != 1.0:
        image = ImageEnhance.Contrast(image).enhance(contrast)
    if saturation != 1.0:
        image = ImageEnhance.Color(image).enhance(saturation)
    if blur:
        image = image.filter(ImageFilter.GaussianBlur(blur))
    return image
