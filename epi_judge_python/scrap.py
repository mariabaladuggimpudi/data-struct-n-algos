class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_duplicates(L):

    dummy_head = ListNode(0, L)
    traverse = dummy_head.next
    while traverse and traverse.next and traverse.next.next:
        if traverse.data == traverse.next.data:
            traverse.next = traverse.next.next
            traverse = traverse.next
        else:
            traverse = traverse.next

    if traverse.data == traverse.next.data:
        traverse.next = traverse.next.next
    return dummy_head.next

def add_list(l1, l2):

    added_list_head = added_list_traverse = ListNode()
    carry, result = 0, 0
    while l1 or l2 or carry:
        result = ((l1.data + l2.data) % 10)
        added_list_traverse.next = ListNode(result + carry)
        added_list_traverse = added_list_traverse.next

        carry = (l1.data + l2.data) // 10
        l1, l2 = l1.next, l2.next


    return added_list_head.next