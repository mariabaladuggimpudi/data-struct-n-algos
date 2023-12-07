from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    # TODO - you fill in here.

    max_array = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[i] >= A[j]:
                max_array[i] = max(max_array[i], max_array[j]+1)
    return max(max_array)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
