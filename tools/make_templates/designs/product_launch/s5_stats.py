"""Slide 5: four big numbers."""

from .theme import CYAN, MUTED, PANEL, PANEL_LINE, PINK, VIOLET, WHITE, heading, new_slide

STATS = [
    ("2x", CYAN, "Faster speed", "Compared with the\nprevious model"),
    ("40%", VIOLET, "Less power", "Longer life on\none charge"),
    ("99.9%", PINK, "Uptime", "Reliable every\nsingle day"),
    ("1M+", CYAN, "Happy users", "Around the world\nand growing"),
]


def build():
    page = new_slide(5)
    heading(page, "Results in Numbers")
    for i, (number, color, label, note) in enumerate(STATS):
        x = 120 + i * 430
        page.shape("rectangle", x - 2, 318, 394, 564, PANEL_LINE, radius=30, name=f"Card border {i + 1}")
        page.shape("rectangle", x, 320, 390, 560, PANEL, radius=28, name=f"Card {i + 1}")
        page.shape("rectangle", x + 135, 372, 120, 8, color, radius=4, name=f"Accent {i + 1}")
        page.text(number, x, 425, 104, color, width=390, align="center", name=f"Number {i + 1}")
        page.text(label, x, 600, 42, WHITE, width=390, align="center", name=f"Label {i + 1}")
        page.text(note, x, 680, 30, MUTED, bold=False, width=390, align="center", name=f"Note {i + 1}")
    return page
