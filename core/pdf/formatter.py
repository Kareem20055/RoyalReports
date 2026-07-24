from datetime import datetime, time


def format_date(value):
    """
    Format date for display.
    """
    if not value:
        return ""

    if isinstance(value, datetime):
        return value.strftime("%d/%m/%Y")

    return str(value)


def format_time(value):
    """
    Format time for display.
    """

    if not value:
        return "--:--"

    if isinstance(value, (datetime, time)):
        value = value.strftime("%I:%M %p").lstrip("0")
    else:
        value = str(value)

    parts = value.split()

    if len(parts) == 2:
        clock, period = parts
        return f"{period.upper()} {clock}"

    return value


def format_minutes(minutes):
    """
    Convert minutes to HH:MM.
    """
    if minutes is None:
        return "--:--"

    hours = minutes // 60
    mins = minutes % 60

    return f"{hours:02d}:{mins:02d}"
    
def format_shift(start, end):
    """
    Format shift time range.
    """

    if not start or not end:
        return "--"

    return f"{format_time(start)} - {format_time(end)}"