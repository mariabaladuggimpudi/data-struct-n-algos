from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # TODO - you fill in here.
    citations.sort()
    #print(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i

    return 0



if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
