#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.24%)
# Likes:    934
# Dislikes: 0
# Total Accepted:    98.1K
# Total Submissions: 141.8K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
# class Solution:
#     def numTrees(self, n: int) -> int:
#         if not n: return 0
#         dp = [1 for _ in range(n+1)]
#         for i in range(2, n+1):
#             _sum = 0
#             for j in range(i):
#                 _sum += dp[j] * dp[i-j-1]
#             dp[i] = _sum
#         return dp[n]
class Solution:
    def numTrees(self, n: int) -> int:
        if not n:
            return 0
        dp = [0 for i in range(n+1)]
        def dfs(n):
            if n <= 1:
                return 1
            if dp[n]:
                return dp[n]
            else:
                count = 0
                for i in range(1, n+1):
                    leftCount = dfs(i-1)
                    rightCount = dfs(n-i)
                    count += (leftCount * rightCount)
            dp[n] = count
            return count
            

        
        return dfs(n)
# @lc code=end
so = Solution()
ans = so.numTrees(3)
print(ans)
