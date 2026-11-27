"""YouTube thumbnail: Match Highlights (black and red, slanted stripes)."""

from fe.page import Page

META = {
    "id": "match-highlights", "type": "youtube-thumbnail", "name": "Match Highlights",
    "keywords": ["sports", "dark", "red", "modern"],
}


def build():
    page = Page(1280, 720)
    page.background("#0a0a0a")
    page.gradient([("#1f1f1f", 0), ("#0a0a0a", 1)], angle=0)
    page.shape("rectangle", 760, -100, 150, 950, "#dc2626", rotation=18, name="Stripe red")
    page.shape("rectangle", 940, -100, 60, 950, "#ffffff", rotation=18, name="Stripe white")
    page.shape("rectangle", 1030, -100, 280, 950, "#dc2626", rotation=18, name="Stripe red wide")
    page.shape("rectangle", 70, 90, 300, 66, "#dc2626", name="Label")
    page.text("FULL TIME", 70, 98, 40, "#ffffff", width=300, align="center")
    page.text("MATCH", 70, 150, 230, "#ffffff", family="Impact", bold=False)
    page.text("HIGHLIGHTS", 70, 355, 112, "#dc2626", family="Impact", bold=False)
    page.text("2 : 1", 70, 530, 120, "#ffffff", family="Impact", bold=False)
    page.shape("star", 1010, 330, 200, 200, "#fde047", rotation=-8, name="Star")
    return [page]
