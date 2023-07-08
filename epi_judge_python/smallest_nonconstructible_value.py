from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    # TODO - you fill in here.

    A.sort()
    count, sum = 0, 0
    for i in A:
        if i > count +1:
            break
        count += i
    return count + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
