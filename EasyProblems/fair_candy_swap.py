from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        aliceSizes.sort()
        bobSizes.sort()
        diff = (a - b) / 2
        left = 0
        right = 0

        while True:
            tmp = aliceSizes[left] - bobSizes[right]
            if tmp > diff:
                right += 1
            elif tmp < diff:
                left += 1
            else:
                return [aliceSizes[left], bobSizes[right]]


a = [1, 2, 5]
b = [2, 4]
obj = Solution()
print(obj.fairCandySwap(a, b))
