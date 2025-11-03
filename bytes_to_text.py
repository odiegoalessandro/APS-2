# Décima primeira parte - transcrição do texto descriptografado em bytes para mensagem original

# Definição de função que transforma para texto comum o que foi escrito em bytes
def bytes_to_text(number: int) -> str:
    # cálculo de comprimento dos bytes
    length = (number.bit_length() + 7) // 8
    # Converte o número inteiro para bytes, logo em seguida o decodifica usando UTF-8
    return number.to_bytes(length, "big").decode("utf-8")
