from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # TODO - you fill in here.
    nearest_distance, word_n_id = float('inf'), {}
    for index, word in enumerate(paragraph):
        if word in word_n_id:
            nearest_distance = min(nearest_distance, index - word_n_id[word])
        word_n_id[word] = index

    return int(nearest_distance) if nearest_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
