from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        nums.sort()

        for i in range(len(nums)):
            if original == nums[i]:
                original *= 2
        return original
