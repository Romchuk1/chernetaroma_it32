
import csv
import json
from pathlib import Path

print("Roman Cherneta, IT-32")

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "expenses.csv"
JSON_FILE = BASE_DIR / "data" / "expenses.json"

records = []

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["note"]
        })

with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

file_size = JSON_FILE.stat().st_size

print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({file_size} bytes)")
