from collections import Counter
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = Counter(set(nums1))
        c.update(set(nums2))
        c.update(set(nums3))

        arr = []
        for i, j in c.items():
            if j > 1:
                arr.append(i)
        return arr
