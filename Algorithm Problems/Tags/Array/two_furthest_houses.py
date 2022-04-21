from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_n = 0

        for i in range(len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    diff = abs(i - j)
                    max_n = max(max_n, diff)
        return max_n
        # Time Complexity O(i + j)


# other solution

def maxDistance(A):
    res = 0
    for i, x in enumerate(A):
        if x != A[0]:
            res = max(res, i)
        if x != A[-1]:
            res = max(res, len(A) - 1 - i)
    return res
