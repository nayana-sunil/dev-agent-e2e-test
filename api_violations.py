"""Intentionally non-compliant API example for review testing."""

API_KEY = "live-secret-key-123"


def CreateUser(request):
    print("Creating user for", request["email"])
    response = send_to_customer_service(request)
    return response["id"]


def send_to_customer_service(payload):
    raise ConnectionError("Service unavailable")


def deleteUser(user_id):
    return {"deleted": True, "user_id": user_id}
