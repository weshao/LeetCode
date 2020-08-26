#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}
        for ch in s:
            charMap[ch] = charMap.get(ch, 0) + 1

        for i in range(len(s)):
            if charMap[s[i]] == 1:
                return i
        return -1
# @lc code=end

