from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    # TODO - you fill in here.

    service_times.sort()
    tot_wait_time = 0
    for i, query_time in enumerate(service_times):
        num_of_queries_remaining = len(service_times) - (i+1)
        tot_wait_time += num_of_queries_remaining * query_time

    return tot_wait_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
