import asyncio
import os
import time
import pygame

from voice.synthesizer import Synthesizer
from voice.voices import Voices
from voice.audio_manager import AudioManager


class Speaker:
    """
    Handles voice playback.
    Uses AudioManager for audio device management.
    """

    def __init__(self, audio_manager: AudioManager):

        self.audio = audio_manager

        if not self.audio.is_initialized():
            self.audio.initialize()

        self.synth = Synthesizer()

    def speak(self, text):

        if not text or not text.strip():
            print("⚠ Empty text. Nothing to speak.")
            return

        filename = asyncio.run(
            self.synth.generate(
                text=text,
                voice=Voices.DEFAULT
            )
        )

        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.music.unload()

        finally:
            if os.path.exists(filename):
                os.remove(filename)