
# Primeira Parte do Programa - garantia de números primos para a geração de chave

# Importação da classe tuple(estrutura de dado similar a uma lista) diretamente do módulo typing do python
from typing import Tuple

# definição da função "teste de primalidade de fermet", algorítmo usado com intuito de determinar se um número é provavelmente primo
def fermat_primality_test(n: int, a: int) -> Tuple[bool, int]:
    if n == 2 or n == 3:
        return True, -1  # nenhuma testemunha necessaria

    # "not n & 1" é equivalente a "n % 2 == 0"
    if n < 2 or not n & 1:
        return False, -1  # nenhum primo maior que 2 é par

    # a^n - 1 ≡ 1 (mod n)
    if pow(a, n - 1, n) != 1:
        return False, a  # a = witness ou seja a é uma testemunha que n não é primo

    return True, -1  # nenhuma testemunha, há chances de ser primo
