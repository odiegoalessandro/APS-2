# Segunda Parte do Programa - outra medida de garantia de números primos para a geração de chave

# Importação do módulo "random" do python
import random

# importação da primeira função criada anteriorment para garantia de números possivelmente primos
from fermat_primality_test import fermat_primality_test

# definição da função do teste de Primalidade de Miller Rabin, com intuito de garantir a primalidade de números gerados
# Onde o "n" será o número testado para a primalidade
# E o "k" serve como um parâmetro de controle para as iterações do código
def miller_rabin_test(n: int, k: int = 40) -> bool:
    d = n - 1
    r = 0
    a = random.randint(2, n - 2)

    # enquanto d for par ele é dividido por 2
    # decompondo n-1 em d*2^r
    while not d & 1:
        # equivalente a d //= 2
        d >>= 1
        r += 1

    for i in range(k):
        # em fermat não existe falsos negativos então removemos os falsos obveis
        if not fermat_primality_test(n, a)[0]:
            return False

        x = pow(a, d, n)

        
        #regra de miller-rabin para verificar se n é composto ou seja se x é igual a 1 ou igual a n - 1 tem chances dele ser primo
        
        if x == 1 or x == n - 1:
            continue

        for j in range(r - 1):
            # x = (x * x) % n ou seja x^2 mod n
            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            return False

    return True
