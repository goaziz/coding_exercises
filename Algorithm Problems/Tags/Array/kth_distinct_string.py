from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        arr_str = []
        for i, j in c.items():
            if j == 1:
                arr_str.append(i)

        for i, j in enumerate(arr_str, start=1):
            if i == k:
                return j
        return ''

# other solution
# def kthDistinct(self, arr: List[str], k: int) -> str:
# 	arr = [i for i in arr if arr.count(i) == 1]
# 	return "" if k > len(arr) else arr[k - 1]

# class Solution2:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         freq = Counter(arr)
#         for x in arr:
#             if freq[x] == 1:
#                 k -= 1
#             if k == 0:
#                 return x
#         return ""
