#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (73.54%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    107.4K
# Total Submissions: 145.7K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例：
# 
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# 
# 提示：
# 
# 
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        sList = [list(ss) for ss in sList]
        for j in range(len(sList)):
            for i in range(len(sList[j])//2):
                sList[j][i], sList[j][len(sList[j])-1-i] = sList[j][len(sList[j])-1-i] , sList[j][i]
        sList = [''.join(ss) for ss in sList]
        return ' '.join(sList)   
# @lc code=end
so = Solution()
ans = so.reverseWords("Let's take LeetCode contest")
print(ans)
