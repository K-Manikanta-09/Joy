class Planner:
    """
    Breaks an intent into executable steps.
    """

    def create_plan(self, intent, message):

        return {
            "intent": intent,
            "steps": [
                {
                    "action": intent,
                    "target": message
                }
            ]
        }