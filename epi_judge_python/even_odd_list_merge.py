from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.

    even_head = even_list = ListNode()
    odd_head = odd_list = ListNode()
    count = 0
    while L:
        if count % 2 == 0:
            even_list.next = L
            even_list = even_list.next
            L = L.next
            count += 1
        else:
            odd_list.next = L
            odd_list = odd_list.next
            L = L.next
            count += 1

    odd_list.next = None
    even_list.next = odd_head.next

    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
