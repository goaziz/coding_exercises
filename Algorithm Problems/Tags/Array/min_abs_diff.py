from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        abs_val = max(arr)
        ans = []
        arr.sort()
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            abs_val = min(abs_val, diff)

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == abs_val:
                ans.append([arr[i], arr[i + 1]])
        return ans
