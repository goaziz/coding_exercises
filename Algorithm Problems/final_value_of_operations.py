from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum_n = 0

        for operation in operations:
            if operation == '++X' or operation == 'X++':
                sum_n += 1
            elif operation == 'X--' or operation == '--X':
                sum_n -= 1
        return sum_n  # or online solution return sum(1 if '+' in i else -1 for i in operations)
