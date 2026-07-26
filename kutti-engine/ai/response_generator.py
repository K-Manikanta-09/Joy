class ResponseGenerator:
    """
    Generates JOY's response based on reasoning.
    """

    def generate(self, decision):

        if decision["approved"]:

            intent = decision["plan"]["intent"]

            return f"Executing {intent} request."

        return "Request rejected."