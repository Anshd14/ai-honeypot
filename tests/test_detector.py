import pytest
from honeypot.detector import ScamDetector

def test_detect_scam_keyword():
    detector = ScamDetector()
    is_scam, scam_type = detector.analyze("Your account will be blocked, verify now")
    assert is_scam is True
    assert scam_type == "verify"

def test_safe_message():
    detector = ScamDetector()
    is_scam, scam_type = detector.analyze("Hello friend, how are you?")
    assert is_scam is False
    assert scam_type is None
