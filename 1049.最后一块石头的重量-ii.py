#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
# https://leetcode-cn.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (48.86%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 15.5K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
# 
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 
# 
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 
# 
# 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
# 
# 
# 
# 示例：
# 
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        elif n == 2:
            return abs(stones[0] - stones[1])
        
        s = sum(stones) // 2
        dp = [False for _ in range(s+1)]
        
        dp[0] = True
        for i in range(n):
            for j in range(s, 0, -1):
                if stones[i] <= j:
                    dp[j] = dp[j] | dp[j - stones[i]]
                else:
                    dp[j] = dp[j]
        sum1 = 0
        for j in range(s, 0, -1):
            if dp[j] == True:
                sum1 = j
                break
        sum2 = sum(stones) - sum1
        return abs(sum2 - sum1)

        
        
# @lc code=end
so = Solution()
ans = so.lastStoneWeightII([2,7,4,1,8,1])
print(ans)
