"""Card: Wedding Invitation (white roses on the left, cream panel with a gold frame and script names)."""

from fe import assets
from fe.page import Page

META = {
    "id": "wedding-invitation", "type": "card", "name": "Wedding Invitation",
    "keywords": ["wedding", "elegant", "floral", "invitation", "gold"], "photos": ["rose_garden"],
}

CREAM = "#fbf6ec"
GOLD = "#b08d57"
GREEN = "#2f4a3a"
SOFT = "#8a7a5a"
TEXT = "#5b5547"
PANEL_X, PANEL_W = 420, 630


def build():
    page = Page(1050, 600)
    page.background(CREAM)
    page.photo(assets.photo("rose_garden"), x=0, y=0, w=PANEL_X + 40, h=600, focus=(0.42, 0.5), saturation=1.1,
               contrast=1.05, name="Roses photo")
    page.overlay([("#fbf6ec00", 0), ("#fbf6ecff", 1)], angle=0, name="Photo fade", box=(PANEL_X - 40, 0, 80, 600))
    page.shape("rectangle", PANEL_X + 28, 30, PANEL_W - 58, 540, GOLD, opacity=0.7, name="Frame")
    page.shape("rectangle", PANEL_X + 31, 33, PANEL_W - 64, 534, CREAM, name="Frame inner")
    page.shape("rectangle", PANEL_X + 44, 46, PANEL_W - 92, 508, GOLD, opacity=0.35, name="Frame fine")
    page.shape("rectangle", PANEL_X + 45, 47, PANEL_W - 94, 506, CREAM, name="Frame fine inner")
    cx = PANEL_X + 28 + (PANEL_W - 58) / 2   # middle of the frame
    box = dict(x=PANEL_X + 28, width=PANEL_W - 58, align="center")
    page.text("TOGETHER WITH THEIR FAMILIES", y=84, size=15, color=SOFT, family="Georgia", bold=False,
              letter_spacing=22, name="Families", **box)
    page.shape("rectangle", cx - 150, 135, 90, 1.5, GOLD, name="Line left")
    page.shape("diamond", cx - 7, 128, 14, 14, GOLD, name="Diamond")
    page.shape("rectangle", cx + 60, 135, 90, 1.5, GOLD, name="Line right")
    page.text("Emma & James", y=164, size=58, color=GREEN, family="Segoe Script", bold=False, name="Names", **box)
    page.text("request the pleasure of your company\nat their wedding celebration", y=286, size=22, color=TEXT,
              family="Georgia", bold=False, italic=True, name="Request", **box)
    page.text("SATURDAY   ·   14 JUNE 2026", y=388, size=20, color=GREEN, family="Georgia", bold=True,
              letter_spacing=14, name="Date", **box)
    page.text("FOUR O'CLOCK IN THE AFTERNOON", y=428, size=14, color=SOFT, family="Georgia", bold=False,
              letter_spacing=22, name="Time", **box)
    page.text("The Rose Garden, Willow Lane", y=456, size=22, color=TEXT, family="Georgia", bold=False, italic=True,
              name="Venue", **box)
    page.text("RSVP BY 1 MAY   ·   EMMA.JAMES@EMAIL.COM", y=514, size=13, color=SOFT, family="Georgia", bold=False,
              letter_spacing=16, name="RSVP", **box)
    return [page]
