from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if i < j and abs(nums[i] - nums[j]) == k:
                    count += 1
        return count


# other solution
class Solution2:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            counter += seen[num - k] + seen[num + k]
            seen[num] += 1
        return counter


nums = [1, 2, 2, 1]
k = 1
obj = Solution2()
print(obj.countKDifference(nums, k))