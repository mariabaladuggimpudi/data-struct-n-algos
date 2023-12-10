from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    while x:
        result += x & 1
        x >>= 1

    return 1 if (result % 2) == 1 else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
