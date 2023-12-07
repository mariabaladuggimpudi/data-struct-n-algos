from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    #print(x, "integer")
    flag=0
    if x<0:
        flag = 1
        x = -x
    s = []
    while x:
        s.append(chr(ord('0') + x%10))
       # print(x%10)
        x //= 10
    #print(''.join(reversed(s)))
    if x == 0:
        s.append(chr(ord('0')))
    return '-'+''.join(reversed(s)) if flag else ''.join(reversed(s))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    #print(s, "in string")
    count, flag, k = 0, 0, []
    #print(s, "in string :::")
    for i in s:
        #print(i, "I am here")
        if count == 0 and i == '-':
            flag = 1
            count += 1
        elif count == 0 and i == '+':
            count += 1
        else:
            k.append(ord(i) - ord('0'))
    result = 0
    #print(k, " hey")
    for j in range(len(k)):
        result = result * 10 + k[j]
    #print(result)

    return -result if flag else result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
