
import json
from datetime import date

print("Roman Cherneta, IT-32")

original_data = {
    "owner": "Roman Cherneta",
    "group": "IT-32",
    "created": date.today(),
    "currency": "UAH"
}

# Спосіб 1. Використання параметра default

try:
    json.dumps(original_data)
except TypeError as error:
    print("TypeError:", error)


def date_converter(value):
    if isinstance(value, date):
        return value.isoformat()

    raise TypeError(f"Unsupported type: {type(value)}")


json_text = json.dumps(
    original_data,
    default=date_converter,
    ensure_ascii=False,
    indent=2
)

print("\nMethod 1:")
print(json_text)


# Спосіб 2. Власна серіалізація та десеріалізація

def prepare_for_json(data):
    result = data.copy()

    for key, value in result.items():
        if isinstance(value, date):
            result[key] = value.isoformat()

    return result


def restore_dates(data):
    result = data.copy()

    for key, value in result.items():
        if key == "created":
            result[key] = date.fromisoformat(value)

    return result


prepared_data = prepare_for_json(original_data)

with open("date_data.json", "w", encoding="utf-8") as file:
    json.dump(prepared_data, file, ensure_ascii=False, indent=2)

with open("date_data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

restored_data = restore_dates(loaded_data)

print("\nMethod 2:")
print("Restored data:", restored_data)
print("Data matches:", restored_data == original_data)
print("Date type:", type(restored_data["created"]))
