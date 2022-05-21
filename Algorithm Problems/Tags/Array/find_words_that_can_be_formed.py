from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        found = True
        res = 0
        for word in words:
            for char in word:
                if chars.count(char) >= word.count(char):
                    found = True
                else:
                    found = False
                    break
            if found:
                res += len(word)

        return res

    # another solution
    def countCharacters2(self, words: List[str], chars: str) -> int:
        res = 0
        chars_counter = Counter(chars)
        for word in words:
            word_counter = Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                res += len(word)
        return res
