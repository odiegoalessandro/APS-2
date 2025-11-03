# Sexta parte - salvar chaves geradas em arquivos

# Definição de função para salvar chaves geradas
def save_key(path: str, key: tuple[int, int]) -> None:
    # Abre ou cria um arquivo
    with open(path, "w") as f:
        # Escreve a chave no arquivo
        f.write(f"{key[0]}\n{key[1]}\n")
