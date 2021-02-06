#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (55.24%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 52K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 
# 
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于
# n 的值 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# strs[i] 仅由 '0' 和 '1' 组成
# 1 
# 
# 
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        if not k:
            return 0
        count = [[0, 0] for _ in range(k)]
        for i in range(k):
            numCount = Counter(strs[i])
            count[i][0] = numCount['0']
            count[i][1] = numCount['1']
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # for i in range(m+1):
        #     dp[0][i] = 1
        # for i in range(n+1):
        #     dp[i][0] = 1
        # dp[0][0] = 0
        
        for kk in range(k):
            for nn in range(n, count[kk][1] - 1, -1):
                for mm in range(m, count[kk][0] - 1, -1):
                    if count[kk][0] <= mm and count[kk][1] <= nn:
                        dp[nn][mm] = max(1 + dp[nn - count[kk][1]][mm - count[kk][0]], dp[nn][mm])
        
        return dp[-1][-1]
# @lc code=end
so = Solution()
ans = so.findMaxForm(strs = ["0","00","1"], m = 1, n = 0)
print(ans)