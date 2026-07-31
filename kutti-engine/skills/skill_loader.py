from skills.base_skill import BaseSkill


class SkillLoader:
    """
    Registers and manages JOY skills.
    """

    def __init__(self):
        self._skills = {}

    def register(self, skill: BaseSkill):
        self._skills[skill.name] = skill

    def unregister(self, name: str):
        if name in self._skills:
            del self._skills[name]

    def get(self, name: str):
        return self._skills.get(name)

    def exists(self, name: str):
        return name in self._skills

    def list_skills(self):
        return sorted(self._skills.keys())