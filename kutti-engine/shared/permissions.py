from pathlib import Path


def is_readable(path: str) -> bool:

    return Path(path).exists()


def is_writable(path: str) -> bool:

    try:

        with open(path, "a"):
            pass

        return True

    except Exception:

        return False