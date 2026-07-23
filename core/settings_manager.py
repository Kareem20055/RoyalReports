import json
import os


class SettingsManager:

    SETTINGS_FILE = "settings.json"

    DEFAULT_SETTINGS = {
        "language": "en",
        "company": "Royal Glass",
        "output_folder": "output"
    }

    @classmethod
    def load(cls):

        if not os.path.exists(cls.SETTINGS_FILE):
            cls.save(cls.DEFAULT_SETTINGS)

        with open(cls.SETTINGS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def save(cls, settings):

        with open(cls.SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                settings,
                file,
                indent=4,
                ensure_ascii=False
            )