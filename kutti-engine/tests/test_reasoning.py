from ai.reasoning import Reasoning

reasoning = Reasoning()

valid = {
    "intent": "OPEN",
    "steps": [
        {
            "action": "OPEN",
            "target": "chrome"
        }
    ]
}

invalid = {
    "intent": "OPEN",
    "steps": []
}

print(reasoning.evaluate(valid))
print(reasoning.evaluate(invalid))