import math
import sys
from pathlib import Path
from datetime import date, timedelta

print("Roman Cherneta, IT-32")

FILE = Path(__file__).parent / "data" / "expenses.csv"

if not FILE.exists():
    print(f"Помилка: файл {FILE} не знайдено.", file=sys.stderr)
    sys.exit(1)

expenses = {}

with FILE.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        try:
            if len(parts) != 4:
                raise ValueError("неправильна кількість полів")

            expense_date = date.fromisoformat(parts[0])
            amount = float(parts[2])

            if amount < 0:
                raise ValueError("сума не може бути від'ємною")

            expenses[expense_date] = expenses.get(expense_date, 0) + amount

        except ValueError as error:
            print(
                f"Попередження: рядок {line_number} пропущено: {error}",
                file=sys.stderr
            )

if not expenses:
    print("Помилка: немає коректних записів про витрати.", file=sys.stderr)
    sys.exit(1)

first_date = min(expenses)
last_date = max(expenses)

period_days = (last_date - first_date).days + 1

print(
    f"period: {first_date:%d.%m.%Y} ({first_date:%A}) - "
    f"{last_date:%d.%m.%Y} ({last_date:%A}), {period_days} days"
)

weekday_totals = [0.0] * 7
daily_totals = []

current_date = first_date

while current_date <= last_date:
    amount = expenses.get(current_date, 0.0)

    weekday_totals[current_date.weekday()] += amount
    daily_totals.append(amount)

    current_date += timedelta(days=1)

weekdays = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

print("\nweekday      total")

for index, weekday in enumerate(weekdays):
    print(f"{weekday:<12} {weekday_totals[index]:8.2f}")

total = math.fsum(daily_totals)
average = total / len(daily_totals)

variance = math.fsum(
    (amount - average) ** 2 for amount in daily_totals
) / len(daily_totals)

standard_deviation = math.sqrt(variance)

top_date = max(
    (first_date + timedelta(days=index) for index in range(period_days)),
    key=lambda day: expenses.get(day, 0.0)
)

no_spend_days = sum(1 for amount in daily_totals if amount == 0)

print(f"\ntotal:        {total:.2f}")
print(f"per day:      {average:.2f} +- {standard_deviation:.2f}")
print(
    f"top day:      {top_date:%d.%m.%Y} "
    f"({top_date:%A}), {expenses.get(top_date, 0.0):.2f}"
)
print(f"no-spend days: {no_spend_days}")

# Визначаємо перший день наступного місяця
if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)

month_start = date(last_date.year, last_date.month, 1)
days_in_month = (next_month - month_start).days
days_left = (next_month - last_date).days - 1
month_forecast = average * days_in_month

print(f"days in {last_date:%B}: {days_in_month}")
print(f"left after {last_date:%d.%m}: {days_left}")
print(f"month forecast: {month_forecast:.2f}")