import requests

API_URL = "http://193.111.249.67:20043"
API_KEY = "your api key"

def solve_hcaptcha(rqdata, proxy):
    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "rqdata": rqdata,
        "proxy": proxy
    }
    response = requests.post(f"{API_URL}/api/solve", json=payload, headers=headers)
    return response.json()

rqdata = "rqdata from hCaptcha requests, on our discord you will find how to get rqdata"
proxy = "user:pass123@123.123.123.123:8080"

result = solve_hcaptcha(rqdata, proxy)
print(result)