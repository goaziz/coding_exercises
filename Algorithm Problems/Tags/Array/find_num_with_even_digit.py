from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            count_dig = 0
            while i > 0:
                dig = i % 10
                count_dig += 1
                i //= 10

            if count_dig % 2 == 0:
                count += 1

        return count

# other solution
# def findNumbers(self, nums: List[int]) -> int:
#     return sum(len(str(n)) % 2 == 0 for n in nums)
