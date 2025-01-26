from collections import defaultdict

def main(results: list) -> dict:
    shuffled_data = defaultdict(list)
    for result in map_results:
        for word, count in result:
            shuffled_data[word].append(count)
    return dict(shuffled_data)
