from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_arr = []

        for i, n in enumerate(nums):
            target_arr.insert(index[i], n)
        return target_arr


obj = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(obj.createTargetArray(nums, index))
