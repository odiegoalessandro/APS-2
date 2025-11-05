def text_to_bytes(text: str) -> int:
    return int.from_bytes(text.encode("utf-8"), "big")
