from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = dict()
        for i, j in enumerate(mat):
            d.update({i: j.count(1)})
        s = {i: j for i, j in sorted(d.items(), key=lambda item: item[1])}
        l = list(s.keys())
        return l[:k]


# another option with binary search
# from heapq import nsmallest
#
#
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         return [i for count, i in nsmallest(k, ((self.count_ones(row), i) for i, row in enumerate(mat)))]
#
#     def count_ones(self, a):
#         x, lo, hi = 0, 0, len(a)
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if a[mid] > x:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
