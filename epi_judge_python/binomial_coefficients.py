from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    def compute_binomial_coeff_helper(x,y):

        if y in (0, x):
            return 1
        if x_choose_y[x][y] == 0:
            without_y = compute_binomial_coeff_helper(x-1, y-1)
            with_y = compute_binomial_coeff_helper(x-1, y)
            x_choose_y[x][y] = without_y + with_y

        return x_choose_y[x][y]

    x_choose_y = [[0] * (k+1) for _ in range(n+1)]
    return compute_binomial_coeff_helper(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
