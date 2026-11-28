"""Card: Business Card Minimal (warm white, serif type, a dark side band with a gold monogram)."""

from fe.page import Page

META = {
    "id": "business-card-minimal", "type": "card", "name": "Business Card Minimal",
    "keywords": ["business", "minimal", "simple", "professional", "gold"],
}

PAPER = "#fbfaf7"
INK = "#1b1b1b"
GOLD = "#b08d57"
GREY = "#7a7468"


def build():
    page = Page(1050, 600)
    page.background(PAPER)
    # the dark side band with the monogram
    page.shape("rectangle", 790, 0, 260, 600, "#1f1f1f", name="Side band")
    page.shape("rectangle", 818, 28, 204, 544, GOLD, opacity=0.55, name="Band frame")
    page.shape("rectangle", 820, 30, 200, 540, "#1f1f1f", name="Band inner")
    page.text("SB", 790, 210, 96, GOLD, family="Georgia", bold=False, width=260, align="center", name="Monogram")
    page.shape("rectangle", 895, 345, 50, 2, GOLD, name="Monogram rule")
    page.text("STUDIO NORTH", 790, 375, 17, "#cfc6b4", family="Georgia", bold=False, letter_spacing=26, width=260,
              align="center", name="Studio")
    # left side
    page.shape("rectangle", 70, 72, 20, 20, INK, name="Mark")
    page.text("STUDIO NORTH", 104, 66, 18, INK, family="Georgia", bold=False, letter_spacing=26, name="Company")
    page.text("Sofia Bennett", 66, 176, 64, INK, family="Georgia", bold=False, name="Name")
    page.text("Architect & Interior Designer", 70, 270, 27, GREY, family="Georgia", bold=False, italic=True,
              name="Job title")
    page.shape("rectangle", 72, 335, 64, 3, GOLD, name="Rule")
    cells = [("PHONE", "+44 20 7946 0958", 72, 410), ("EMAIL", "sofia@studionorth.com", 400, 410),
             ("WEB", "www.studionorth.com", 72, 490), ("STUDIO", "14 Mill Lane, London", 400, 490)]
    for label, value, x, y in cells:
        page.text(label, x, y, 14, GOLD, family="Georgia", bold=True, letter_spacing=24, name=f"{label.title()} label")
        page.text(value, x, y + 24, 23, INK, family="Georgia", bold=False, name=f"{label.title()} value")
    return [page]
