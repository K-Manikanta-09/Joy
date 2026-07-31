from skills.base_skill import BaseSkill
from skills.skill_loader import SkillLoader


class DemoSkill(BaseSkill):

    name = "demo"

    description = "Demo Skill"

    def execute(self, **kwargs):
        print("Demo Skill Executed")


loader = SkillLoader()

demo = DemoSkill()

loader.register(demo)

print("Registered Skills:")
print(loader.list_skills())

print()

print("Skill Exists:")
print(loader.exists("demo"))

print()

print("Executing Skill:")
loader.get("demo").execute()

print()

loader.unregister("demo")

print("Remaining Skills:")
print(loader.list_skills())