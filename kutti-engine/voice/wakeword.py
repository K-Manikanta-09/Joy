class WakeWord:

    WORDS = [
        "kutti"
    ]

    def detect(self, text):
        text = text.lower()

        return any(word in text for word in self.WORDS)