#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (45.58%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    39.5K
# Total Submissions: 86.4K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
# 
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
# 
# 
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| 
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 
# 
# 提示：a + b 意味着字符串 a 和 b 连接。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# s1、s2、和 s3 都由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        dp = [[False for _ in range(n2+1)] for _ in range(2)]
        dp[0][0] = True
        for i in range(0, n1+1):
            for j in range(0, n2+1):
                if i > 0:
                    if s1[i-1] == s3[i+j-1]:
                        dp[i%2][j] = dp[i%2-1][j]
                if j > 0:
                    if s2[j-1] == s3[i+j-1]:
                        if dp[i%2][j-1]:
                            dp[i%2][j] = dp[i%2][j-1]
            # dp[0] = dp[1]
            # dp[1] = [False for _ in range(n2+1)]
        
        return dp[(n1-1)%2][-1]
# @lc code=end
so = Solution()
ans = so.isInterleave(s1 = "", s2 = "", s3 = "")
print(ans)
