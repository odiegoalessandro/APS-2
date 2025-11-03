# Décima parte - descriptografia da mensagem criptografada

# Definição da função que é responsável por descriptografar a mensagen usando o parâmetros de inteiro e da chave privada
def decrypt(ciphertext: int, private_key: tuple[int, int]) -> int:
    d, n = private_key
    # Mensagem descriptografada = (mensagem criptografadaᵉ) mod n
    return pow(ciphertext, d, n)