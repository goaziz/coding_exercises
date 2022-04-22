from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        val = words[0]
        chars = list(val)
        for word in words:
            check = []
            for char in word:
                if char in chars:
                    check.append(char)
                    chars.remove(char)
            chars = check
        return chars
