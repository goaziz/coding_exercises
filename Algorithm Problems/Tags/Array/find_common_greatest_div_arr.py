from typing import List


class Solution:

    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        rem = a % b
        return self.gcd(b, rem)

    def findGCD(self, nums: List[int]) -> int:
        max_n = nums[0]
        min_n = nums[0]

        for i in range(len(nums)):
            if nums[i] > max_n:
                max_n = nums[i]
            elif nums[i] < min_n:
                min_n = nums[i]
        div = self.gcd(max_n, min_n)
        return div

# other solution
# def findGCD(nums: List[int]) -> int:
#     a, b = min(nums), max(nums)
#     while a:
#         a, b = b % a, a
#     return b
