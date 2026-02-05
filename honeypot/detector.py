import re
class ScamDetector:
    suspicious_keywords = [
        "verify", "blocked", "urgent", "upi", "account", "password",
        "lottery", "suspension", "click here", "payment"
    ]

    def analyze(self, text: str):
        text_lower = text.lower()
        for kw in self.suspicious_keywords:
            if kw in text_lower:
                return True, kw
        return False, None
