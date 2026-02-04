import random

class DecoyPersona:
    def __init__(self, name="Alex"):
        self.name = name
        self.responses = [
            "Oh, that sounds interesting. Can you explain more?",
            "Hmm, I’m not sure I understand. Could you repeat?",
            "Wow, really? How does that work?",
            "I’ll need some time to think about that."
        ]

    def respond(self, scam_message: str):
        return random.choice(self.responses)
