from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = nums[i - 1] - nums[i] + 1
                count += diff
                nums[i] = nums[i - 1] + 1

        return count

    # other solution
    # def minOperations(self, nums: List[int]) -> int:
    #     cnt = prev = 0
    #     for cur in nums:
    #         if cur <= prev:
    #             prev += 1
    #             cnt += prev - cur
    #         else:
    #             prev = cur
    #     return cnt