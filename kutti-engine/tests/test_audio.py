from voice.audio_manager import AudioManager

audio = AudioManager()

audio.initialize()

print(audio.is_initialized())

audio.shutdown()

print(audio.is_initialized())