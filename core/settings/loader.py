import json
from pathlib import Path

from models.settings import Settings


SETTINGS_FILE = Path("settings.json")


def load_settings() -> Settings:
    """
    Load application settings from settings.json.

    Returns
    -------
    Settings
    """

    if not SETTINGS_FILE.exists():
        return Settings()

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    except (json.JSONDecodeError, OSError):
        return Settings()

    return Settings(
        company=data.get("company", ""),
        language=data.get("language", "en"),
        late_grace_minutes=data.get("late_grace_minutes", 30),
        absence_after_minutes=data.get("absence_after_minutes", 360),
        calculate_from_absence_time_if_checkout_only=data.get(
            "calculate_from_absence_time_if_checkout_only",
            True,
        ),
        pdf_font_size=data.get("pdf_font_size", 10),
    )
def save_settings(settings: Settings) -> None:
    """
    Save application settings to settings.json.
    """

    data = {
        "company": settings.company,
        "language": settings.language,
        "late_grace_minutes": settings.late_grace_minutes,
        "absence_after_minutes": settings.absence_after_minutes,
        "calculate_from_absence_time_if_checkout_only":
            settings.calculate_from_absence_time_if_checkout_only,
        "pdf_font_size": settings.pdf_font_size,
    }

    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )