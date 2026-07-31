from engine.state_manager import StateManager
from engine.lifecycle import Lifecycle
from engine.health import HealthMonitor
from engine.kernel import Kernel
from engine.dispatcher import Dispatcher

# Engine Components
state = StateManager()
lifecycle = Lifecycle(state)
health = HealthMonitor()

# Kernel
kernel = Kernel(
    state=state,
    lifecycle=lifecycle,
    health=health
)

kernel.start()

dispatcher = Dispatcher(kernel)

dispatcher.dispatch("open chrome")

kernel.stop()