import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.pdfbase import pdfmetrics

from design.fonts import (
    ENGLISH_FONT,
    ENGLISH_BOLD_FONT,
    ARABIC_FONT,
    ARABIC_BOLD_FONT,
)


def is_arabic(text: str) -> bool:
    if not text:
        return False

    return any('\u0600' <= ch <= '\u06FF' for ch in text)


def prepare_text(text: str):
    if not text:
        return text

    if is_arabic(text):
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)

    return text


def get_font(text: str, bold=False):
    if is_arabic(text):
        return ARABIC_BOLD_FONT if bold else ARABIC_FONT

    return ENGLISH_BOLD_FONT if bold else ENGLISH_FONT


def draw_text(
    canvas,
    text,
    x,
    y,
    align="left",
    bold=False,
    size=10,
):
    original = str(text)
    prepared = prepare_text(original)

    font = get_font(original, bold)

    # -------- DEBUG --------
    print("----------------------")
    print("Original :", repr(original))
    print("Prepared :", repr(prepared))
    print("Font     :", font)
    print("----------------------")
    # -----------------------

    canvas.setFont(font, size)

    width = pdfmetrics.stringWidth(prepared, font, size)

    if align == "right":
        canvas.drawString(x - width, y, prepared)
    elif align == "center":
        canvas.drawString(x - width / 2, y, prepared)
    else:
        canvas.drawString(x, y, prepared)