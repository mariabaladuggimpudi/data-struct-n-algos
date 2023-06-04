from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    profit_1, profit_2 = 0.0, 0.0
    price_1, price_2 = float('inf'), float('inf')

    for i in range(len(prices)):
        price_1 = min(price_1, prices[i])
        profit_1 = max(profit_1, prices[i] - price_1)

        price_2 = min(price_2, prices[i]-profit_1)
        profit_2 = max(profit_2, prices[i]-price_2)


    return profit_2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
