#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (46.68%)
# Likes:    712
# Dislikes: 0
# Total Accepted:    262.1K
# Total Submissions: 561.3K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
            elif i == 0 and nums[i] > target:
                return 0
                
            elif nums[i] < target and i < len(nums) - 1 and nums[i + 1]> target:
                return i + 1
            
            elif i == len(nums)-1: 
                return len(nums)
# @lc code=end

sol = Solution()
ans = sol.searchInsert([1, 3, 5, 6], 7)
print(ans)