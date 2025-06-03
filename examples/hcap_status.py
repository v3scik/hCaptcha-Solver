import requests

API_URL = "http://193.111.249.67:20043"
API_KEY = "your api key"

def check_hcaptcha_status():
    headers = {"X-API-Key": API_KEY}
    response = requests.get(f"{API_URL}/api/status", headers=headers)
    print(response.json())

check_hcaptcha_status()