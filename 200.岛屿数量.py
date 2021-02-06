#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (51.02%)
# Likes:    885
# Dislikes: 0
# Total Accepted:    183K
# Total Submissions: 356.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
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
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#
from typing import Collection, List
# @lc code=start
from collections import deque
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     row = len(grid)
    #     if not row:
    #         return 0
    #     col = len(grid[0])
    #     count = 0
    #     visit = dict()
    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c] == '1':
    #                 count += 1
    #                 self.dfs(grid, r, c)

    #     return count

    # def dfs(self, grid, r, c):
    #     grid[r][c] = 0
    #     for x, y in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
    #         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
    #             self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    neighbors = deque([(r, c)])
                    while neighbors:
                        nr, nc = neighbors.popleft()
                        for x, y in [(nr - 1, nc), (nr+1, nc), (nr, nc-1), (nr, nc+1)]:
                            if 0 <= x < row and 0 <= y < col and grid[x][y]=='1':
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        
        return count

                    
                           
                
                
# @lc code=end
so = Solution()
ans = so.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(ans)
