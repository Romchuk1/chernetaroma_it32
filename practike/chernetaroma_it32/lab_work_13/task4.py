import math
import random
import sys
from pathlib import Path
from datetime import datetime

print("Roman Cherneta, IT-32")

# Заміни на свій справжній рік народження
YEAR = 2007

random.seed(YEAR)

# Генеруємо 5 прикладів
sqrt_number = random.randint(2, 20) ** 2

factorial_number = random.randint(3, 7)

gcd_a = random.randint(20, 100)
gcd_b = random.randint(10, 80)

comb_n = random.randint(5, 10)
comb_k = random.randint(2, comb_n - 1)

percent = random.randint(2, 20)
percent_number = random.randint(100, 500)

questions = [
    (
        f"sqrt({sqrt_number})",
        math.isqrt(sqrt_number)
    ),
    (
        f"{factorial_number}!",
        math.factorial(factorial_number)
    ),
    (
        f"gcd({gcd_a}, {gcd_b})",
        math.gcd(gcd_a, gcd_b)
    ),
    (
        f"comb({comb_n}, {comb_k})",
        math.comb(comb_n, comb_k)
    ),
    (
        f"{percent}% of {percent_number}",
        percent * percent_number // 100
    ),
]

start_time = datetime.now()
score = 0

for number, (question, correct_answer) in enumerate(questions, start=1):
    answer = input(f"{number}) {question} = ")

    try:
        user_answer = int(answer.strip())
        correct = user_answer == correct_answer
    except ValueError:
        correct = False

    if correct:
        print("   correct")
        score += 1
    else:
        print(f"   wrong, answer: {correct_answer}")

end_time = datetime.now()
seconds = (end_time - start_time).total_seconds()

print(f"score: {score}/5, time: {seconds:.1f} s")

# Шлях до файлу історії
script_directory = Path(__file__).parent
results_directory = script_directory / "results"
results_directory.mkdir(parents=True, exist_ok=True)

history_file = results_directory / "history.csv"

# Заголовок додається лише під час створення файлу
if not history_file.exists():
    with history_file.open("w", encoding="utf-8") as file:
        file.write("# datetime;score;seconds\n")

# Записуємо результат спроби
with history_file.open("a", encoding="utf-8") as file:
    file.write(
        f"{end_time:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n"
    )

# Читаємо історію спроб
attempts = []

with history_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        try:
            attempt_date = datetime.strptime(
                parts[0], "%Y-%m-%d %H:%M"
            )
            attempt_score = int(parts[1])
            attempt_seconds = float(parts[2])

            attempts.append(
                (attempt_date, attempt_score, attempt_seconds)
            )

        except (ValueError, IndexError):
            print(
                f"Попередження: некоректний рядок історії: {line}",
                file=sys.stderr
            )

if not attempts:
    print("Помилка: не вдалося прочитати історію спроб.", file=sys.stderr)
    sys.exit(1)

# Найкращий результат: більше балів, а за рівних балів — менше часу
best = min(attempts, key=lambda item: (-item[1], item[2]))

print(f"attempts: {len(attempts)}")
print(
    f"best: {best[1]}/5 in {best[2]:.1f} s "
    f"({best[0]:%Y-%m-%d %H:%M})"
)