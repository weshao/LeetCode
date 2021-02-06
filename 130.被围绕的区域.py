#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.26%)
# Likes:    428
# Dislikes: 0
# Total Accepted:    80.4K
# Total Submissions: 190.3K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

from typing import List
# @lc code=start\
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr = len(board)
        if not nr:
            return board
        nc = len(board[0])
        visit = [[0 for _ in range(nc)] for _ in range(nr)]
        for i in range(nr):
            if i == 0 or i == nr-1:
                for j in range(nc):
                    if board[i][j] == 'O':
                        visit[i][j] = 1
                        board[i][j] = 'X'
                        neighbors = deque([(i, j)])
                        while neighbors:
                            r, c = neighbors.popleft()
                            for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                                if 0<= rr < nr and 0<= cc < nc:
                                    if board[rr][cc] == 'O':
                                        visit[rr][cc] = 1
                                        board[rr][cc] = 'X'
                                        neighbors.append((rr, cc))

            else:
                for j in [0, nc-1]:
                    if board[i][j] == 'O':
                        visit[i][j] = 1
                        board[i][j] = 'X'
                        neighbors = deque([(i, j)])
                        while neighbors:
                            r, c = neighbors.popleft()
                            for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                                if 0<= rr < nr and 0<= cc < nc:
                                    if board[rr][cc] == 'O':
                                        visit[rr][cc] = 1
                                        board[rr][cc] = 'X'
                                        neighbors.append((rr, cc))
        
        for i in range(nr):
            for j in range(nc):
                if visit[i][j] == 1:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        # return board
        
# @lc code=end
so = Solution()
ans = so.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])
print(ans)
