from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        return l


# second option
class Solution2:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]
