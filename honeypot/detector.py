from transformers import pipeline

class ScamDetector:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

        self.scam_keywords = [
            "lottery",
            "urgent",
            "verify account",
            "bank login",
            "password",
            "click here",
            "reset password",
            "confirm account"
        ]

    def analyze(self, text: str):
        result = self.classifier(text)[0]
        label = result["label"]

        keyword_hit = any(word in text.lower() for word in self.scam_keywords)

        if keyword_hit or label == "NEGATIVE":
            return True, "phishing"

        return False, None
