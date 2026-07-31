import subprocess

from skills.base_skill import BaseSkill


class OpenAppSkill(BaseSkill):

    name = "open_app"

    description = "Opens desktop applications."

    APPS = {
        "chrome": "start chrome",
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "explorer": "explorer",
        "cmd": "cmd",
    }

    def execute(self, app=None, **kwargs):

        if not app:
            print("No application specified.")
            return False

        command = self.APPS.get(app.lower())

        if not command:
            print(f"Application '{app}' is not supported.")
            return False

        subprocess.Popen(command, shell=True)

        print(f"Opening {app}...")

        return True