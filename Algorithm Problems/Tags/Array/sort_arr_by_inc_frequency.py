from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))


# other solution
# class Solution2:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         d = Counter(nums)
#
#         def check(x):
#             return d[x]
#
#         nums.sort(reverse=True)
#         nums.sort(key=check)
#         return nums
