from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_val = float('inf')
        res = -1
        for i, (a, b) in enumerate(points):
            if x == a or y == b:
                abs_val = abs(x - a) + abs(y - b)
                if abs_val < min_val:
                    min_val = abs_val
                    res = i
        return res
