#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (43.51%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    45.9K
# Total Submissions: 96.3K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
from typing import ChainMap


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = [0 for _ in range(26)]
        for char in s:
            count[ord(char) - ord('a')] += 1
        isInside = [False for _ in range(26)]
        for i in range(len(s)):
            if not isInside[ord(s[i]) - ord('a')]:
                while stack and s[i] < stack[-1]:
                    char = stack[-1]
                    if count[ord(char) - ord('a')] >= 1:
                        stack.pop()
                        isInside[ord(char) - ord('a')] = False
                    else:
                        break
                
                stack.append(s[i])
                isInside[ord(s[i]) - ord('a')] = True
            count[ord(s[i]) - ord('a')] -= 1
        return ''.join(stack)


# @lc code=end
so = Solution()
ans = so.removeDuplicateLetters("adedsagqgegadfgdsfasdfashge")
print(ans)