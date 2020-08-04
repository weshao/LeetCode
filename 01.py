class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
A = Solution()
b = A.twoSum([3,2,4], 6)

