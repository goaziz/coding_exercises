from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pref_sum = 0
        max_n = 0

        for i in range(len(gain)):
            pref_sum += gain[i]
            max_n = max(max_n, pref_sum)
        return max_n
