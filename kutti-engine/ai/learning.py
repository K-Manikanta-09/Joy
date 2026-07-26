class Learning:
    """
    Future learning engine.

    Currently stores observations.
    """

    def __init__(self):
        self.knowledge = []

    def learn(self, observation):
        self.knowledge.append(observation)

    def get_knowledge(self):
        return self.knowledge