import logging
from logging.handlers import TimedRotatingFileHandler

from shared.constants.paths import LOGS_DIR
from shared.logging.formatter import KuttiFormatter


def get_console_handler():

    handler = logging.StreamHandler()

    handler.setFormatter(KuttiFormatter())

    return handler


def get_file_handler():

    logfile = LOGS_DIR / "kutti.log"

    handler = TimedRotatingFileHandler(
        logfile,
        when="midnight",
        interval=1,
        backupCount=30,
        encoding="utf-8",
    )

    handler.setFormatter(KuttiFormatter())

    return handler