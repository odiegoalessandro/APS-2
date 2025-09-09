import secrets

from miller_rabin_test import miller_rabin_test


def gen_prime(bits: int = 2048): 
    while True:

        candidate = secrets.randbelow(
            (1 << bits) - (1 << (bits - 1))) + (1 << (bits - 1)) | 1

        if miller_rabin_test(candidate):
            return candidate

