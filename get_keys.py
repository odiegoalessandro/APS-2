# Quinta parte - Geração das chaves de criptografia

# Importação da função criada anteriormente para geração de números primos
from gen_prime import gen_prime
# Importação da função criada anteriormente para calcúlar o inverso módular de um número
from modinv import modinv

# Definição da função que é responsável pela geração de chaves
# Parâmetro define tamanho 
def gen_keys(bits=512):
    while True:
        # Gera dois números primos grandes
        p = gen_prime(bits)
        q = gen_prime(bits)
        # Verificação que garante que sejam diferentes
        if p == q:
            continue
        # Cálculo do módulo publico
        n = p * q
        # Cálculo da função totient de Euler
        phi = (p - 1) * (q - 1)
        # Expoente público fixo
        e = 65537
        # Verificação de coprimos entre "e" e "phi", se sim sai do loop
        if modinv(e, phi):
            break
    # Expoente privado
    d = modinv(e, phi)
    # Montagem das chaves
    public_key = (e, n)
    private_key = (d, n)
    #retorno das chaves
    return public_key, private_key
