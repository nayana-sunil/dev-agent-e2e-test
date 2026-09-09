import requests

def fetch_report(report_id):
    try:
        r = requests.get(f"https://api.example.com/reports/{report_id}")
        return r.json()
    except:
        print("report fetch failed", report_id)
        return None
