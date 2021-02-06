#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.32%)
# Likes:    887
# Dislikes: 0
# Total Accepted:    101.9K
# Total Submissions: 252.7K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
# 
#
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(len(nums)):
            j = nums[i] - 1
            while j >= 0 and j < len(nums) and nums[i]!=nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1


        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        
        return nums[-1] + 1


# @lc code=end
so = Solution()
ans = so.firstMissingPositive([1,2,0])
print(ans)