def save_key(path: str, key: tuple[int, int]) -> None:
    with open(path, "w") as f:
        f.write(f"{key[0]}\n{key[1]}")
