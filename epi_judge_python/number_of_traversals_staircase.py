from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    # TODO - you fill in here.

    def number_of_ways_to_top_helper(h):

        if h <= 1:
            return 1

        if number_of_ways[h] == 0:
            number_of_ways[h] = sum(number_of_ways_to_top_helper(h - i) for i in range(1, min(maximum_step, h) +1))
        return number_of_ways[h]

    number_of_ways = [0] * (top+ 1)
    return number_of_ways_to_top_helper(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
