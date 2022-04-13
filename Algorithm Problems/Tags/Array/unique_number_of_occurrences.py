from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        q = Counter(arr)

        return len(q) == len(set(q.values()))
