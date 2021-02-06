#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (39.88%)
# Likes:    872
# Dislikes: 0
# Total Accepted:    96.6K
# Total Submissions: 241.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        start = 0
        count = 0
        minLength = len(s) + 1
        minLocation = [0, 0]

        for i in range(len(t)):
            if t[i] not in hashmap:
                hashmap[t[i]] = 0
            hashmap[t[i]] += 1

        

        for end in range(len(s)):
            char = s[end]
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    count += 1
            
            while count == len(hashmap):
                if minLength > (end - start + 1):
                    minLength = (end - start + 1)
                    minLocation[0] = start
                    minLocation[1] = end

                leftChar = s[start]
                start += 1
                if leftChar in hashmap:
                    if hashmap[leftChar] == 0:
                        count -= 1
                    hashmap[leftChar] += 1
        
        if minLength > len(s):
            return ""
        else:
            return s[minLocation[0]: minLocation[1]+1]

                
# @lc code=end
so = Solution()
ans = so.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(ans)
