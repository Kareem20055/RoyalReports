import re


def format_date_range(date_range: str) -> str:
    """
    Converts:
    2026-07-25 00:00:00 - 2026-07-30 23:59:59

    To:
    2026-07-25 - 2026-07-30
    """

    if not date_range:
        return ""

    dates = re.findall(r"\d{4}-\d{2}-\d{2}", str(date_range))

    if len(dates) >= 2:
        return f"{dates[0]} - {dates[1]}"

    return str(date_range)