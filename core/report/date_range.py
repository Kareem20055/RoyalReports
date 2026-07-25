import re


def build_folder_name(date_range: str) -> str:

    dates = re.findall(r"\d{4}-\d{2}-\d{2}", date_range)

    if len(dates) == 2:
        return f"{dates[0]} - {dates[1]}"

    return "Unknown Period"