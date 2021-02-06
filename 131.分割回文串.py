#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (69.70%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    57.5K
# Total Submissions: 82K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_Palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def dfs(start, end, current):
            if start > end:
                result.append(current[:])
                return
            
            for i in range(start, end+1):
                if is_Palindrome(start, i):
                    current.append(s[start: i+1])
                    dfs(i+1, end, current)
                    current.pop()
        
        result = []
        dfs(0, len(s)-1, [])
        return result

# @lc code=end
so = Solution()
ans = so.partition("")
print(ans)