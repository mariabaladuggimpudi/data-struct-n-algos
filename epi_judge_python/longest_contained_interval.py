from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    # TODO - you fill in here.
    long_interval = 0
    given_elements = set(A)
    while given_elements:
        curr_ele = given_elements.pop()
        lower_bound = curr_ele -1
        while (lower_bound) in given_elements:
            given_elements.remove(lower_bound)
            lower_bound -= 1
        upper_bound = curr_ele + 1
        while (upper_bound) in given_elements:
            given_elements.remove(upper_bound)
            upper_bound += 1

        long_interval = max(long_interval, upper_bound-lower_bound - 1)
    return long_interval


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
