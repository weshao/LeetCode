#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (64.41%)
# Likes:    449
# Dislikes: 0
# Total Accepted:    117.9K
# Total Submissions: 183.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

from typing import Coroutine, List
# @lc code=start
""" class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        allCombinations = []
        self.combinationSum2_recur(candidates, target, [], allCombinations)
        return allCombinations
    def combinationSum2_recur(self, candidates, target, currentSum, allCombinations):
        if target == 0:
            allCombinations.append(list(currentSum))
            return True
        elif target < 0:
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            currentSum.append(candidates[i])
            if self.combinationSum2_recur(candidates[i+1:], target - candidates[i], currentSum, allCombinations):
                del currentSum[-1]
                break
            del currentSum[-1]
 """
from typing import List
# @lc code=start
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         allCombination = []
#         candidates.sort()
#         self.allCombinationSum(candidates, target, [], allCombination)
#         return allCombination
    
#     def allCombinationSum(self, candidates, target, currentSum, allCombination):
#         if target == 0:
#             allCombination.append(list(currentSum))
#             return True
#         elif target <0:
#             return
#         for i in range(len(candidates)):
#             currentSum.append(candidates[i])
#             if self.allCombinationSum(candidates[i:], target - candidates[i], currentSum, allCombination):
#                 del currentSum[-1]
#                 break    
#             del currentSum[-1]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        if not candidates:
            return result
        
        candidates.sort()
        

        def dfs(current, i, target):
            if target == 0:
                result.append(list(current))
                return
            if target < 0 or i >= len(candidates):
                return
            
    
            for j in range(i, len(candidates)):
                if i != j and j>0 and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] <= target:
                    current.append(candidates[j])
                    dfs(current, j+1, target - candidates[j])
                    del current[-1]
                else:
                    break
            

        # for i in range(len(candidates)):
        #     if candidates[i] <= target:
        dfs([], 0 , target)
        return result


            
# @lc code=end
so = Solution()
ans = so.combinationSum2(candidates = [2,5,2,1,2], target = 5)
print(ans)
