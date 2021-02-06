#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (25.01%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    79.9K
# Total Submissions: 317.4K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 题目数据保证答案肯定是一个 32 位的整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "0"
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：s = "1"
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：s = "2"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 只包含数字，并且可能包含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        n = len(s)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            if s[i] == "0" and (s[i-1] == '1' or s[i-1] == '2'):
                dp[i] = dp[i-2]
            elif s[i] == "0" and not (s[i-1] == '1' or s[i-1] == '2'):
                return 0
            elif 1 <= int(s[i]) <= 9 and s[i-1] == '1':
                dp[i] = dp[i-1] + dp[i-2]
            elif 1 <= int(s[i]) <= 6 and s[i-1] == '2':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        
        return dp[n-1]

# @lc code=end
so = Solution()
ans = so.numDecodings("110")
print(ans)
