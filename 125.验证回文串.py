#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (46.69%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    188.8K
# Total Submissions: 403.7K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start, end = 0, n-1
        while start < end:
            while start < n and (not ('0'<= s[start]<='9' or 'a'<= s[start]<='z' or 'A'<= s[start]<='Z')):
                start += 1
            while end > 0 and (not ('0'<= s[end]<='9' or 'a'<= s[end]<='z' or 'A'<= s[end]<='Z') and end > 0):
                end -= 1
            if start <= end:
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
        return True
# @lc code=end
so = Solution()
ans = so.isPalindrome(".,")
print(ans)