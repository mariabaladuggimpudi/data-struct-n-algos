from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    start, end = 0, 63
    if x>0:
        while start < end:
            if ((x>>start)&1) != ((x>>end)&1):
                x ^= ((1<<start)|(1<<end))
            start += 1
            end -= 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
