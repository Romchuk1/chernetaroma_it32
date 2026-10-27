import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def list_files(directory):
    """Повертає список файлів у вказаній папці.

    Args:
        directory: Шлях до папки.

    Returns:
        Список назв файлів.
    """
    path = Path(directory)

    if not path.is_dir():
        logger.warning("Папку не знайдено: %s", directory)
        return []

    files = [item.name for item in path.iterdir() if item.is_file()]
    logger.info("Знайдено файлів: %d", len(files))

    return files


def find_files(directory, substring):
    """Знаходить файли, у назвах яких є заданий текст.

    Args:
        directory: Шлях до папки.
        substring: Текст для пошуку.

    Returns:
        Список назв знайдених файлів.
    """
    files = list_files(directory)
    matches = [name for name in files if substring in name]

    logger.info("Знайдено відповідних файлів: %d", len(matches))

    return matches


def create_file(path, text):
    """Створює файл і записує в нього текст.

    Args:
        path: Шлях до файлу.
        text: Текст для запису.

    Returns:
        Шлях до створеного файлу.
    """
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")

    logger.info("Створено файл: %s", file_path)

    return str(file_path)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    print("Перевірка модуля")
    print("Список файлів:", list_files("."))
    print("Файли зі словом main:", find_files(".", "main"))