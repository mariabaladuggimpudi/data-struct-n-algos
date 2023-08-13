from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.

    num_of_scores = [[1] + [0] * final_score for _ in range(len(individual_play_scores))]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score+1):
            without_curr_play = num_of_scores[i-1][j] if i >= 1 else 0
            with_curr_play = num_of_scores[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0
            num_of_scores[i][j] = with_curr_play + without_curr_play

    return num_of_scores[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
