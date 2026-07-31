from skills.skill_loader import SkillLoader
from skills.desktop.open_app import OpenAppSkill


class Dispatcher:
    """
    Executes routed commands.
    """

    def __init__(self, kernel):

        self.kernel = kernel

        self.loader = SkillLoader()

        # Register Skills
        self.loader.register(OpenAppSkill())

    def dispatch(self, command: str):

        command = command.lower()

        # --------------------------
        # Existing Engine Commands
        # --------------------------

        if "health" in command:
            return self.kernel.health_status()

        if "status" in command:
            return {
                "engine": self.kernel.state.state.value
            }

        # --------------------------
        # Desktop Skills
        # --------------------------

        if command.startswith("open "):

            app = command.replace("open ", "").strip()

            skill = self.loader.get("open_app")

            return skill.execute(app=app)

        # --------------------------
        # Default
        # --------------------------

        return f"Unknown command: {command}"