class Shutdown:
    """
    Handles graceful engine shutdown.
    """

    def __init__(self, kernel):

        self.kernel = kernel

    def execute(self):

        self.kernel.stop()