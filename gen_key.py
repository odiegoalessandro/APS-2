import secrets

def gen_key(bits: int = 2048):

    """
    secrets.randbits(bits) gera um numero aleatorio com a quantidade de bits especficada
    | (1 << (bits - 1)) garante que o bit mais significativo seja 1 (garante o tamnho correto do numero)
    | 1 garante que o o bit menos significativo seja 1 (garante que o numero seja impar)
    """
    candidate = secrets.randbits(bits) | (1 << (bits - 1)) | 1

    # TODO: implementar um looping para testar os candidatos até encontrar um primo
    