from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    pascal_triangle = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            temp_list.append(1)
        pascal_triangle.append(temp_list)

    if n <= 2:
        return pascal_triangle
    else:
        for i in range(2, n):
            for j in range(1,len(pascal_triangle[i]) - 1):
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]

    return pascal_triangle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
