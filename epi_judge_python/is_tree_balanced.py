import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
    def check_balance(tree_inner):
        if not tree_inner:
            return BalancedStatusWithHeight(True, -1)
        left_subtree = check_balance(tree_inner.left)
        if not left_subtree.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_subtree = check_balance(tree_inner.right)
        if not right_subtree.balanced:
            return BalancedStatusWithHeight(False, 0)

        height = max(left_subtree.height, right_subtree.height) + 1
        balanced = abs(left_subtree.height - right_subtree.height) <= 1
        return BalancedStatusWithHeight(balanced, height)
    return check_balance(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
