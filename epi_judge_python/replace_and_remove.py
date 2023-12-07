import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    write_id, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_id] = s[i]
            write_id += 1
        if s[i] == 'a':
            a_count += 1

    curr_id = write_id - 1
    write_id += a_count - 1
    final_size = write_id + 1
    while curr_id >= 0:
        if s[curr_id] == 'a':
            s[write_id-1:write_id+1] = 'dd'
            write_id -= 2
        else:
            s[write_id] = s[curr_id]
            write_id -= 1
        curr_id -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
