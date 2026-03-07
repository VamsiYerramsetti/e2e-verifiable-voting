from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes

def generate_keys():
    key = ElGamal.generate(256, get_random_bytes)    #This line generates all cryptographic parameters p,g,x,y
    return key.publickey(), key

if __name__ == "__main__":
    pub, priv = generate_keys()
    print("Public key generated")

#256-bit key size is used because:
#suitable for academic prototypes
#faster for testing
#lower computational overhead

#If server knows the key → server can read votes - so cant use aes