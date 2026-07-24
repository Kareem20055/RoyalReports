from dataclasses import dataclass


@dataclass
class Settings:

    company: str = ""

    language: str = "en"

    late_grace_minutes: int = 30

    absence_after_minutes: int = 360

    calculate_from_absence_time_if_checkout_only: bool = True

    pdf_font_size: int = 10