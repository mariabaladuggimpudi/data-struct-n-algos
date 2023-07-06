from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    a, b, write_idx = m-1, n-1, m+n-1
    while b >= 0 and a >=0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            write_idx -= 1
            a -= 1
        elif A[a] < B[b]:
            A[write_idx] = B[b]
            write_idx -= 1
            b -= 1
        else:
            A[write_idx] = A[a]
            A[write_idx - 1] = B[b]
            write_idx -= 2
            a -= 1
            b -= 1
    if b >= 0:
        while b >= 0:
            A[write_idx] = B[b]
            write_idx -= 1
            b -= 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
