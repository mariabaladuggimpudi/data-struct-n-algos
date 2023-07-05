from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    # TODO - you fill in here.

    collatz_comp_num = set()
    for i in range(3, n+1):
        temp = i
        temp_sequence = set()
        while temp - 1:
            if temp in temp_sequence:
                return False
            temp_sequence.add(temp)
            if temp in collatz_comp_num:
                return True
            if temp % 2 == 0:
                temp = (temp // 2)
            else:
                temp = (3 * temp) + 1
        collatz_comp_num.add(i)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
