#!/usr/bin/python3
"""
this scripts continously sends post requests to a free hosted api i wrote to keep it from being idle and restarting
"""
import requests
import time
from datetime import datetime

# Configuration - Update these values
API_URL = "http://127.0.0.1:5001/keepalive"  # Replace with your API endpoint
PAYLOAD = {"message": "KEEP ALIVE"}  # Your POST data
HEADERS = {
    "Content-Type": "application/json"
}
INTERVAL_SECONDS = 5  # Time between requests
MAX_RETRIES = 3  # Max retries for failed requests
RETRY_DELAY = 2  # Seconds between retries

def send_post_request():
    attempt = 0
    while attempt < MAX_RETRIES:
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Sending POST request to {API_URL}...")
            
            response = requests.post(
                API_URL,
                json=PAYLOAD,
                headers=HEADERS,
                timeout=10  # Timeout in seconds
            )
            
            # Print response details
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print("Request successful!")
            else:
                print(f"Request completed but with status {response.status_code}")
            
            # Print response body if it exists
            try:
                if response.text:
                    print(f"Response: {response.text[:200]}...")  # Print first 200 chars
            except:
                pass
            
            print()  # Empty line for readability
            return True
            
        except requests.exceptions.RequestException as e:
            attempt += 1
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Attempt {attempt} failed: {str(e)}")
            if attempt < MAX_RETRIES:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
    
    print("Max retries reached. Moving to next scheduled request.\n")
    return False

if __name__ == "__main__":
    print(f"""Starting POST request scheduler:
    - Endpoint: {API_URL}
    - Interval: {INTERVAL_SECONDS} seconds
    - Max retries: {MAX_RETRIES}
    - Press Ctrl+C to stop\n""")
    
    try:
        while True:
            send_post_request()
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nStopping the request scheduler...")