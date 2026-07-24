from datetime import datetime, date, time, timedelta


def combine(date_value: date, time_value: time) -> datetime | None:
    """
    Combine date and time into datetime.
    """

    if date_value is None or time_value is None:
        return None

    return datetime.combine(date_value, time_value)


def minutes_between(
    start: datetime | None,
    end: datetime | None,
) -> int:
    """
    Returns the number of minutes between two datetimes.

    If either value is None, returns 0.
    """

    if start is None or end is None:
        return 0

    minutes = int((end - start).total_seconds() // 60)

    return max(minutes, 0)


def add_minutes(
    value: datetime | None,
    minutes: int,
) -> datetime | None:
    """
    Add minutes to datetime.
    """

    if value is None:
        return None

    return value + timedelta(minutes=minutes)


def subtract_minutes(
    value: datetime | None,
    minutes: int,
) -> datetime | None:
    """
    Subtract minutes from datetime.
    """

    if value is None:
        return None

    return value - timedelta(minutes=minutes)


def is_after(
    first: datetime | None,
    second: datetime | None,
) -> bool:
    """
    Returns True if first > second.
    """

    if first is None or second is None:
        return False

    return first > second


def is_before(
    first: datetime | None,
    second: datetime | None,
) -> bool:
    """
    Returns True if first < second.
    """

    if first is None or second is None:
        return False

    return first < second


def format_minutes(minutes: int) -> str:
    """
    Convert minutes to HH:MM.
    """

    if minutes <= 0:
        return "00:00"

    hours = minutes // 60
    mins = minutes % 60

    return f"{hours:02}:{mins:02}"


def format_time(value: datetime | None) -> str:
    """
    Convert datetime to HH:MM.
    """

    if value is None:
        return "--"

    return value.strftime("%H:%M")


def has_value(value) -> bool:
    """
    Check if a value exists.
    """

    return value is not None