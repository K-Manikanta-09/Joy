from engine.state_manager import StateManager
from engine.lifecycle import Lifecycle
from engine.health import HealthMonitor

from shared.logging import get_logger


class Startup:
    """
    Bootstraps the entire JOY Engine.
    """

    def __init__(self):

        self.logger = get_logger("Startup")

    def initialize(self):

        self.logger.info("Initializing JOY Engine...")

        state = StateManager()

        lifecycle = Lifecycle(state)

        health = HealthMonitor()

        self.logger.info("Initialization Complete.")

        return {
            "logger": self.logger,
            "state": state,
            "lifecycle": lifecycle,
            "health": health,
        }