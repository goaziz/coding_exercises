from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1
        n = len(nums)

        while True:
            while even_index < n and nums[even_index] % 2 == 0:
                even_index += 2
            while odd_index < n and nums[odd_index] % 2 != 0:
                odd_index += 2
            if even_index < n and odd_index < n:
                tmp = nums[even_index]
                nums[even_index] = nums[odd_index]
                nums[odd_index] = tmp
            else:
                break
        return nums

# other solution
# class Solution:
#     def sortArrayByParityII(self, nums):
#         i, j, n = 0, 1, len(nums)
#         while j < n and i < n:
#             if nums[i] % 2 == 0:
#                 i += 2
#             elif nums[j] % 2 == 1:
#                 j += 2
#             else:
#                 nums[i], nums[j] = nums[j], nums[i]
#         return nums
