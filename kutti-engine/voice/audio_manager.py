import pygame


class AudioManager:
    """
    Central Audio Controller for JOY.
    Responsible for initializing and shutting down
    the audio system.
    """

    def __init__(self):
        self.initialized = False

    def initialize(self):
        """
        Initialize pygame mixer only once.
        """
        if not self.initialized:
            pygame.mixer.init()
            self.initialized = True
            print("🔊 Audio Manager Initialized")

    def shutdown(self):
        """
        Shutdown audio system.
        """
        if self.initialized:
            pygame.mixer.quit()
            self.initialized = False
            print("🔇 Audio Manager Shutdown")

    def is_initialized(self):
        """
        Returns current audio state.
        """
        return self.initialized