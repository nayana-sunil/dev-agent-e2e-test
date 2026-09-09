import requests

def sync_orders(endpoint):
    try:
        r = requests.get(endpoint)
        return r.json()
    except:
        print("order sync failed", endpoint)
        return None
