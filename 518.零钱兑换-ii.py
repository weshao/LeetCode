#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (56.26%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    39.6K
# Total Submissions: 70K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if not amount:
            return 1
        if not n:
            return 0
        dp = [0] * (amount + 1)
        
        for i in range(n):
            dp[0] = 1
            for j in range(amount, 0, -1):
                if coins[i] <= j:
                    dp[j] += dp[j-coins[i]]
        return dp[-1]
# @lc code=end
so = Solution()
ans = so.change(amount = 5, coins = [1, 2, 5])
print(ans)