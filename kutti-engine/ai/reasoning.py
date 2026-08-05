class Reasoning:
    """
    Evaluates whether a generated plan is valid
    before execution.
    """

    def evaluate(self, plan):

        if not plan:
            return {
                "approved": False,
                "reason": "No execution plan found."
            }

        if "steps" not in plan:
            return {
                "approved": False,
                "reason": "Execution plan has no steps."
            }

        if len(plan["steps"]) == 0:
            return {
                "approved": False,
                "reason": "Execution plan is empty."
            }

        step = plan["steps"][0]

        action = step.get("action")
        target = step.get("target")

        if not action:
            return {
                "approved": False,
                "reason": "No action detected."
            }

        if not target:
            return {
                "approved": False,
                "reason": "No target detected."
            }

        return {
            "approved": True,
            "plan": plan
        }