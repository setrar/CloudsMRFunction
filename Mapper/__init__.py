
def main(line: str):
    words = line.split()
    return [(word.lower(), 1) for word in words]
