"""Slide 7: four-step timeline."""

from .theme import BG, CYAN, MUTED, PANEL_LINE, VIOLET, WHITE, heading, new_slide

STEPS = [
    ("Q1", "Prototype", "Design and first test\nunits are ready."),
    ("Q2", "Beta", "1,000 early users\ntry Nova X."),
    ("Q3", "Launch", "On sale in\n20 countries."),
    ("Q4", "Scale", "New models and\npartner stores."),
]


def build():
    page = new_slide(7)
    heading(page, "Roadmap")
    page.shape("rectangle", 200, 536, 1520, 8, PANEL_LINE, radius=4, name="Timeline")
    page.shape("rectangle", 200, 536, 780, 8, CYAN, radius=4, name="Timeline done")
    for i, (quarter, title, text) in enumerate(STEPS):
        cx = 280 + i * 453
        color = CYAN if i < 2 else VIOLET
        page.text(quarter, cx - 210, 380, 64, color, width=420, align="center", name=f"Quarter {i + 1}")
        page.shape("ellipse", cx - 44, 496, 88, 88, color, opacity=0.25, name=f"Dot halo {i + 1}")
        page.shape("ellipse", cx - 26, 514, 52, 52, color, name=f"Dot {i + 1}")
        page.text(title, cx - 210, 620, 46, WHITE, width=420, align="center", name=f"Step {i + 1}")
        page.text(text, cx - 210, 700, 30, MUTED, bold=False, width=420, align="center", name=f"Step text {i + 1}")
    return page
