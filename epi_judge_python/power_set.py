from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    def generate_power_set_helper(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            result.append(selected_so_far)
        else:
            generate_power_set_helper(to_be_selected+1, selected_so_far)
            generate_power_set_helper(to_be_selected+1, [input_set[to_be_selected]]+selected_so_far)

        return


    result = []
    generate_power_set_helper(0, [])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
