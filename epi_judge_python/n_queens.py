from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    # TODO - you fill in here.

    def n_queens_helper(row):
        if row == n:
            result.append(n_queens_placements.copy())
            return

        for col in range(n):
            if all(
                abs(c - col) not in (0, row - i)
                for i, c in enumerate(n_queens_placements[:row])):
                n_queens_placements[row] = col
                n_queens_helper(row+1)



    result: List[List[int]] = []
    n_queens_placements = [0] * n
    n_queens_helper(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
