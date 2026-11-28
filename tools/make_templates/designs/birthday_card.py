"""Card: Birthday (the cake with letter candles, a wish in script, confetti)."""

import random

from fe import assets
from fe.page import Page

META = {
    "id": "birthday-card", "type": "card", "name": "Birthday Wish",
    "keywords": ["birthday", "party", "dark", "gift", "colorful"], "photos": ["cake"],
}

NAVY = "#0a1220"
CONFETTI = ["#ff4d6d", "#ffd166", "#06d6a0", "#4cc9f0", "#c77dff", "#ff9f1c"]


def build():
    page = Page(1050, 600)
    page.background(NAVY)
    page.photo(assets.photo("cake"), x=0, y=105, w=1050, h=495, focus=(0.5, 0.55), saturation=1.25, contrast=1.1,
               name="Cake photo")
    page.overlay([(NAVY + "ff", 0), (NAVY + "00", 1)], angle=90, name="Photo fade top", box=(0, 105, 1050, 120))
    page.overlay([(NAVY + "00", 0), (NAVY + "e8", 1)], angle=90, name="Dark bottom", box=(0, 470, 1050, 130))
    page.vignette(0.45)
    page.glow(250, -60, 550, 300, "#ff9f1c", opacity=0.14, name="Warm glow")
    rng = random.Random(21)   # the same confetti every time
    for i in range(22):
        kind = rng.choice(["rectangle", "ellipse", "star", "diamond"])
        size = rng.randint(14, 30)
        x, y = rng.randint(30, 1000), rng.randint(14, 120)
        page.shape(kind, x, y, size, size if kind != "rectangle" else size // 2, rng.choice(CONFETTI),
                   rotation=rng.randint(0, 80), opacity=0.9, name=f"Confetti {i + 1}")
    page.text("Make a wish", 0, 14, 104, "#ffe3a6", family="Segoe Script", bold=False, width=1050, align="center",
              shadow=(4, 6, 12, 0.7), name="Wish")
    page.text("Wishing you a day full of joy and sweet surprises", 0, 528, 25, "#e8ecf5", family="Georgia", bold=False,
              italic=True, width=1050, align="center", name="Message")
    return [page]
