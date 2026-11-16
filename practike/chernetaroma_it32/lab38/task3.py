
import requests
import sys

print("Roman Cherneta, IT-32")

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 48.45,
    "longitude": 34.98,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(
        URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()
    current = data["current"]

    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]

    print(
        f"Dnipro (48.45, 34.98): "
        f"{temperature} C, wind {wind_speed} km/h"
    )

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)
except (KeyError, TypeError) as error:
    print(f"Data error: {error}", file=sys.stderr)
    sys.exit(1)
