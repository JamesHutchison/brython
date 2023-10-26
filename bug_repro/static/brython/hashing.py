import hashlib


def sha256(message) -> str:
    # Convert the string to bytes
    message_bytes = message.encode("utf-8")

    # Compute the sha256 hash
    hash_obj = hashlib.sha256(message_bytes)

    return hash_obj.hexdigest()
