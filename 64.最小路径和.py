#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.67%)
# Likes:    718
# Dislikes: 0
# Total Accepted:    159.8K
# Total Submissions: 236.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# 0 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre = grid[0]
        for j in range(1, n):
            pre[j] = pre[j] + pre[j-1]
        if m == 1:
            return pre[-1]
        else:
            for i in range(1, m):
                cur = grid[i]
                cur[0] = cur[0] + pre[0]
                for j in range(1, n):
                    cur[j] = min((cur[j] + cur[j-1]), cur[j] + pre[j])
                pre = cur
            return cur[-1]                
                
# @lc code=end

so = Solution()
ans = so.minPathSum([[1,2,3]])
print(ans)