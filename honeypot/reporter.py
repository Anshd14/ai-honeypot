import requests
import yaml
class Reporter:
    def __init__(self):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        self.endpoint = config["reporting"]["final_callback"]
    def send_final(self, payload: dict):
        try:
            response = requests.post(self.endpoint, json=payload, timeout=5)
            return response.status_code
        except Exception as e:
            return str(e)
