#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (43.32%)
# Likes:    643
# Dislikes: 0
# Total Accepted:    85.6K
# Total Submissions: 195.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#
from typing import List
# @lc code=start
""" class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        res = 0
        if not r:
            return res
        c = len(matrix[0])
        
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if dp[i-1][j]:
                    dp[i][j] = int(matrix[i][j]) * (dp[i-1][j] + int(matrix[i][j]))
                else:
                    dp[i][j] = int(matrix[i][j])
        for i in range(r):
            column = [0] + dp[i] + [0]
            stack = []
            left = [0 for _ in range(c+2)]
            right = [0 for _ in range(c+2)]
            for m in range(len(column)):
                while stack and column[m] < column[stack[-1]]:
                    left[stack[-1]] = m
                    stack.pop()
                stack.append(m)
            stack = []
            for m in range(len(column)-1, -1, -1):
                while stack and column[m] < column[stack[-1]]:
                        right[stack[-1]] = m
                        stack.pop()
                stack.append(m)
            width = [left[m] - right[m] -1 for m in range(len(column))]
            
            for m in range(len(column)):
                res = max(res, min(width[m]**2, column[m]**2))

        return res """
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        res = 0
        if not r:
            return res
        c = len(matrix[0])
        
        maxside = 0
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxside = max(maxside, dp[i][j])
        return maxside ** 2
            

                

            
# @lc code=end
so = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
ans = so.maximalSquare(matrix)
print(ans)