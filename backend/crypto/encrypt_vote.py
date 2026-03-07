from Crypto.Random import random

def encrypt_vote(public_key, vote):
    p = int(public_key.p)
    g = int(public_key.g)
    y = int(public_key.y)

    k = random.randint(1, p - 2)

    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = (vote * s) % p

    return (c1, c2)