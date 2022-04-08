from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sum = 0
        for i, j in d.items():
            if j == 1:
                sum += i

        return sum
