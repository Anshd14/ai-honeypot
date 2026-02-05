import random
class DecoyPersona:
    responses = [
        "Why is my account being suspended?",
        "Can you explain more clearly?",
        "I don’t understand, what do you mean?",
        "How do I verify safely?",
        "What happens if I don’t share?"
    ]
    def respond(self, message: str):
        return random.choice(self.responses)
