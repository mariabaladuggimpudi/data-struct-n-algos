from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    # TODO - you fill in here.
    word_n_id, start, long_dist = {}, 0, 0
    for index, num in enumerate(A):
        if str(num) in word_n_id:
            dup_id = word_n_id[str(num)]
            if dup_id >= start:
                long_dist = max(long_dist, len(A[start:index]))
                start = word_n_id[str(num)] + 1

        word_n_id[str(num)] = index
    #long_dist = max(long_dist, len(word_n_id))
    return max(long_dist, len(A) - start)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
