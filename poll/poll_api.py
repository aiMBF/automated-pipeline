import requests
import time
from datetime import datetime

API_URL = "http://api:8000/data"

def poll_api_every_5s():
    while True:
        timestamp = datetime.utcnow().isoformat()
        try:
            response = requests.get(API_URL)
            print(f"[{timestamp}] Status: {response.status_code} | Response: {response.text}")
        except Exception as e:
            print(f"[{timestamp}] Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    poll_api_every_5s()
