from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = [word for word in words if any(set(word.lower()) <= row for row in keyboard)]
        return res


obj = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]

print(obj.findWords(words))
