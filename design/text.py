import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.pdfbase import pdfmetrics


import re

TIME_PATTERN = re.compile(
    r"^(\d{1,2}:\d{2})\s*(AM|PM)$",
    re.IGNORECASE,
)

from design.fonts import (
    ENGLISH_FONT,
    ENGLISH_BOLD_FONT,
    ARABIC_FONT,
    ARABIC_BOLD_FONT,
)


def is_arabic(text: str):
    if not text:
        return False

    return any('\u0600' <= ch <= '\u06FF' for ch in text)


def prepare_text(text: str):
    if not text:
        return text

    if is_arabic(text):
        return get_display(arabic_reshaper.reshape(text))

    return text


def get_font(text: str, bold=False):
    if is_arabic(text):
        return ARABIC_BOLD_FONT if bold else ARABIC_FONT

    return ENGLISH_BOLD_FONT if bold else ENGLISH_FONT


def text_width(text: str, bold=False, size=10):
    original = str(text or "")
    prepared = prepare_text(original)

    font = get_font(original, bold)

    return pdfmetrics.stringWidth(prepared, font, size)


def wrap_text(
    text,
    max_width,
    bold=False,
    size=10,
):
    text = str(text or "").strip()

    if not text:
        return [""]

    if TIME_PATTERN.match(text):
        return [text]

    words = text.split()

    if len(words) <= 1:
        return [text]

    lines = []
    current = words[0]

    for word in words[1:]:
        candidate = f"{current} {word}"

        if text_width(candidate, bold, size) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word

    lines.append(current)

    return lines


def text_height(
    text,
    max_width,
    bold=False,
    size=10,
    line_spacing=1.2,
):
    lines = wrap_text(
        text=text,
        max_width=max_width,
        bold=bold,
        size=size,
    )

    return len(lines) * size * line_spacing


def _font_metrics(font_name, size):
    """
    Returns font ascent/descent in points.
    """

    face = pdfmetrics.getFont(font_name).face

    ascent = face.ascent * size / 1000.0
    descent = abs(face.descent) * size / 1000.0

    return ascent, descent

def draw_multiline_text(
    canvas,
    text,
    x,
    y,
    max_width,
    align=None,
    bold=False,
    size=10,
    line_spacing=1.2,
):
    """
    Draw wrapped multiline text.

    y = center of the text block.
    """

    if isinstance(text, list):
        lines = text

    else:
        text = format_time(text)

        lines = wrap_text(
            text=text,
            max_width=max_width,
            bold=bold,
            size=size,
        )

    line_height = size * line_spacing
    total_height = len(lines) * line_height

    sample = next(
        (line for line in lines if str(line).strip()),
        "",
    )

    font = get_font(sample, bold)

    ascent, descent = _font_metrics(
        font,
        size,
    )

    baseline = (
        y
        + (total_height / 2)
        - ascent
        + ((ascent + descent - size) / 2)
    )

    current_y = baseline

    for line in lines:

        draw_text(
            canvas=canvas,
            text=line,
            x=x,
            y=current_y,
            align=align,
            bold=bold,
            size=size,
        )

        current_y -= line_height

    return total_height


def draw_text(
    canvas,
    text,
    x,
    y,
    align=None,
    bold=False,
    size=10,
):
    """
    Draw text using the current language direction.
    """

    original = str(text)

    if TIME_PATTERN.match(original.strip()):
        prepared = original
    else:
        prepared = prepare_text(original)

    font = get_font(original, bold)

    canvas.setFont(font, size)

    width = pdfmetrics.stringWidth(
        prepared,
        font,
        size,
    )

    if align is None:
        align = "right" if is_rtl() else "left"

    if align == "right":
        canvas.drawRightString(
            x,
            y,
            prepared,
        )

    elif align == "center":
        canvas.drawCentredString(
            x,
            y,
            prepared,
        )

    else:
        canvas.drawString(
            x,
            y,
            prepared,
        )
    
def format_time(text):
    """
    Convert:
        9:50 AM -> AM 9:50
        10:00 PM -> PM 10:00
    """

    if not isinstance(text, str):
        return text

    match = TIME_PATTERN.match(text.strip())

    if not match:
        return text

    time_part, period = match.groups()

    return f"{period.upper()} {time_part}"