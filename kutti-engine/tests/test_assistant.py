from engine.state_manager import StateManager
from engine.lifecycle import Lifecycle
from engine.health import HealthMonitor
from engine.kernel import Kernel
from engine.assistant import Assistant

state = StateManager()
lifecycle = Lifecycle(state)
health = HealthMonitor()

kernel = Kernel(
    state=state,
    lifecycle=lifecycle,
    health=health
)

kernel.start()

assistant = Assistant(kernel)

print("\n===== ASSISTANT PIPELINE TEST =====")

print("\n1. Engine Status")
print(assistant.process("status"))

print("\n2. Health")
print(assistant.process("health"))

print("\n3. Open Chrome")
print(assistant.process("open chrome"))

print("\n4. Launch Chrome")
print(assistant.process("launch chrome"))

print("\n5. Start Calculator")
print(assistant.process("start calculator"))

print("\n6. Run Notepad")
print(assistant.process("run notepad"))

print("\n7. Open Browser (Alias)")
print(assistant.process("open browser"))

print("\n8. Launch Terminal (Alias)")
print(assistant.process("launch terminal"))

print("\n9. Start Editor (Alias)")
print(assistant.process("start editor"))

print("\n10. Open Spreadsheet (Alias)")
print(assistant.process("open spreadsheet"))

print("\n11. Empty Command")
print(assistant.process(""))

kernel.stop()