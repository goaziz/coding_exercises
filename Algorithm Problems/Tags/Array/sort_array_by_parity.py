from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        return even + odd

# another solution
# class Solution2(object):
#     def sortArrayByParity(self, A):
#         i, j = 0, len(A) - 1
#         while i < j:
#             if A[i] % 2 > A[j] % 2:
#                 A[i], A[j] = A[j], A[i]
#
#             if A[i] % 2 == 0: i += 1
#             if A[j] % 2 == 1: j -= 1
#
#         return A
