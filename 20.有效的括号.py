#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')':'(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in bracketMap:
                if not stack or stack[-1] != bracketMap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack

# @lc code=end

