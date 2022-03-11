from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = list(s)
        d = dict(zip(indices, l))
        sorted_d = {k: d[k] for k in sorted(d)}
        res = ''
        for i in sorted_d.values():
            res += i
        return res

# Other Solution
# class Solution2:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         res = [''] * len(s)
#         print(res)
#         for index, char in enumerate(s):
#             res[indices[index]] = char
#         return "".join(res)
