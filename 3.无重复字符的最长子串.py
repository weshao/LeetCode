#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        charDict = {}
        start = 0
        maxLength = 1
        for end in range(len(s)):
            rightChar = s[end]
            if rightChar in charDict:
                start = max(start, charDict[rightChar] + 1)
            charDict[rightChar] = end
            maxLength = max(maxLength, end - start + 1)
        return maxLength

                
# @lc code=end

test = Solution()
print(test.lengthOfLongestSubstring(""))