from honeypot.intelligence import IntelligenceExtractor
def test_extract_upi_id():
    extractor = IntelligenceExtractor()
    text = "Please send money to scammer@upi immediately"
    intelligence = extractor.extract(text)
    assert "scammer@upi" in intelligence["upiIds"]
def test_extract_phishing_link():
    extractor = IntelligenceExtractor()
    text = "Click here: http://malicious-link.example"
    intelligence = extractor.extract(text)
    assert "http://malicious-link.example" in intelligence["phishingLinks"]
