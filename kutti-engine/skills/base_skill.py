from abc import ABC, abstractmethod


class BaseSkill(ABC):
    """
    Base class for all JOY Skills.
    Every skill must inherit from this class.
    """

    name = "base"

    description = "Base Skill"

    @abstractmethod
    def execute(self, **kwargs):
        """
        Execute the skill.
        """
        pass