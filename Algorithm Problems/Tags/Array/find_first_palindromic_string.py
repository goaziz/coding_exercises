from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            new_str = ''
            for char in range(len(word) - 1, -1, -1):
                new_str += word[char]
            if new_str == word:
                return new_str
        return ""


class Solution2:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
