import pandas as pd
import os
from datetime import datetime

class MetadataLogger:
    def __init__(self, save_path="logs/scam_metadata.csv"):
        self.save_path = save_path
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

    def collect(self, scam_message, response, scam_type):
        metadata = {
            "timestamp": datetime.utcnow().isoformat(),
            "scam_message": scam_message,
            "honeypot_response": response,
            "scam_type": scam_type,
            "phishing_urls": ",".join([
               word for word in scam_message.split()
              if word.startswith("http")
           ])
           
        }

        df = pd.DataFrame([metadata])

        if os.path.exists(self.save_path):
            df.to_csv(self.save_path, mode="a", header=False, index=False)
        else:
            df.to_csv(self.save_path, index=False)

        return metadata
