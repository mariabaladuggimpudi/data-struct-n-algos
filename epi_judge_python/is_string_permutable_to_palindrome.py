import collections

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    s_dict = collections.Counter(s)
    count = 1
    for key, val in s_dict.items():
        if count > 2:
            return False
        if val % 2:
            count += 1
    return True if count <= 2 else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
