import logging


class KuttiFormatter(logging.Formatter):
    """
    Standard formatter used across the entire engine.
    """

    FORMAT = (
        "[%(asctime)s] "
        "[%(levelname)s] "
        "[%(name)s] "
        "%(message)s"
    )

    DATEFMT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        super().__init__(
            fmt=self.FORMAT,
            datefmt=self.DATEFMT,
        )