from voice.audio_manager import AudioManager
from voice.speaker import Speaker

audio = AudioManager()

speaker = Speaker(audio)

speaker.speak(
    "Hello Captain. I am JOY. Voice Engine is online."
)

audio.shutdown()