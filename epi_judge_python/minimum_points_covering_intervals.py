import collections
import functools
import operator
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    # TODO - you fill in here.
    intervals.sort(key=operator.attrgetter('right'))
    last_time_visit, num_visits = float('-inf'), 0
    for i in intervals:
        if i.left > last_time_visit:
            last_time_visit = i.right
            num_visits += 1
    return num_visits


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
