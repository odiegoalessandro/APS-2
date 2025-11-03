# Oitava parte - transformação do texto para bytes

# Definição de função que transforma em bytes o que foi escrito em texto comum
def text_to_bytes(text: str) -> int:
    # Converte a string usando a codificação UTF-8 e garante q seja um número inteiro
    return int.from_bytes(text.encode("utf-8"), "big")
