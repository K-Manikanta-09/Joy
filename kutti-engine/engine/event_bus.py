from collections import defaultdict


class EventBus:
    """
    Simple publish/subscribe event system.
    """

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_name: str, callback):
        self._subscribers[event_name].append(callback)

    def publish(self, event_name: str, data=None):
        for callback in self._subscribers[event_name]:
            callback(data)