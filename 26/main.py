class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        window: int = 0

        for i in range(1, l):
            if nums[i] > nums[i - 1]:
                nums[i - window] = nums[i]
            else:
                window += 1

        return l - window


s = Solution()

arr = [1,1,2]
print(s.removeDuplicates(arr), arr)

arr = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(arr), arr)

arr = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(arr), arr)

arr = [1]
print(s.removeDuplicates(arr), arr)

arr = [3,3,3,3,3]
print(s.removeDuplicates(arr), arr)

arr = [1,2,3,4,5]
print(s.removeDuplicates(arr), arr)
