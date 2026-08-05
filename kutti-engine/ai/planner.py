class Planner:
    """
    Breaks an intent into executable steps.
    """

    APP_ALIASES = {
        # Browsers
        "browser": "chrome",
        "internet": "chrome",
        "google": "chrome",

        # Editors
        "editor": "notepad",
        "text editor": "notepad",

        # Terminal
        "terminal": "cmd",
        "command prompt": "cmd",

        # File Manager
        "files": "explorer",
        "file explorer": "explorer",

        # Office
        "spreadsheet": "excel",
        "document": "word",
        "presentation": "powerpoint",
    }

    def create_plan(self, intent, message):

        message = message.lower()

        target = message

        if intent == "OPEN":
            target = (
                message.replace("open", "")
                .replace("launch", "")
                .replace("start", "")
                .replace("run", "")
                .strip()
            )

        elif intent == "CLOSE":
            target = (
                message.replace("close", "")
                .replace("exit", "")
                .replace("quit", "")
                .replace("terminate", "")
                .strip()
            )

        elif intent == "SEARCH":
            target = (
                message.replace("search", "")
                .replace("find", "")
                .replace("look", "")
                .replace("lookup", "")
                .strip()
            )

        elif intent == "PLAY":
            target = (
                message.replace("play", "")
                .replace("watch", "")
                .replace("listen", "")
                .strip()
            )

        # Convert aliases into actual application names
        target = self.APP_ALIASES.get(target, target)

        return {
            "intent": intent,
            "steps": [
                {
                    "action": intent,
                    "target": target
                }
            ]
        }