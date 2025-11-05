if __name__ == "__main__":
    while True:
        mensagem = input("Digite uma mensagem para que ela seja criptografada(maximo de 128 caracteres):")

        if len(mensagem) > 128 or mensagem.strip() == "":
            print("A mensagem deve ter apenas 128 caracteres ou menos e não pode estar vazia.")
            continue

        pass
    