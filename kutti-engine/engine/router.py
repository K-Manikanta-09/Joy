from engine.dispatcher import Dispatcher


class Router:
    """
    Determines where a request should go.
    """

    def __init__(self, kernel):

        self.kernel = kernel

        self.dispatcher = Dispatcher(kernel)

    def route(self, command: str):

        command = command.lower()

        return self.dispatcher.dispatch(command)