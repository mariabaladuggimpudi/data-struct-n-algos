import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # TODO - you fill in here.

    def optimum_subject_to_capacity_helper(k, available_capacity):
        if k < 0:
            return 0

        if capacity_2D[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_capacity_helper(k-1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight else items[k].value + optimum_subject_to_capacity_helper(k-1, available_capacity-items[k].weight))
            capacity_2D[k][available_capacity] = max(with_curr_item, without_curr_item)
        return capacity_2D[k][available_capacity]




    capacity_2D = [[-1] * (capacity + 1) for _ in range(len(items))]
    return optimum_subject_to_capacity_helper(len(items) -1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
