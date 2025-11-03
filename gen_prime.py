
# Terceira parte - geração de números primos para cálculo das chaves públicas e privadas

# Importação o módulo "secrets" do python 
import secrets

# Importação da função criada anteriormente para garantia de números primos
from miller_rabin_test import miller_rabin_test

# Definição da função "gen_prime" responsável pela geração dos números primos para as chaves de criptografia
def gen_prime(bits: int = 2048): 

    # Garante que o loop continue até a geração de um número primo
    while True:

        # Primeira parte para a geração do número primo consiste em uma definição de intervalo de 2*(bits-1) a partir de (((1 << bits) - (1 << (bits - 1)))
        # Em seguida garante o tamanho mínimo a partir de (1 << (bits - 1))
        # E por fim garante que seu ultimo bit seja 1 através de | 1
        candidate = secrets.randbelow(
            (1 << bits) - (1 << (bits - 1))) + (1 << (bits - 1)) | 1
        
        # Passagem do número gerado pelo teste de primalidade, que caso seja verdadeiramente primo, será retornado
        if miller_rabin_test(candidate):
            return candidate

