class Reasoning:
    """
    Decides how JOY should respond.
    """

    def evaluate(self, plan):

        return {
            "approved": True,
            "plan": plan
        }