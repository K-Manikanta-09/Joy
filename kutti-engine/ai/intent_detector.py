class IntentDetector:
    """
    Detects the user's intent from input text.
    """

    INTENTS = {
        "OPEN": [
            "open",
            "launch",
            "start",
            "run",
        ],

        "CLOSE": [
            "close",
            "exit",
            "quit",
            "terminate",
        ],

        "SEARCH": [
            "search",
            "find",
            "look",
            "lookup",
        ],

        "PLAY": [
            "play",
            "listen",
            "watch",
        ],
    }

    def detect(self, message: str):

        message = message.lower()

        for intent, keywords in self.INTENTS.items():

            for keyword in keywords:

                if keyword in message:
                    return intent

        return "CHAT"