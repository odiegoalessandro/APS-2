from gen_prime import gen_prime
from modinv import modinv


def gen_keys(bits=512):
    while True:
        p = gen_prime(bits)
        q = gen_prime(bits)
        if p == q:
            continue
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        if modinv(e, phi):
            break
    d = modinv(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key
