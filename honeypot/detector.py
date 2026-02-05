from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
class ScamDetector:
    def __init__(self):
        # Training data (you can expand this with real phishing dataset)
        scam_examples = [
            "Verify your account at http://fakebank.com",
            "Urgent! Your bank login is required",
            "You won the lottery, click here",
            "Password reset required immediately"
        ]
        safe_examples = [
            "Hello, how are you?",
            "Meeting scheduled for tomorrow",
            "Lunch at 1 PM?",
            "This is a safe test message"
        ]
        texts = scam_examples + safe_examples
        labels = [1] * len(scam_examples) + [0] * len(safe_examples)  # 1=scam, 0=safe
        # TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(texts)
        # Logistic Regression classifier
        self.classifier = LogisticRegression()
        self.classifier.fit(X, labels)

    def analyze(self, text: str):
        X_test = self.vectorizer.transform([text])
        prediction = self.classifier.predict(X_test)[0]

        if prediction == 1:
            return True, "phishing"
        return False, None