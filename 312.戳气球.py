#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (67.26%)
# Likes:    616
# Dislikes: 0
# Total Accepted:    36.7K
# Total Submissions: 54.5K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 说明:
# 
# 
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 示例:
# 
# 输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#
from typing import List
from functools import lru_cache
# @lc code=start
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         n = len(nums)
#         val = [1] + nums + [1]

#         @lru_cache(None)
#         def solve(left: int, right: int) -> int:
#             if left >= right - 1:
#                 return 0
            
#             best = 0
#             for i in range(left+1, right):
#                 total = val[left] * val[i] * val[right]
#                 total += solve(left, i) + solve(i, right)
#                 best = max(best, total)
            
#             return best
#         return solve(0, n+1)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        
        return rec[0][n+1]
# @lc code=end
so = Solution()
ans = so.maxCoins([3, 1, 5, 8])
print(ans)
