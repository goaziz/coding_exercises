from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums.copy()

        return nums + arr  # or nums * 2
