from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.

    def generate_balanced_parentheses_helper(num_of_lef_pairs_needed, num_of_right_pairs_needed, valid_prefix, result=[]):

        if num_of_lef_pairs_needed > 0:
            generate_balanced_parentheses_helper(num_of_lef_pairs_needed-1, num_of_right_pairs_needed, valid_prefix+'(')

        if num_of_right_pairs_needed > num_of_lef_pairs_needed:
            generate_balanced_parentheses_helper(num_of_lef_pairs_needed, num_of_right_pairs_needed-1, valid_prefix+')')

        if not num_of_right_pairs_needed:
            result.append(valid_prefix)

        return result



    return generate_balanced_parentheses_helper(num_pairs, num_pairs, '')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
