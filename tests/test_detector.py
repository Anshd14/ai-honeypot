from honeypot.detector import ScamDetector

def test_detection():
    detector = ScamDetector()
    result, _ = detector.analyze("verify your account now")
    assert result
