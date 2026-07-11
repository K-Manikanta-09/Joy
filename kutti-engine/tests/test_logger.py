from shared.logging import get_logger

logger = get_logger("Engine")


def main():
    logger.info("Engine Started")
    logger.warning("Warning Example")
    logger.error("Error Example")


if __name__ == "__main__":
    main()