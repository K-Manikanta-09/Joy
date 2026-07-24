from engine.state_manager import StateManager, EngineState
from engine.lifecycle import Lifecycle
from engine.health import HealthMonitor


state = StateManager()
life = Lifecycle(state)

print("Initial:", state.state)

life.start()
print("Starting:", state.state)

life.running()
print("Running:", state.state)

health = HealthMonitor()

print("Health:", health.get_summary())

life.shutdown()
print("Shutdown:", state.state)

life.stop()
print("Stopped:", state.state)