
import json
from pathlib import Path
from datetime import date

print("Roman Cherneta, IT-32")

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "data" / "expenses.json"
UPDATED_FILE = BASE_DIR / "data" / "expenses_updated.json"

with open(JSON_FILE, "r", encoding="utf-8") as file:
    records = json.load(file)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 100.0,
    "comment": "added expense"
}

records.append(new_record)
added = 1

old_count = len(records)

records = [
    record for record in records
    if record["amount"] >= 10
]

deleted = old_count - len(records)

with open(UPDATED_FILE, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"total records: {len(records)}")
print("saved: data/expenses_updated.json")
