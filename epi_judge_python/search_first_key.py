from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    start, end = 0, len(A) - 1
    result = -1
    while start <= end:
        mid = (end + start) // 2
        if A[mid] == k:
            end = mid -1
            result = mid
        elif A[mid] <  k:
            start = mid + 1
        else:
            end = mid -1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
