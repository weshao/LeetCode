#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.37%)
# Likes:    681
# Dislikes: 0
# Total Accepted:    90.9K
# Total Submissions: 123.9K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例：
# 
# 输入：4
# 输出：[
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        map = [float('inf') for _ in range(n)]
        result = []

        self.helper(map, result, 0, n)
        resultchar = []
        for num in result:
            charList = [['.' for _ in range(n)] for _ in range(n)]
            for i in range(n):
                charList[i][num[i]] = 'Q'
                charList[i] = ''.join(charList[i])
            resultchar.append(charList)
        return resultchar

            
        # return result
    def helper(self, map, result, index, n):
        if index == n:
            result.append(list(map))
            return 

        if index == 0:
            for i in range(n):
                map[0] = i
                self.helper(map, result, index+1, n)
                map[0] = float('inf')
        else:
            for i in range(n):
                flag2 = False
                if i in map:
                    continue

                for j in range(1, index+1):
                    if map[index-j] == i - j or map[index-j] == i + j:
                        flag2 = True
                        break
                if flag2:
                    continue

                map[index] = i
                self.helper(map, result, index+1, n)
                map[index] = float('inf')
        
        return

        
# @lc code=end
so = Solution()
ans = so.solveNQueens(5)
print(len(ans))