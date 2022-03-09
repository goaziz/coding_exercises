from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        arr = []
        for i, j in zip(arr1, arr2):
            arr.append(i)
            arr.append(j)
        return arr

# another solution
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         result = []
#         for i in range(n):
#             result.append(nums[i])
#             result.append(nums[n + i])
#         return result
