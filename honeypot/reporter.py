import requests

class Reporter:
    def __init__(self, endpoint="https://cert.example.org/report"):
        self.endpoint = endpoint

    def send(self, metadata: dict):
        try:
            requests.post(self.endpoint, json=metadata, timeout=5)
        except Exception as e:
            print(f"Reporting failed: {e}")
