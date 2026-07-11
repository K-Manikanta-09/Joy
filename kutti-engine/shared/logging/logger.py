import logging

from shared.logging.handlers import (
    get_console_handler,
    get_file_handler,
)


_LOGGERS = {}


def get_logger(name: str) -> logging.Logger:
    """
    Returns a singleton logger instance.
    """

    if name in _LOGGERS:
        return _LOGGERS[name]

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    logger.propagate = False

    if not logger.handlers:

        logger.addHandler(get_console_handler())

        logger.addHandler(get_file_handler())

    _LOGGERS[name] = logger

    return logger