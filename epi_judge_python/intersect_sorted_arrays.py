from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    start_1, start_2, intersection, i = 0, 0, [], 0
    while start_1 < len(A) and start_2 < len(B):
        if A[start_1] == B[start_2]:
            if i == 0 or intersection[i - 1] != A[start_1]:
                intersection.append(A[start_1])
                i += 1
            start_1 += 1
            start_2 += 1
        elif A[start_1] < B[start_2]:
            start_1 += 1
        else:
            start_2 += 1

    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
