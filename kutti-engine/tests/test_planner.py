from ai.planner import Planner

planner = Planner()

tests = [
   ("OPEN", "open browser"),
("OPEN", "launch terminal"),
("OPEN", "start editor"),
("OPEN", "open files"),
("OPEN", "open spreadsheet"),
("OPEN", "open presentation"),
]

for intent, message in tests:
    print(planner.create_plan(intent, message))