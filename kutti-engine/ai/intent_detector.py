class IntentDetector:
    """
    Detects the user's intent from input text.
    """

    def detect(self, message: str):

        message = message.lower()

        if "open" in message:
            return "OPEN"

        if "close" in message:
            return "CLOSE"

        if "search" in message:
            return "SEARCH"

        if "play" in message:
            return "PLAY"

        return "CHAT"