"""YouTube thumbnail: Travel Diary (teal sky, sun, big white title)."""

from fe.page import Page

META = {
    "id": "travel-diary", "type": "youtube-thumbnail", "name": "Travel Diary",
    "keywords": ["travel", "summer", "holiday", "colorful"],
}


def build():
    page = Page(1280, 720)
    page.background("#0ea5b7")
    page.gradient([("#0e7490", 0), ("#2dd4bf", 1)], angle=90)
    page.shape("ellipse", 1000, 50, 200, 200, "#fde047", name="Sun")
    page.shape("ellipse", 950, 0, 300, 300, "#fde047", opacity=0.25, name="Sun glow")
    page.shape("triangle", -60, 420, 700, 360, "#115e59", name="Mountain back")
    page.shape("triangle", 380, 470, 760, 320, "#134e4a", name="Mountain middle")
    page.shape("triangle", 850, 440, 560, 340, "#115e59", name="Mountain right")
    page.text("TRAVEL", 0, 90, 230, "#ffffff", family="Impact", bold=False, width=1280, align="center")
    page.text("DIARY", 0, 335, 140, "#fde047", family="Impact", bold=False, width=1280, align="center")
    page.shape("rectangle", 420, 600, 440, 76, "#ffffff", radius=38, name="Label")
    page.text("BALI  |  EPISODE 1", 420, 610, 38, "#0e7490", width=440, align="center")
    return [page]
