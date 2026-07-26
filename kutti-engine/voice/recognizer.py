import speech_recognition as sr


class Recognizer:
    """
    Converts speech into text.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize(self):

        with sr.Microphone() as source:

            print("🎤 Speak now...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"Recognized: {text}")

            return text

        except sr.UnknownValueError:

            print("Could not understand audio.")

            return ""

        except sr.RequestError:

            print("Speech Recognition service unavailable.")

            return ""