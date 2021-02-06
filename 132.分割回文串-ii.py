#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (44.48%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 42K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回符合要求的最少分割次数。
# 
# 示例:
# 
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPalindrome = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True
        
        for startIndex in range(n-1, -1, -1):
            for endIndex in range(startIndex+1, n):
                if s[startIndex] == s[endIndex]:
                    if endIndex - startIndex == 1 or isPalindrome[startIndex+1][endIndex-1]:
                        isPalindrome[startIndex][endIndex] = True
        
        cuts = [0 for _ in range(n)]
        for startIndex in range(n-1, -1, -1):
            minCuts = n
            for endIndex in range(n-1, startIndex-1, -1):
                if isPalindrome[startIndex][endIndex]:
                    minCuts = 0 if endIndex == n-1 else min(minCuts, 1 + cuts[endIndex + 1])
            cuts[startIndex] = minCuts
        return cuts[0]

# @lc code=end
so = Solution()
ans = so.minCut("abddbba")
print(ans)
