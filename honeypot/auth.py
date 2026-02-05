import yaml
from datetime import datetime, timedelta
class APIKeyAuth:
    def __init__(self):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        self.api_key = config["security"]["api_key"]
        self.expiry_days = config["security"]["expiry_days"]
        self.created = datetime.now()

    def is_valid(self, key: str) -> bool:
        if key != self.api_key:
            return False
        if datetime.now() > self.created + timedelta(days=self.expiry_days):
            return False
        return True
