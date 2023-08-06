from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.
    def generate_balanced_helper(left_paren, right_paren, valid_prefix, result=[]):

        if left_paren > 0:
            generate_balanced_helper(left_paren-1, right_paren, valid_prefix+'(')
        if left_paren < right_paren:
            generate_balanced_helper(left_paren, right_paren-1, valid_prefix+')')

        if not right_paren:
            result.append(valid_prefix)
        return result

    return generate_balanced_helper(num_pairs, num_pairs, "")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
