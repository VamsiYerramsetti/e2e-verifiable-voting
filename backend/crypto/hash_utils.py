import hashlib

def sha256(data):
    return hashlib.sha256(str(data).encode()).hexdigest()
