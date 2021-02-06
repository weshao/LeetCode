#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (66.88%)
# Likes:    667
# Dislikes: 0
# Total Accepted:    123.9K
# Total Submissions: 185K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 
# 每一步只能移动到下一行中相邻的结点上。
# 
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 
# 示例 2：
# 
# 
# 输入：triangle = [[-10]]
# 输出：-10
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return triangle
        n = len(triangle)
        c = len(triangle[-1])
        dp = [0 for _ in range(n)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
        return min(dp)

# @lc code=end
so = Solution()
ans = so.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(ans)
