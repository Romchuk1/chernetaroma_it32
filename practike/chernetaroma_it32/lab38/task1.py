
import requests

print("Roman Cherneta, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )

    response.raise_for_status()

    rates = response.json()

    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))

    for code in ["USD", "EUR"]:
        currency = next(
            (item for item in rates if item["cc"] == code),
            None
        )

        if currency:
            print(
                f"{code}: {currency['rate']:.2f} UAH "
                f"(date: {currency['exchangedate']})"
            )

except requests.RequestException as error:
    import sys
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)
