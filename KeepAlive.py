import requests
import time
from datetime import datetime

# Disable proxy (if you're behind a corporate network)
session = requests.Session()
session.trust_env = False  # Ignore system proxy settings

API_URL = "https://cnn-classifier-api-server.onrender.com/keepalive"
PAYLOAD = {"message": "keepalive"}
HEADERS = {"Content-Type": "application/json"}

def send_post_request():
    try:
        response = session.post(
            API_URL,
            json=PAYLOAD,
            headers=HEADERS,
            timeout=10,
            verify=True  # Enable SSL verification (set False only if SSL fails)
        )
        print(f"[{datetime.now()}] Status: {response.status_code}, Response: {response.text}")
        return True
    except Exception as e:
        print(f"[{datetime.now()}] Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting keepalive requests... (Ctrl+C to stop)")
    while True:
        send_post_request()
        time.sleep(10)