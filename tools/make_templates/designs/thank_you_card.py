"""Card: Thank You (a pink dahlia, frosted panel, script title)."""

from fe import assets
from fe.page import Page

META = {
    "id": "thank-you-card", "type": "card", "name": "Thank You Bloom",
    "keywords": ["thank you", "floral", "elegant", "gift", "simple"], "photos": ["dahlia"],
}


def build():
    page = Page(1050, 600)
    page.photo(assets.photo("dahlia"), focus=(0.5, 0.5), saturation=1.15, contrast=1.05, name="Dahlia photo")
    page.overlay([("#3a0b3a66", 0), ("#3a0b3a99", 1)], angle=90, name="Plum tint")
    page.vignette(0.45)
    # frosted panel: soft white fill and a fine white border
    page.shape("rectangle", 148, 128, 754, 330, "#ffffff", radius=30, opacity=0.34, name="Panel border")
    page.shape("rectangle", 151, 131, 748, 324, "#2a0a2c", radius=28, opacity=0.50, name="Panel")
    page.text("Thank You", 0, 148, 104, "#ffffff", family="Segoe Script", bold=False, width=1050, align="center",
              shadow=(4, 6, 12, 0.6), name="Title")
    page.text("from the bottom of my heart", 0, 292, 32, "#ffe9f5", family="Georgia", bold=False, italic=True,
              width=1050, align="center", name="Message")
    page.shape("rectangle", 385, 372, 280, 1.5, "#ffffff", opacity=0.6, name="Rule")
    page.shape("star", 513, 363, 24, 24, "#ffd6ec", name="Star")
    page.text("WITH LOVE   ·   YOUR NAME", 0, 390, 18, "#ffffff", family="Georgia", bold=False, letter_spacing=20,
              width=1050, align="center", name="Signature")
    return [page]
