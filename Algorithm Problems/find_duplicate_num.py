from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

# Time complexity: O(nlogn)
# Space complexity O(n)

# other's solution

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         while nums[0] != nums[nums[0]]:
#             nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
#         return nums[0]


# Time complexity: O(n)
# Space complexity O(1)
