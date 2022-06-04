from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        n = len(arr)
        val = int(n * 0.05)
        l = arr[val:n - val]
        return sum(l) / len(l)
