from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)

        index = 0
        for i in arr2:
            n = c.setdefault(i, 0)
            for _ in range(n):
                arr1[index] = i
                index += 1
            c.pop(i)

        for key in sorted(c.keys()):
            count = c.get(key)
            while count:
                arr1[index] = key
                count -= 1
                index += 1
        return arr1


# def relativeSortArray(A, B):
#     k = {b: i for i, b in enumerate(B)}
#     return sorted(A, key=lambda a: k.get(1000 + a))
