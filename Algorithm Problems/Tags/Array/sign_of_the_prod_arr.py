import math
from functools import reduce
from typing import List


class Solution:
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def arraySign(self, nums: List[int]) -> int:
        # res = reduce(lambda x, y: x * y, nums)
        res = math.prod(nums)
        return self.signFunc(res)
