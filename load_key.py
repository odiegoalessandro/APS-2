def load_key(path: str):
    with open(path, "r") as f:
        part1 = int(f.readline().strip())
        part2 = int(f.readline().strip())
    return (part1, part2)
