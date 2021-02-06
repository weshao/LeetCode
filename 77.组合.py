#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (75.90%)
# Likes:    442
# Dislikes: 0
# Total Accepted:    115.9K
# Total Submissions: 152.7K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
from typing import List
# @lc code=start
""" class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.combine_recur(1, n, k, 0, [], combinations)
        return combinations

    def combine_recur(self, parrent, n, k, depth, current, combinations):
        if depth == k:
            combinations.append(current[:])
            return
        
        for i in range(parrent, n+1):
            if depth == 0 and i > n-k+1:
                continue
            current.append(i)
            self.combine_recur(i + 1, n, k, depth + 1, current, combinations)
            del current[-1]
        
         """
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(current, i):
            if len(current) == k:
                result.append(current[:])
            
            for j in range(i+1, n+1):
                if k - len(current) > n - j + 1:
                    continue
                current.append(j)
                dfs(current, j)
                del current[-1]

        result = []
        if not n or not k:
            return result
        dfs([], 0)
        return result
# @lc code=end
so = Solution()
ans = so.combine(5, 3)
print(ans)