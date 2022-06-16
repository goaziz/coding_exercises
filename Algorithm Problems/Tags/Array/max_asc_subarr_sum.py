from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        max_total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                total += nums[i]
            else:
                total = nums[i]

            if total > max_total:
                max_total = total
        return max_total
