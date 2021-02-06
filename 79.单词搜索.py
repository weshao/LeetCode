#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.73%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    123.7K
# Total Submissions: 282.7K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, visit, word, index, r, c):
            visit[r][c] = 1
            if index == len(word):
                return True
            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0<=i< len(board) and 0<=j<len(board[0]) and not visit[i][j] and board[i][j] == word[index]:
                    if dfs(board, visit, word, index + 1, i, j):
                        return True
            visit[r][c] = 0
            return False

        nr, nc = len(board), len(board[0])
        visit = [[0 for _ in range(nc)] for _ in range(nr)]
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == word[0]:
                    if dfs(board, visit, word, 1, i, j):
                        return True
                    visit[i][j] = 0
        
        return False
        


# @lc code=end
so = Solution()
ans = so.exist(board =
[
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], word = "ABCE")
print(ans)
