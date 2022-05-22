from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indices = []
        even_indices = []

        if len(nums) == 2:
            return nums

        for i in range(len(nums)):
            if i % 2 == 0:
                even_indices.append(nums[i])
            else:
                odd_indices.append(nums[i])

        odd_indices.sort(reverse=True)
        even_indices.sort()

        even_index = 0
        odd_index = 0

        for i, j in enumerate(nums):
            if i % 2 == 0:
                nums[i] = even_indices[even_index]
                even_index += 1
            else:
                nums[i] = odd_indices[odd_index]
                odd_index += 1

        return nums

# other's solution
# nums[::2] = sorted(nums[::2])
# nums[1::2] = sorted(nums[1::2])[::-1]
