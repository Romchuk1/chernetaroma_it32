
def parse_line(line):
    parts = line.strip().split(";")

    if len(parts) != 4:
        raise ValueError("Рядок повинен містити 4 поля")

    try:
        amount = float(parts[2])
    except ValueError:
        raise ValueError("Сума повинна бути числом")

    return {
        "date": parts[0],
        "category": parts[1],
        "amount": amount,
        "comment": parts[3]
    }

def total_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        amount = record["amount"]

        totals[category] = totals.get(category, 0) + amount

    return {
        category: round(total, 2)
        for category, total in totals.items()
    }

def load_expenses(path):
    records = []

    with open(path, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.lower().startswith("date;"):
                continue

            records.append(parse_line(line))

    return records