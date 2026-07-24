from pathlib import Path


def file_exists(path: str) -> bool:
    return Path(path).exists()


def is_not_empty(text: str) -> bool:

    if text is None:
        return False

    return len(text.strip()) > 0