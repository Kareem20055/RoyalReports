from core.pdf.components import divider

from design.layout import (
    PAGE_MARGIN,
    FOOTER_MARGIN,
)

from design.fonts import SMALL_SIZE
from design.text import draw_text

from i18n import t
from core.pdf.layout_engine import LayoutEngine


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

    # النص الموجود على بداية الصفحة (يمين في العربي - شمال في الإنجليزي)
    draw_text(
        canvas=canvas,
        text=t("generated_by"),
        x=LayoutEngine.page_start(width, PAGE_MARGIN),
        y=current_y,
        size=SMALL_SIZE,
    )

    # رقم الصفحة في نهاية الصفحة (شمال في العربي - يمين في الإنجليزي)
    draw_text(
        canvas=canvas,
        text=str(canvas.getPageNumber()),
        x=LayoutEngine.page_end(width, PAGE_MARGIN),
        y=current_y,
        align=LayoutEngine.text_align(),
        size=SMALL_SIZE,
    )