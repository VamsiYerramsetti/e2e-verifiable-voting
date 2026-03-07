def decrypt_vote(private_key, ciphertext):
    p = int(private_key.p)
    x = int(private_key.x)

    c1, c2 = ciphertext

    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)

    vote = (c2 * s_inv) % p

    return vote