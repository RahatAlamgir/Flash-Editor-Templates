"""Slide 2: agenda with four numbered rows."""

from .theme import BG, CYAN, MUTED, PANEL_LINE, WHITE, heading, new_slide

ROWS = [
    ("The Problem", "Why change is needed"),
    ("Our Solution", "Meet Nova X"),
    ("Key Numbers", "Results that matter"),
    ("Roadmap", "What comes next"),
]


def build():
    page = new_slide(2)
    heading(page, "Agenda", size=100)
    page.text("A quick tour of\nwhat we built and\nwhere we are going.", 124, 360, 44, MUTED, bold=False)
    page.shape("hexagon", 120, 700, 300, 300, CYAN, opacity=0.14, name="Hexagon")
    for i, (title, note) in enumerate(ROWS):
        y = 170 + i * 200
        page.shape("ellipse", 820, y, 100, 100, CYAN, name=f"Number circle {i + 1}")
        page.text(str(i + 1), 820, y + 18, 50, BG, width=100, align="center", name=f"Number {i + 1}")
        page.text(title, 960, y - 6, 56, WHITE, name=f"Item {i + 1}")
        page.text(note, 962, y + 62, 32, MUTED, bold=False, name=f"Item note {i + 1}")
        page.shape("rectangle", 820, y + 140, 980, 2, PANEL_LINE, name=f"Line {i + 1}")
    return page
