#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
from collections import deque
# @lc code=start
# class ParenthesesString:
#     def __init__(self, str, openCount, closeCount) -> None:
#         self.str = str
#         self.openCount = openCount
#         self.closeCount = closeCount

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []
#         queue = deque()
#         queue.append(ParenthesesString('', 0, 0))
#         while queue:
#             ps = queue.popleft()
#             if ps.openCount == n and ps.closeCount == n:
#                 result.append(ps.str)
#             else:
#                 if ps.openCount < n:
#                     queue.append(ParenthesesString(ps.str + '(', ps.openCount + 1, ps.closeCount))
#                 if ps.openCount > ps.closeCount:
#                     queue.append(ParenthesesString(ps.str + ')', ps.openCount, ps.closeCount + 1))

#         return result

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if not n:
            return result

        def dfs(current, left, right):
            if left >= n and right >= n:
                result.append(current)
                return
            
            if left < n:
                dfs(current+'(', left +1, right)
            
            if right < left:
                dfs(current + ')', left, right+1)
        
    
        dfs('', 0, 0)
        return result

# @lc code=end
test = Solution()
ans = test.generateParenthesis(2)
print(ans)

