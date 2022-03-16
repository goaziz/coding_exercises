from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    break
            else:
                count += 1

        return count


# other solution
class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0

        for word in words:
            for char in word:
                if char not in allowed:
                    count += 1
                    break
        return len(words) - count
