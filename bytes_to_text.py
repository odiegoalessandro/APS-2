def bytes_to_text(number: int) -> str:
    length = (number.bit_length() + 7) // 8
    return number.to_bytes(length, "big").decode("utf-8")
