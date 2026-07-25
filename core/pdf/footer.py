from core.pdf.components import divider

from design.layout import (
    PAGE_MARGIN,
    FOOTER_MARGIN,
)

from design.fonts import SMALL_SIZE
from design.text import draw_text


def draw(
    canvas,
    width,
):
    """
    Draw the report footer.
    """

    current_y = FOOTER_MARGIN

    divider.draw(
        canvas=canvas,
        y=current_y + 12,
        width=width,
    )

    # النص أسفل يمين الصفحة
    draw_text(
        canvas=canvas,
        text="تم إنشاء التقرير بواسطة RoyalReports",
        x=width - PAGE_MARGIN,
        y=current_y,
        align="right",
        size=SMALL_SIZE,
    )

    # رقم الصفحة أسفل يسار الصفحة
    draw_text(
        canvas=canvas,
        text=str(canvas.getPageNumber()),
        x=PAGE_MARGIN,
        y=current_y,
        align="left",
        size=SMALL_SIZE,
    )