#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (42.02%)
# Likes:    1015
# Dislikes: 0
# Total Accepted:    170.9K
# Total Submissions: 404.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 你可以认为每种硬币的数量是无限的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 
# 示例 2：
# 
# 
# 输入：coins = [2], amount = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：coins = [1], amount = 0
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：coins = [1], amount = 1
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：coins = [1], amount = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
# @lc code=end
so = Solution()
ans = so.coinChange(coins = [1], amount = 0)
print(ans)