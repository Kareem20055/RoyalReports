from datetime import datetime, time

from models.attendance_row import AttendanceRow
from models.parsed_attendance import ParsedAttendance


TIME_FORMATS = (
    "%H:%M:%S",
    "%H:%M",
)


def parse_time(value) -> time | None:
    """
    Parse a time value from Hikvision.
    """

    if value is None:
        return None

    if isinstance(value, time):
        return value

    text = str(value).strip()

    if not text:
        return None

    for fmt in TIME_FORMATS:

        try:
            return datetime.strptime(text, fmt).time()

        except ValueError:
            continue

    return None


def parse_schedule(schedule: str) -> tuple[time | None, time | None]:
    """
    Parse Hikvision schedule.

    Example
    -------
    (10:00:00-20:00:00)
    """

    if schedule is None:
        return None, None

    text = str(schedule).strip()

    if not text:
        return None, None

    text = text.replace("(", "").replace(")", "")

    if "-" not in text:
        return None, None

    start_text, end_text = text.split("-", 1)

    return (
        parse_time(start_text),
        parse_time(end_text),
    )


def parse_date(value):
    """
    Parse Excel date.
    """

    if value is None:
        return None

    if hasattr(value, "date"):
        return value.date()

    text = str(value).strip()

    if not text:
        return None

    for fmt in (
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
    ):

        try:
            return datetime.strptime(text, fmt).date()

        except ValueError:
            continue

    return None


def parse_attendance(
    attendance_row: AttendanceRow,
) -> ParsedAttendance:
    """
    Convert raw AttendanceRow into ParsedAttendance.
    """

    attendance_date = parse_date(attendance_row.date)

    shift_start_time, shift_end_time = parse_schedule(
        attendance_row.schedule
    )

    check_in_time = parse_time(attendance_row.check_in)

    check_out_time = parse_time(attendance_row.check_out)

    shift_start = (
        datetime.combine(attendance_date, shift_start_time)
        if attendance_date and shift_start_time
        else None
    )

    shift_end = (
        datetime.combine(attendance_date, shift_end_time)
        if attendance_date and shift_end_time
        else None
    )

    check_in = (
        datetime.combine(attendance_date, check_in_time)
        if attendance_date and check_in_time
        else None
    )

    check_out = (
        datetime.combine(attendance_date, check_out_time)
        if attendance_date and check_out_time
        else None
    )

    return ParsedAttendance(
        date=attendance_date,
        weekday=attendance_row.weekday,
        shift_start=shift_start,
        shift_end=shift_end,
        check_in=check_in,
        check_out=check_out,
    )