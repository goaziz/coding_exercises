from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort()
        target.sort()
        return target == arr

# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return collections.Counter(target) == collections.Counter(arr)
