#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indexDict = {}
        # for i in range(len(nums)):
        #     indexDict[nums[i]] = indexDict.get(nums[i], 0) + i
        # nums.sort()
        # left = 0
        # right = len(nums) - 1 
        # while left < right:
        #     if nums[left] + nums[right] == target:
        #         return [indexDict.get(nums[left]), indexDict.get(nums[right])]
        #     elif nums[left] + nums[right] > target:
        #         right -= 1
        #     elif nums[left] + nums[right] < target:
        #         left += 1
        # return [-1, -1]


        # for i in range(len(nums) - 1):
        #     other = target - nums[i]
        #     if other in nums[i+1:]:
        #         return [i, nums[i+1:].index(other) + i + 1]
        # return [-1, -1]

        hashmap = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in hashmap:
                return [hashmap.get(other), index]
            hashmap[num] = index
        return [-1, -1]
            

# @lc code=end
test = Solution()
print(test.twoSum([3, 2, 4], 6))
