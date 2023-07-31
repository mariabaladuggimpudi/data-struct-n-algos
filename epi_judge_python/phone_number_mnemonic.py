from typing import List

from test_framework import generic_test, test_utils

mapping = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            result.append(''.join(partial_mnemonic))
        else:
            for c in mapping[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit+1)



    result = []
    partial_mnemonic = ['0'] * len(phone_number)
    phone_mnemonic_helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
