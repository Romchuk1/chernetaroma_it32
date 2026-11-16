
import csv
from collections import defaultdict
from decimal import Decimal
from tabulate import tabulate

print("Roman Cherneta, IT-32")

expenses = defaultdict(lambda: {"count": 0, "total": Decimal("0.00")})

with open("data/expenses.csv", "r", encoding="utf-8-sig", newline="") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        if parts[0].lower() == "date":
            continue

        if len(parts) < 3:
            continue

        category = parts[1].strip()
        amount = Decimal(parts[2].strip().replace(",", "."))

        expenses[category]["count"] += 1
        expenses[category]["total"] += amount

rows = []

total_count = 0
total_amount = Decimal("0.00")

for category, values in sorted(expenses.items()):
    rows.append([
        category,
        values["count"],
        values["total"]
    ])

    total_count += values["count"]
    total_amount += values["total"]

rows.append(["TOTAL", total_count, total_amount])

print(
    tabulate(
        rows,
        headers=["category", "count", "total"],
        tablefmt="github",
        floatfmt=".2f"
    )
)