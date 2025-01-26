def main(input: dict) -> dict:
    """
    Reduces a word and a list of counts to a word and its total count.

    :param input: A dictionary with "word" and "counts" keys.
    :return: A dictionary with "word" and "total_count" keys.
    """
    word = input["word"]
    counts = input["counts"]
    print(f"Word: {word}, Counts: {counts}")
    return {"word": word, "total_count": sum(counts)}
