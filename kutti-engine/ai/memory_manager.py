class MemoryManager:
    """
    Temporary memory manager.

    Long-term memory arrives later.
    """

    def __init__(self):

        self.short_term = []

    def remember(self, item):

        self.short_term.append(item)

    def recall(self):

        return self.short_term

    def forget(self):

        self.short_term.clear()