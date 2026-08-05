from ai.intent_detector import IntentDetector

detector = IntentDetector()

tests = [
    "open chrome",
    "launch chrome",
    "start vscode",
    "run calculator",
    "close chrome",
    "exit vscode",
    "search python",
    "find weather",
    "play music",
    "watch youtube",
    "hello joy",
]

for text in tests:
    print(f"{text} -> {detector.detect(text)}")