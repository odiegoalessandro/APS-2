# Quarta Parte - definição da função com o objetivo de calcúlar o inverso módular de um número
# Calcúlo necessário para a definição de chaves da criptografia RSA 

# Os parâmetros são "e" número do qual queremos o inverso, e o "phi_n" o módulo
def modinv(e: int, phi_n: int) -> int:
    # Retorna o inteiro D que satisfaz (e * d) % phi_n == 1
    return pow(e, -1, phi_n)
