#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (65.94%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 41.8K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
# 
# 
# 
# 示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
# 
# 输入：S = "12345"
# 输出：["12345"]
# 
# 
# 
# 
# 提示：
# 
# 
# S 的长度不超过12。
# S 仅由数字和字母组成。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        if S == '':
            return result
        self.dfs(S, result, '', 0)

        return result
    def dfs(self, S, result, current, index):
        if index == len(S):
            result.append(current)
            return
        
        if 'a'<= S[index] <='z' or 'A'<= S[index] <='Z':
            self.dfs(S, result, current + S[index].lower(), index+1)
            self.dfs(S, result, current + S[index].upper(), index+1)
        
        else:
            self.dfs(S, result, current + S[index], index+1)
            
# @lc code=end
so = Solution()
ans = so.letterCasePermutation('12345')
print(ans)