from core.pdf.components import divider
from core.pdf.layout_engine import LayoutEngine

from design.layout import (
    HEADER_SPACING,
    PAGE_MARGIN,
    SECTION_SPACING,
)

from design.fonts import SUBTITLE_SIZE

from design.text import draw_text


def draw(
    canvas,
    title,
    current_y,
    width,
):
    """
    Draw a section title.

    Parameters
    ----------
    canvas : reportlab.pdfgen.canvas.Canvas
        PDF canvas.

    title : str
        Section title.

    current_y : float
        Current drawing position.

    width : float
        Page width.

    Returns
    -------
    float
        Y position for the next content.
    """

    divider.draw(
        canvas=canvas,
        y=current_y,
        width=width,
    )

    current_y -= HEADER_SPACING

    draw_text(
        canvas=canvas,
        text=title,
        x=width - PAGE_MARGIN,
        y=current_y,
        align="right",
        bold=True,
        size=SUBTITLE_SIZE,
    )

    current_y -= SECTION_SPACING

    return current_y