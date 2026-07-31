import subprocess

from skills.base_skill import BaseSkill
from data.applications.windows_apps import WINDOWS_APPS


class OpenAppSkill(BaseSkill):

    name = "open_app"

    description = "Opens desktop applications."

    def execute(self, app=None, **kwargs):

        if not app:
            print("No application specified.")
            return False

        command = WINDOWS_APPS.get(app.lower())

        if not command:
            print(f"Application '{app}' is not supported.")
            return False

        subprocess.Popen(command, shell=True)

        print(f"Opening {app}...")

        return True