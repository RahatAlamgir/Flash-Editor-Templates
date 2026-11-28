"""Card: Eid Mubarak (mosque at sunset, deep green and gold, crescent and stars)."""

from fe import assets
from fe.page import Page

META = {
    "id": "eid-mubarak-card", "type": "card", "name": "Eid Mubarak",
    "keywords": ["eid", "holiday", "gold", "green", "elegant"], "photos": ["mosque"],
}

GREEN = "#06241b"
GOLD = "#f2c14e"


def build():
    page = Page(1050, 600)
    page.background(GREEN)
    page.photo(assets.photo("mosque"), focus=(0.5, 0.80), saturation=1.45, contrast=1.3, name="Mosque photo")
    page.overlay([(GREEN + "f2", 0), (GREEN + "b0", 0.38), (GREEN + "00", 0.7)], angle=90, name="Green top")
    page.overlay([(GREEN + "00", 0.7), (GREEN + "d8", 1)], angle=90, name="Green bottom")
    page.vignette(0.45)
    page.glow(790, 270, 360, 360, GOLD, opacity=0.30, name="Sun glow")
    # crescent and stars
    page.glow(24, 24, 190, 190, GOLD, opacity=0.18, name="Moon glow")
    page.crescent(52, 66, 88, GOLD, rotation=-28, name="Crescent")
    page.shape("star", 134, 52, 26, 26, GOLD, rotation=10, name="Star big")
    page.shape("star", 158, 104, 16, 16, GOLD, rotation=-8, opacity=0.8, name="Star small")
    page.shape("star", 118, 140, 12, 12, GOLD, opacity=0.7, name="Star tiny")
    page.text("Eid Mubarak", 0, 44, 92, "#ffffff", family="Segoe Script", bold=False, width=1050, align="center",
              shadow=(4, 6, 12, 0.7), name="Title")
    page.shape("rectangle", 400, 182, 250, 2, GOLD, opacity=0.8, name="Rule")
    page.text("May your days be filled with peace, joy and blessings", 0, 194, 25, "#f6ecd0", family="Georgia",
              bold=False, italic=True, width=1050, align="center", name="Message")
    page.text("WITH LOVE AND PRAYERS", 0, 534, 16, GOLD, family="Georgia", bold=False, letter_spacing=26,
              width=1050, align="center", name="Signature")
    return [page]
