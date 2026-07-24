from datetime import datetime


def current_timestamp() -> str:
    """
    Returns current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def safe_str(value) -> str:
    """
    Converts None to empty string.
    """

    if value is None:
        return ""

    return str(value)