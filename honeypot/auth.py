import yaml
from datetime import datetime, timedelta

class APIKeyAuth:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        self.api_key = config["security"]["api_key"]
        self.expiry_days = config["security"]["expiry_days"]
        self.created_at = datetime.utcnow()

    def is_valid(self, key: str) -> bool:
        if key != self.api_key:
            return False
        expiry_date = self.created_at + timedelta(days=self.expiry_days)
        return datetime.utcnow() <= expiry_date
