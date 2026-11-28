"""Card: Business Card Modern (dark navy, cyan accents, hexagon pattern, monogram)."""

from fe.page import Page

META = {
    "id": "business-card-modern", "type": "card", "name": "Business Card Modern",
    "keywords": ["business", "modern", "dark", "professional", "corporate"],
}

BG = "#0b1020"
CYAN = "#22d3ee"
MUTED = "#a8b3cf"


def build():
    page = Page(1050, 600)
    page.background(BG)
    page.gradient([("#1d3a8a", 0), (BG, 1)], radial=True, name="Blue glow", box=(300, -250, 1100, 1100))
    # hexagon pattern on the right
    page.shape("hexagon", 640, -90, 470, 470, CYAN, opacity=0.10, name="Hexagon big")
    page.shape("hexagon", 780, 150, 330, 330, CYAN, opacity=0.18, name="Hexagon middle")
    page.shape("hexagon", 700, 380, 190, 190, CYAN, opacity=0.30, name="Hexagon small")
    page.shape("rectangle", 880, -40, 6, 700, CYAN, opacity=0.5, rotation=24, name="Slash")
    page.shape("rectangle", 905, -40, 2, 700, "#ffffff", opacity=0.25, rotation=24, name="Slash thin")
    # monogram
    page.shape("ellipse", 76, 66, 92, 92, CYAN, name="Monogram circle")
    page.text("AM", 76, 83, 40, BG, width=92, align="center", name="Monogram")
    page.text("MORGAN STUDIO", 188, 96, 20, "#ffffff", letter_spacing=24, name="Company")
    # name and title
    page.text("Alex Morgan", 76, 205, 70, "#ffffff", shadow=(4, 6, 10, 0.4), name="Name")
    page.text("CREATIVE DIRECTOR", 80, 298, 22, CYAN, letter_spacing=22, name="Job title")
    page.shape("rectangle", 80, 350, 90, 4, CYAN, radius=2, name="Rule")
    # contact lines
    rows = ["+1 (555) 123-4567", "alex@morgan.studio", "www.morgan.studio", "123 Design Street, Springfield"]
    for i, row in enumerate(rows):
        y = 392 + i * 47
        page.shape("ellipse", 80, y + 10, 14, 14, CYAN, name=f"Dot {i + 1}")
        page.text(row, 112, y, 25, "#e6ebf7", bold=False, name=f"Contact {i + 1}")
    return [page]
