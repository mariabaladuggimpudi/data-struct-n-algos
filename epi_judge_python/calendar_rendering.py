import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.

    endpoint = []
    for i in A:
        endpoint.append((i.start, True))
        endpoint.append((i.finish, False))
    endpoint.sort(key=lambda x: (x[0], not x[1]))
    num_of_simultaneous_events, max_events = 0, 0
    #print(endpoint)
    for i in endpoint:
        if i[1]:
            num_of_simultaneous_events += 1
            max_events = max(max_events, num_of_simultaneous_events)
        else:
            num_of_simultaneous_events -= 1

    return max_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
