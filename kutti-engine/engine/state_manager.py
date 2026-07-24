from enum import Enum
from threading import Lock


class EngineState(Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    SHUTTING_DOWN = "shutting_down"


class StateManager:
    """
    Central engine state manager.

    Thread-safe singleton-style state storage.
    """

    def __init__(self):
        self._lock = Lock()
        self._state = EngineState.STOPPED

    @property
    def state(self):
        with self._lock:
            return self._state

    def set_state(self, state: EngineState):
        with self._lock:
            self._state = state

    def is_running(self):
        return self.state == EngineState.RUNNING

    def is_stopped(self):
        return self.state == EngineState.STOPPED