from voice.microphone import Microphone
from voice.listener import Listener
from voice.wakeword import WakeWord
from voice.recognizer import Recognizer

mic = Microphone()
listener = Listener()
wake = WakeWord()
recognizer = Recognizer()

mic.start()

print("\n===== WAKE WORD TEST =====")

text = listener.listen()

print(text)

print(wake.detect(text))

print("\n===== SPEECH TEST =====")

speech = recognizer.recognize()

print(speech)

mic.stop()