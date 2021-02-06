#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (66.68%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    63.5K
# Total Submissions: 95K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# 提示：
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def solveSudoku(self, board_new: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        cellset = [[set() for _ in range(3)] for _ in range(3)]
        allset = set([str(i+1) for i in range(9)])
        space = []
        count = [0]
        for i in range(9):
            for j in range(9):
                if board_new[i][j] != '.':
                    rowset[i].add(board_new[i][j])
                    colset[j].add(board_new[i][j])
                    cellset[i//3][j//3].add(board_new[i][j])
                    count[0] += 1
                if board_new[i][j] == '.':
                    space.append((i, j))
        valid = False
            

        
        def dfs(pos):
            # print(count[0])
            nonlocal valid
            if pos == len(space):
                valid = True
                return

            i, j = space[pos]
            if allset - (rowset[i] | colset[j] | cellset[i//3][j//3]):
                for num in allset - (rowset[i] | colset[j] | cellset[i//3][j//3]):
                    board_new[i][j] = str(num)
                    rowset[i].add(str(num))
                    colset[j].add(str(num))
                    cellset[i//3][j//3].add(str(num))
                    dfs(pos+1)
                    rowset[i].remove(str(num))
                    colset[j].remove(str(num))
                    cellset[i//3][j//3].remove(str(num))
                    if valid:return
            else:
                return
                            
        dfs(0)
        return board_new
# @lc code=end
so = Solution()
ans = so.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(ans)