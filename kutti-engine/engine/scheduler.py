import threading


class Scheduler:
    """
    Simple scheduler for delayed tasks.
    """

    def schedule(self, delay, func, *args, **kwargs):
        timer = threading.Timer(delay, func, args=args, kwargs=kwargs)
        timer.start()
        return timer