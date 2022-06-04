from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        q = len(set(candyType))
        return min(q, len(candyType) // 2)


obj = Solution()
candyType = [1, 1, 2, 3]
print(obj.distributeCandies(candyType))
