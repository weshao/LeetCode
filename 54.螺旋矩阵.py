#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.43%)
# Likes:    543
# Dislikes: 0
# Total Accepted:    90.1K
# Total Submissions: 217.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = [] 
        if matrix == [] or matrix[0] == []:
            return result
        else:
            row1, row2 = 0, len(matrix) - 1
            column1, column2 = 0, len(matrix[0]) - 1
            i = row1
            j = column1
            result.append(matrix[i][j])
            while row1 <= row2 and column1 <= column2:
                while j < column2 and row1 <= row2 and column1 <= column2:
                    j += 1
                    result.append(matrix[i][j])
                    
                row1 += 1
                while i < row2 and row1 <= row2 and column1 <= column2:
                    i += 1
                    result.append(matrix[i][j])
                    
                column2 -= 1
                while j> column1 and row1 <= row2 and column1 <= column2:
                    j -= 1
                    result.append(matrix[i][j])
                    
                row2 -= 1
                while i > row1 and row1 <= row2 and column1 <= column2:
                    i -= 1
                    result.append(matrix[i][j])
                    
                column1 += 1
            
            return result
# @lc code=end
so = Solution()
ans = so.spiralOrder([
 []
])
print(ans)