def decrypt(ciphertext: int, private_key: tuple[int, int]) -> int:
    d, n = private_key
    return pow(ciphertext, d, n)
