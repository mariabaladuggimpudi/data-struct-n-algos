from typing import List

from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    def phone_mnemonic_helper(digit):
        if len(phone_number) == digit:
            mnemonics.append(''.join(partial_mnemonics))
        else:
            for letter in MAPPING[int(phone_number[digit])]:
                partial_mnemonics[digit] = letter
                phone_mnemonic_helper(digit + 1)






    mnemonics = []
    partial_mnemonics = [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
