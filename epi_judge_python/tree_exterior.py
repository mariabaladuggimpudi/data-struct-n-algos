import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # TODO - you fill in here.
    def leftside_tree(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        exterior.append(subtree)
        if subtree.left:
            leftside_tree(subtree.left)
        else:
            leftside_tree(subtree.right)

    def leaves(subtree):
        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        leaves(subtree.left)
        leaves(subtree.right)


    def rightside_tree(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        if subtree.right:
            rightside_tree(subtree.right)
        else:
            rightside_tree(subtree.left)

        exterior.append(subtree)


    if not tree:
        return []

    exterior = [tree]
    leftside_tree(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    rightside_tree(tree.right)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
