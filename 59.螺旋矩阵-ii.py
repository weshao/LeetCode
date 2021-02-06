#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.41%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 70K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        rows, rowe = 0, n-1
        cols, cole = 0, n-1
        result = [[-1 for _ in range(n)] for _ in range(n)]
        r, c = 0, 0
        result[r][c] = 1
        for i in range(n*n-1):
            if r == rows and c < cole:
                c += 1
                if c == cole:
                    rows += 1
            elif c == cole and r < rowe:
                r += 1
                if r == rowe:
                    cole -= 1
            elif r == rowe and c > cols:
                c -= 1
                if c == cols:
                    rowe -= 1
            elif c == cols and r > rows:
                r -= 1
                if r == rows:
                    cols += 1
            result[r][c] = i+2
            
        return result
# @lc code=end
so = Solution()
ans = so.generateMatrix(1)
print(ans)
