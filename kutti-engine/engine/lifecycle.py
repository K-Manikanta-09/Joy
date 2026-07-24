from engine.state_manager import EngineState


class Lifecycle:
    """
    Controls engine lifecycle transitions.
    """

    def __init__(self, state_manager):
        self.state_manager = state_manager

    def start(self):
        self.state_manager.set_state(EngineState.STARTING)

    def running(self):
        self.state_manager.set_state(EngineState.RUNNING)

    def pause(self):
        self.state_manager.set_state(EngineState.PAUSED)

    def shutdown(self):
        self.state_manager.set_state(EngineState.SHUTTING_DOWN)

    def stop(self):
        self.state_manager.set_state(EngineState.STOPPED)