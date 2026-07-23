import json
import os

LANGUAGE_FOLDER = "assets/languages"


def load_language(language="en"):
    path = os.path.join(LANGUAGE_FOLDER, f"{language}.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)