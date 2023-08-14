from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.
    # Converting the string 'A' to string 'B'
    def levenshtein_distance_helper(A_idx, B_idx):

        if A_idx < 0:
            return B_idx + 1
        if B_idx < 0:
            return A_idx + 1
        if store_distance_2d[A_idx][B_idx] == 0:
            if A[A_idx] == B[B_idx]:
                store_distance_2d[A_idx][B_idx] = levenshtein_distance_helper(A_idx - 1, B_idx -1)
            else:
                substitute = levenshtein_distance_helper(A_idx-1, B_idx-1)
                add = levenshtein_distance_helper(A_idx, B_idx-1)
                delete = levenshtein_distance_helper(A_idx - 1, B_idx)

                store_distance_2d[A_idx][B_idx] = 1 + min(substitute, add, delete)

        return store_distance_2d[A_idx][B_idx]
    store_distance_2d = [[0] * len(B) for _ in range(len(A))]
    return levenshtein_distance_helper(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
