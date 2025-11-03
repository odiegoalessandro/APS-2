# Sétima parte - carregar chaves salvas em arquivos 

# Definição de função para carregar chaves posteriormente salvas
def load_key(path: str):
    # Abre o arquivo em modo leitura "r"
    # "f" é o objeto do arquivo
    with open(path, "r") as f:
        # Lê o arquivo, remove espaços em branco e converte o numero para inteiro 
        part1 = int(f.readline().strip())
        part2 = int(f.readline().strip())
        # retorna os arquivos
    return (part1, part2)
