from enum import Enum


class AIState(Enum):

    IDLE = "idle"

    THINKING = "thinking"

    SPEAKING = "speaking"

    EXECUTING = "executing"