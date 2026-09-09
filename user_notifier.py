import requests

def notify_user(user_id, message):
    try:
        r = requests.post(f"https://api.example.com/users/{user_id}/notify", json={"message": message})
        return r.status_code == 200
    except:
        print("notify failed", user_id, message)
        return False
