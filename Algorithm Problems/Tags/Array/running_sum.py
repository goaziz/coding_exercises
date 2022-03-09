from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []

        for i in range(len(nums)):
            running_sum.append(sum(nums[:i + 1]))

        return running_sum

# another solution
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         return nums
