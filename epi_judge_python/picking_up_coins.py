from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    # TODO - you fill in here.

    def max_rev_helper(a, b):
        if a > b:
            return 0
        if coins_2d_processed[a][b] == -1:
            max_rev_a = coins[a] + min(
                max_rev_helper(a+2, b),
                max_rev_helper(a+1, b-1))
            max_rev_b = coins[b] + min(
                max_rev_helper(a, b-2),
                max_rev_helper(a+1, b-1)
            )
            coins_2d_processed[a][b] = max(max_rev_a, max_rev_b)

        return coins_2d_processed[a][b]

    coins_2d_processed = [[-1] * len(coins) for _ in range(len(coins))]
    return max_rev_helper(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
