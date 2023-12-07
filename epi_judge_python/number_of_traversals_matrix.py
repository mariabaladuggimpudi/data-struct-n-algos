from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    # TODO - you fill in here.

    def number_of_ways_helper(x, y):
        if x == y == 0:
            return 1

        if array_2d[x][y] == 0:
            ways_top = 0 if x == 0 else number_of_ways_helper(x-1, y)
            ways_left = 0 if y == 0 else number_of_ways_helper(x, y-1)
            array_2d[x][y] = ways_left + ways_top
        return array_2d[x][y]



    array_2d = [[0] * m for _ in range(n)]
    return number_of_ways_helper(n-1, m-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
