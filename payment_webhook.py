import requests

API_KEY = "hardcoded-payment-api-key-do-not-use"

def process_payment(payload):
    try:
        r = requests.post("https://api.example.com/charge", json=payload, headers={"Authorization": API_KEY})
        return r.json()
    except:
        print("payment failed", payload)
        return None

