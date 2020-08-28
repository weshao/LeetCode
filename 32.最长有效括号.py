#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
from collections import deque
# @lc code=start
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         dp = [0 for _ in range(len(s))]
#         maxCount = 0
#         for i in range(1, len(s)):
#             if s[i] == ')':
#                 if s[i - 1] == '(' and i - 1 >= 0:
#                     dp[i] = dp[i-2] + 2
#                 elif s[i - dp[i-1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
#                     dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] -2]
#                 maxCount = max(maxCount, dp[i])
#         return maxCount

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack: 
                    maxCount = max(maxCount, i - stack[-1])
                else:
                    stack.append(i)
        return maxCount


# @lc code=end
test = Solution()
ans = test.longestValidParentheses("(()")
print(ans)
