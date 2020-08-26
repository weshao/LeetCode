#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        maxlength = 1
        maxLocal = []
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if end - start + 1> maxlength:
                            maxlength = end - start + 1
                            maxLocal = [start, end]
        if maxlength == 1:
            return s[0]
        else:
            return s[maxLocal[0]:maxLocal[1] + 1]
# @lc code=end
test = Solution()
print(test.longestPalindrome("cbbd"))
