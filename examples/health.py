import requests

API_URL = "http://193.111.249.67:20043"

def check_api_status():
    response = requests.get(f"{API_URL}/health")
    print(response.json())

check_api_status()