#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.53%)
# Likes:    612
# Dislikes: 0
# Total Accepted:    126.6K
# Total Submissions: 192.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0
# 来代替。
# 
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
# 
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
# 
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        if not n:
            return T
        res = [0 for _ in range(n)]
        maxH = {}
        maxT = T[-1]
        maxH[n-1] = n
        for i in range(n-2, -1, -1):
            if T[i] >= maxT:
                maxT = T[i]
                maxH[i] = n
                res[i] = 0
            else:
                index = i + 1
                while index < n and T[i] >= T[index]:
                    index = maxH[index]
                maxH[i] = index
                res[i] = index - i
        return res
            