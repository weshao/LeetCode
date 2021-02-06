#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (49.15%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 38.1K
# Testcase Example:  '"()())()"'
#
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
# 
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
# 
# 示例 1:
# 
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 
# 
# 示例 2:
# 
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 
# 
# 示例 3:
# 
# 输入: ")("
# 输出: [""]
# 
#

# @lc code=start
""" class Solution:
    def __init__(self) -> None:
        super().__init__()
        self.valid_expressions = None
        self.min_removed = None
    
    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float('inf')
    
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        if index == len(string):

            if left_count == right_count:
                if rem_count <= self.min_removed:
                    possible_ans = ''.join(expr)
                    if rem_count < self.min_removed:
                        self.valid_expressions =set()
                        self.min_removed = rem_count
                    self.valid_expressions.add(possible_ans)
        
        else:
            current_char = string[index]

            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)
                expr.append(current_char)

                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)
                
                expr.pop()


    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.reset()
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)
      """   

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = 0
        right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left
        result = {}
        
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(
                        s, index + 1, left_count, right_count, 
                        left_rem - (s[index] == '('),
                        right_rem - (s[index] == ')'),
                        expr
                    )
                expr.append(s[index])

                if s[index] != '(' and s[index] != ')':
                    recurse(
                        s, index + 1,
                        left_count,
                        right_count,
                        left_rem,
                        right_rem,
                        expr
                    )
                elif s[index] == '(':
                    recurse(
                        s, index + 1,
                        left_count + 1,
                        right_count,
                        left_rem,
                        right_rem,
                        expr
                    )
                elif s[index] == ')' and left_count > right_count:
                    recurse(
                        s, index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem,
                        expr
                    )
                expr.pop()
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())
# @lc code=end

