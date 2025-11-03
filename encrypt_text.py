# Nona parte - criptografia do texto em bytes

# Definição da função que é responsável por criptografar a mensagen em bytes usando o parâmetros de inteiro e da chave pública
def encrypt(plaintext: int, public_key: tuple[int, int]) -> int:
    e, n = public_key
    # Mensagem criptografada = (mensagemᵉ) mod n
    return pow(plaintext, e, n )