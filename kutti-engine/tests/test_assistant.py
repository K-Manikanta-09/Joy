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

print(assistant.process("status"))

print(assistant.process("health"))

print(assistant.process("open chrome"))

kernel.stop()