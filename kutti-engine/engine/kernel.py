from shared.logging import get_logger


class Kernel:
    """
    Central runtime kernel.
    """

    def __init__(
        self,
        state,
        lifecycle,
        health,
    ):

        self.logger = get_logger("Kernel")

        self.state = state

        self.lifecycle = lifecycle

        self.health = health

    def start(self):

        self.logger.info("Kernel Starting...")

        self.lifecycle.start()

        self.lifecycle.running()

        self.logger.info("Kernel Running.")

    def stop(self):

        self.logger.info("Kernel Shutdown...")

        self.lifecycle.shutdown()

        self.lifecycle.stop()

        self.logger.info("Kernel Stopped.")

    def health_status(self):

        return self.health.get_summary()