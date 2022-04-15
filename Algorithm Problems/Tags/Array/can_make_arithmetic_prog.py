from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        ans = []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            ans.append(diff)

        return all(ans[i] == ans[i + 1] for i in range(len(ans) - 1))

# another solution
# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr.sort()
#         diff = arr[0] - arr[1]
#         for i in range(2, len(arr)):
#             if diff != arr[i - 1] - arr[i]:
#                 return False
#         return True
