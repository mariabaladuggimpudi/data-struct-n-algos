from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # TODO - you fill in here.
    result, temp_result = [], []
    for i in range(len(s)):
        if int(s[:i+1]) < 256:
            temp_result.append(s[:i+1])
        else:
            break
        for j in range(i+1,len(s)):
            if int(s[i+1:j+1]) < 256:
                temp_result.append(s[i+1:j+1])
            else:
                break
            # for k in range(j+1, len(s)):
            #     if int()

    return []


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
