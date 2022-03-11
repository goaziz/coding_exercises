from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []

        def get_min_count(n):
            count = 0
            for i in nums:
                if i != n and n > i:
                    count += 1
            return count

        for i in nums:
            count_n = get_min_count(i)
            arr.append(count_n)

        return arr
