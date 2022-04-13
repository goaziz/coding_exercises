from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_list = []
        for row in matrix:
            min_list.append(min(row))

        result = []
        for col in zip(*matrix):
            max_num = max(col)
            if max_num in min_list:
                result.append(max_num)

        return result
