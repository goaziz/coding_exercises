from collections import Counter
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans_zero = []
        ans_one = []

        for i in nums1:
            if i not in nums2:
                ans_zero.append(i)

        for j in nums2:
            if j not in nums1:
                ans_one.append(j)

        return [list(set(ans_zero)), list(set(ans_one))]

    # other solution
    # def findDifference(self, nums1, nums2):
    #     s1, s2 = set(nums1), set(nums2)
    #     return [list(s1 - s2), list(s2 - s1)]
