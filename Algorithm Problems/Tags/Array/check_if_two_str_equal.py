from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str_1 = ''.join(word1)
        str_2 = ''.join(word2)

        return str_1 == str_2


# other solution
# class Solution2:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         for c1, c2 in zip(self.generate(word1), self.generate(word2)):
#             if c1 != c2:
#                 return False
#         return True
#
#     def generate(self, wordlist: List[str]):
#         for word in wordlist:
#             for char in word:
#                 yield char
#         yield None