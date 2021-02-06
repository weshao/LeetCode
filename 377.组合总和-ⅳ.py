#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
# https://leetcode-cn.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (43.44%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 50.9K
# Testcase Example:  '[1,2,3]\n4'
#
# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
# 
# 示例:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# 请注意，顺序不同的序列被视作不同的组合。
# 
# 因此输出为 7。
# 
# 
# 进阶：
# 如果给定的数组中含有负数会怎么样？
# 问题会产生什么变化？
# 我们需要在题目中添加什么限制来允许负数的出现？
# 
# 致谢：
# 特别感谢 @pbrother 添加此问题并创建所有测试用例。
# 
#
from typing import List
import typing
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
        return dp[target] 
# @lc code=end
so = Solution()
ans = so.combinationSum4([1,2,3], 4)
print(ans)
