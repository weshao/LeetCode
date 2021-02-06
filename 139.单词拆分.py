#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (48.61%)
# Likes:    792
# Dislikes: 0
# Total Accepted:    111.1K
# Total Submissions: 227.9K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        wordSet = set(wordDict)
        # wordLength = set([len(word) for word in wordSet])
        if s[0] in wordSet:
            dp[0] = True
        for i in range(1, len(s)):
            if s[:i+1] in wordSet:
                dp[i] = True
            else:
                j = i
                while j >= 0:
                    if dp[j] and s[j+1: i+1] in wordSet:
                        dp[i] = True
                        break
                    else:
                        j -= 1
        
        return dp[len(s)-1]
# @lc code=end
so = Solution()
ans = so.wordBreak("abcd",
["a","abc","b","cd"])
print(ans)
