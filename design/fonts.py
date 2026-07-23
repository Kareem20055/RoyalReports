from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")


def register_fonts():
    pdfmetrics.registerFont(
        TTFont(
            "NotoSans",
            os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "NotoSans-Bold",
            os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "Amiri",
            os.path.join(FONT_DIR, "Amiri-Regular.ttf")
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "Amiri-Bold",
            os.path.join(FONT_DIR, "Amiri-Bold.ttf")
        )
    )


ENGLISH_FONT = "NotoSans"
ENGLISH_BOLD_FONT = "NotoSans-Bold"

ARABIC_FONT = "Amiri"
ARABIC_BOLD_FONT = "Amiri-Bold"


TITLE_SIZE = 20
SUBTITLE_SIZE = 13
HEADER_SIZE = 11
BODY_SIZE = 10
SMALL_SIZE = 8