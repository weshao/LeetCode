#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (48.74%)
# Likes:    736
# Dislikes: 0
# Total Accepted:    55.9K
# Total Submissions: 111.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 0 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # r = len(matrix)
        # if not r:
        #     return 0
        # c = len(matrix[0])
        # maxWidth = [[0 for _ in range(c)] for _ in range(r)]
        # one = 0
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == "1":
        #             one += 1
        #             maxWidth[i][j] = one
        #         else:
        #             one = 0
        #     one = 0
        # area = 0
        # maxArea = 0
        # for i in range(r):
        #     for j in range(c):
        #         minWidth = c
        #         for k in range(i, -1, -1):
        #             minWidth = min(minWidth, maxWidth[k][j])
        #             area = minWidth * (i - k + 1)
        #             maxArea = max(maxArea, area)
        
        # return maxArea

        r = len(matrix)
        if not r:
            return 0
        c = len(matrix[0])
        maxWidth = [[0 for _ in range(c)] for _ in range(r)]
        one = 0
        for j in range(c):
            for i in range(r):
                if matrix[i][j] == "1":
                    one += 1
                    maxWidth[i][j] = one
                else:
                    one = 0
            one = 0
        area = 0
        maxArea = 0

        for i in range(r):
            heights = [0] + maxWidth[i] + [0]
            n = len(heights)
            left, right = [0] * n, [n] * n
            stack = []
            for i in range(n):
                while stack and heights[i] < heights[stack[-1]]:
                    right[stack[-1]] = i
                    stack.pop()
                stack.append(i)
            
            
            stack = []
            for i in range(n-1, 0, -1):
                while stack and heights[i] < heights[stack[-1]]:
                    left[stack[-1]] = i
                    stack.pop()
                stack.append(i)

            area = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
            maxArea = max(maxArea, area)
            
        return maxArea



# @lc code=end
so = Solution()
# matrix = [["1","1"]]
matrix = [["1"],["1"]]
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
ans = so.maximalRectangle(matrix)
print(ans)
