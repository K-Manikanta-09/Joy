from engine.router import Router

from ai.intent_detector import IntentDetector
from ai.planner import Planner
from ai.reasoning import Reasoning


class Assistant:
    """
    Main AI Assistant.

    Receives user requests,
    detects intent,
    creates an execution plan,
    validates it,
    and delegates execution.
    """

    def __init__(self, kernel):

        self.kernel = kernel

        self.router = Router(kernel)

        self.intent_detector = IntentDetector()

        self.planner = Planner()

        self.reasoning = Reasoning()

    def process(self, user_input: str):

        if not user_input.strip():
            return "I didn't receive any command."

        # -------------------------
        # Engine Commands
        # -------------------------

        command = user_input.lower().strip()

        if command == "status":
            return self.router.route(command)

        if command == "health":
            return self.router.route(command)

        # -------------------------
        # AI Processing
        # -------------------------

        intent = self.intent_detector.detect(user_input)

        plan = self.planner.create_plan(intent, user_input)

        # -------------------------
        # Reasoning
        # -------------------------

        decision = self.reasoning.evaluate(plan)

        if not decision["approved"]:
            return decision["reason"]

        plan = decision["plan"]

        step = plan["steps"][0]

        action = step["action"]

        target = step["target"]

        # -------------------------
        # Temporary Bridge
        # -------------------------

        if action == "OPEN":
            return self.router.route(f"open {target}")

        if action == "CLOSE":
            return self.router.route(f"close {target}")

        if action == "SEARCH":
            return self.router.route(f"search {target}")

        if action == "PLAY":
            return self.router.route(f"play {target}")

        return self.router.route(user_input)