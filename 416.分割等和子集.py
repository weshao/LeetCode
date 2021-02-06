#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (49.22%)
# Likes:    664
# Dislikes: 0
# Total Accepted:    98.2K
# Total Submissions: 199.2K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        maxNum = max(nums)
        if maxNum > target:
            return False
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        
        for i in range(n):
            for j in range(target, 0, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] | dp[j - nums[i]]
                else:
                    dp[j] = dp[j]
        return dp[target]
# @lc code=end
so = Solution()
ans = so.canPartition([1, 2, 3, 5])
print(ans)
