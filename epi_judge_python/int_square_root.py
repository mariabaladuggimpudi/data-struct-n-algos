from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.

    start, end = 1, k
    while start <= end:
        mid = (start + end) // 2
        midsquared = mid * mid
        if midsquared <= k:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
