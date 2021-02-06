#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode-cn.com/problems/decode-string/description/
#
# algorithms
# Medium (53.52%)
# Likes:    624
# Dislikes: 0
# Total Accepted:    75.3K
# Total Submissions: 140K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 
# 
# 示例 2：
# 
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 
# 
# 示例 3：
# 
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 
# 
# 示例 4：
# 
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s):
            if '[' not in s and ']' not in s:
                return s
            res = ''
            i = 0
            left = 0
            count = 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    count = count * 10 + int(s[i])
                    i += 1
                elif s[i] == '[':
                    left += 1
                    i += 1
                    news = ''
                    while left:
                        if s[i] == '[':
                            left += 1
                            news += s[i]
                            i += 1
                        elif s[i] == ']':
                            left -= 1
                            if left != 0:
                                news += ']'
                            i += 1
                        else:
                            news += s[i]
                            i += 1
                    res += count * dfs(news)
                    count = 0
                else:
                    res += s[i]
                    i += 1
            return res
        return dfs(s)


# @lc code=end
so = Solution()
ans = so.decodeString("15[l]5[n]")
print(ans)
