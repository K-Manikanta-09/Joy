from engine.startup import Startup
from engine.kernel import Kernel
from engine.assistant import Assistant
from engine.event_bus import EventBus
from engine.scheduler import Scheduler
from engine.plugin_manager import PluginManager
from engine.shutdown import Shutdown

import time


# -----------------------------
# Startup
# -----------------------------
startup = Startup()

components = startup.initialize()

kernel = Kernel(
    state=components["state"],
    lifecycle=components["lifecycle"],
    health=components["health"],
)

kernel.start()


# -----------------------------
# Assistant
# -----------------------------
assistant = Assistant(kernel)

print("\n===== ASSISTANT TEST =====")

print(assistant.process("status"))

print(assistant.process("health"))

print(assistant.process("Open Chrome"))


# -----------------------------
# Event Bus
# -----------------------------
bus = EventBus()

scheduler = Scheduler()


def on_message(data):
    print("EVENT RECEIVED:", data)


bus.subscribe("voice", on_message)

bus.publish("voice", "Hello Captain")


# -----------------------------
# Scheduler
# -----------------------------
scheduler.schedule(
    2,
    lambda: print("Scheduled task executed.")
)


# -----------------------------
# Plugin Manager
# -----------------------------
plugin_manager = PluginManager()

print("Loaded Plugins:", plugin_manager.loaded_plugins())


# -----------------------------
# Wait
# -----------------------------
time.sleep(3)


# -----------------------------
# Shutdown
# -----------------------------
shutdown = Shutdown(kernel)

shutdown.execute()