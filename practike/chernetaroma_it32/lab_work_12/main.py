import logging
from pathlib import Path

import cherneta_files

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

directory = Path(__file__).parent

# Отримання списку файлів
files = cherneta_files.list_files(directory)
print("Список файлів:", files)

# Пошук файлів за частиною назви
found_files = cherneta_files.find_files(directory, "cher")
print("Знайдені файли:", found_files)

# Створення файлу з інформацією про студента
student_text = (
    "Ім'я: Роман\n"
    "Прізвище: Чернета\n"
    "Група: IT-32"
)

created_path = cherneta_files.create_file(
    directory / "student_info.txt",
    student_text
)

print("Створено файл:", created_path)

# Читання створеного файлу
print("Вміст файлу:")
print(Path(created_path).read_text(encoding="utf-8"))