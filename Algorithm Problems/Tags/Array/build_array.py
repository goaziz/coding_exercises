from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = []
        for i in range(n):
            t.append(nums[nums[i]])
        return t


# other's solution
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             nums[i] = nums[i] + n * (nums[nums[i]] % n)
#
#         for i in range(n):
#             nums[i] = nums[i] // n
#         return nums
