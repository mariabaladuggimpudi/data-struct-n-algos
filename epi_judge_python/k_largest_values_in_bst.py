from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    k_large_elements = []
    def find_k_elements(tree):
        if tree and len(k_large_elements) < k:
            find_k_elements(tree.right)
            if len(k_large_elements) < k:
                k_large_elements.append(tree.data)
                find_k_elements(tree.left)

    find_k_elements(tree)
    return k_large_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
