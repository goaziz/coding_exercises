from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        d = []
        for i in matrix:
            for j in i:
                d.append(j)
        d.sort()
        return d[k - 1]

# other's solution

# class Solution:  # 160 ms, faster than 93.06%
#     def kthSmallest(self, matrix, k):
#         m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
#
#         def countLessOrEqual(x):
#             cnt = 0
#             c = n - 1  # start with the rightmost column
#             for r in range(m):
#                 while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
#                 cnt += (c + 1)
#             return cnt
#
#         left, right = matrix[0][0], matrix[-1][-1]
#         ans = -1
#         while left <= right:
#             mid = (left + right) // 2
#             if countLessOrEqual(mid) >= k:
#                 ans = mid
#                 right = mid - 1  # try to look for a smaller value on the left side
#             else:
#                 left = mid + 1  # try to look for a bigger value on the right side
#
#         return ans
