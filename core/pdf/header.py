from core.pdf.components import divider

from design.layout import (
    HEADER_TOP,
    HEADER_SPACING,
    HEADER_BOTTOM_SPACING,
)

from design.fonts import (
    TITLE_SIZE,
    SUBTITLE_SIZE,
)

from design.text import draw_text


def draw(
    canvas,
    report,
    settings,
    width,
    height,
):
    """
    Draw the report header.

    Parameters
    ----------
    canvas : reportlab.pdfgen.canvas.Canvas
        PDF canvas.

    report : Report
        Report model.

    settings : Settings
        Application settings.

    width : float
        Page width.

    height : float
        Page height.

    Returns
    -------
    float
        Y position for the next section.
    """

    center_x = width / 2
    current_y = height - HEADER_TOP

    if report.company:

        draw_text(
            canvas=canvas,
            text=report.company,
            x=center_x,
            y=current_y,
            align="center",
            bold=True,
            size=TITLE_SIZE,
        )

        current_y -= HEADER_SPACING

    draw_text(
        canvas=canvas,
        text=report.title,
        x=center_x,
        y=current_y,
        align="center",
        bold=True,
        size=SUBTITLE_SIZE,
    )

    current_y -= HEADER_SPACING

    if report.date_range:

        draw_text(
            canvas=canvas,
            text=report.date_range,
            x=center_x,
            y=current_y,
            align="center",
            size=SUBTITLE_SIZE,
        )

        current_y -= HEADER_SPACING

    divider.draw(
        canvas=canvas,
        y=current_y,
        width=width,
    )

    current_y -= HEADER_BOTTOM_SPACING

    return current_y