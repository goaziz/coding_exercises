import collections
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [i for i, j in collections.Counter(nums).items() if j > 1][0]
