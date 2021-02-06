#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.50%)
# Likes:    1028
# Dislikes: 0
# Total Accepted:    199.8K
# Total Submissions: 359.6K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if digits == '':
        #     return []
        # keyboard = {
        #     '2': ['a', 'b', 'c'],
        #     '3': ['d', 'e', 'f'],
        #     '4': ['g', 'h', 'i'],
        #     '5': ['j', 'k', 'l'],
        #     '6': ['m', 'n', 'o'],
        #     '7': ['p', 'q', 'r', 's'],
        #     '8': ['t', 'u', 'v'],
        #     '9': ['w', 'x', 'y', 'z'],
        # }
        # result = deque([''])
        # # while result:
        # for digit in digits:
        #     for _ in range(len(result)):
        #         now = result.popleft()
        #         # copy = now.copy()
        #         for char in keyboard[digit]:
        #             result.append(now+char)
        
        # return list(result)
        result = []
        if digits == '':
            return result
        keyboard = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        self.dfs(keyboard, digits, result, '', 0)
        return result

    def dfs(self, keyboard, digits, result, current, index):
        # if index >= len(digits):
        #     return
        if index == len(digits):
            result.append(current)
            return
        
        for char in keyboard[digits[index]]:
            current += char
            self.dfs(keyboard, digits, result, current, index+1)
            current = current[:-1]
        
    




# @lc code=end
so = Solution()
ans = so.letterCombinations("22")
print(ans)