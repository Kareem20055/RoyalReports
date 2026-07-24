from core.pdf.layout_engine import LayoutEngine


def build_columns(
    headers,
    rows,
    page_width,
    margin,
    weights,
    max_column_widths,
):
    """
    Build table columns using LayoutEngine.
    """

    layout = LayoutEngine.data_table_layout(
        headers=headers,
        rows=rows,
        page_width=page_width,
        margin=margin,
        weights=weights,
        max_column_widths=max_column_widths,
    )

    # نرجع الأعمدة فقط كما كان التصميم الأصلي
    return layout.columns