#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.find_two_sums(nums, -nums[i], i+1, result)
        return result
    def find_two_sums(self, nums, target, left, result):
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and  nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
# @lc code=end

test = Solution()
ans = test.threeSum([-2,0,0,2,2])
print(ans)