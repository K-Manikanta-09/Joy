class Dispatcher:
    """
    Executes routed commands.

    Temporary implementation.
    Skills will replace this later.
    """

    def __init__(self, kernel):
        self.kernel = kernel

    def dispatch(self, command: str):

        command = command.lower()

        if "health" in command:
            return self.kernel.health_status()

        if "status" in command:
            return {
                "engine": self.kernel.state.state.value
            }

        return f"Command received: {command}"