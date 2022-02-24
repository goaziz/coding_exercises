from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        count = 0
        for i in arr:
            if i != 0:
                if self.binary_search(i, arr) and self.binary_search(i * 2, arr):
                    return True
            else:
                count += 1
        return count >= 2

    def binary_search(self, target, nums):
        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return True
        return False


# another solution
def checkIfExists(arr):
    if arr.count(0) > 1:
        return True
    set_arr = set(arr) - {0}

    for i in arr:
        if 2 * i in set_arr:
            return True
    return False
