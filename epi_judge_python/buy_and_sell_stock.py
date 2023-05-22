from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    profit, price = 0.0, float('inf')
    for i in range(0, len(prices)):
        price = min(price, prices[i])
        profit = max(profit, prices[i] - price)
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
