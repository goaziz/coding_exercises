from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while students and students.count(sandwiches[0]) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)

    # other's solution

    # def countStudents2(self, A, B):
    #     count = Counter(A)
    #     n, k = len(A), 0
    #     while k < n and count[B[k]]:
    #         count[B[k]] -= 1
    #         k += 1
    #     return n - k