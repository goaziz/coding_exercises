from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count


# other solution

class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
                print(hashMap)
            else:
                # print(hashMap)
                hashMap[number] = 1
        return res


obj = Solution2()
nums = [1, 2, 3, 1, 1, 3]
print(obj.numIdenticalPairs(nums))
