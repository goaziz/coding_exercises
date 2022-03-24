from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                prod = (nums[i] - 1) * (nums[j] - 1)
                curr_max = max(curr_max, prod)
        return curr_max


# other solution
# class Solution2:
#     def maxProduct(self, nums: List[int]) -> int:
#         m, n = 0, 0
#         for num in nums:
#             if num >= m:
#                 n = m
#                 m = num
#             elif num > n:
#                 n = num
#         return (m - 1) * (n - 1)