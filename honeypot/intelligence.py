import re
class IntelligenceExtractor:
    def extract(self, text: str):
        intelligence = {
            "bankAccounts": re.findall(r"\b\d{4}-\d{4}-\d{4}\b", text),
            "upiIds": re.findall(r"\b[\w\.-]+@upi\b", text),
            "phishingLinks": re.findall(r"https?://\S+", text),
            "phoneNumbers": re.findall(r"\+91\d{10}", text),
            "suspiciousKeywords": [kw for kw in ["urgent","verify","blocked","payment"] if kw in text.lower()]
        }
        return intelligence
