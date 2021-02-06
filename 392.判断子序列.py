#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (50.65%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    102.6K
# Total Submissions: 202.3K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 进阶：
# 
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢：
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# 两个字符串都只由小写字符组成。
# 
# 
#

# @lc code=start
""" class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        dp = [[False for _ in range(nt+1)] for _ in range(ns+1)]
        dp[0] = [True] * (nt+1)
        for i in range(ns):
            for j in range(nt):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
                
        return dp[-1][-1]
 """

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        count = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        if count == len(s):
            return True
        else:
            return False

# @lc code=end
so = Solution()
ans = so.isSubsequence(s = "abc", t = "ab")
print(ans)
