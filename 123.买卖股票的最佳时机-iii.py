#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (46.48%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    65.7K
# Total Submissions: 140.7K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
#
import heapq
from typing import List
from heapq import *
# @lc code=start
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        d = dict()
        n = len(prices)
        def recur(index, status, k):
            if (index, status, k) in d:
                return d[index, status, k]
            if index == n or k >= 2:
                return 0
            a = 0
            b = 0
            c = 0
            a = recur(index+1, status, k)
            if status:#已经买了
                b = recur(index+1, 0, k+1) + prices[index]
            else:#没有买
                c = recur(index+1, 1, k) - prices[index]
            d[index, status, k] = max(a, b, c)
            return d[index, status, k]
        
        return recur(0, 0, 0)

'''

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         dp1= -prices[0]
#         dp2 = 0
#         dp3 = -prices[0]
#         dp4 = 0
#         for i in range(1, n):
#             dp1 = max(dp1, - prices[i])
#             dp2 = max(dp1 + prices[i], dp2)
#             dp3= max(dp2 - prices[i], dp3 )
#             dp4 = max(dp4, dp3 + prices[i])
        
#         return max(dp1, dp2, dp3, dp4)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp1_in = -prices[0]
        dp1_out = 0
        dp2_in = -prices[0] #initilized for the first day when there's no money so it's -prices[0] 
        dp2_out = 0
        for i in range(1, len(prices)):
            dp1_in = max(dp1_in, -prices[i])
            dp1_out = max(dp1_out, dp1_in+prices[i])
            dp2_in = max(dp2_in, dp1_out-prices[i])
            dp2_out = max(dp2_out, dp2_in+prices[i])
        return max(dp1_in, dp1_out, dp2_in, dp2_out)
# @lc code=end
so = Solution()
ans = so.maxProfit([1,2,3,4,5])
print(ans)

        
# @lc code=end

