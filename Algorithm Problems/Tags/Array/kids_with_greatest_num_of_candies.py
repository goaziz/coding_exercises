from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            if candies[i] >= max_c:
                candies[i] = True
            else:
                candies[i] = False

        return candies

    # other solution
    # return [candy + extraCandies >= max_c for candy in candies]
