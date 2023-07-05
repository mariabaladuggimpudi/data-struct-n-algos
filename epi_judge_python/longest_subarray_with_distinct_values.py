from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    # TODO - you fill in here.
    word_n_id, start, long_dist = {}, 0, float('-inf')
    for index, num in enumerate(A):
        if str(num) in word_n_id:
            long_dist = max(long_dist, len(A[start:index]))
            start = word_n_id[str(num)] + 1
            print(long_dist, start)
        word_n_id[str(num)] = index

    return long_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
