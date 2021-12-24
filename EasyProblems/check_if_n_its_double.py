from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr) - 1):
            print(arr[i])
            if arr[i] == arr[i + 1] * 2:
                return True
        return False


obj = Solution()
arr = [10, 2, 5, 3]
print(obj.checkIfExist(arr))
