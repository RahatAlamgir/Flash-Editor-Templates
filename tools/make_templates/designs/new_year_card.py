"""Card: Happy New Year (golden fireworks, big year in serif gold)."""

from fe import assets
from fe.page import Page

META = {
    "id": "new-year-card", "type": "card", "name": "New Year Sparkle",
    "keywords": ["new year", "party", "gold", "dark", "holiday"], "photos": ["fireworks"],
}

GOLD = "#f5c453"
PALE = "#fff1c9"


def build():
    page = Page(1050, 600)
    page.background("#05060d")
    page.photo(assets.photo("fireworks"), focus=(0.72, 0.18), saturation=1.15, contrast=1.1, name="Fireworks photo")
    page.overlay([("#05060df2", 0), ("#05060dc8", 0.42), ("#05060d10", 0.85)], angle=0, name="Dark left")
    page.overlay([("#05060d00", 0.6), ("#05060dc0", 1)], angle=90, name="Dark bottom")
    page.glow(-150, 120, 700, 700, GOLD, opacity=0.10, name="Gold glow")
    page.text("HAPPY NEW YEAR", 70, 98, 23, GOLD, family="Georgia", bold=False, letter_spacing=30, name="Greeting")
    page.shape("rectangle", 72, 148, 110, 2, GOLD, name="Rule top")
    page.text("2027", 62, 152, 190, PALE, family="Georgia", bold=True, shadow=(0, 0, 26, 0.55), name="Year")
    page.text("May every moment sparkle.", 74, 408, 32, "#ffffff", family="Georgia", bold=False, italic=True,
              name="Wish")
    page.text("WISHING YOU JOY, HEALTH & HAPPINESS", 76, 484, 15, GOLD, family="Georgia", bold=False,
              letter_spacing=22, name="Tagline")
    page.shape("rectangle", 72, 468, 110, 2, GOLD, name="Rule bottom")
    return [page]
