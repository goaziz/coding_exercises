from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        return sum(w1[key] == w2[key] == 1 for key in w1)
