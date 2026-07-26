class Microphone:
    """
    Handles microphone access.
    """

    def __init__(self):
        self.active = False

    def start(self):
        self.active = True
        print("🎤 Microphone Activated")

    def stop(self):
        self.active = False
        print("🎤 Microphone Stopped")

    def status(self):
        return self.active