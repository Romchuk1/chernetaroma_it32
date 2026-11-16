
import json
import requests
import sys
from pathlib import Path
from datetime import datetime, timezone

print("Roman Cherneta, IT-32")

BASE_DIR = Path(__file__).resolve().parent
CACHE_DIR = BASE_DIR / "cache"
CACHE_FILE = CACHE_DIR / "rates.json"

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

CACHE_DIR.mkdir(exist_ok=True)


def load_rates():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as file:
                cache = json.load(file)

            saved_time = datetime.fromisoformat(cache["saved_at"])

            age = (
                datetime.now(timezone.utc) - saved_time
            ).total_seconds()

            if 0 <= age < 3600:
                print(f"source: cache (age {int(age)} s)")
                return cache["rates"]

        except (ValueError, KeyError, json.JSONDecodeError):
            pass

    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )

    response.raise_for_status()

    rates = response.json()

    cache = {
        "saved_at": datetime.now(timezone.utc).isoformat(),
        "rates": rates
    }

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, indent=2, ensure_ascii=False)

    print("source: api (cache saved)")

    return rates


try:
    rates = load_rates()

    for code in ["USD", "EUR"]:
        currency = next(
            (item for item in rates if item["cc"] == code),
            None
        )

        if currency:
            print(f"{code}: {currency['rate']:.2f} UAH")

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)
