from i18n import is_rtl


def normalize_table(
    headers,
    rows,
    weights=None,
    max_column_widths=None,
):
    """
    Normalize table structure for the current language.
    """

    if not is_rtl():
        return (
            headers,
            rows,
            weights,
            max_column_widths,
        )

    headers = list(reversed(headers))
    rows = [list(reversed(row)) for row in rows]

    if weights is not None:
        weights = list(reversed(weights))

    if max_column_widths is not None:
        max_column_widths = list(reversed(max_column_widths))

    return (
        headers,
        rows,
        weights,
        max_column_widths,
    )