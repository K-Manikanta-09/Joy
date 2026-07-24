from engine.startup import Startup
from engine.kernel import Kernel


startup = Startup()

components = startup.initialize()


kernel = Kernel(
    state=components["state"],
    lifecycle=components["lifecycle"],
    health=components["health"],
)

kernel.start()

print(kernel.health_status())

kernel.stop()