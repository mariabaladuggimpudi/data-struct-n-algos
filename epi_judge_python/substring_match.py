import functools

from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    # TODO - you fill in here.
    base = 26
    t_hash = functools.reduce(lambda result, i: result*base + ord(i), t[:len(s)], 0)
    s_hash = functools.reduce(lambda result, i: result * base + ord(i), s, 0)

    power_s = base ** max(len(s)-1, 0)
    for i in range(len(s), len(t)-1):
        if t_hash == s_hash and (s == t[i-len(s):i]):
            return i - len(s)
        t_hash -= power_s * ord(t[i-len(s)])
        t_hash = t_hash * base + ord(t[i])


    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
