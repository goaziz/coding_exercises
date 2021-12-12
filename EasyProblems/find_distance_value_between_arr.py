from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for i in arr1:
            bs = self.binary_search(arr2, i)

            if abs(i - bs) > d:
                ans += 1
        return ans

    def binary_search(self, arr, t):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] < t:
                left = mid + 1
            else:
                right = mid - 1

        ans = -1
        if left < len(arr):
            ans = arr[left]

        if right >= 0 and abs(arr[right] - t) < abs(ans - t):
            ans = arr[right]

        return ans
