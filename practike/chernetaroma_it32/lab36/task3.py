
import json
import sys
from pathlib import Path

print("Roman Cherneta, IT-32")

BASE_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = BASE_DIR / "settings.json"
EXPENSES_FILE = BASE_DIR / "data" / "expenses.json"

default_settings = {
    "owner": "Roman Cherneta",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            default_settings,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("settings.json not found, default created")
    sys.exit(0)

try:
    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        settings = json.load(file)

except json.JSONDecodeError as error:
    print(
        f"JSON error in line {error.lineno}: {error.msg}",
        file=sys.stderr
    )
    sys.exit(1)

with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
    records = json.load(file)

spent = sum(record["amount"] for record in records)

limit = settings["monthly_limit"]
left = limit - spent

print(f"owner: {settings['owner']}")
print(f"group: {settings['group']}")
print(f"limit: {limit:.2f} {settings['currency']}")
print(f"spent: {spent:.2f} {settings['currency']}")
print(f"left: {left:.2f} {settings['currency']}")
