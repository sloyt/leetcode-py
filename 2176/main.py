from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1

        return count


s = Solution()

print('4', s.countPairs([3,1,2,2,2,1,3], 2))
print('0', s.countPairs([1,2,3,4], 1))
print('0', s.countPairs([2], 2))
print('18', s.countPairs([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], 7))
print('8', s.countPairs([10,2,3,4,9,6,3,10,3,6,3,9,1], 4))
