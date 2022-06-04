from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        salary.remove(min_salary)
        salary.remove(max_salary)

        return sum(salary) / len(salary)

        # one line
        # return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
