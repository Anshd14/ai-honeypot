
import pandas as pd
import os
import yaml
class MetadataLogger:
    def __init__(self):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        self.save_path = config["logging"]["save_path"]
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
    def collect(self, session_id, message, response, scam_type):
        data = {
            "sessionId": session_id,
            "message": message,
            "response": response,
            "scamType": scam_type
        }
        df = pd.DataFrame([data])
        if not os.path.exists(self.save_path):
            df.to_csv(self.save_path, index=False)
        else:
            df.to_csv(self.save_path, mode="a", header=False, index=False)
        return data
