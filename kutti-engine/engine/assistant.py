from engine.router import Router


class Assistant:
    """
    Main AI Assistant.

    Receives user requests and delegates them to the router.
    """

    def __init__(self, kernel):

        self.kernel = kernel

        self.router = Router(kernel)

    def process(self, user_input: str):

        if not user_input.strip():
            return "I didn't receive any command."

        return self.router.route(user_input)