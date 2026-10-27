import math
import sys
from pathlib import Path
from datetime import datetime

print("Roman Cherneta, IT-32")

usage = "usage: python3 task3.py [--dry-run] <dir>"

args = sys.argv[1:]
dry_run = False

if args and args[0] == "--dry-run":
    dry_run = True
    args = args[1:]

if len(args) != 1:
    print(usage, file=sys.stderr)
    sys.exit(2)

directory = Path(args[0]).expanduser()

if not directory.exists():
    print(f"error: {directory} does not exist", file=sys.stderr)
    sys.exit(1)

if not directory.is_dir():
    print(f"error: {directory} is not a directory", file=sys.stderr)
    sys.exit(1)

files = sorted(
    (item for item in directory.iterdir() if item.is_file()),
    key=lambda item: item.stat().st_mtime
)

if not files:
    print("У каталозі немає файлів.")
    sys.exit(0)


def format_size(size):
    units = ["B", "KB", "MB", "GB"]

    if size == 0:
        return "0 B"

    unit_index = min(int(math.log(size, 1024)), len(units) - 1)
    value = size / (1024 ** unit_index)

    return f"{value:.1f} {units[unit_index]}"


plan = []

for file_path in files:
    modified = datetime.fromtimestamp(file_path.stat().st_mtime)
    folder_name = modified.strftime("%Y-%m")
    destination_folder = directory / folder_name
    destination = destination_folder / file_path.name

    plan.append({
        "source": file_path,
        "destination": destination,
        "folder": folder_name,
        "size": file_path.stat().st_size,
        "modified": modified,
    })

for item in plan:
    print(
        f"{item['source'].name:<20} "
        f"{format_size(item['size']):>10}  "
        f"{item['modified']:%d.%m.%Y %H:%M}  "
        f"-> {item['folder']}/"
    )

# Попередньо перевіряємо всі файли до початку переміщення
for item in plan:
    if item["destination"].exists():
        print(
            f"error: {item['destination']} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

folders_count = len({item["folder"] for item in plan})

if dry_run:
    print(
        f"{len(plan)} files, {folders_count} folders "
        "(dry run, nothing moved)"
    )
    sys.exit(0)

# Переміщуємо файли після успішної перевірки
try:
    for item in plan:
        destination_folder = item["destination"].parent
        destination_folder.mkdir(parents=True, exist_ok=True)
        item["source"].rename(item["destination"])

except OSError as error:
    print(f"error: {error}", file=sys.stderr)
    sys.exit(1)

print(f"{len(plan)} files, {folders_count} folders")

# Записуємо звіт поруч зі скриптом
script_directory = Path(__file__).parent
reports_directory = script_directory / "reports"
reports_directory.mkdir(parents=True, exist_ok=True)

run_time = datetime.now()
report_name = run_time.strftime("organize_%Y%m%d_%H%M.txt")
report_path = reports_directory / report_name

with report_path.open("w", encoding="utf-8") as report:
    report.write("Roman Cherneta, IT-32\n")
    report.write(f"Run time: {run_time:%Y-%m-%d %H:%M:%S}\n")
    report.write(f"Directory: {directory}\n\n")

    for item in plan:
        report.write(
            f"{item['source'].name}; "
            f"{format_size(item['size'])}; "
            f"{item['modified']:%Y-%m-%d %H:%M}; "
            f"{item['destination']}\n"
        )

print(f"report saved to: {report_path}")