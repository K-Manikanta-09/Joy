class Summarizer:
    """
    Summarizes conversation history.
    """

    def summarize(self, history):

        if not history:
            return "No conversation."

        return (
            f"Conversation contains "
            f"{len(history)} messages."
        )