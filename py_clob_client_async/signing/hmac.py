import hmac
import hashlib
import base64
import json


def build_hmac_signature(
    secret: str, timestamp: str, method: str, requestPath: str, body=None
):
    """
    Creates an HMAC signature by signing a payload with the secret
    """
    base64_secret = base64.urlsafe_b64decode(secret)
    message = str(timestamp) + str(method) + str(requestPath)
    if body:
        # Use compact JSON format to match what httpx sends
        if isinstance(body, str):
            body_str = body
        else:
            body_str = json.dumps(body, separators=(',', ':'), sort_keys=True)
        message += body_str

    h = hmac.new(base64_secret, bytes(message, "utf-8"), hashlib.sha256)

    # ensure base64 encoded
    return (base64.urlsafe_b64encode(h.digest())).decode("utf-8")
