class Solution:
    def guessNumber(self, n: int) -> int:
        right = n
        left = 1

        while left <= right:
            mid = (left + right) // 2
            pick = guess(mid)

            if pick == 0:
                return mid
            elif pick == 1:
                left = mid + 1
            else:
                right = mid - 1
