from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if right == 0:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[right] != nums[right - 1]:
            return nums[right]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid - 1
        return -1


# def single_element(arr):
#     left = 0
#     right = len(arr)
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
#             return arr[mid]
#
#         if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 != 0 and arr[mid] == arr[mid - 1]):
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# print(single_element(nums))
obj = Solution()
print(obj.singleNonDuplicate(nums))