import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    # TODO - you fill in here.
    if not len(A):
        return []
    result = []
    min_heap = [(-(A[0]), 0)]
    heapq.heapify(min_heap)
    index = 0
    while min_heap and len(result) < k:
        num, index = heapq.heappop(min_heap)
        result.append(-num)

        if ((2*index) + 1) < len(A):
            heapq.heappush(min_heap, (-A[(2*index) + 1], 2*index +1))
        if ((2 * index) + 2) < len(A):
            heapq.heappush(min_heap, (-A[(2 * index) + 2], 2 * index + 2))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
