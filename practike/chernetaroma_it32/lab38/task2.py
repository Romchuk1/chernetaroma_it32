
import csv
import requests
import sys
from pathlib import Path

print("Roman Cherneta, IT-32")

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "expenses.csv"

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_rate(currency_code, mode=None):
    url = URL
    timeout = 10

    if mode == "connection":
        url = "https://this-domain-does-not-exist-12345.example"
    elif mode == "http":
        url = "https://bank.gov.ua/this-page-does-not-exist"
    elif mode == "timeout":
        timeout = 0.001

    response = requests.get(
        url,
        params={"valcode": currency_code, "json": ""},
        timeout=timeout
    )

    response.raise_for_status()

    return response.json()[0]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else None

    total = 0.0

    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            total += float(row["amount"])

    usd = get_rate("USD", mode)
    eur = get_rate("EUR")

    print(f"total: {total:.2f} UAH")
    print(f"USD: {total / usd['rate']:.2f}")
    print(f"EUR: {total / eur['rate']:.2f}")


try:
    main()

except requests.ConnectionError as error:
    print(f"Connection error: {error}", file=sys.stderr)
    sys.exit(1)

except requests.Timeout as error:
    print(f"Timeout error: {error}", file=sys.stderr)
    sys.exit(1)

except requests.HTTPError as error:
    print(f"HTTP error: {error}", file=sys.stderr)
    sys.exit(1)

except requests.RequestException as error:
    print(f"Request error: {error}", file=sys.stderr)
    sys.exit(1)

except (ValueError, KeyError) as error:
    print(f"Data error: {error}", file=sys.stderr)
    sys.exit(1)
