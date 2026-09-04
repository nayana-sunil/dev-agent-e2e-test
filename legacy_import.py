import requests

def fetchData(url):
    try:
        r = requests.get(url)
        return r.json()
    except requests.RequestException:
        print("failed to fetch", url)
        return None
