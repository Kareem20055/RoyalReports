from design.colors import LIGHT_GRAY

from design.layout import PAGE_MARGIN


def draw(
    canvas,
    y,
    width,
    color=LIGHT_GRAY,
):
    """
    Draw a horizontal divider.

    Parameters
    ----------
    canvas : reportlab.pdfgen.canvas.Canvas
        PDF canvas.

    y : float
        Divider Y position.

    width : float
        Page width.

    color : Color, optional
        Divider color.

    Returns
    -------
    float
        Divider Y position.
    """

    canvas.setStrokeColor(color)

    canvas.line(
        PAGE_MARGIN,
        y,
        width - PAGE_MARGIN,
        y,
    )

    return y