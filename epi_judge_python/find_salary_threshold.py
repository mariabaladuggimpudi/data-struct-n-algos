from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    # TODO - you fill in here.


    current_salaries.sort()
    sum = 0
    for i, val in enumerate(current_salaries):
        temp_tot_sal = len(current_salaries[i:]) * val
        if temp_tot_sal+sum < target_payroll:
            sum = sum + val
        else:
            current_sum = (target_payroll - sum) / len(current_salaries[i:])
            return current_sum


    return -1.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
