#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (60.02%)
# Likes:    1273
# Dislikes: 0
# Total Accepted:    94.7K
# Total Submissions: 157.6K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# word1 和 word2 由小写英文字母组成
# 
# 
#
import time

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = dict()
        # return self.helper(word1, word2, dp)




    # def helper(self, word1, word2, dp):
        # if (word1, word2) in dp:
        #     return dp[(word1, word2)]

        # if not word2 and not word1:
        #     dp[(word1, word2)] = 0
        #     return dp[(word1, word2)]

        # a, b= float('inf'), float('inf')

        # if not word2:
        #     a = self.helper(word1[1:], '', dp) + 1
        #     dp[(word1, word2)] = a
        #     return dp[(word1, word2)]
            
        # elif not word1:
        #     a = self.helper('', word2[1:], dp) + 1
        #     dp[(word1, word2)] = a
        #     return dp[(word1, word2)]
        # elif word1[0] == word2[0]:
        #     a = self.helper(word1[1:], word2[1:], dp)
        
        #     # b = self.helper(word1[1:], word2[1:]) + 1
        #     # c = self.helper(word1, word2[1:]) + 1
        #     # e = self.helper(word1[1:], word2) + 1
        #     # t,  ,d
        # b = min(self.helper(word1[1:], word2[1:], dp) + 1, self.helper(word1, word2[1:], dp) + 1, self.helper(word1[1:], word2, dp) + 1)
        
        # dp[(word1, word2)] = min(a, b)
        # return dp[(word1, word2)]




        n1, n2 = len(word1), len(word2)
        n = max(n1, n2)
        dp = [i for i in range(n + 1)]
        # for i in range(n+1):
        #     dp[i] = i
        # for i in range(n+1):
        #     dp[i][0] = i
        for i in range(1, n+1):
            dp[0] = i
            for j in range(1, n+1):
                if j > n2:
                    dp[j] = dp[j-1] + 1

                elif i > n1:
                    dp[j] = dp[j] + 1
                
                elif word1[i-1] == word2[j-1]:
                    dp[j] = dp[j-1]
                else:
                    dp[j] = min(dp[j] + 1, dp[j-1]+1, dp[j-1]+1)
        return dp[n2] 

    

# @lc code=end
s = time.time()
so = Solution()
ans = so.minDistance("horse", "ros")
print(ans)
print("time", time.time()-s)