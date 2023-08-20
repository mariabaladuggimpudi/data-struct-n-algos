from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    # TODO - you fill in here.
    def is_pattern_contained_in_grid_helper(x, y, offset):

        if len(pattern) == offset:
            return True

        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])) or (pattern[offset] != grid[x][y]) or ((x, y, offset) in visited_points):
            return False

        if any(is_pattern_contained_in_grid_helper(x+a, y+b, offset+1) for a, b in ((1,0), (-1,0), (0, 1), (0, -1))):
            return True

        visited_points.add((x, y, offset))
        return False


    visited_points = set()
    return any(is_pattern_contained_in_grid_helper(i, j, 0) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
